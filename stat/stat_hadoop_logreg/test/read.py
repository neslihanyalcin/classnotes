#!/usr/bin/env python
import collections, math, sys, json, os, pandas

lines = [ line for line in sys.stdin ]
d = []
features = []
for line in lines:
    x = json.loads(line)
    features.append(x['features'])
    d.append(x)

df = pandas.DataFrame(d,columns=['id','class'])
df2 = pandas.DataFrame(features)
df3 = df.combine_first(df2)
df3.to_csv("/home/burak/test.data.csv",index=False)
