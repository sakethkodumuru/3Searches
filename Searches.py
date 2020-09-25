print("Welcome to Searching Techniques by Bhargav , Phani and Saketh")
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
#hash search implementation
def hash(lis):
    x = lis%a
    k = 0
    succ = None
    while l[x]!=0 and k<max_trails:
            x = (x+1)%a
            k = k+1
            succ = "Not"
    if(l[x]==0):
        l[x] = lis
        succ = 1
    return succ

def search(lstt,target):
    index = target % a
    k=0
    suc = 0
    print(lstt)
    while lstt[index]!= target and k<max_trails:
        index = (index+1) % a
        k = k+1
    if(lstt[index]==target):
        return index+1

print("enter 1. Binary Search  \n 2. Hash search \n 3. linked list search")

ch = int(input("choose any"))
if ( ch ==1):
    start = 0
    end = a-1
    count = 0
    while start <= end:
        count = count +1
        mid = int((start+end)/2)
        if s == lst[mid]:
            print ("element found at ", mid+1)
            break
        elif s> lst[mid] :
            start = mid+1
        else:
            end = mid-1
        if count == a-1:
            print("element not found :(")

elif (ch==2):
    for i in range(0,a):
        if (hash(lst[i])==0) :
            print("value not inserted")
            break
    print("the value u r searching is found at ",search(l,s)," position")
elif(ch==3):
    llist = LinkedList()
    def link_search(lst, target):
        for i in range(0, len(lst)):
            llist.push(lst[i])

        if llist.search(target):
            print("found at ",(len(lst)-llist.search(target) +1), " position")
        else:
            print("element not No")
    link_search(lst, s)
else:
    print("please choose a valid option")
