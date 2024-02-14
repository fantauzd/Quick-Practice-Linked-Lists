class Node:
    """
    Represents a node in a linked list
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A linked list implementation of the List ADT
    """

    def __init__(self):
        self._head = None

    def add(self, val):
        """
        Adds a node containing val to the linked list
        """
        if self._head is None:  # If the list is empty
            self._head = Node(val)
        else:
            current = self._head
            while current.next is not None:
                current = current.next
            current.next = Node(val)

    def display(self):
        """
        Prints out the values in the linked list
        """
        current = self._head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def remove(self, val):
        """
        Removes the node containing val from the linked list
        """
        if self._head is None:  # If the list is empty
            return

        if self._head.data == val:  # If the node to remove is the head
            self._head = self._head.next
        else:
            current = self._head
            while current is not None and current.data != val:
                previous = current
                current = current.next
            if current is not None:  # If we found the value in the list
                previous.next = current.next

    def is_empty(self):
        """
        Returns True if the linked list is empty,
        returns False otherwise
        """
        return self._head is None

    def to_regular_list(self):
        """
        Returns a regular Python list containing the same values,
        in the same order, as the linked list
        """
        result = []
        current = self._head
        while current is not None:
            result += [current.data]
            current = current.next
        return result

    def reverse(self, current_node = None, next_node = None, previous_node = None):
        """
        reverses the order of the nodes in the linked list by changing the next value each node holds
        :return: None
        """
        if self._head is None or self._head.next is None:
            return
        if current_node is None:
            current_node = self._head
            next_node = current_node.next
            previous_node = current_node
        if next_node is None:
            self._head = current_node
            return
        node_prev = current_node
        next_to_reverse = next_node
        self.reverse(next_node, next_node.next, current_node)
        next_to_reverse.next = node_prev
        next_to_reverse.next.next = None
        return

lion = LinkedList()
lion.add(5)
lion.add(2)
lion.add(1)
lion.add(3)
lion.add('karate-chop')
lion.add(6)
lion.add(1)
lion.add(1)
lion.display()
lion.reverse()
lion.display()





