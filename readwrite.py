# Functions to read / write edges to text file
# Author: Yamila M. Omar
# Date: 4/4/2019

def read_edges_from_file(filename):
    '''Read edges from file. The file contains one edge (i,j) and its weight 
    w_ij per line as follows: i j w_ij. The separator is whitespace. While
    i and j will be read as string, w_ij is read as float.'''
    edges = {}
    with open(filename) as fileHandle:
        for line in fileHandle:
            line = line.strip().split()
            i, j, w_ij = line[0], line[1], line[2]
            w_ij = float(w_ij)
            edges[(i,j)] = w_ij        
    return edges
        
        
def write_edges_to_file(filename, G):
    '''Write dictionary of edges G to file. G must be a dictionary. 
    Keys are tuples (i,j) of edges and values are weights w_ij.'''
    with open(filename, 'w') as f:
        for k,v in G.items():
            i, j, w_ij = str(k[0]), str(k[1]), str(v)
            f.write(i + ' ' + j + ' ' + w_ij + '\n')
    return True
    
    
def read_nodes_capacity_from_file(filename):
    '''Read nodes capacity from file. The file contains one node i and its  
    capacity c_i per line as follows: i c_i. The separator is whitespace. While
    i will be read as string, c_i is read as integer.'''
    nodes_capacity = {}
    with open(filename) as fileHandle:
        for line in fileHandle:
            line = line.strip().split()
            i, c_i = line[0], line[1]
            c_i = integer(c_i)
            nodes_capacity[i] = c_i        
    return nodes_capacity