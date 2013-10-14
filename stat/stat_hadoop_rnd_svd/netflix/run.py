import os, sys, glob

fout = "/home/burak/Downloads/netflix/download/netflix1_reorg.csv"
for f in glob.glob("/home/burak/Downloads/netflix/download/training_set/*"):
    cmd = "cat %s | python reorg.py >> %s" % (f,fout)
    print cmd
    os.system(cmd)
