from BelFord_7.Node import Node


class Edge:
    def __init__(self, src: Node, destination: Node, weight):
        self.src = src
        self.dest = destination
        self.weight = weight