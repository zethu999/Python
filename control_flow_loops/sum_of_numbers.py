"""Find sum of given numbers as input"""

count_of_number = int(input("Enter count of numbers: "))
sum = 0
while(count_of_number != 0 ):
    num = int(input("Input Number " + str(count_of_number) + " :"))
    sum += num
    count_of_number -= 1

print(sum)
