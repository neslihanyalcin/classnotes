#python netflix/transpose.py  hdfs:///user//netflix1_reorg.csv --output hdfs:///user/A.dat --no-output -r hadoop 

hadoop dfs -rmr hdfs:///user/Y.dat

python mrproj.py  hdfs:///user/A.dat --n=17771 --file mrc.py --k=7 --output hdfs:///user/Y.dat --no-output -r hadoop

python mrr.py hdfs:///user/Y.dat -r hadoop --k=7 > R.dat

hadoop dfs -rmr hdfs:///user/Q.dat

python mrq.py hdfs:///user/Y.dat -r hadoop --R=R.dat --file R.dat  --output hdfs:///user/Q.dat --no-output

hadoop dfs -rmr hdfs:///user/BT.dat

python mraq.py hdfs:///user/A.dat hdfs:///user/Q.dat --output hdfs:///user/BT.dat --no-output --file mrc.py -r hadoop --k=7 --n=17771

python mrr.py hdfs:///user/BT.dat  -r hadoop  --k=7  > R_BT.dat

hadoop dfs -rmr hdfs:///user/U_final.dat 

python mr_q_uhat.py hdfs:///user/Q.dat --output hdfs:///user/U_final.dat  --no-output -r hadoop --R=R_BT.dat --file R_BT.dat 

