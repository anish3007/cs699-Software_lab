%{
#include "calc2.tab.h"  //has definition for token NUMTOKEN used in this lex file. the def comes from bison 
%}
NUM [0-9]    
%%
{NUM}+	{ yylval = atoi(yytext); return NUMTOKEN;}
{NUM}+"."{NUM}+	{ yylval = atof(yytext); return NUMTOKEN;}  // yylval is the value accessible in bis
[-+%*/^] { return yytext[0];}   	// operators
.    {}	
%%




