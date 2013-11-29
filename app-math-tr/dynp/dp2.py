from functools import wraps

DAG = {
    'a': {'b':2, 'f': 9},
    'b': {'d':2, 'c':1, 'f': 6},
    'c': {'d':7},
    'd': {'e':2, 'f': 3},
    'e': {'f':4},
    'f': {}
}

def memo(func):
    cache = {}                                  
    @wraps(func)                                
    def wrap(*args):                            
        if args not in cache:
            print 'miss', args
            cache[args] = func(*args)
        else: print 'hit', args
        return cache[args]                      
    return wrap                                 

def rec_dag_sp(W, s, t):                        # Shortest path from s to t
    @memo                                       # Memoize f
    def d(u):                                   # Distance from u to t
        if u == t: return 0                     # We're there!
        return min(W[u][v]+d(v) for v in W[u])  # Best of every first step
    return d(s)                                 # Apply f to actual start node

print rec_dag_sp(DAG, 'a', 'f')

