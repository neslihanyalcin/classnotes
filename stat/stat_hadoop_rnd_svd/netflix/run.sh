DIM=7
N=17770
DIR=/home/burak/Downloads/netflix/download
#rm $DIR/netflix1_reorg.csv; python run.py test
#python transpose.py $DIR/netflix1_reorg.csv > $DIR/A.dat
#python ../mrproj.py $DIR/A.dat --k=$DIM --n=$N > $DIR/Y.dat
#python ../mrr.py $DIR/Y.dat  --k=$DIM > R.dat # cholesky R
#python ../mrq.py $DIR/Y.dat --R=R.dat --file R.dat > $DIR/Q.dat 
python ../mraq.py $DIR/A.dat $DIR/Q.dat --k=$DIM --n=$N > BT.dat
python ../mrr.py BT.dat  --k=$DIM  > R_BT.dat
python ../mr_q_uhat.py $DIR/Q.dat --R=R_BT.dat --file R_BT.dat > U_final.dat
