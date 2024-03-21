cpp = -std=c++11

bb_g:
	g++ ${cpp} -o bb_g bb.cpp -g

clean:
	rm *.o a.out 
	rmdir *.dSYM