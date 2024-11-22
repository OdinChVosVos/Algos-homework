from Node import Node


class RBTree:

    def __init__(self):
        self.root = None

        # Black leaf
        self.NIL = Node(-1, "")
        self.NIL.is_black = True


    def remove(self, key: int) -> [Node, None]:
        node = self.__find_node(self.root, key)
        if node in [None, self.NIL]:
            return None

        self.__remove(node)
        return node


    def __remove(self, node: Node):
        current_node = node
        current_is_black = current_node.is_black

        # If there is no children or there is one we can easily transplant nodes
        if node.left == self.NIL:
            next_node = node.right
            self.__transplant(node, node.right)
        elif node.right == self.NIL:
            next_node = node.left
            self.__transplant(node, node.left)

        # Else we got both children
        else:
            # Current node which gotta be on the deleted one's place is chosen from the most left of right child
            current_node = self.__minimum(node.right)
            current_is_black = current_node.is_black
            next_node = current_node.right

            if current_node.parent == node:
                next_node.parent = current_node
            else:
                self.__transplant(current_node, current_node.right)
                current_node.right = node.right
                current_node.right.parent = current_node

            self.__transplant(node, current_node)
            current_node.left = node.left
            current_node.left.parent = current_node
            current_node.is_black = node.is_black

        # After transplanting we need to rebalance the tree if the deleted or newly transplanted was black
        if current_is_black:
            self.__fix_delete(next_node)


    def __minimum(self, node: Node) -> Node:
        while node.left != self.NIL:
            node = node.left
        return node


    def __transplant(self, first: Node, second: Node) -> None:
        if first.parent is None:
            self.root = second
        elif first == first.parent.left:
            first.parent.left = second
        else:
            first.parent.right = second
        second.parent = first.parent


    def __fix_delete(self, node):
        while node != self.root and node.is_black:

            if node == node.parent.left:
                uncle = node.parent.right

                if not uncle.is_black:  # Case 1: uncle is red
                    uncle.is_black = True
                    node.parent.is_black = False
                    self.__rotate_left(node.parent)
                    uncle = node.parent.right

                if uncle.left.is_black and uncle.right.is_black:  # Case 2: both of uncle's children are black
                    uncle.is_black = False
                    node = node.parent
                else:
                    if uncle.right.is_black:  # Case 3: uncle's right child is black, left is red
                        uncle.left.is_black = True
                        uncle.is_black = False
                        self.__rotate_right(uncle)
                        uncle = node.parent.right

                    uncle.is_black = node.parent.is_black  # Case 4: uncle's right child is red
                    node.parent.is_black = True
                    uncle.right.is_black = True
                    self.__rotate_left(node.parent)
                    node = self.root
            else:
                uncle = node.parent.left
                if not uncle.is_black:  # Symmetric cases for the left
                    uncle.is_black = True
                    node.parent.is_black = False
                    self.__rotate_right(node.parent)
                    uncle = node.parent.left
                if uncle.right.is_black and uncle.left.is_black:
                    uncle.is_black = False
                    node = node.parent
                else:
                    if uncle.left.is_black:
                        uncle.right.is_black = True
                        uncle.is_black = False
                        self.__rotate_left(uncle)
                        uncle = node.parent.left
                    uncle.is_black = node.parent.is_black
                    node.parent.is_black = True
                    uncle.left.is_black = True
                    self.__rotate_right(node.parent)
                    node = self.root

        node.is_black = True


    def __find_node(self, node: Node, key: int) -> [None, Node]:
        if node in [None, self.NIL]:
            return None
        elif  node.key == key:
            return node
        elif key < node.key:
            return self.__find_node(node.left, key)
        else:
            return self.__find_node(node.right, key)


    def add(self, node: Node) -> None:
        if self.root is None:
            node.is_black = True
            self.root = node
            self.root.left = self.root.right = self.NIL
        else:
            self.__add(node, self.root)
            self.__balance(node)


    def __add(self, node: Node, parent: Node) -> None:
        if node.key > parent.key:
            if parent.right in [None, self.NIL]:
                node.parent = parent
                parent.right = node
                node.left = node.right = self.NIL
            else:
                self.__add(node, parent.right)
        elif node.key < parent.key:
            if parent.left in [None, self.NIL]:
                node.parent = parent
                parent.left = node
                node.left = node.right = self.NIL
            else:
                self.__add(node, parent.left)


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



    # Rotation of the parent node and the right daughter
    def __rotate_left(self, node: Node) -> None:
        right = node.right

        right.left.parent = node
        node.right = right.left
        right.parent = node.parent

        if node == self.root:
            self.root = right
        else:
            if node == node.parent.right:
                node.parent.right = right
            else:
                node.parent.left = right

        right.left = node
        node.parent = right


    # Rotation of the parent node and the left daughter
    def __rotate_right(self, node: Node) -> None:
        left = node.left

        left.right.parent = node
        node.left = left.right
        left.parent = node.parent

        if node == self.root:
            self.root = left
        else:
            if node == node.parent.right:
                node.parent.right = left
            else:
                node.parent.left = left

        left.right = node
        node.parent = left


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
                    floor.append(f"{"B" if node.is_black else "R"}.{node.key}|{node.value}")

        res.append(floor)
        return self.__get_by_floors(children_nodes, res)
