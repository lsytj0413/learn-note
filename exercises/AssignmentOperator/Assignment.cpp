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
	//���追�����캯������������˹���

	if (m_pData != rhs.m_pData)
	{
		if (NULL != m_pData)
		{
			delete [] m_pData;
		}

		m_pData = rhs.m_pData;	//�˴�ָ��ͬһ��������ʱ�а�ȫ����
	}
}

Assignment::~Assignment(void)
{
}

Assignment& Assignment::operator= (const Assignment& rhs)
{
	if (m_pData != rhs.m_pData)	//�Ը�ֵ��ȫ��
	{
		Assignment temp(rhs.m_pData);	//�쳣��ȫ��

		char *pTemp = m_pData;
		m_pData = temp.m_pData;
		temp.m_pData = pTemp;
	}

	return *this;
}