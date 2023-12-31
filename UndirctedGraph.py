"""
What is a Undircted Graph?
    its a graph where all the edges are connected and each Vertices and its neighbor are connected indirectly meaning from V we can visite U and from U we can visit V unlike 
    dircted Graph where we can only visite U from V but not V from U.

what are the properties of Undircted Graph?
    From each Vertices we can visite all other vertices.
    A graph that has at least n-1 edges is a (undirected connected graph) meaning we can visite all other Vertices by traversing any other vertices.

How can we represent a undircted graph?
    They are many way to represent the graph Like Mtrixe but the most famouse way is an Adjacency list where the we create a dictionary were keys are vertices and vales are 
    a list of vertices.

What are the most used algorithmes to solve Undirected Graphs problems?

    - Prime's algorithmes (shortest path)
    - Union Find (disjoin sets)
    - Kruskal's Algoritme (Minimum Spanning Tree)
    - Depth First Search 
    - Breth First Search 
"""

# Representation

from collections import defaultdict
import queue

Edges = [["A","B"],["B","C"],["B","S"],["S","Z"],["S","U"]]

# Creating a Adjacency List 
adjlist = defaultdict(list)

for v, u in Edges:
    adjlist[v].append(u)
    adjlist[u].append(v)

# Traversing the Graph Using Bfs
queue = queue.Queue()
queue.put(Edges[0])
visited = set()

while queue:
    Vertice, Neighbor = queue.popleft()

    if Vertice in visited:
        continue
    
    visited.add(Vertice)

    for neighbor in adjlist[Vertice]:
        if neighbor not in visited:
            queue.put(neighbor)









