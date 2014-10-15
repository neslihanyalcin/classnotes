def threshold(size, c): return c / size 

def felzenswalb(E, t):
    print list(sorted(E))
    C = {u[1]:u[1] for u in E}
    print C
    ts = {x:threshold(1,t) for x in C}
    print ts
