import random
from dl_node import DLNode


class EvilList:
    def __init__(self):
        self.head = None

    def put(self, data):
        node = DLNode(data)
        node.next = self.head
        if self.head is not None:
            self.head.previous = node
        self.head = node
        return node.get_id()

    def remove_by_id(self, id):
        current = self.head
        while current is not None:
            if current.get_id() == id:
                if current.previous is not None:
                    current.previous.next = current.next
                    if current.next is not None:
                        current.next.previous = current.previous
                elif current.previous is None:
                    self.head = current.next
                    if current.next is not None:
                        current.next.previous = None
                return
            current = current.next

    def find_by_id(self, id):
        current = self.head
        while current is not None:
            if current.get_id() == id:
                current.record_access()
                self.rearrange(current)
                return current.data
            current = current.next
        return None

    def rearrange(self, node):
        if node.next is not None:
            if node.previous is not None:
                node.previous.next = node.next
            else:
                self.head = node.next
            node.next.previous = node.previous
            temp = node.next.next
            node.next.next = node
            node.previous = node.next
            node.next = temp

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def is_sorted(self):
        current = self.head
        while current is not None and current.next is not None:
            if current.get_popularity() > current.next.get_popularity():
                return False
            current = current.next
        return True

    def shuffle_list(self):
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(current)
            current = current.next

        random.shuffle(nodes)

        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]
            nodes[i + 1].previous = nodes[i]
        nodes[0].previous = None
        nodes[-1].next = None
        self.head = nodes[0]

    def sort(self):
        while not self.is_sorted():
            self.shuffle_list()
