"""Calculate discounted when amount<=1000 and other condtions"""

amt = int(input("Enter amount: "))

if(amt <= 1000):
    print("10"+"%"+" discount applied total amount to pay: ",amt - ((amt*10)/100))
elif(amt > 1000 and amt <= 5000):
    print("20"+"%"+" discount applied total amount to pay: ",amt - ((amt*20)/100))
elif(amt > 5000 and amt <= 10000):
    print("30"+"%"+" discount applied total amount to pay: ",amt - ((amt*30)/100))
else:
    print("50"+"%"+" discount applied total amount to pay: ",amt - ((amt*50)/100))
