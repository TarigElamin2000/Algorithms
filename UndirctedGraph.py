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
    Vertice, Neighbor = queue.get()

    if Vertice in visited:
        continue
    
    visited.add(Vertice)

    for neighbor in adjlist[Vertice]:
        if neighbor not in visited:
            queue.put(neighbor)



# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


"""
How to find a cycle in a undirected Graph?

one of the most importent topics when it comes to graph is finding a cycle in a graph in a directed or undirected graph.
as we menstioned in a undirected graph all nodes are connected so that means a path from U to V exiest and a path from V to U which also means we can visite all the nodes,
form any Vertices in the Graph.

So knowing that we can preform one DFS search on the any node and add visited node to a visited set then if we visite a node that is in the set and its not the perant node,
(remeber a path from V-> perant to U-> chiled exiest in tow diracteion) then a cycle is found.

"""


# Representation
# reminder test this code in the moring 

from collections import defaultdict

class isCycle:
        def __init__(self,edges : list[list]):
            self.edges = edges
            self.visitedSet = set()
            self.adjlist = defaultdict(list)
            self.create_adjList()


        def create_adjList(self):
            for u, v in self.edges:
                self.adjlist[u].append(v)
                self.adjlist[v].append(u)
            return


        def dfs(self,node,parent):
            if node in self.visitedSet:
                return False
                    
            self.visitedSet.add(node)


            for nei in self.adjlist[node]:
                if not self.dfs(nei,node):
                    if nei == parent:
                        continue
                    else:
                        return False
                        
            return True
        
CyclicGraph = isCycle([[1,2],[1,3],[1,4]])




    






