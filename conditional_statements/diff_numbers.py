"""Find difference between two numbers and if negative value is the answer, make it positive"""

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if(num1 - num2 > 0) :
    print("+", num1 - num2)
else :
    print("-", -1 * (num1 - num2)) 
