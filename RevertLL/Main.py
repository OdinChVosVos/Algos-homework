from LinkedList import LinkedList
from Node import Node

my_list = LinkedList()
[my_list.add(Node(i)) for i in range(100)]

my_list.print_list()
print()

my_list.revert()
my_list.print_list()