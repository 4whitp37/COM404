#for loop - text in reverse
#word = ""

print("What phrase do you see?")
phrase = str(input())
print("Reversing...")
print()
print("The phrase is: ")

for position in range(len(phrase)-1,-1, -1):
    print( phrase[position], end='')
print()