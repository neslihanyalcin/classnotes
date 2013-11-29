class WeightedGraph(object):
    def __init__(self,g):
        self.g = g        
    def weight(self,u,v):
        return self.g[u][v]    
    def itervertices(self):
        return self.g.keys()
    def neighbors(self, u):
        return self.g[u].keys()
    
class ShortestPathResult(object):
    def __init__(self):
        self.d = {}
        self.parent = {}
    
def shortest_path_bottomup(graph, s):
    result = ShortestPathResult()
    for v in graph.itervertices():
        result.d[v] = float('inf')
        result.parent[v] = None
    result.d[s] = 0
    for v in graph.g.keys():
        print 'v=', v
        for w in graph.neighbors(v):
            print '   w=', w
            new_distance = result.d[v] + graph.weight(v, w)
            if result.d[w] > new_distance:
                result.d[w] = new_distance
                result.parent[w] = v                
    return result

if __name__ == "__main__": 
 
    DAG = {
        'a': {'b':2, 'f': 9},
        'b': {'d':2, 'c':1, 'f': 6},
        'c': {'d':7},
        'd': {'e':2, 'f': 3},
        'e': {'f':4},
        'f': {}
        }

    graph = WeightedGraph(DAG)
        
    path = shortest_path_bottomup(graph, 'a')
    print path.d, path.parent
