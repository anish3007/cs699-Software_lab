%{
#include <list>
#include <string>
#include <algorithm>
#include <cctype>
#include <strings.h>
#include "checker.tab.h"  //has definition for token NUMTOKEN used in this lex file. the def comes from bison 

using namespace std; 

list<string> subList;
list<string> objList;
list<string> verbList;

int iequals(const char* a, const char* b)
{
    while(*a!='\0'&&*b!='\0'){
        if (tolower(*a) != tolower(*b))
            return 1;
	a++;
	b++;
    }
    return 0;
}

int isSubject(char *str){
	for (list<string>::const_iterator itr=subList.begin(); itr!=subList.end(); ++itr){
		if(iequals(str,itr->c_str())==0)
		 return 1;
	}
	return 0;
}

int isVerb(char *str){
	for (list<string>::const_iterator itr=verbList.begin(); itr!=verbList.end(); ++itr){
		if(iequals(str,itr->c_str())==0)
		 return 1;
	}
	return 0;
}

int isObject(char *str){
	for (list<string>::const_iterator itr=objList.begin(); itr!=objList.end(); ++itr){
		if(iequals(str,itr->c_str())==0)
		 return 1;
	}
	return 0;
}

int isUpper(char ch){
	if(ch>='A'&&ch<='Z')
	 return 1;
	else
	 return 0;
}

%}
WORD [a-zA-Z]+    
%%
{WORD}		{if(isSubject(yytext)&&isUpper(yytext[0]))
			return SUBJECT;
		else if(isVerb(yytext))
			return VERB;
		else if(isObject(yytext))
			return OBJECT;}
\.  		{return DOT;}
. 		{}
\n		{}
%%


