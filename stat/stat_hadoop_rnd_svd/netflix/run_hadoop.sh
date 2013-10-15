K=7
N=17771

python /home/burak/stat_hadoop_rnd_svd/netflix/transpose.py  hdfs:///user//netflix1_reorg.csv \
        --output hdfs:///user/A.dat --no-output -r hadoop 

python /home/burak/stat_hadoop_rnd_svd/mrproj.py  hdfs:///user/A.dat \
        --n=17771 --k=7 --output hdfs:///user/Y.dat --no-output -r hadoop 

python /home/burak/stat_hadoop_rnd_svd/mrr.py hdfs:///user/Y.dat \
        -r hadoop --k=7 > R.dat
