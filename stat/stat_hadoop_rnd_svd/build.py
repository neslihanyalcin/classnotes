import os, sys

if sys.argv[1] == 'zip':
    os.system("zip %s/Downloads/mr_rnd_svd_0.3.zip arxiv/* netflix/* *.py *.csv *matrix* " % os.environ['HOME'])
if sys.argv[1] == 'send':
    os.system("scp -r * hduser@host2:/home/hduser/stat_hadoop_rnd_svd")
if sys.argv[1] == 'send-local':
    os.system("cp -r * /home/hduser/stat_hadoop_rnd_svd")
if sys.argv[1] == 'sfile':
    os.system("scp -r /home/burak/Downloads/netflix burak@host2:/home/burak/Downloads")
