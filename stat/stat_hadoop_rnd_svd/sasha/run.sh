DIR1=/home/burak/Downloads/sasha/node1/
RESPONSE=tcp://localhost:5040
CONF=local
#cp ../A.dat $DIR1/
python proj.py $CONF -i A.dat -o Y.dat  -r $RESPONSE
python ata.py $CONF -i Y.dat -o YtY.dat -r $RESPONSE
sort $DIR1/YtY.dat > $DIR1/YtY_sorted.dat 
python chol.py $DIR1/YtY_sorted.dat /tmp/R.dat
python a_inv_r.py $CONF -i Y.dat -o Q.dat  -f /tmp/R.dat -r $RESPONSE
python join.py $CONF -i A.dat,Q.dat -o AQ.dat -r $RESPONSE
python atq.py $CONF -i AQ.dat -o BT.dat -r $RESPONSE
sort -h $DIR1/BT.dat > $DIR1/BT_sorted.dat	
python ata.py $CONF -i BT_sorted.dat -o BTB.dat -r $RESPONSE
sort -h $DIR1/BTB.dat > $DIR1/BTB_sorted.dat
python chol.py $DIR1/BTB_sorted.dat /tmp/R_BT.dat
python q_uhat.py $CONF -i Q.dat -o U_final.dat  -f /tmp/R_BT.dat -r $RESPONSE
