#include <iostream>
#include "mylib.h"
using namespace std;

int main (int argc, char *argv[]) {

string s;
int c;
	c = count(string(argv[0]));
	cout<<"length of "<< argv[0] << ":" << c << endl;

	c = count(string(argv[1]));
	cout<<"length of "<< argv[1] << ":" << c << endl;
}
