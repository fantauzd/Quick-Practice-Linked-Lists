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
        Returns a regular Python list containing the same values, in the same order, as the linked list
        """
        result = []
        current = self._head
        while current is not None:
            result += [current.data]
            current = current.next
        return result

    def insert(self, val, pos):
        """
        takes as parameters a value and a position (in that order). A position of zero means that the new value will
        become the new first element. A position of one means it will become the new second element, etc.
        A position >= the length of the list means it will be added at the end of the list.
        :param val: value of node
        :param pos: position in linked list to add to
        :return: None
        """
        # if list is empty then we insert to pos 0 (only possible position)
        if self._head is None:
            self._head = Node(val)
            return
        # we find the last node in the list and assign to current
        current = self._head
        length = 0
        while current.next is not None:
            length += 1
            current = current.next
        if pos > length:  # if pos is at or after all current positions, we simply use add to insert at the end
            self.add(val)
            return
        # if inserting to first position,we copy the head to second variable and create a new head node that points
        # to second_node
        if pos == 0:
            second_node = Node(self._head.data)
            second_node.next = self._head.next
            new_head = Node(val)
            new_head.next = second_node
            self._head = new_head
            return
        else:
            node_before = self._head
            position = 1
            while position != pos:
                position += 1
                node_before = node_before.next
            if position == pos:
                new_node = Node(val)
                new_node.next = node_before.next
                node_before.next = new_node

my_list = LinkedList()
my_list.add(13)
my_list.add(81)
my_list.insert(2,1)