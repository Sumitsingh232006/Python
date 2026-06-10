#ARITHMETIC OPERATOR
'''
print(15/3)  #/ gives float value
print(15%4)
print(3**2)
print(16//3) #// gives quotient

#LOGICAL OPERATOR
print(5>8 and 6>3)   # for and both statment must be true
print(4>1 or 5<3)    # for or only one statement must be true
print(not False)     # reverse the given'''

#MEMBERSHIP OPERATOR
"""name=("python")
print("p" in name)
name = ("singh")
print("g" not in name)
name=("sumit")
print("f" in name)

#IDENTITY OPERATOR
x=10
y=20
print(x is y) # both same true. if not same false
print(x is not y)

#BITWISE OPERATOR
print(5&3)
print(5|3)

#SWAPPING
a=10
b=20
temp =a
a=b
b=temp
print(a,b)
a = 10
b = 20
a,b = b,a  # pyhton shortcut for swapping
print(a,b)"""

#SIMPLE CALCULATOR

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
add= num1+num2
sub=num1-num2
multiply=num1*num2
divide=num1/num2
print("addition=",add)
print("subtraction=",sub)
print("multiplication=",multiply)
print("division=",divide)

# 1. Take the inputs from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# 2. Ask the user for the mathematical operation they want
print("\nChoose an operator: +, -, *, /")
operator = input("Enter your choice: ")

# 3. Use match-case to process only the chosen math rule
match operator:
    case "+":
        print("Addition =", num1 + num2)
    case "-":
        print("Subtraction =", num1 - num2)
    case "*":
        print("Multiplication =", num1 * num2)
    case "/":
        # Python handles float division automatically
        print("Division =", num1 / num2)
    case _:
        print("Error: Invalid Operator selected!")