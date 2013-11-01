DIR1=/home/burak/Downloads/sasha/node1/
DIR2=/home/burak/Downloads/sasha/node2/
CONF=local2
#split ../A.dat -n l/2; mv xaa $DIR1/A.dat; mv xab $DIR2/A.dat
python proj.py $CONF -i A.dat -o Y.dat  -r tcp://localhost:5040
python ata.py $CONF -i Y.dat -o YtY.dat -r tcp://localhost:5040
cat $DIR1/YtY.dat $DIR2/YtY.dat > YtY.dat 
sort YtY.dat > YtY_sorted.dat
python chol.py YtY_sorted.dat /tmp/R.dat
python a_inv_r.py $CONF -i Y.dat -o Q.dat  -f /tmp/R.dat -r tcp://localhost:5040
