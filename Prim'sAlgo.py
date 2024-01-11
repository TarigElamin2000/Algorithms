"""
What is Prim's algorithem and what is it used for?
Prim's algorithem is used to find a minmum spanning tree with in a undiracted weghited graph. 

What is Minmum Spanning Tree (mst)?
a mst is a tree with in an undiracted graph that connects all the vertices in graph without creating a cycle and has the minmum cost.

"""

import heapq

# Given a list of edges of a connected undirected graph,
# with nodes numbered from 1 to n,
# return a list edges making up the minimum spanning tree.
def minimumSpanningTree(edges, n):
    adj = {}
    for i in range(1, n + 1):
        adj[i] = []
    for n1, n2, weight in edges:
        adj[n1].append([n2, weight])
        adj[n2].append([n1, weight])


    mst = []
    # to detect a cycle 
    visited = set(1)
    # to pop the least cost of edges 
    minheap = heapq.heapify()

    for n, weight in adj[1]:
        heapq.heappush([weight, 1, n])

    while minheap:
        w, n, nei = heapq.heappop(minheap)

        if nei in visited:
            continue 

        visited.add(nei)
        mst.append([n,nei])

        for neighbor, weight in adj[nei]:
            heapq.heappush(minheap,[weight, nei, neighbor])

    return mst






