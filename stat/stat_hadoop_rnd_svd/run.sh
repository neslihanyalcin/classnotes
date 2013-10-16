DIM=7
#N=30
N=3730
#python prepare.py /home/burak/Downloads/movielens_small/movielens2.csv A.dat
#python prepare.py /home/burak/Downloads/movielens2.csv A.dat
#python prepare.py w1.csv A.dat 
#python mrproj.py A.dat --k=$DIM --n=$N --file mrc.py --runner=local > Y.dat
#python mrr.py Y.dat  --k=$DIM > R.dat # cholesky R
#python mrq.py Y.dat --R=R.dat --file R.dat  > Q.dat
#pig -x local join.pig
python mraq.py A.dat Q.dat --k=$DIM --n=$N  --file mrc.py  > BT.dat
#python mrr.py BT.dat  --k=$DIM > R_BT.dat
#python mr_q_uhat.py Q.dat --R=R_BT.dat --file R_BT.dat > U_final.dat
