from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, node):
        if not isinstance(node, Node):
            raise ValueError("Only Node instances can be added.")

        match self.head:
            case None:
                self.head = node
                self.tail = node
            case _:
                self.tail.next = node
                self.tail = node

        self.size += 1

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end = " ")
            cur = cur.next


    def insert(self, node, n):
        if not isinstance(node, Node):
            raise ValueError("Only Node instances can be added.")

        if 0 <= n < self.size:
            if n == 0:
                head = self.head
                node.next = head
                self.head = node
            elif n == self.size - 1:
                self.tail.next = node
                self.tail = node
            else:
                cur = self.head
                prev = None
                for i in range(n):
                    prev = cur
                    cur = cur.next
                prev.next = node
                node.next = cur

            self.size += 1


    def remove(self, n):
        if n < self.size:
            cur = self.head
            prev = None
            for i in range(n):
                prev = cur
                cur = cur.next
            if prev is not None:
                prev.next = cur.next

            self.size -= 1


    def get_parent(self, index: int):
        cur = self.head
        for i in range(index -1):
            cur = cur.next
        return None if index == 0 else cur


    # Changing each mirror elms' places
    # Unique case for head and tail coz self links changes
    def __merge_mirror(self, left_index: int):
        if 0 <= left_index < self.size - 1:
            if left_index == 0:
                tail_prev = self.get_parent(self.size - 1)
                head = self.head

                tail_prev.next = self.head
                self.head = self.tail
                self.tail = head
                self.head.next = self.tail.next
                self.tail.next = None

            else:
                right_index = self.size - left_index - 1
                left_prev = self.get_parent(left_index)
                right_prev = self.get_parent(right_index)
                right = right_prev.next
                left_next = left_prev.next.next

                right_prev.next = left_prev.next
                left_prev.next = right
                right_prev.next.next = right.next
                # The last case with border elms needed to replace left_next with right_prev coz ln is r and infinitive cycle
                right.next = left_next if right_index - left_index > 1 else right_prev

    # Merging each pair of elms (without reverting of linking direction) O(n^2)
    def revert_replacing(self):
        for i in range(self.size // 2):
            self.__merge_mirror(i)

    # Each elm's next link becoming prev elm (reverting the linking direction) O(n)
    def revert_on_step(self):
        prev = None
        cur = self.head

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        self.tail = self.head
        self.head = prev