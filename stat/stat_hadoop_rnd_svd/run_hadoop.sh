
hadoop dfs -rmr hdfs:///user/Y.dat
python /home/burak/stat_hadoop_rnd_svd/mrproj.py  hdfs:///user/A.dat \
        --k=7 --output hdfs:///user/Y.dat --no-output -r hadoop \
        --jobconf mapred.map.tasks=2 --jobconf mapred.reduce.tasks=2 

python /home/burak/stat_hadoop_rnd_svd/mrr.py hdfs:///user/Y.dat \
        -r hadoop --k=7 > R.dat

hadoop dfs -rmr hdfs:///user/Q.dat
python /home/burak/stat_hadoop_rnd_svd/mrq.py hdfs:///user/Y.dat \
        -r hadoop --R=R.dat --file R.dat --output hdfs:///user/Q.dat \
        --no-output

hadoop dfs -rmr hdfs:///user/BT.dat
python /home/burak/stat_hadoop_rnd_svd/mraq.py hdfs:///user/A.dat \
        hdfs:///user/Q.dat --output hdfs:///user/BT.dat --no-output \
        -r hadoop --k=7 
        
python /home/burak/stat_hadoop_rnd_svd/mrr.py hdfs:///user/BT.dat \
        -r hadoop  --k=7  > R_BT.dat

hadoop dfs -rmr :///user/U_final.dat 
python /home/burak/stat_hadoop_rnd_svd/mr_q_uhat.py hdfs:///user/Q.dat \
        --output hdfs:///user/U_final.dat --no-output -r hadoop \
        --R=R_BT.dat --file R_BT.dat 

