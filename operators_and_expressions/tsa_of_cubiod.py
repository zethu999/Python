""" Calculate total surface area of cubiod """

l = int(input("Enter lenght of cubiod: "))
b = int(input("Enter breadth of cubiod: "))
h = int(input("Enter height of cubiod: "))

tsa = 2 * (l*b + b*h + h*l)
print(tsa)