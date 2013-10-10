#tail -n+2 $HOME/Downloads/movielens1.csv | head -20 > ~/Downloads/movielens1-small.csv
#python mrproj.py ~/Downloads/movielens1-small.csv > $HOME/Downloads/movielens2.csv
#python tabify.py ~/Downloads/movielens1-small.csv ~/Downloads/movielens1-small1.csv 
#python mrr.py ~/Downloads/movielens2.csv  > R
#python mrq.py ~/Downloads/movielens2.csv --file R > Q
#python mr_q_ur.py Q --file R > U
python mraq.py ~/Downloads/movielens1-small1.csv Q 
