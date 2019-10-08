#while statement to sum user numbers
count = 0
total = 0
print("How many numbers should I sum up?")
numbers = int(input())

while count < numbers:
    count += 1
    print("Please enter number " + str(count) + " of " + str(numbers) + ":")
    number = int(input())
    total = total+number

print("The answer is " + str(total))