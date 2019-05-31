# Graphviz Plot - Full Network: No Antiparallel Edges
# Author: Yamila Omar
# Date: 23/05/2019

import readwrite
from graph import Graph
from capacity import Capacity
import string
from graphviz import Digraph


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


# Get node list
# =============
nodes = flow_network.nodes

# Nodes positions in plot
# =======================
positions = {'source': "0,9!", 
             '0': "-1,8!",
             '1': "1,8!",
             '2': "-1,7!",
             '3': "1,7!",
             '4': "0,6!",
             '5': "0,5!",
             '6': "0,4!",
             '7': "0,3!",
             '8': "-2,2!",
             '9': "2,2!",
             '10': "0,1!",
             'A': "2,3.5!",
             'B': "0,2!",
             'C': "-1,1.5!",
             'D': "1,1.5!",
             'E': "-1,5.5!",
             'F': "-1,4.5!",
             'G': "-1,3.5!",
             'H': "-2,3.5!",
             'I': "1,3.5!",
             'sink': "0,0!"}
             
# Graphviz
# ========
g = Digraph("G", engine="neato", filename="results/no_antiparallel.gv")
g.attr(rankdir="TB", size='10,10', splines="true")

g.attr("node", shape="diamond", style="filled", color="lightgrey", fontname="Courier-Bold", fontsize="16")
g.node("source", pos=positions['source'])
g.node("sink", pos=positions['sink'])

g.attr("node", shape="circle", fixedsize="true", style="filled", fontname="Courier-Bold", fontsize="20")
for n in nodes:
    if n not in ['source', 'sink'] and n not in string.ascii_uppercase:
        g.node(str(n), width='0.5', color="#72BCD4", pos=positions[n])
    elif n in string.ascii_uppercase:
        g.node(str(n), width='0.5', color="#D48A72", pos=positions[n])
        
for i in nodes:
    for j in nodes:
        if (i,j) in flow_network.edges.keys():
            weight = str(5 * flow_network.edges[(i,j)] /1000)
            g.edge(str(i), str(j), penwidth=weight, color="#000000")


g.view()