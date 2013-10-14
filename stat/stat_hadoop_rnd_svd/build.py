import os, sys

if sys.argv[1] == 'zip':
    os.system("zip %s/Downloads/mr_rnd_svd_0.2.zip *.py *.csv *matrix* " % os.environ['HOME'])
if sys.argv[1] == 'send':
    os.system("scp -r * burak@host2:/home/burak/stat_hadoop_rnd_svd")
