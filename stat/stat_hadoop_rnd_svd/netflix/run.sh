DIM=7
DIR=/home/burak/Downloads/netflix/download
#python run.py
#python transpose.py $DIR/netflix1_reorg.csv > $DIR/netflix1_reorg_user_movie.csv 
#python mrproj.py $DIR/A.dat --k=$DIM > $DIR/Y.dat
python mrr.py $DIR/Y.dat  --k=$DIM > $DIR/R.dat # cholesky R
