from BelFord_7.Edge import Edge
from BelFord_7.Node import Node


class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

    def bellman_ford(self, start: Node):
        distances = {node.key: 0 if node == start else float('inf') for node in self.nodes}

        for _ in self.nodes:
            for edge in self.edges:
                if self.__check_edge(edge, distances):
                    distances[edge.dest.key] = distances[edge.src.key] + edge.weight

        # Проверка на наличие циклов отрицательного веса
        for edge in self.edges:
            if self.__check_edge(edge, distances):
                print("Граф содержит цикл с отрицательным весом.")
                return None

        return distances

    @staticmethod
    def __check_edge(edge: Edge, distances) -> bool:
        return (distances[edge.src.key] != float('inf') and
                distances[edge.src.key] + edge.weight < distances[edge.dest.key])