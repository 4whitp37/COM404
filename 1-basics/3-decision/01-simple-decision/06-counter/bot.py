#demonstrate how a variable can be used as a counter
print("Please enter the first whole number.")
number1 = input()
print("Please enter the second whole number.")
number2 = input()
print("Please enter the third whole number.")
number3 = input()

evencount = 0
oddcount = 0

if(int(number1) % 2)==0:
    evencount += 1
else:
    oddcount += 1
if(int(number2) % 2)==0:
    evencount += 1
else:
    oddcount += 1
if(int(number3) % 2)==0:
    evencount += 1
else:
    oddcount += 1

#evencount = even + even2 + even3
#oddcount = 3 - evencount

print ("There were " + str(evencount) + " even and " + str(oddcount) + " odd numbers")
