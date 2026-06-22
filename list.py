""" list=[10,20,30,40,50,60]
print("list",list)
print("first element = ",list[0])
print("last element",list[5])
print("second element",list[-5])
print("second last element",list[-2])
print("lenght",len(list))

#Adding elements in empty list we use append()
number=[]
number.append(10)
number.append(904)
print(number)
number= [90,80]
number.append(10)
number.append(20)
print(number)
print(number[len(number)-1])

#Taking input from user one number
number=[]
num=int(input("enter n"))
number.append(num)
print(number)  

#Taking multiple enter from user
print("enter 3 number")
number=[]
for i in range(3):
    num=int(input())
    number.append(num)
print(number) 
    
n=(int(input("how many elements?")))
number=[]
for i in range(n):
    y=int(input())
    number.append(y)
print(number)

#Element Traversal
numbers=[12,24,36,48,60]
for elements in numbers:
    print(elements)

#Index traversal    
numbers = [5, 10, 15]
for i in range(len(numbers)):
    print(numbers[i])   
    
n= int(input("enter no. of elements"))
number=[]
for i in range(n):
    z=int(input())
    number.append(z)
for element in range(len(number)):
    print("Index ",element,"=",number[element])
    
#print only odd number    
n= int(input("enter no.of element"))
number=[]
for i in range(n):
    num=int(input())
    number.append(num)
for x in number:
    if (x%2!=0):
        print("odd=",x)    
 """ 
#Reverse print        
number=[1,5,4,7,8,2]
for i in range((len(number)-1),-1,-1):
    print(number[i])
    
N=int(input("no. of element"))
q=[]
for i in range(N):
    e=int(input())
    q.append(e)
for j in range((len(q)-1),-1,-1):
    print("Index ",j,"= ",q[j] )    

#Updating value
number=[2,4,5,7,9,0]
number[3]=34
print(number)

n=int(input('enter n'))
number=[]
for i in range(n):
    q=int(input())
    number.append(q)
t=int(input("enter index you want to update"))
u=int(input("enter new value"))
number[t]=u
print(number)

n= int(input("enter n"))
lists=[]
for i in range(n):
    w=int(input())
    lists.append(w)
q=int(input("enter index"))    
lists[q]=lists[q]*2
print(lists)

#List slicing
a = [10, 20, 30, 40, 50, 60]
print(a[::2])
print(a[:])
print(a[-3:])
print(a[:-2])
print(a[::-1])

#Membership Operators in Lists gives TRUE or FALSE  
number=[7,8,5,88,96]
print(6 in number)
print(88 in number)
print(96 not in number)

#LIST METHOD
#1) APPEND() => (element which you want to add)
u=[8,9,0,7]
u.append(3)
u.append(5)
print(u)

#2) INSERT METHOD => (index,element which you want to add)
s=[6,7,9,3]
s.insert(2,8)
print(s)

#3)REMOVE => (value which you want to remove)
y=[3,8,7,5,9,8]
y.remove(8)
print(y)

#4) POP  =>(index)
a=[5,7,9,6,8]
a.pop(3)
print(a)

