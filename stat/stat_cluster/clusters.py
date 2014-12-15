import pickle, re, pandas as pd

def describe(n_clusters):
    all_rules = {}

    # Starting from node follow parents all the way to the top to
    # determine the "path" that led to that node
    def trace(node):
        tr = []
        while node:
            # we start from bottom so dont append, insert in the
            # beginning for the right trace
            tmp = node # if name exists use it
            if tmp in nodes: tmp=nodes.get(node)
            tr.insert(0, (tmp,nodes_yn.get(node)))
            node=parents.get(node)
        return tr

    # Walk the tree using recursion, visiting each node, until
    # reaching a bottommost leaf, and report the path from root to
    # that bottommost leaf. Those paths are our rules.
    def walk(T,node,rules):
        if node not in branches:
            rules.append(trace(node))
            return
        left, right = branches[node]
        parents[left] = node
        walk(T, left, rules)
        parents[right] = node
        walk(T, right, rules)
        
    df = pd.read_csv('/tmp/customers_clustered.csv',sep=';',index_col='user_id')
    print 'original dataset', len(df)
    
    for cluster in range(n_clusters):
        #print 'Tree %d' % cluster
        trees = open('/tmp/tree-%d.txt' % cluster).read()
        for tree in trees.split('booster[')[1:]:
            nodes_yn = {}
            nodes = re.findall(r'(\d+):\[(.*?)\]',tree,re.DOTALL|re.MULTILINE)
            nodes = dict(x for x in nodes)
            branches = re.findall(r'(\d+):\[.*?(yes=\d+),(no=\d+)',tree,re.DOTALL|re.MULTILINE)
            for x in branches: nodes_yn[x[1].replace('yes=','')] = 'yes'
            for x in branches: nodes_yn[x[2].replace('no=','')] = 'no'
            branches = dict((x[0],(x[1].replace('yes=',''),x[2].replace('no=',''))) for x in branches)
            leaves = re.findall(r'(\d+):leaf=(.*?)\n',tree,re.DOTALL|re.MULTILINE)        
            leaves = dict(x for x in leaves)

            parents = {}; rules = []
            walk(nodes, '0', rules)

            # shift yes/not stuff by one to the left, because
            # decisions look weird
            new_rules = []
            for rule in rules:
                new_rules.append([(rule[i][0],rule[i+1][1]) for i in range(len(rule)-1)])
            rules = new_rules            

            for rule in rules: 
                df_slice = df.copy()
                for x in rule:
                    if '<' not in x[0]:
                        df_slice = df_slice[df_slice[x[0]] == int(x[1]=='yes')]
                    else:
                        a,b = x[0].split('<')
                        df_slice = df_slice[(df_slice[a] < float(b)) == (x[1]=='yes') ]

                # only report if slice count is high
                if len(df_slice) > 100:
                    print
                    dedup = [rule[i] for i in range(len(rule)) if i == 0 or rule[i] != rule[i-1]]
                    for x in rule: print x
                    print
                    print 'count', len(df_slice)
                    print
                    
if __name__ == "__main__": 
    describe(3)
    
