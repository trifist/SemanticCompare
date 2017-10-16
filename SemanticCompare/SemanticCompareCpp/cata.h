#ifndef __IFLY_CATA_H__
#define __IFLY_CATA_H__
#include <string>
#include <vector>

/* return */
typedef int							CATARETVAL;
typedef unsigned long int           CATAUINT64;

/* CataIndex instance*/
typedef void*			 HCATAINST;
typedef HCATAINST*		PHCATAINST;

//mode参数预定义宏
#define ONLY_RAW			            0x0
#define RAW_AND_PINYIN		           0x01
#define TAG					           0x02   //用作标识字段
#define	RAW_AND_TJIU	               0x03
#define	RAW_AND_PINYIN_AND_TJIU	       0x04

//type parameter predefined macros
enum resourceType{
	CLU_INDEX=1,   /* This engine type is for internal use only.*/
	EXTEND_PY_FUZZY=2, 
	EXTEND_ALIAS=3,
	GLOBAL_MANDARIN_PY=4,
	GLOBAL_CANTONESE_PY=5
};

// The print level of the log information
enum logLevel {
	LOG_ZERO = 0,
	LOG_DEBUG = 1,
	LOG_WARN = 2,
	LOG_DEBUG_WARN = 3,
	LOG_DEBUG_ERROR = 4,
	LOG_ERROR = 5,	
	LOG_ALL = 6
};

typedef struct dataCan {
	std::string field;
	std::vector<std::string> texts;
	int mode;
	int servPattern;
	dataCan() 
	{
		field="";
		texts.clear();
		mode=0;
		servPattern = 0;   //1 - refers to the contact business,0 - refers to other businesses 
	}
} SEGVAL;

typedef struct resmem_info {
	void* addr;
	CATAUINT64 offset;
	resmem_info()
	{
		addr=NULL;
		offset=0;
	}
} RESMEM_INFO_STRUCT;
typedef RESMEM_INFO_STRUCT*	   RESMEMINFO;
typedef RESMEMINFO*           PRESMEMINFO;


typedef struct ContactPeople
{
	std::string name;
	std::string number;      
	ContactPeople() 
	{
		name = "";
		number = "";
	}
}ContactPeople;



#endif /*__IFLY_CATA_H__*/