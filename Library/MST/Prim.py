from collections import defaultdict
import heapq

def prim(first_node, edges):
    mst = []
    adjacent_edges = defaultdict(list)
    for weight, node1, node2 in edges:
        adjacent_edges[node1].append((weight, node1, node2))
        adjacent_edges[node2].append((weight, node2, node1))

    connected = set(first_node)
    candidate = adjacent_edges[first_node]
    heapq.heapify(candidate)

    while candidate:
        weight, node1, node2 = heapq.heappop(candidate)
        if node2 not in connected:
            connected.add(node2)
            mst.append((weight, node1, node2))

            for edge in adjacent_edges[node2]:
                if edge[2] not in connected:
                    heapq.heappush(candidate, edge)

    return mst