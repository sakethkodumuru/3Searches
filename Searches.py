Print("Welcome to Searching Techniques by Bargav , Phani and Saketh")
a = int(input("enter the no. of elements "))
lst = []
l = [0]*a
max_trails = 3
for i in range(0, a):
    ele = int(input("enter ur element "))
    lst.append(ele)

s = int(input("enter the element to be searched "))
# linked list implementation


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def search(self, x):
        c = 0
        current = self.head
        while current != None:
            c += 1
            if current.data == x:
                return c

            current = current.next
        return False
