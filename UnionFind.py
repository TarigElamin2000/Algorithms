"""
- what is the Union find Algorthim and what is it used for?

The union find algo is used to connect disjoin graphs meaning taking edges of a graph and creating a acyclic graph.

 - why is it used?

using a union find algrothim you can chech if a graph has a cycle or not you can also check if tow vertics are already connected. 
union find is used with other algorithms like Kruskul algo used to sing the minmum spanning tree.
"""

# implemention 

class union_find:
    def __init__ (self, numberOfEdges):
        self.parent = [i for i in range(len(numberOfEdges))]
        self.rank = [1 for i in range(len(numberOfEdges))]

    def find(self,node):

        while node != self.parent[node]:

            self.parent[node] = self.parent[self.parent[node]]

            node = self.parent[node]
        return node

    
    def union(self,node1,node2):
        n1, n2 = self.find(node1), self.find(node2)

        if n1 == n2:
            return False

        if self.rank[n1] > self.rank[n2]:
            self.rank[n1] += self.rank[n2]
            self.parent[n2] = n1
        else:
            self.rank[n2] += self.rank[n1]
            self.parent[n1] = n2
            
        return True