#for loop - count down
count = 0

print("How far are we from the cave?")
steps = int(input())

for count in range(steps,count,-1):
    print(str(steps) + " steps remaining")
    steps = steps -1