
class Node:
    def __init__(self, data: int):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.is_black = False