%{
// Text to be placed in the output file

#include <iostream>
	
using namespace std;
%}
ID STOP

%%
. {cout << yytext;}
{ID} {exit(0);}
%%
#include <cstdio>
int main (int argc, char*argv[]) {


	/*yyin = fopen (argv[1],"r");*/
 yylex ();

}
