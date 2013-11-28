class WeightedGraph(object):
    def __init__(self,g):
        self.g = g        
    def weight(self,u,v):
        return self.g[u][v]    
    def itervertices(self):
        return self.g.keys()
    def neighbors(self, u):
        return self.g[u].keys()
    def inverse_neighbors(self,v):
        res = [k for k in self.g if v in self.g[k]]
        return res
    
class ShortestPathResult(object):
    def __init__(self):
        self.d = {}
        self.parent = {}
    
def shortest_path(graph, s):
    result = ShortestPathResult()
    result.d[s] = 0
    result.parent[s] = None
    for v in graph.itervertices():
        sp_dp(graph, v, result)
    return result

def sp_dp(graph, v, result):
    if v in result.d:
        return result.d[v]
    result.d[v] = float('inf')
    result.parent[v] = None
    for u in graph.inverse_neighbors(v):
        new_distance = sp_dp(graph, u, result) + graph.weight(u, v)
        if new_distance < result.d[v]:
            result.d[v] = new_distance
            result.parent[v] = u
    return result.d[v]

if __name__ == "__main__": 
 
    DAG = {
        'a': {'b':2, 'f': 9},
        'b': {'d':2, 'c':1, 'f': 6},
        'c': {'d':7},
        'd': {'e':2, 'f': 3},
        'e': {'f':4},
        'f': {}
        }

    print DAG['a']['b']
    graph = WeightedGraph(DAG)
    
    path = shortest_path(graph, 'a')
    print path.d, path.parent
    
