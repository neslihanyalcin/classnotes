INCDIR = -I.
DBG    = -g
OPT    = -O3
CPP    = g++  -std=c++11 
CFLAGS = $(DBG) $(OPT) $(INCDIR) 
LINK   = -lm 

.cpp.o:
	$(CPP) $(CFLAGS) -c $< -o $@

all: test

test: test.cpp  segment-graph.h disjoint-set.h
	$(CPP) $(CFLAGS) -o test test.cpp $(LINK)

clean:
	/bin/rm -f segment *.o

clean-all: clean
	/bin/rm -f *~ 



