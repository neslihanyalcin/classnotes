import pickle, re, pandas as pd, numpy as np

n_clusters = 6

# Node dugumunden basla ve ebeveynleri tepeye kadar takip et
# boylece yolu ortaya cikar
def trace(node):
    tr = []
    while node:
        # alttan yukari ciktigimiz icin yol listesinin sonuna ekleme,
        # bas tarafina "insert" et
        tmp = node 
        if tmp in nodes: tmp=nodes.get(node)
        tr.insert(0, (tmp,nodes_yn.get(node)))
        node=parents.get(node)
    return tr

# Ozyineli olarak tum dugumleri ziyaret et, en alta gelince yukari dogru
# yolu ortaya cikar
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
    trees = open('/tmp/tree-%d.txt' % cluster).read()
    for tree in trees.split('booster[')[1:]:

        # her agacin tum dugumlerinin bilgisini oku
        nodes_yn = {}
        crit = re.DOTALL|re.MULTILINE
        nodes = re.findall(r'(\d+):\[(.*?)\]',tree,crit)
        nodes = dict(x for x in nodes)
        branches = re.findall(r'(\d+):\[.*?(yes=\d+),(no=\d+)',tree,crit)
        for x in branches: nodes_yn[x[1].replace('yes=','')] = 'yes'
        for x in branches: nodes_yn[x[2].replace('no=','')] = 'no'
        branches = dict((x[0],(x[1].replace('yes=',''),x[2].replace('no=',''))) \
                            for x in branches)
        leaves = re.findall(r'(\d+):leaf=(.*?)\n',tree,crit)
        leaves = dict(x for x in leaves)

        parents = {}; rules = []
        walk(nodes, '0', rules)

        # evet hayir kararlari herkesin bir saginda duruyor, onlari
        # bir sola cek kurallar temiz gorunsun
        new_rules = []
        for rule in rules:
            new_rules.append([(rule[i][0],rule[i+1][1]) \
                                  for i in range(len(rule)-1)])
        rules = new_rules            

        for rule in rules:
            # kural icinde en azindan bir yane 'yes' olmali tamami
            # 'no' olan kurallari sozel olarak belirtmek zor
            res = np.array(['yes' in x for x in rule])
            if ~np.any(res): continue

            df_slice = df.copy()
            # kuralin her ogesini gezerken onu dilimleme kriteri olarak
            # kullaniyoruz, hep ayni df_slice degiskenini kullaniyoruz,
            # onu kese kese tum kurallari temsil eden nihai veri kesiti
            # haline getiriyoruz
            for x in rule:
                if '<' not in x[0]:
                    df_slice = df_slice[df_slice[x[0]] == int(x[1]=='yes')]
                else:
                    a,b = x[0].split('<')
                    df_slice = df_slice[(df_slice[a] < float(b)) == (x[1]=='yes') ]

            # sadece eger veri kesiti yeterince buyukse rapor et
            if len(df_slice) > 400:
                print
                dedup = [rule[i] for i in range(len(rule)) \
                             if i == 0 or rule[i] != rule[i-1]]
                for x in rule: print x
                print
                print 'count', len(df_slice)
                    
    
