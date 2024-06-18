"""
You are permitted to write code between Start and End.
Besides, you can write other extra functions or classes outside, 
but don't change the template.
"""


class Node:
    def __init__(self, element, pointer):
        self.element = element
        self.pointer = pointer


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, data):
        # Start writing your code.
        temp = Node(data, self.head)
        self.head = temp
        # End writing your code.


def quick_sort(node):
    # Start writing your code.
    list = []
    while node.pointer != None:
        list.append(node.element)
        node = node.pointer
    if node.pointer == None:
        list.append(node.element)
    list.sort()
    list.reverse()
    result = SinglyLinkedList()
    for i in list:
        result.insert(i)
    return result.head
    # End writing your code.


# We will utilize the code similar to the following to check your answer.
if __name__ == '__main__':
    test_list = SinglyLinkedList()
    nums = [4,2,3,1,0,5]  # An example.
    for num in nums:
        test_list.insert(num)
    first_node = test_list.head  # Get the first node of the linked list.
    print('The number of nodes in test_list is:')
    p = quick_sort(first_node)
    while p.pointer != None:
        print(p.element)
        p = p.pointer
    print(p.element)
    
