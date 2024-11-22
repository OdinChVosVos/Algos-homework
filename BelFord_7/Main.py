from BelFord_7.Edge import Edge
from BelFord_7.Graph import Graph
from BelFord_7.Node import Node

nodes = [Node(chr(i), "value") for i in range(ord('A'), ord('F'))]
edges = [
    Edge(nodes[0], nodes[1], -1),
    Edge(nodes[0], nodes[2], 4),
    Edge(nodes[1], nodes[2], 3),
    Edge(nodes[1], nodes[3], 2),
    Edge(nodes[1], nodes[4], 2),
    Edge(nodes[3], nodes[2], 5),
    Edge(nodes[3], nodes[1], 1),
    Edge(nodes[4], nodes[3], -3),
]

graph = Graph(nodes, edges)
start_node = nodes[0]
result = graph.bellman_ford(start_node)

if result:
    print(f"Кратчайшие расстояния от вершины {start_node.key}: {result}")
