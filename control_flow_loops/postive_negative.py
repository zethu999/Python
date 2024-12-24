"""Find postive sum and negative sum"""

count_of_number = int(input("Enter count of numbers: "))
psum = 0
nsum = 0
while(count_of_number != 0 ):
    num = int(input("Input Number " + str(count_of_number) + " :"))
    if( num >=0 ):
        psum += num
    else:
        nsum += num
    count_of_number -= 1

print(psum,nsum)
