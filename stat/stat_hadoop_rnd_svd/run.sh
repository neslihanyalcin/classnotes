DIM=7
#python tabify.py /home/burak/Downloads/movielens2.csv A.dat
python tabify.py w1.csv A.dat
python mrproj.py A.dat --k=$DIM > Y.dat
python mrr.py Y.dat  --n=$DIM > R.dat # cholesky R
python mrq.py Y.dat --R=R.dat --file R.dat > Q.dat 
python mraq.py A.dat Q.dat --n=$DIM > BT.dat
python mrr.py BT.dat  --n=$DIM  > R_BT.dat
python mr_q_uhat.py Q.dat --R=R_BT.dat --file R_BT.dat > U_final.dat
