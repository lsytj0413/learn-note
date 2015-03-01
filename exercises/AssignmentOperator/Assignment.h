#pragma once


class Assignment
{
public:
	Assignment(char* pData=NULL);
	Assignment(const Assignment& rhs);
	~Assignment(void);

public:
	Assignment& operator= (const Assignment& rhs);

private:
	char* m_pData;
};

