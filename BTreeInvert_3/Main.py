from BTree import BTree
from Node import Node

tree = BTree()
nodes = [19, 12, 15, 18, 23, 36]
[tree.add(Node(i)) for i in nodes]

tree.print_tree()
print()

tree.invert_tree()
tree.print_tree()