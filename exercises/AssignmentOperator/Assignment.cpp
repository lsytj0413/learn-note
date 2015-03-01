#include "StdAfx.h"
#include "Assignment.h"

#include <string>

Assignment::Assignment(char* pData/* =NULL */)
{
	if (NULL != pData)
	{
		m_pData = new char[strlen(pData) + 1];
		strcpy_s(m_pData, strlen(pData) + 1, pData);
	}
	else
	{
		m_pData = NULL;
	}
}

Assignment::Assignment(const Assignment& rhs)
{
	//假设拷贝构造函数完美的完成了功能

	if (m_pData != rhs.m_pData)
	{
		if (NULL != m_pData)
		{
			delete [] m_pData;
		}

		m_pData = rhs.m_pData;	//此处指向同一处，析构时有安全隐患
	}
}

Assignment::~Assignment(void)
{
}

Assignment& Assignment::operator= (const Assignment& rhs)
{
	if (m_pData != rhs.m_pData)	//自赋值安全性
	{
		Assignment temp(rhs.m_pData);	//异常安全性

		char *pTemp = m_pData;
		m_pData = temp.m_pData;
		temp.m_pData = pTemp;
	}

	return *this;
}