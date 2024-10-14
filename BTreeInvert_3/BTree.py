
from Node import Node


class BTree:

    def __init__(self):
        self.root   =   None
        self.size   =   0

    def add(self, node: Node, cur: Node = None) -> None:
        match cur:
            case None:
                if self.root is None:
                    self.root = node
                    self.size += 1
                else:
                    self.add(node, self.root)
            case _:
               if node.data > cur.data:
                   if cur.right is None:
                       cur.right = node
                       self.size += 1
                   else:
                       self.add(node, cur.right)
               elif node.data < cur.data:
                   if cur.left is None:
                       cur.left = node
                       self.size += 1
                   else:
                       self.add(node, cur.left)


    def invert_tree(self):
        self.__invert_tree([self.root])


    def __invert_tree(self, src: list[Node]) -> None:
        # Getting lists of parents and their children
        parent_nodes = src
        children_nodes = []

        # If all parents are None th method ends
        if all(i is None for i in parent_nodes):
            return

        # Passing by each parent node changing left and right and add them into children list
        for node in parent_nodes:
            match node:
                case None:
                    children_nodes.append(None)
                    children_nodes.append(None)
                case _:
                    left = node.left
                    node.left = node.right
                    node.right = left

                    children_nodes.append(node.left)
                    children_nodes.append(node.right)

        # Recursively invert next floor (children list becomes parents one)
        self.__invert_tree(children_nodes)



    def print_tree(self) -> None:
        floors = self.__get_by_floors(
            [self.root],
            []
        )

        for i, floor in enumerate(floors):
            temp        = 2 ** (len(floors) - i)
            lead_space  = " " * (temp - 1)
            join_spaces = " " * (2 * temp - 1)
            print(lead_space, end = '')
            print(join_spaces.join(floor))


    def __get_by_floors(self, src: list[Node], res: list[list[str]]) -> list[list[str]]:
        parent_nodes = src
        children_nodes = []
        floor = []

        if all(i is None for i in parent_nodes):
            return res

        for node in parent_nodes:
            match node:
                case None:
                    children_nodes.append(None)
                    children_nodes.append(None)
                    floor.append("X")
                case _:
                    children_nodes.append(node.left)
                    children_nodes.append(node.right)
                    floor.append(str(node.data))

        res.append(floor)
        return self.__get_by_floors(children_nodes, res)