"""Print a multiplation table of a given number"""

num = int(input("Enter a number: "))
i=0
while(i <= 10):
    print(str(num) + " x " + str(i) + " = " + str(num*i))
    i+=1