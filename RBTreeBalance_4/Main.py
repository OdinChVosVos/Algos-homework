from Node import Node
from RBTree import RBTree

my_tree = RBTree()
nodes = [23, 16, 30, 40, 43, 42, 45]
[ my_tree.add(Node(i)) for i in nodes ]

my_tree.print_tree()