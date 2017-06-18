#include <iostream>
#include "newlib.h"

int count_diff(string s1, string s2){
	int len1 = s1.length();
	int len2 = s2.length();
	return ((len1 >= len2)? len1-len2 : len2-len1) ;
}
	
