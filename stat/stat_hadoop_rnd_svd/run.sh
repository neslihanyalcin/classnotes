#tail -n+2 $HOME/Downloads/movielens1.csv | head -20 > ~/Downloads/movielens1-small.csv
#python mrproj.py ~/Downloads/movielens1-small.csv > $HOME/Downloads/movielens2.csv
#python tabify.py ~/Downloads/movielens1-small.csv ~/Downloads/movielens1-small1.csv 
#python mrr.py ~/Downloads/movielens2.csv  > R.dat
#python mrq.py ~/Downloads/movielens2.csv --file R.dat > Q.dat
#python mr_q_ur.py Q.dat --file R.dat > U.dat
#python mraq.py ~/Downloads/movielens1-small1.csv Q.dat > BT.dat
#python mrr.py BT.dat  > R_BT.dat
#python svd_vt.py R_BT.dat U_hat.dat
