#python tabify.py w1.csv A.dat
#python mrproj.py A.dat > Y.dat
#python mrr.py Y.dat  --n=7 > R.dat # cholesky R
#python mrq.py Y.dat --R=R.dat --file R.dat > Q.dat # get Q
#python mraq.py A.dat Q.dat > BT.dat
python mrr.py BT.dat  --n=7  > R_BT.dat
#python mr_q_uhat.py Q.dat --R=R_BT.dat --file R_BT.dat > U_final.dat
