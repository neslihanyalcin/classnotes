DIR1=/home/burak/Downloads/sasha/node1/
python proj.py local -l ../A.dat -o Y.dat  -r tcp://localhost:5040
python ata.py local -i Y.dat -o YtY.dat -r tcp://localhost:5040
sort $DIR1/YtY.dat > $DIR1/YtY_sorted.dat
python chol.py $DIR1/YtY_sorted.dat /tmp/R.dat -r tcp://localhost:5040
python a_inv_r.py local -i Y.dat -o Q.dat  -f /tmp/R.dat -r tcp://localhost:5040
