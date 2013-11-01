# 4
#  local:
#    base_tmp_dir: /mnt/ram
# medium, 45 sec
date
DIM=7
N=30
#N=3730
#N=17771
#python prepare.py /home/burak/Downloads/movielens2.csv A.dat # large
#python prepare.py /home/burak/Downloads/movielens_SMALL/movielens2.csv A.dat # medium
#python prepare.py w1.csv A.dat # small
#python mrproj.py A.dat --k=$DIM --n=$N --file mrc.py --runner=local > Y.dat
#python mrr.py Y.dat  --k=$DIM > R.dat # cholesky R
python mrq.py Y.dat --R=R.dat --file R.dat  > Q.dat
#python mraq.py A.dat Q.dat --k=$DIM --n=$N  --file mrc.py --runner=local > BT.dat
#python mrr.py BT.dat  --k=$DIM > R_BT.dat
#python mr_q_uhat.py Q.dat --R=R_BT.dat --file R_BT.dat > U_final.dat
date
