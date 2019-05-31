# main.py
# Author: Yamila Omar
# Date: 22nd May 2018

import readwrite
from graph import Graph 
from capacity import Capacity
from fordfulkerson import FordFulkerson
import string


# Load edges
# ==========
filename = "data/manufacturing_data.txt"
edges = readwrite.read_edges_from_file(filename)
G = Graph(edges)


# Get edges capacity
# ==================
filename = "data/nodes_capacity.txt"
nodes_capacity = readwrite.read_nodes_capacity_from_file(filename)
C = Capacity(nodes_capacity, source_node='source', sink_node='sink')
C_edges = C.get_edges_capacity(G, "weight")


# Flow Network
# ============
flow_network = Graph(C_edges.copy())

antiparallel_edges = flow_network.find_antiparallel_edges()
counter = 0
while len(antiparallel_edges) > 0:
    edge = antiparallel_edges.pop(0)
    anti = (edge[1],edge[0])
    antiparallel_edges.remove( anti )
    w = flow_network.edges[anti]
    flow_network.deleteEdge(anti[0], anti[1])
    new_node = string.ascii_uppercase[counter]
    flow_network.addEdge(i=edge[1], j=new_node, w_ij=w)
    flow_network.addEdge(i=new_node, j=edge[0], w_ij=w)
    counter += 1
    
    
# Maximum Flow
# ============
flow, residual_network = FordFulkerson(flow_network, startNode='source', endNode='sink')


# Final flow
# ==========
flow = {k:v for k,v in flow.items() if v > 0}
flow_fraction = {k:round(v/C_edges[k],2) for k,v in flow.items()}

# Total items to produce daily
# ============================
count = 0
for k,v in flow.items():
    if k[1] == "sink": count += v 
    
print("Total items to produce per day: ", count)


# Save flow fraction
# ==================
filename = "results/flow_fraction.txt" 
readwrite.write_edges_to_file(filename, flow_fraction)