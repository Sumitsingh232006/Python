#Data Type
city="Agra"
print(type(city))

#Indexing
District="KANPUR"
print(District[0])
print(District[1])
print(District[5])
print(District[-1])
print(District[-4])
print(District[-5])

#String Slicing
name = "SUMIT"
print(name[0:3])   
print(name[:2])   
print(name[3:])
print(name[:])  
print(name[-4:-1])  
print(name[-3:])
print(name[:-1])
print(name[::-1])
print(name[::-2])
print(name[1:-2])
print(name[5:0:-2])

print("Hi" * 3)  #  * repeats a string.

# String Methods
name="sumit Singh"
print(name.upper())
print(name.lower())
name = "sumit"
name = name.upper()
print(name)
name = "my name is sumit "
print(name.title())
print(name.capitalize())
print(name.strip())
name="my name is sumit"
print(name.replace("sumit","Sumit Singh"))
print(name.count("i"))
print(name.find("t"))
print(name.find("z"))
name="PYTHON"
print(name.endswith("ON"))
print(name.startswith("YT"))

name="SUMIT"  #count characters
count=0
for ch in name:
    count+=1
print(count) 

name="SUMIT"  #counting vowels
count=0
for ch in name:
    if ch in"aeiouAEIOU":
        count+=1
        print(ch)    
print(count)    

name="SuMiT"     #Count Uppercase Letters
count=0
for ch in name:
    if ch.isupper():
        count+=1
print(count)        

name="SUMIT"    #Reverse a string
rev=""                 
for ch in name:
    rev=ch+rev
print(rev)    

name="BANANA"
count=0
for ch in name:
    if (ch == "N"):
        count+=1
print(count)       

name="BANANA"
for ch in name:
    if (ch=="A"):
        continue
    print(ch,end="") 
print()       
    
n= "radar"     #palindrome
rev=""
for ch in n:
    rev=ch+rev
if(rev==n):
    print("palindrome")
else:
    print("not palindrome")    
      

fruit="banana"       #Frequency of characters
result=""
for ch in fruit:
    if ch not in result:
        result=result+ch
print(result) 
for ch in result:
    count=0
    for x in fruit:
        if (x==ch):
            count+=1
    print(ch,":",count)           


fruit="banana"           #Remove Duplicates
result=""
for ch in fruit:
    if ch not in result:
        result=result+ch
print(result)

#password check
password= (input("enter your passord"))    
print(password)
if (len(password)<8):
    print("please re enter your 8 alphanumeric password")
else:
    upper=0
    lower=0
    digit=0
    for ch in password:
        if ch.isupper():
            upper+=1
        if ch.islower():
            lower+=1  
        elif ch.isdigit():
            digit+=1      
    print(upper)   
    print(digit)  
    print(lower)
    if(upper!=0 and lower!=0 and digit!=0):
        print("entered password is corect")
    else:
        print("invalid password") 
      
email=input("enter email id")
print(email)
if "@" in email and "." in email:
    print("email id is valid")
else:
    print("email id is invalid")  
    
        