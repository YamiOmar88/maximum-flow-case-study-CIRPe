# Graphviz Plot - Full Network
# Author: Yamila Omar
# Date: 23/05/2019

import readwrite
from graph import Graph
from graphviz import Digraph


# Load edges
# ==========
filename = "data/manufacturing_data.txt"
edges = readwrite.read_edges_from_file(filename)
G = Graph(edges)

# Get node list
# =============
nodes = G.nodes

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
             '8': "-1,2!",
             '9': "1,2!",
             '10': "0,1!",
             'sink': "0,0!"}
             
# Graphviz
# ========
g = Digraph("G", engine="neato", filename="results/full_network.gv")
g.attr(rankdir="TB", size='10,10', splines="true")

g.attr("node", shape="diamond", style="filled", color="lightgrey", fontname="Courier-Bold", fontsize="16")
g.node("source", pos=positions['source'])
g.node("sink", pos=positions['sink'])

g.attr("node", shape="circle", fixedsize="true", style="filled", fontname="Courier-Bold", fontsize="20")
for n in nodes:
    if n not in ['source', 'sink']:
        g.node(str(n), width='0.5', color="#72BCD4", pos=positions[n])
        
for i in nodes:
    for j in nodes:
        if (i,j) in G.edges.keys():
            weight = str(5 * G.edges[(i,j)])
            g.edge(str(i), str(j), penwidth=weight, color="#000000")


g.view()