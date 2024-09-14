# v is the current node
def topologicalSortUtil(v, adj, visited, stack):
    # Mark the current node as visited
    visited[v] = True

    # we want to visit all the nodes the current node is connected with before visiting the current node, so
    # recurse for all adjacent vertices
    for i in adj[v]:
        if not visited[i]:
            topologicalSortUtil(i, adj, visited, stack)

    # Push current vertex to stack which stores the result
    stack.append(v)


# adj is an adjacency list
# V is the total number of nodes
def topologicalSort(adj, V):
    # Stack to store the result -> the order in which we will go through the nodes at the end of the algo
    stack = []

    # keeps track of which nodes we visited in the graph traversal
    # this could be a set instead of an array
    visited = [False] * V


    # go through all the nodes that we have not visited
    for i in range(V):
        if not visited[i]:
            topologicalSortUtil(i, adj, visited, stack)