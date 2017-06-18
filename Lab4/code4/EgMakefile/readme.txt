Here we are defining a user defined function count_diff which takes two strings and returns the difference in the length of the two strings.

CountDiff.cpp -- contains code for the user defined function count_diff(string, string)

myprog11.cpp -- contains the main function which implements the count_diff() function.

newlib.h -- This is a user defined library which contains the declaration for the count_diff() function. This should be #included in the cpp code whenever we wish to use the function count_diff().

Makefile -- This creates the dependencies between CountDiff.cpp and myprog11.cpp object file. If we change the basic implementation of the count_diff() function in CountDiff.cpp file and 'make' command from the terminal, the change will automatically be reflected wherever count_diff() is implemented. This takes place due to the sependencies created in Makefile.   
