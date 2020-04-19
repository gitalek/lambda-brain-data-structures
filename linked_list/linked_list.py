class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    # очистка нод (свойства next)?_?
    # мутабельный LinkedList?_?
    # добавить указатель на текущую ноду списка?_?

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

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

    def delete(self, val, all=False):  # returned value?_?
        curNode = self.head
        deletedNodes = []
        while curNode is not None:
            if curNode.value != val:
                prevNode = curNode
                curNode = curNode.next
                continue

            if curNode is self.head and curNode is self.tail:
                self.head = None
                self.tail = None
            elif curNode is self.head:
                self.head = curNode.next
            elif curNode is self.tail:
                prevNode.next = None  # experiment
                self.tail = prevNode
            else:
                prevNode.next = curNode.next

            if not all:
                return curNode
            else:
                deletedNodes.append(curNode)

            curNode = curNode.next
        return deletedNodes

    def clean(self):
        # need immutable version?_?
        # return LinkedList()
        # need mutable version?_?
        self.head = None
        self.tail = None

    def len(self):
        node = self.head
        i = 0
        while node is not None:
            i += 1
            node = node.next
        return i

    def insert(self, afterNode, newNode):
        if afterNode is None:
            newNode.next = self.head
            self.head = newNode
            self.tail = newNode  # Interface method?_?
            return
        if afterNode is self.tail:
            self.add_in_tail(newNode)
            return

        node = self.head
        while node is not None:
            if node is afterNode:
                afterNode.next = newNode
            node = node.next

    def to_list(self, onlyValues=False):
        node = self.head
        nodes = []
        while node is not None:
            value = node.value if onlyValues else node
            nodes.append(value)
            node = node.next
        return nodes


def zip_lists(list1, list2):
    count = list1.len()
    if count != list2.len():
        return None
    if count == 0:
        return LinkedList()

    result = LinkedList()
    node1 = list1.head
    node2 = list2.head
    for _ in range(count):
        val1, val2 = node1.value, node2.value
        node = Node(val1 + val2)
        result.add_in_tail(node)
        node1, node2 = node1.next, node2.next
    return result
