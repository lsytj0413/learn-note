# coding=utf-8

import pyes

conn = pyes.ES(['localhost:9200'])

# print conn.indices
# conn.indices.create_index(u'megacorp')

# mapping = {
#         'last_name': {
#             'type': 'string',
#             'analyzer': 'ik_max_word',
#             'search_analyzer': 'ik_max_word',
#             'include_in_all': 'true',
#             'boost': 8
#         }
# }
# conn.indices.put_mapping(u'employee', {
#     'properties': mapping
# }, [u'megacorp'])

conn.index({
    'first_name': 'John',
    'last_name': 'Smith',
    'age': 25,
    'about': 'I love to go rock climbing',
    'interests': ['sports', 'music']
}, 'megacorp', 'employee', 1)

conn.index({
    'first_name': 'Jane',
    'last_name': 'Smith Jane',
    'age': 32,
    'about': 'I like to collect rock albums',
    'interests': ['music']
}, 'megacorp', 'employee', 2)

conn.index({
    'first_name': 'Douglas',
    'last_name': 'Fir',
    'age': 45,
    'about': 'I like to build cabinets',
    'interests': ['forestry']
}, 'megacorp', 'employee', 3)

conn.index({
    'last_name': '中国人强壮'
}, 'megacorp', 'employee', 4)

conn.index({
    'last_name': '强中国人壮'
}, 'megacorp', 'employee', 5)

conn.index({
    'last_name': '强壮中人国'
}, 'megacorp', 'employee', 6)

q = pyes.QueryStringQuery('last_name:强壮')
results = conn.search(q, indices='megacorp', start=1, size=1)
# results = conn.search(
#     index='megacorp',
#     query={
#         'query':{
#             'match': {
#                 'last_name': '强壮'
#             }
#         }
#     }
# )
print results.total
for r in results:
    print r['last_name'].encode('UTF-8')

# conn.delete('megacorp', 'employee', 'AVbfpxsW0J0x9nNSd3NH')
# conn.indices.delete_index('megacorp')
