%{
// Text to be placed in the output file

#include <iostream>
#include <fstream>

using namespace std;

int count=0;
%}

SPACE " "

%%
{SPACE} {count++;}
. {}
"\n" {}
%%

#include <cstdio>
int main (int argc, char*argv[]) {
	if(argv[1]==NULL){
		cout<<"Input filename missing"<<endl;
		exit(0);
	}
	else
		yyin = fopen (argv[1],"r");

 	yylex ();
	cout<<count<<endl;

}



