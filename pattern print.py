"""for i in range(1,4):           # pattern
    for j in range(1,4):       # ***
        print("*", end=" ")    # ***
    print()                    # ***
    
for i in range(1,4):           #pattern
    for j in range(1,4):       # 1 2 3
        print(j,end=" ")       # 1 2 3
    print()                    # 1 2 3

for i in range(1,4):           #pattern
    for j in range(1,4):       # 1 1 1
        print(j,end=" ")       # 2 2 2
    print()                    # 3 3 3
    
for i in range(1,4):            #pattern
    for j in range(1,4):        # 2 3 4
        print(i + j, end=" ")   # 3 4 5
    print()                     # 4 5 6
    
for i in range(1,4):            #pattern
    for j in range(1,i+1):        # *
        print("*", end=" ")       # * *
    print()                       # * * *

for i in range(1,5):          #pattern
    for j in range(1,6-i):    # * * * *
        print("*",end=" ")    # * * *
    print()                   # * *
                              # *
                              
for i in range(1,5):           #pattern
    for j in range(1,i+1):     # 1
        print(j,end=" ")       # 1 2
    print()                    # 1 2 3
                               # 1 2 3 4              

for i in range(1,5):           #pattern
    for j in range(1,i+1):     # 1
        print(i, end=" ")      # 2 2
    print()                    # 3 3 3
                               # 4 4 4 4

for i in range(1,5):           #pattern
    for j in range(i,0,-1):    # 1
        print(j, end=" ")      # 2 1
    print()                    # 3 2 1
                               # 4 3 2 1
"""
num = 1                         # pattern
for i in range(1,5):            # 1
    for j in range(1,i+1):      # 2 3
        print(num, end=" ")     # 4 5 6
        num=num+1               # 7 8 9 10
    print()    

num=1
for i in range(1,4):           #pattern
    for j in range(1,i+1):     #1
        print(num, end=" ")    #2 3
        num+=1                 # 4 5 6
    print()    

num = 10
for i in range (1,4):            #pattern
    for j in range(1,i+1):       #10
        print(num, end=" ")      #11 12 
        num+=1                   #13 14 15
    print()                      

num=2
for i in range (1,4):        #pattern
    for j in range(1,1+i):   # 2
        print(num, end=" ")  # 4 6
        num=num+2            # 8 10 12
    print()    

for i in range(1,5):                     #pattern
    for j in range(1,i+1):               # A
        print(chr(64+j), end = " ")      # A B
    print()                              # A B C 
                                         # A B C D

for i in range(1,4):                 #pattern
    for j in range(1,1+i):           # A
        print(chr(64+i), end=" ")    # B B
    print()                          # C C C

                                     # pattern
for i in range(1,5):                 # D
    for j in range(1,i+1):           # D C
        print(chr(69-j), end=" ")    # D C B
    print()                          # D C B A
 
ch=65                                # pattern
for i in range (1,5):                # A
    for j in range(1,i+1):           # B C
        print(chr(ch), end = "")    # D E F
        ch+=1                        # G H I J
    print()       