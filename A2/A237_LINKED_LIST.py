class Node1:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)


def print_list(node):
    while node is not None:
        print(node, end=" ")
        node = node.next
    print()

def print_backward(list):
    if list is None: return
    print_backward(list.next)
    print(list, end=" ")

def print_backward_nicely(list):
    print("[", end=" ")
    print_backward(list)
    print("]")

def remove_second(list):
    if list is None: return
    first = list
    second = list.next
    first.next = second.next
    second.next = None
    return second

node1 = Node1(1)
node2 = Node1(2)
node3 = Node1(3)

node1.next = node2
node2.next = node3

print_list(node1)

print_backward(node1)
print()
print_backward_nicely(node1)

print_list(remove_second(node1))
print_list(node1)


#
print()
#

class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        
    def print_backward(self):
        print("[", end=" ")
        if self.head is not None:
            self.head.print_backward()
        print("]")

    def add_first(self, cargo):
        node = Node2(cargo)
        node.next = self.head
        self.head = node
        self.length += 1

class Node2:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next  = next

    def __str__(self):
        return str(self.cargo)
    
    def print_backward(self):
        if self.next is not None:
            tail = self.next
            tail.print_backward()
        print(self.cargo, end=" ")


n1 = Node2(1)
n2 = Node2(2)
n3 = Node2(3)

n1.next = n2
n2.next = n3

l=LinkedList()
l.head=n1
l.print_backward()
print()

l.add_first(0)

l.print_backward()

