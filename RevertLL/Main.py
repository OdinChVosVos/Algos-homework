from LinkedList import LinkedList
from Node import Node

my_list = LinkedList()
[my_list.add(Node(i)) for i in range(10)]

my_list.print_list()
print()

my_list.revert_replacing()
my_list.print_list()

print()

my_list.revert_on_step()
my_list.print_list()