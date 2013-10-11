tail -n+2 $HOME/Downloads/movielens1.csv > ~/Downloads/movielens2.csv
python mrproj.py ~/Downloads/movielens2.csv > $HOME/Downloads/movielens3.csv
python tabify.py ~/Downloads/movielens3.csv ~/Downloads/movielens4.csv 
python mrr.py ~/Downloads/movielens4.csv  > R.dat
python mrq.py ~/Downloads/movielens4.csv --R=R.dat --file R.dat > Q.dat
python mr_q_ur.py Q.dat --R=R.dat --file R.dat > U.dat
python mraq.py ~/Downloads/movielens4.csv Q.dat > BT.dat
python mrr.py BT.dat  > R_BT.dat
python mr_q_uhat.py Q.dat --R=R_BT.dat --file R_BT.dat > U_final.dat
