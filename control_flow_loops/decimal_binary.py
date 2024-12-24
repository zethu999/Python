"""Convert a decimal to binary"""

n = int(input("Enter a number: "))

binary = ''
while (n > 0):
    r = n % 2
    n = n // 2
    binary = str(r) + binary

print(binary)
