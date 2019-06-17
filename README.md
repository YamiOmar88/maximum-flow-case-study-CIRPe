# Maximum Flow - Case Study

## What is this?
In this repository you will find the complete (anonymized) dataset and code for the paper presented in CIRPe conference.

## How do I reproduce your results?
Easy, run the main.py file.

## What can I find in this repository?

### Data
You will find the anonymized data used for this work in the following paths:
* data/manufacturing_data.txt
* data/nodes_capacity.txt

The first file contains data in three columns separated by whitespace. The data consists of edges $(i,j)$ and weights $w_{ij}$. Each line looks like this: $i j w_{ij}$.

The second file provides node capacity values in units/day. Each line looks like this: $i C_i$.

### Code
You will find the following modules:
+ `graph.py`: object with attributes and methods of graphs.
+ `readwrite.py`: list of functions to read or write graphs to text files.
+ `capacity.py`: object with methods to distribute node capacity to edges.
+ `breadthfirstsearch.py`: object with methods to find shortest paths using BFS algorithm.
+ `fordfulkerson.py`: function for the Ford-Fulkerson algorithm.

You can reproduce the results in the paper running `main.py`.

You will also find three files with code to make the plots in the paper: `plot_full_network.py`, `plot_no_antiparallel.py`, `plot_flow_fraction.py`.

## Can I re-use your code?
Absolutely. Please make sure to cite our work. (Correct citation will be provided shortly).
