%{
// Text to be placed in the output file

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

char* s;
char* t;
%}

ID [a-zA-Z0-9][a-zA-Z0-9]*
%%
{ID} {if(strcmp(yytext,s)==0) cout<<t; 
	else cout<<yytext;}
%%

#include <cstdio>
int main (int argc, char*argv[]) {

	if(argv[1]==NULL){
		cout<<"file name missing"<<endl;
		exit(0);
	}
	else	
		yyin = fopen (argv[1],"r");
	if(argv[2]==NULL){
		cout<<"find word missing"<<endl;
		exit(0);
	}
	else
		s=argv[2];
	if(argv[3]==NULL){
		cout<<"replace word missing"<<endl;
		exit(0);
	}
	else
		t=argv[3]; 

 	yylex ();

}



