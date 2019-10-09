#for loop - text in reverse
word = ""

print("What phrase do you see?")
phrase =str(input())

for position in range(0,len(phrase), -1):
    print("The phrase is: " + phrase[position])
    #number = number +1

