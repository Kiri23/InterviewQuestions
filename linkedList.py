"""
Problem: Implement a Doubly Linked List Data Structure

Classes:
1. Node
   - Properties: data, prev, next
   - Purpose: Basic building block for the linked list

2. MyLinkedList
   - Methods needed:
     * append(data, add_prev): Add new node to end of list
     * print_forward(): Print list from start to end
   - Challenge: Handle cases where some nodes have prev links and others don't

Example usage:
node = MyLinkedList(5)
node.append(8)
node.append(10, add_prev=True)  # This node will have prev reference
"""


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None


class MyLinkedList():
    def __init__(self, data=None):
        self.first_node = Node(data)

    def append(self, data, add_prev=False):
        newNode = Node(data)
        currentNode = self.first_node
        while currentNode.next is not None:
            currentNode = currentNode.next
        if add_prev:
            newNode.prev = currentNode
        currentNode.next = newNode

    def print_foward(self):
        currentNode = self.first_node
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next


# implement foward
node = MyLinkedList(5)
node.append(8)
node.append(10, True)
node.append(11)
node.append(15)
node.print_foward()
