#while calculate factorial
count = 1
total = 1

print("Please enter a number?")
number = int(input())

while count<=number:
    total = total*count
    count +=1

print("The factorial is " + str(total))