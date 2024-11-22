from Node import Node
from RBTree import RBTree

my_tree = RBTree()
nodes = [
    (23, "Tom"),
    (16, "Adam"),
    (30, "John"),
    (40, "Mike"),
    (43, "Tony"),
    (42, "Bob"),
    (45, "Walter")
]
# [ my_tree.add(Node(i[0], i[1])) for i in nodes ]
[ my_tree.add(Node(i, "value")) for i in range(1, 11) ]

my_tree.print_tree()

my_tree.remove(2)
my_tree.print_tree()
