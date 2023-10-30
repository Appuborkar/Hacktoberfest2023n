#Linear search=search by random

def linear_search(list1,n,key):
    for i in range(0,n):
        if (list1[i]==key):
            return i
    return -1 
list1=[7,6,5,4,3,2,1]
key=1
n=len(list1)            
res=linear_search(list1,n,key)
if (res==-1):
    print("Element not found")
else:
    print(f"Element found at index {res}")
