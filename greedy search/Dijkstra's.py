from collections import defaultdict


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
#  distances = {'A': inf,'B': inf,'C': inf,'D': inf}

    distances[start] = 0
    visited = set()
    spanning_tree = {}

    while len(visited) < len(graph):
        min_node = None
        for node in graph:
            if node not in visited and (min_node is None or distances[node] < distances[min_node]):
                min_node = node

        visited.add(min_node)

        for neighbor, weight in graph[min_node]:
            if distances[min_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[min_node] + weight
                # Store edge in spanning tree
                spanning_tree[neighbor] = (min_node, weight)

    return spanning_tree


graph = defaultdict(list)
num_edges = int(input("Enter the number of edges: "))

for _ in range(num_edges):
    u, v, weight = input(
        "Enter edge (start_vertex end_vertex weight): ").split()
    graph[u].append((v, int(weight)))
    graph[v].append((u, int(weight)))

start_node = input("Enter the starting node: ")
minimal_spanning_tree = dijkstra(graph, start_node)

print("\nMinimal Spanning Tree:")
for node, edge in minimal_spanning_tree.items():
    parent, weight = edge
    print("{} -- {} (Weight: {})".format(parent, node, weight))


# https://poki.com/en/g/parking-fury-3d-night-thief