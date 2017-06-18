#include <iostream>
#include "newlib.h"

using namespace std;

int main(int argc, char *argv[]){
	
	string s1, s2;
	cout<<"Enter two strings:";
	cin>>s1;
	cin>>s2;
	cout<<"\n String1:"<<s1<<endl;
	cout<<"\n String2:"<<s2<<endl;
	cout<<"\n Difference in the length of two Strings is: "<<count_diff(s1,s2)<<endl;
} 
