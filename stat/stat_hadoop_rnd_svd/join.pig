A = LOAD 'A.dat';
Q = LOAD 'Q.dat';

C = JOIN Q BY $0, A BY $0;
store C into '/tmp/AQ.dat';
