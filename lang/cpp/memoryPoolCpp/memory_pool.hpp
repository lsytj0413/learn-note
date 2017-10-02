#pragma once

#include <climits>
#include <cstddef>


template <typename T, size_t BlockSize = 4096>
class memory_pool
{
private:
    union Slot {
        T element;
        Slot* next;
    };

    using data_pointer = char*;
    using slot_type = Slot;
    using slot_pointer = Slot*;

    slot_pointer m_curr_block;
    slot_pointer m_curr_slot;
    slot_pointer m_last_slot;
    slot_pointer m_free_slot;

    static_assert(BlockSize >= (2*sizeof(slot_type)), "BlockSize too small.");

public:
    using pointer = T*;

    template <typename U>
    struct rebind {
        using memory_pool<U> other;
    };

    memory_pool() noexcept {
        m_curr_block = nullptr;
        m_curr_slot = nullptr;
        m_last_slot = nullptr;
        m_free_slot = nullptr;
    };

    ~memory_pool() noexcept {
        slot_pointer curr = m_curr_block;
        while (curr != nullptr) {
            slot_pointer prev = curr->next;
            operator delete(reinterpret_cast<void*>(curr));
            curr = prev;
        }
    };

    pointer allocate(size_t n=1, const T* hint=0) {
        if (nullptr != m_free_slot){
            pointer r = reinterpret_cast<pointer>(m_free_slot);
            m_free_slot = m_free_slot->next;
            return r;
        }
        else {
            if (m_curr_slot >= m_last_slot){
                data_pointer new_block = reinterpret_cast<data_pointer>(operator new(BlockSize));
                if (nullptr == data_pointer){
                    return nullptr;
                }

                reinterpret_cast<slot_pointer>(new_block)->next = m_curr_block;
                m_curr_block = reinterpret_cast<slot_pointer>(new_block);
                data_pointer body = new_block + sizeof(slot_pointer);
                uintptr_t r = reinterpret_cast<uintptr_t>(body);
                size_t body_pad = (alignof(slot_type) - r) % (alignof(slot_type));
                m_curr_slot = reinterpret_cast<slot_pointer>(body + body_pad);
                m_last_slot = reinterpret_cast<slot_pointer>(new_block + BlockSize - sizeof(slot_type));
            }

            return reinterpret_cast<pointer>(m_curr_slot++);
        }
    };

    void deallocate(pointer p, size_t n=1){
        if (nullptr != p){
            reinterpret_cast<slot_pointer>(p)->next = m_free_slot;
            m_free_slot = reinterpret_cast<slot_pointer>(p);
        }
    };

    template <typename U, typename... TArgs>
    void construct(U* p, TArgs&&... args){
        new (p) U(std::forward<TArgs>(args)...);
    };

    template <typename U>
    void destory(U* p){
        p->~U();
    };
};
