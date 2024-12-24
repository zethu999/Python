"""Find maximum number"""

n = int(input("Enter count of numbers: "))

max = 0
while( n!=0 ):
    num = int(input("Enter number: "))
    if( num > max ):
        max = num
    n -= 1

print(max)