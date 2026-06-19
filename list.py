list=[10,20,30,40,50,60]
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