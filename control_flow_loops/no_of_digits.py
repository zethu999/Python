"""Count number of digit in a number"""

num = int(input("Enter a number: "))

count = 0
while(num%10 != 0):
    num = num//10
    count+=1

print(count)