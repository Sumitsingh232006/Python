'''for i in range (1,6):
    print("3 X", i, "=", 3*i)
num = int(input("enter n"))   
for i in range (1,11):
    print(num,"X", i,"=",num*i)

#factorial    
num = int(input("enter n"))
fact=1     
for i in range(num,0,-1):
    fact=fact*i
print("factorial of",num, "is=",fact)

#sum of n natural number
num = int(input("enter n"))
sum=0
for i in range(1, num+1):
    sum=sum+i
print ("sum of first", num, "natural number =",sum)                

#sum of n even natural number
num = int(input("enter n"))
sum=0
for i in range(2,num+1,2):
    sum=sum+i
print(sum)   

n=int(input("enter n"))
mul=1
for i in range(1,n+1):
    mul=mul*i
print(mul) 

# pattern 1 - 2 + 3 - 4 + 5 = 3
n=int(input("enter n"))
sum=0
for i in range(1,n+1):
    if(i%2==0):
        sum=sum-i
    else:
        sum=sum+i     
print(sum)   

# pattern 1 + 2 - 3 + 4 + 5 - 6 + 7 + 8 - 9 = 9       
n=int(input("enter n"))
sum=0
for i in range(1,n+1):
    if(i%3==0):
        sum=sum-i
    else:
        sum=sum+i     
print(sum)  

#pattern 1² - 2² + 3² - 4² + 5² = 15
n=int(input())
sum=0
for i in range(1,n+1):
    if(i%2==0):
        sum=sum-i**2
    else:
        sum=sum+i**2
print(sum)            

#Fibonacci series
n=int(input("enter n"))
a=0
b=1
print(a, end=" ")
print(b, end=" ")
for i in range(n-2):
    c=a+b
    print(c,end=" ")
    a=b
    b=c  
  
#PRIME NUMBER  
n = int(input("enter prime n"))
count=0
for i in range (1,n+1):
    if(n%i==0):
        count+=1
if (count==2):
    print("prime")
else: print("not prime") '''   
            
#palindrome
n = int(input("enter  n"))
p=n
sum=0 
for i in range(n+1>0):
#while(n>0):
    d=n%10
    sum=sum*10+d
    n=n//10
if(sum==p):
    print("palindrome")
else:
    print("not palindrome")          

