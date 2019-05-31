# Graphviz Plot - Flow Fraction
# Author: Yamila Omar
# Date: 23/05/2019

import readwrite
from graph import Graph
from graphviz import Digraph


# Load edges
# ==========
filename = "results/flow_fraction.txt"
edges = readwrite.read_edges_from_file(filename)
G = Graph(edges)

# Get node list
# =============
nodes = G.nodes


# =================================================================
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
              
color_gradient = ["#008000",  #green
                  "#339900", 
                  "#66B200", 
                  "#99CC00", 
                  "#CCE500", 
                  "#FFFF00",   #yellow
                  "#FFCC00", 
                  "#FF9900", 
                  "#FF6600", 
                  "#FF3300", 
                  "#FF0000"]   #red
                  
fraction_list = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]                  
# =================================================================

g = Digraph("G", engine="neato", filename="results/flow_fraction.gv")
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
            fraction = G.edges[(i,j)]
            x = fraction_list.index( round(fraction, 1) )
            col = color_gradient[x]
            g.edge(str(i), str(j), penwidth="2", color=col, label=str(fraction))


g.view()