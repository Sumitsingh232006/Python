'''n=int(input("enter number"))
if(n>0):
    print(n,"is positive number")
else:print(n,"is not positive  number")    

age=int(input("enter age"))
if(age>=18):
    print("eligible to vote")
else:print("not eligible to vote")    

n=int(input("enter the number"))
if(n%2==0):
    print("even number")
else:
    print("odd number")    

a= int(input("enter first number"))
b= int(input("enter second number"))
if(a>b):
    print(a,"is larger")
elif(a<b):
    print(b,"is greater")    
else:
    print("both number are equal")    
    
    marks= int(input("enter number"))
    if(marks>=90):
        print("grade a")
    elif(marks>=75):
        print("grade b")
    elif(marks>=50):
        print("c grade")
    else:
        print("fail")    
            
n=int(input("enter the number"))
if(n>0):
    n=n**2
    print(n)
else:
    n=n**3
    print(n)    
    
a= int(input("enter first number"))
b= int(input("enter second number"))
c= int(input("enter third number"))
if(a>b and a>c):
    print(a,"is largest")
elif(b>a and b>c):
    print(b"is largest")    
else:
    print(c," is largest")   '''
    
n=int(input("enter the number"))
if(n>0):
    if(n%2==0):
        print("positive even number")
    if(n%2!=0):print("positive odd number")
        
elif(n<0):print("negative number")
else: print("zero number")            
    
age=int(input("enter age"))
marks=int(input("enter marks"))
if(age>=18):
    if(marks>=50):
        print("eligible")
    else:print("Not eligible due to low marks")
elif(age<18):
    print("not eligible due to age")            
    
    #LEAP YEAR
year=int(input("enter year"))
if(year%4==0 and year%100!=0 ) or ( year%400==0):
    print(year,"is leap year")
else:
    print(year,"is not leap year")
                
        