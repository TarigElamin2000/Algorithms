"""
what is Dijkstras algorithm ?
Dijkstras algorithm is used to find the shortest path in a weghited dircted graph. 

How dose it work?
Dijkstras algorithm simply uses a minheap which contains the neighbor nodes with there whigted edge and each time pops the edge with the smallest value.

How do we know if all the nodes are visited?
we simply use a set called visited and all the visited nodes into the set if visited == number of nodes the return.

"""

# Given a connected graph represented by a list of edges, where
# edge[0] = src, edge[1] = dst, and edge[2] = weight,
# find the shortest path from src to every other node in the
# graph. There are n nodes in the graph.

from collections import defaultdict
import heapq

def Dijkstras(edges, src, n):

    adjlist = defaultdict(list)
    minheap = heapq.heapify([])

    for v, u, w in edges:
        adjlist[v].append([w,u])

    heapq.heappop(minheap, (0,src))
    visited = {}

    while minheap:
        w, v = heapq.heappop(minheap)

        if len(visited) == n:
            return visited

        if v in visited:
            continue

        visited[v] = w

        for weghit, neighbor in adjlist[v]:
            heapq.heappush(minheap, (weghit + w, neighbor))

    return visited

