# Graph object
# Author: Yamila M. Omar
# Date: 5/4/2019


class Graph:
    def __init__(self, edges=dict()):
        '''Initializes a Graph. Variables:
            - edges: dictionary with edge tuples as keys (i,j) and
            weight w_ij as values.'''
        self.edges = edges
        
    
    def addEdge(self, i, j, w_ij):
        '''Allows to add and edge (i,j) and its weight w_ij to the graph'''
        self.edges[(i,j)] = w_ij
        
    
    def deleteEdge(self, i, j):
        '''Allows to delete an edge (i,j) and its associated weight'''
        try:
            self.edges.pop((i,j))
        except KeyError:
            print("{0} cannot be deleted. {0} in Graph.".format((i,j)))
            
            
    def normalize(self, source_node='i'):
        '''This function allows to set edge weights in a 0 to 1 scale.'''
        totSum = 0
        for k,v in self.edges.items():
            if k[0] == source_node:
                totSum += v
        normalized_edges = {}
        for k,v in self.edges.items():
            normalized_edges[k] = round(v/totSum, 5)
        return normalized_edges
        
        
    def find_antiparallel_edges(self):
        '''This function finds pairs of antiparallel edges.'''
        antiparallel = []
        for k in self.edges.keys():
            antiparallel_edge = (k[1],k[0])
            if self.edges.get(antiparallel_edge, False):
                antiparallel.append(k)
        antiparallel.sort()
        return antiparallel
        
        
    @property
    def nodes(self):
        '''Returns the set of nodes for this graph'''
        edges = list(self.edges.keys())
        nodes = [i[0] for i in edges] + [i[1] for i in edges]
        return set(nodes)
        
    
    @property
    def adjacencyList(self):
        '''Returns the adjacency list.'''
        ingoing, outgoing = {k:[] for k in self.nodes}, {k:[] for k in self.nodes}
        for edge in self.edges.keys():
            i, j = edge[0], edge[1]
            outgoing[i] = outgoing.get(i, []) + [j]
            ingoing[j] = ingoing.get(j, []) + [i]
        ingoing = {k:set(v) for k,v in ingoing.items()}
        outgoing = {k:set(v) for k,v in outgoing.items()}
        return ingoing, outgoing
        
    @property
    def strength(self):
        '''Calculate the strength of each node.'''
        inStrength, outStrength = {k:0 for k in self.nodes}, {k:0 for k in self.nodes}
        for edge,weight in self.edges.items():
            i, j = edge[0], edge[1]
            inStrength[j] = inStrength[j] + weight 
            outStrength[i] = outStrength[i] + weight
        return inStrength, outStrength