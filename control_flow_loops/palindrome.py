"""Palindrome number"""

number = int(input("Enter a number: "))

reverse_number = 0
temp_number = number

while(temp_number%10 != 0):
    reverse_number = (reverse_number * 10) + temp_number%10
    temp_number //= 10

if(number == reverse_number):
    print("Palindrome")
else:
    print("Not Palindrome")


