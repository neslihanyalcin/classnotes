#RESPONSE=tcp://chost1:5040
#CONF=cluster2
RESPONSE=tcp://localhost:5040
CONF=local
#rm /tmp/x-*
#python $HOME/Documents/sasha/servers.py split-copy $CONF /home/burak/Downloads/netflix/download/A_netflix.dat A.dat

date

#CONF=local2
#python $HOME/Documents/sasha/servers.py split-copy $CONF ../A.dat A.dat

python proj.py $CONF -i A.dat -o Y.dat  -r $RESPONSE
# python ata.py $CONF -i Y.dat -o YtY.dat -r $RESPONSE
# python $HOME/Documents/sasha/servers.py pull-combine local2 YtY.dat
# sort /tmp/YtY.dat > /tmp/YtY_sorted.dat # sort the results by key
# python chol.py /tmp/YtY_sorted.dat /tmp/R.dat
# python a_inv_r.py $CONF -i Y.dat -o Q.dat  -f /tmp/R.dat -r $RESPONSE
# python join.py $CONF -i A.dat,Q.dat -o AQ.dat -r $RESPONSE
# python atq.py $CONF -i AQ.dat -o BT.dat -r $RESPONSE
# python ata.py $CONF -i BT.dat -o BTB.dat -r $RESPONSE
# python $HOME/Documents/sasha/servers.py pull-combine local2 BTB.dat
# sort -h /tmp/BTB.dat > /tmp/BTB_sorted.dat
# python chol.py /tmp/BTB_sorted.dat /tmp/R_BT.dat
# python q_uhat.py $CONF -i Q.dat -o U_final.dat  -f /tmp/R_BT.dat -r $RESPONSE
# python $HOME/Documents/sasha/servers.py pull-combine local2 U_final.dat

date