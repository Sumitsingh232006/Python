#WHILE LOOP
'''INITIALIZER
    CONDITION
    WORK
    REPEAT '''
"""
i=1
product=1
while i<=10:
    product=product*i
    print(5*i)
    i=i+1
    
n=int(input("enter n"))
i=1
sum=0
while(i<=n):
    if(i%2==0):
        sum=sum+i
    i+=1
print(sum)        
    
n=10
i=1
count=0
while(i<=n):
    if(i%2==0):
        count+=1
    i+=1
print(count)    

n=4
z=1
sum=0
while(z<=n):
    i=z**2
    sum=sum+i
    z+=1
print(sum)   

n= int(input("enter n"))
count=0
while(n>0):
    n=n//10
    count+=1
print(count)  """   

# n=123456
# count=0
# ecount=0
# while(n>0):
#     digit=n%10
#     n=n//10
#     count+=1
    
#     if(digit%2==0):
#         ecount+=1
            
# print(count)
# print(ecount) 

# n=1234

# sum=0
# while(n>0):
#     digit=n%10
#     n=n//10
#     sum=sum+digit
    
# print(sum)    
"""   
n = int(input("enter n"))
largest =0
while(n>0):
    digits=n%10
    if(digits>largest):
        largest=digits
    n=n//10
print(largest)    
    
   
n=int(input("enter the number"))
rev=0
while(n>0):
    digits=n%10
    n=n//10
    rev=rev*10+digits
print("reverse is",rev)    

n= int(input("enter n "))
d=n
rev=0
while(n>0):
    digits=n%10
    n=n//10
    rev=rev*10+digits
print(rev)    
if(rev==d):
    print("palindrome")
else: print("not palindrome")
 """
        
#smallest        
'''
n= int(input("enter the number"))
smallest=9
while(n>0):
    digits=n%10
    if(smallest>digits):
        smallest=digits
    n=n//10    
print(smallest)   

#ARMSTRONG
n= int(input("enter the number"))
d=n
sum=0
while(n>0):
    digits=n%10 # 3        5      0
    cube=digits**3 # 27    125    1
    sum=sum+cube #27       152    153
    n=n//10         #15      1      0
if(d==sum):
    print("armstrong")
else:
    print("not armstrong")
    
#factorial
n=int(input("enter the number"))  #145
d=n                                #145
sum=0
while(n>0):
    fact=1 
    i=1             
    digits=n%10         
    while(i<=digits):
        fact=fact*i
        i+=1 
    sum=sum+fact              
    n=n//10          
print(sum)        
if(sum==d):
    print(d,"is strong number")
else:
    print(d,"is not strong number")   
    
#Fibonacci sequence 0, 1, 1, 2, 3, 5, 8, 13... 
# in this use the last two numbers to print upcoming number
n=int(input("enter n"))
a=0
b=1
count=0
while(count<n):
    print(a)
    count+=1
    c=a+b
    a=b
    b=c '''
    
    #Checking prime numbers
num=int(input("enter number"))
count=0
i=1
while(i<=num):
    
    if(num%i==0):
        count=count+1
    i+=1
if(count==2):
    print("prime")
else:
    print("odd number")    

n=5
count=0
i=0
while(i<n+1):
    i+=1
    if(n%i==0):
        count+=1
        
if(count==2):
    print("prime")        
        
num = 1

while(num <= 50):
    count = 0
    i = 1

    # check factors of num

    num += 1     
        