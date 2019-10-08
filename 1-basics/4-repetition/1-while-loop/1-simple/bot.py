#while statement
removedcables = 0

print("How many cables should I remove?")
cables = int(input())

while(cables > removedcables):
    print("Removed cable.")
    removedcables = removedcables + 1
