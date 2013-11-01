DIR1=/home/burak/Downloads/sasha/node1/
RESPONSE=tcp://localhost:5040
CONF=local
cp ../A.dat $DIR1/
python proj.py $CONF -i A.dat -o Y.dat  -r $RESPONSE
python ata.py $CONF -i Y.dat -o YtY.dat -r $RESPONSE
cp $DIR1/YtY.dat YtY.dat # combine
sort YtY.dat > YtY_sorted.dat # sort the results by key
python chol.py YtY_sorted.dat /tmp/R.dat
python a_inv_r.py $CONF -i Y.dat -o Q.dat  -f /tmp/R.dat -r $RESPONSE
python join.py $CONF -i A.dat,Q.dat -o AQ.dat -r $RESPONSE
