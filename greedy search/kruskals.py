def kruskal(graph):
    mst = []  # minimum spanning tree
    visited2 = set()  # for storing visited elements for cycle checking
    visited = []
    edges = []
    for node in graph.keys():
        visited.append(node)
        for to, cost in graph[node].items():
            if to not in visited:
                edges.append((cost, node, to))
    edges.sort()

    for cost, frm, to in edges:
        if frm not in visited2 or to not in visited2:
            mst.append((frm, to, cost))
            visited2.add(frm)
            visited2.add(to)
    return mst

# g = {
#     'A': {'B': 9, 'C':75},
#     'B': {'A': 9, 'C': 95, 'D': 19, 'E': 42},
#     'C': {'A': 75, 'B': 95, 'D': 51, 'E': 66},
#     'D': {'B': 19, 'C': 51, 'E': 31},
#     'E': {'B': 42, 'C': 66, 'D': 31}
# }

# User input for creating the graph
graph = {}
num_edges = int(input("Enter the number of edges: "))
for _ in range(num_edges):
    u, v, weight = input("Enter edge (start_vertex end_vertex weight): ").split()
    if u not in graph:
        graph[u] = {}
    if v not in graph:
        graph[v] = {}
    graph[u][v] = int(weight)
    graph[v][u] = int(weight)

print(graph)

# Finding the minimum spanning tree
minimal_spanning_tree = kruskal(graph)

# Displaying the minimal spanning tree
print("\nMinimal Spanning Tree:")
for edge in minimal_spanning_tree:
    frm, to, cost = edge
    print("{} -- {} (Weight: {})".format(frm, to, cost))






# Enter the number of edges: 7
# Enter edge (start_vertex end_vertex weight): A B 4
# Enter edge (start_vertex end_vertex weight): A C 3
# Enter edge (start_vertex end_vertex weight): B C 1
# Enter edge (start_vertex end_vertex weight): B D 2
# Enter edge (start_vertex end_vertex weight): C D 4
# Enter edge (start_vertex end_vertex weight): C E 2
# Enter edge (start_vertex end_vertex weight): D E 4























# def kruskal(graph):
#     mst = []  # minimum spanning tree
#     visited2 = set() # for storing visited elements for cycle checking
#     visited=[]
#     edges = []
#     for node in graph.keys():
#         visited.append(node)
#         for to, cost in graph[node].items():
#             if(to not in visited):
#                 edges.append((cost, node, to))
#     edges.sort()
    
#     i=0
#     while(i<len(edges)):
#         cost, frm, to= edges[i]
#         if(frm not in visited2 or to not in visited2): #if one of the node is not in visited2 then they will not form cycle
#             mst.append((frm,to,cost))
#             visited2.add(frm)
#             visited2.add(to)
#         i+=1
#     return mst

# g = {
#     'A': {'B': 9, 'C':75},
#     'B': {'A': 9, 'C': 95, 'D': 19, 'E': 42},
#     'C': {'A': 75, 'B': 95, 'D': 51, 'E': 66},
#     'D': {'B': 19, 'C': 51, 'E': 31},
#     'E': {'B': 42, 'C': 66, 'D': 31}
# }

# print(kruskal(g))