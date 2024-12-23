"""Find sum of digits in a number"""

num = int(input("Enter a number: "))

sum = 0
while(num%10 != 0):
    sum += num%10
    num//=10

print(sum)
