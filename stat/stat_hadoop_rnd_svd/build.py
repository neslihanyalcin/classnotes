import os, sys

if sys.argv[1] == 'zip':
    os.system("zip %s/Downloads/mr_rnd_svd_0.8.zip arxiv/* netflix/* *.py *.csv *matrix* " % os.environ['HOME'])
if sys.argv[1] == 'send-sasha':
    os.system("scp -r $HOME/Documents/sasha burak@host2:/home/burak/Documents")
if sys.argv[1] == 'send1':
    os.system("scp -r * burak@host2:/home/burak/stat_hadoop_rnd_svd")
if sys.argv[1] == 'send2':
    os.system("scp -r * hduser@host1:/home/hduser/stat_hadoop_rnd_svd")
    os.system("scp -r * hduser@host2:/home/hduser/stat_hadoop_rnd_svd")
if sys.argv[1] == 'send-local':
    os.system("cp -r * /home/hduser/stat_hadoop_rnd_svd")
if sys.argv[1] == 'sfile':
    os.system("scp -r /home/burak/Downloads/netflix burak@host2:/home/burak/Downloads")
