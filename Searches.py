print("Welcome to Searching Techniques by Bhargav , Phani and Saketh")
a = int(input("enter the no. of elements "))
lst =[]
l= [0]*a
max_trails = 3
for i in range(0,a):
    ele = int(input("enter ur element "))
    lst.append(ele)

s =int(input("enter the element to be searched "))

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