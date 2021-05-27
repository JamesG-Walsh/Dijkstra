# Dijkstra
Implements Dijkstra's algorithm to solve the single source shortest path problem in O((|V|+|E|)lg|V|) time.  A heap data structure is implemented and used for the priority queue.  

Usage:

* `python asn3.py infile.txt` – Run using the 25 vertex input file
* `python asn3.py test2.txt` – Run using the 5 vertex input file

Or create a custom input graph file using the same format.  
The 1st line is the number of vertices.  The rest of the lines represent directed edges (a->b):w as "a b w" where a is the source of the edge, b is the destination, and w is the weight (all weights must be non-negative to use Dijkstra's algorithm).
