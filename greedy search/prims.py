def prim(graph, start):
    mst = []  # minimum spanning tree
    visited = set([start])
    edges = [
        (cost, start, to)
        for to, cost in graph[start].items()
    ]
    edges.sort()

    while edges:
        cost, frm, to = edges.pop(0)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, cost))
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    edges.append((cost, to, to_next))
            edges.sort()

    return mst

# g = {
#     'A': {'B': 9, 'C':75},
#     'B': {'A': 9, 'C': 95, 'D': 19, 'E': 42},
#     'C': {'A': 75, 'B': 95, 'D': 51, 'E': 66},
#     'D': {'B': 19, 'C': 51, 'E': 31},
#     'E': {'B': 42, 'C': 66, 'D': 31}
# }


# print(prim(g,'A'))

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



# Finding the minimum spanning tree
minimal_spanning_tree = prim(graph,'A')


print(minimal_spanning_tree)


# https://github.com/Hmaske88/LP2


# A B 4
# A C 3
# B C 1
# B D 2
# C D 4
# C E 2
# D E 4

# [('A', 'C', 3), ('C', 'B', 1), ('B', 'D', 2), ('C', 'E', 2)]