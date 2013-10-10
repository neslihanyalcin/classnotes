#cp /tmp/movielens1.csv $HOME/Downloads/
#tail -n+2 $HOME/Downloads/movielens1.csv | python mrproj.py  > $HOME/Downloads/movielens2.csv
python mrr.py ~/Downloads/movielens2.csv > R
python mrq.py ~/Downloads/movielens2.csv --file R > Q
python mr_q_ur.py Q --file R > U
