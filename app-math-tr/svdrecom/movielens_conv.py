import pandas as pd, re

fin = open ("/home/burak/Downloads/movielens1.csv")
header = fin.readline() # skip
for j,line in enumerate(fin.readlines()):
    #line = line.strip()[:30]
    line = re.findall("(.*?);",line)
    id = line[0]; line = line[1:-1]
    res = [str(i)+":"+str(x) for i,x in enumerate(line) if x]
    print id + '\t' + ';'.join(res)
    if j==10: break
