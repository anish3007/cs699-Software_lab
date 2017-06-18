myprog: CountDiff.o prog11.o
	g++ CountDiff.o prog11.o -o myprog

CountDiff.o: CountDiff.cpp newlib.h
	g++ -c CountDiff.cpp

prog11.o: prog11.cpp newlib.h
	g++ -c prog11.cpp

clean:
	$(RM) *.o *~
