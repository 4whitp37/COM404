#work out what the smallest number is
print("please enter the first number.")
number1 = input()
print("please enter the second number.")
number2 = input()
if number1 < number2:
    print("the first number is smallest")
elif number2 < number1:
    print("the second the number is smallest")
else: 
    print("the numbers are equal")