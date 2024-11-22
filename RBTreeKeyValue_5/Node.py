
class Node:
    def __init__(self, key: int, value):
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        self.is_black = False