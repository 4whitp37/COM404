#for loop - character
number = 0

print("What strange markings do you see?")
markings = str(input())

for position in range(0, len(markings), -1):
    print("index " + str(number) + ": " +  markings[position])
    number = number +1