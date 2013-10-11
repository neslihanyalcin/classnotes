import sys

'''
For testing
'''
fin = open(sys.argv[1])
for x in fin.readlines():
    tokens = x.split('\t')
    print tokens[1].replace('"','').replace("\n","")
    
