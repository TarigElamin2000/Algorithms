"""
What is Topological Sort?

Topological sort is a sorting algorithm that is used only in Acyclic Directed Graphs (ADG). 
What it does is it sorts the nodes of the directed graph in an order where V always comes before U, where V is pointing to U in the directed graph V->U.

When do we use Topological Sort?

It's mostly used when we want to know if V is a direct or indirect parent of U. For example, the question "Courses I" on LeetCode says the following:

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Explanation:

In this question, we have to finish all the courses where a course might have a prerequisite which is a child of the course in terms of Graph. 
So, we understand that to take course 0 we have to take course 1, and in terms of the directed graph, 1 points to 0 (1 -> 0).

The reason topological sort is used in this question is that we can visit the last child of a parent using DFS and see if we can get to the end of the tree (graph). 
If we can, that means we can finish all the courses for V where V is the parent and it is true for the children of V. 
If not, that means we have a loop and we can't finish all the courses.
"""

# Represntaion

from collections import defaultdict

Edges = [[0,2],[0,4],[2,3],[4,3],[3,1]]
numberOfNodes = 5

class TopologicalSort:
    def __init__(self,Edges :list[list], N :int):
        self.edges = Edges
        self.topSort = []
        self.directedGraph = defaultdict(list)

        self.numVertices = N
        self.visited = set()

        self.Create_directedGraph()
        

    def Create_directedGraph(self):
        for V, U in self.edges:
            self.directedGraph[V].append(U)
    
    def dfs(self,node):
        if node in self.visited:
            return 
        self.visited.add(node)

        for neighbor in self.directedGraph[node]:
            self.dfs(neighbor)
        
        self.topSort.append(node)
        return

    def topological_sort(self):
        for i in range(self.numVertices):
            self.dfs(i)
        return self.topSort[::-1]
    

topsort = TopologicalSort(Edges,numberOfNodes)
print(topsort.topological_sort())
        