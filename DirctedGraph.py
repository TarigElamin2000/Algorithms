"""
What is a Dircted Graph and what makes a Dircted Graph?

    A Dircted Graph is a Graph where each u, v have an directed Edge between them
    meaing you can travle from u to v and not from v to u.

How can we find a Cycle in a directed Graph?

    Unlike a undirected Graph if a node is visited dosen't mean the Graph contiens a cycle because a node can have tow incoming Edges so its possible to be visited twice.
    so what can we do, (in a dircted Graph we can't visite all nodes form by only preforming a Search in one Vertices because Edges are directed so its only one way street).
    Knowing this we know that to visite all nodes in a graph we must preform a search in N number of vertitces where N is equle the number of V in graph.
    
    By visiting and preforming a search in each node we create something called a path (a path is a subtree/subgraph from the current graph)
    in each path if a node is visited twices then a cycle is found. 

    why dose this work?
        Because each time we preform a dfs path operation on a vertic its considered to be parent of the current path so if we start from a parent and visite childer of that 
        parent and end up visiting our first parent then there is a cycle.   

        "Not a great Explantion"
"""

from collections import defaultdict

class isCycle:
    def __init__(self,Edges: list[list], N: int) -> None:
        self.adjlist = defaultdict(list)
        self.edges = Edges
        self.numberOfNodes = N
        self.create_adjList()

    def create_adjList(self):
        for v, u in self.edges:
            self.adjlist[v].append(u)
        return
    
    def dfs(self,node,visited: set()) -> bool:

        if node in visited:
            return False
        
        visited.add(node)

        for nei in self.adjlist[node]:
            if not self.dfs(nei,visited):
                print(visited)
                return False
            
        return True
    
    def detectCycle(self):
        for i in range(self.numberOfNodes):
            if not self.dfs(i,set()):
                return False
            
        return True
    
undirectedGraph = isCycle([[1,0],[2,0]],4)
print(undirectedGraph.detectCycle())
            
        
