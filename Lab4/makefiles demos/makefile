final: mylib.o myprog.o
	g++ mylib.o myprog.o -o final

mylib.o: mylib.cpp mylib.h
	g++ -c mylib.cpp

myprog.o: myprog.cpp mylib.h
	g++ -c myprog.cpp
