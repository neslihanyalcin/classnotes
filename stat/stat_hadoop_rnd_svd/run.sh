DIM=7
#python tabify.py /home/burak/Downloads/movielens_small/movielens2.csv A.dat
python tabify.py w1.csv A.dat
python mrproj.py A.dat --k=$DIM > Y.dat
python mrr.py Y.dat  --k=$DIM > R.dat # cholesky R
python mrq.py Y.dat --R=R.dat --file R.dat > Q.dat 
python mraq.py A.dat Q.dat --k=$DIM > BT.dat
python mrr.py BT.dat  --k=$DIM  > R_BT.dat
python mr_q_uhat.py Q.dat --R=R_BT.dat --file R_BT.dat > U_final.dat

# hadoop dfs -copyFromLocal /home/burak/Documents/classnotes/stat/stat_hadoop_rnd_svd/A.dat /user/
# hadoop dfs -copyFromLocal /home/burak/Documents/classnotes/stat/stat_hadoop_rnd_svd/Q.dat /user/
# hadoop dfs -copyFromLocal /home/burak/Documents/classnotes/stat/stat_hadoop_rnd_svd/Q.dat /user/

#python /home/burak/Documents/classnotes/stat/stat_hadoop_rnd_svd/mraq.py hdfs:///user/A.dat hdfs:///user/Q.dat -r hadoop --n=7 --jobconf mapred.map.tasks=1 --jobconf mapred.reduce.tasks=1 --n=7
