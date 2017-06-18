%{

#include <iostream>
//#include <cmath>
#include <list>
using namespace std;   // some declarations we need for c++ action code

int yylex (void); // just the declaration, yyparse calls it, the imple. comes from flex generated code

void yyerror (char const *err) { cout << "NOT OK"<< endl;};  // needs to be defined

//extern char* yytext; // use it if you need
//extern size_t yyleng; // useit if you need

int flag=0; // using it for storing  the result, in the end, we have final result in it
%}

%define api.value.type {int}    // means our $$ return avlue is int type
%token SUBJECT
%token VERB
%token OBJECT
%token DOT
%%

input	: %empty
	| input sentence
	;

sentence 	: SUBJECT VERB OBJECT DOT
		| SUBJECT VERB DOT
		;
%%


#include <cstdio>
#include <string>
#include <fstream>

extern FILE *yyin;
extern list<string> subList;
extern list<string> objList;
extern list<string> verbList;
void yyerror (char *const err) {cout << "NOT OK"<< endl;};

int main (int argc, char *argv[]) { // first arg: calc program
 ifstream subfile;
 ifstream verbfile;
 ifstream objfile;
 yyin = fopen (argv[1],"r");
 subfile.open ("subjects");
 verbfile.open ("verbs");
 objfile.open ("objects");
 string buf;
 while(getline(subfile, buf)){
 // cout<<<<endl;
  subList.push_back(buf);
 }
 while(getline(verbfile, buf)){
 // cout<<<<endl;
  verbList.push_back(buf);
 }
 while(getline(objfile, buf)){
 // cout<<<<endl;
  objList.push_back(buf);
 }
 if(yyparse()==0){
	cout<<"OK"<<endl;
 }
}


