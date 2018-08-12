"""Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields,
it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list;
it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python),
you can assume you have access to get_pointer and dereference_pointer functions
that converts between nodes and memory addresses."""


class Node:
    def __init__(self, data=None, _previous=0, _next=0):
        self._data = data
        self._both = _previous ^ _next

    def update_both(self, _previous=0, _next=0):
        self._both = _previous ^ _next


class LinkedList:
    def __init__(self):
        self._head = Node()
        self.nodes_id = {id(self._head): self._head}  # This should simulate reference/dereference pointers

    def add(self, element):
        walker = self._head
        previous_id = 0
        while previous_id ^ walker._both:
            previous_walker = walker
            walker = self.nodes_id[previous_id ^ walker._both]
            previous_id = id(previous_walker)
        walker.update_both(previous_id, id(element))
        self.nodes_id[id(element)] = element
        element.update_both(id(walker), 0)

    def get(self, index):
        _index = index
        if not index:
            raise IndexError("Index starts with 1")
        walker = self._head
        previous_id = 0
        while previous_id ^ walker._both and _index:
            previous_walker = walker
            walker = self.nodes_id[previous_id ^ walker._both]
            previous_id = id(previous_walker)
            _index -= 1
        if _index:
            raise IndexError("Index {} don't exist".format(index))
        return walker


linked_list = LinkedList()
linked_list.add(Node(4))
print(linked_list.get(1)._data)
linked_list.add(Node(7))
print(linked_list.get(2)._data)
linked_list.add(Node(5))
print(linked_list.get(3)._data)

