from operator import truediv

from Node import Node


class RBTree:

    def __init__(self):
        self.root = None

        # Black leaf
        self.NIL = Node(-1)
        self.NIL.is_black = True


    def add(self, node: Node) -> None:
        if self.root is None:
            node.is_black = True
            self.root = node
        else:
            self.__add(node, self.root)
            self.__balance(node)


    def __add(self, node: Node, parent: Node) -> None:
        if node.data > parent.data:
            if parent.right in [None, self.NIL]:
                node.parent = parent
                parent.right = node
                node.left = node.right = self.NIL
            else:
                self.__add(node, parent.right)
        elif node.data < parent.data:
            if parent.left in [None, self.NIL]:
                node.parent = parent
                parent.left = node
                node.left = node.right = self.NIL
            else:
                self.__add(node, parent.left)


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
                    floor.append(f"{"B" if node.is_black else "R"}.{node.data}")

        res.append(floor)
        return self.__get_by_floors(children_nodes, res)


    # Rotation of the parent node and the right daughter
    def __rotate_left(self, node: Node) -> None:
        right = node.right

        right.left.parent = node
        node.right = right.left
        right.parent = node.parent

        if node == node.parent.right:
            node.parent.right = right
        else:
            node.parent.left = right

        if node == self.root:
            self.root = right

        right.left = node
        node.parent = right


    # Rotation of the parent node and the left daughter
    def __rotate_right(self, node: Node) -> None:
        left = node.left

        left.right.parent = node
        node.left = left.right
        left.parent = node.parent

        if node == node.parent.right:
            node.parent.right = left
        else:
            node.parent.left = left

        if node == self.root:
            self.root = left

        left.right = node
        node.parent = left


    # Method of balancing the tree (balance black heights)
    def __balance(self, node: Node) -> None:
        # While the condition {NOT red -> red} is not provided do
        while not node.parent.is_black :

            # Two scenarios: if parent is right or left
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right

                # Two general cases:
                # 1) If the uncle and father are red: recolor them and grandparent and continue the same for grandparent
                # 2) Else: if the node is right need to rotate it's parent left and continue with the parent as the node
                #    and then or left either right node is we need
                #    to recolor the father and grandparent nodes and rotate grandparent right
                if not uncle.is_black:
                    node.parent.is_black = True
                    uncle.is_black = True
                    node.parent.parent.is_black = False
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.__rotate_left(node)

                    node.parent.is_black = True
                    node.parent.parent.is_black = False
                    self.__rotate_right(node.parent.parent)

            # The second mirrored scenario
            else:
                uncle = node.parent.parent.left

                if not uncle.is_black:
                    node.parent.is_black = True
                    uncle.is_black = True
                    node.parent.parent.is_black = False
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.__rotate_right(node)

                    node.parent.is_black = True
                    node.parent.parent.is_black = False
                    self.__rotate_left(node.parent.parent)

            # When we got high stop
            if node == self.root:
                break

        # Extra save condition for the case with the red root
        self.root.is_black = True