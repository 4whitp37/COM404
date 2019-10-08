#while count statement
livecables = 0
print("How many live cables must I avoid?")
cables = int(input())

while(cables > livecables):
    count = livecables + 1
    print("Avoiding...Done! " + str(count) + " live cables avoided.")
    livecables = livecables + 1