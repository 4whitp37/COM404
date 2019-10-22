#Nesting
health = 100


for position in range(0,5,1):
    print("...Oh dear, who is that?")
    answer = input()
    if(answer == "Smiler's Bot"):
        print("Time to jam out of here!")
        health = health-20
    elif(answer == "Hacker"):
        print("Yay! Better follow this one!")
        health = health+20
    else:
        print("Phew, just another emoji!")
    print()

print("Escaped! Health is " + str(health) +  "%")
    

