class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    # покрыть тестами
    def add_in_head(self, item):
        if self.head is None:
            self.tail = item
            item.prev = None
            item.next = None
        else:
            self.head.prev = item
            item.next = self.head
        self.head = item

    # поиск с разных концов (флаг)
    # переписать на рекурсию
    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        nodes = []
        while node is not None:
            if node.value == val:
                nodes.append(node)
            node = node.next
        return nodes

    def delete(self, val, all=False):
        pointer = self.head
        removedNodes = []
        while pointer is not None:
            if pointer.value != val:
                pointer = pointer.next
                continue

            if pointer is self.head and pointer is self.tail:
                self.head = None
                self.tail = None
            elif pointer is self.head:
                self.head = pointer.next
                pointer.next.prev = None
            elif pointer is self.tail:
                self.tail = pointer.prev
                pointer.prev.next = None
            else:
                pointer.prev.next = pointer.next
                pointer.next.prev = pointer.prev

            if not all:
                return pointer
            else:
                removedNodes.append(pointer)

            pointer = pointer.next
        return removedNodes

    def clean(self):
        # need immutable version?_?
        # return LinkedList()
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        i = 0
        while node is not None:
            i += 1
            node = node.next
        return i

    def is_empty(self):
        return self.head is None

    def insert(self, afterNode, newNode):
        if afterNode is None:
            (self.add_in_head(newNode) if self.is_empty()
             else self.add_in_tail(newNode))
            return
        if afterNode is self.tail:
            self.add_in_tail(newNode)
            return

        node = self.node
        while node is not None:
            if node is afterNode:
                newNode.next = afterNode.next
                afterNode.next = newNode
                newNode.prev = afterNode
            node = node.next

    def to_list(self, onlyValues=False):
        node = self.head
        nodes = []
        while node is not None:
            value = node.value if onlyValues else node
            nodes.append(value)
            node = node.next
        return nodes
