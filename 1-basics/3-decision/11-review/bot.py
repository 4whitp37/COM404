#review - which bird
print("What colour was the bird?")
colour = input()
if colour=="black":
    print("It was a blackbird!")
elif ((colour=="brown") or (colour=="grey")):
    print("was it bigger than a blackbird?")
    size = input()
    print("was it in a flock?")
    flock = input()
    if ((size=="yes") and (flock=="no")):
        print("it was a mistle thrush!")
    elif ((size=="yes") and (flock=="yes")):
        print("it was a fieldfare!") 
    elif ((size=="no" and flock=="yes")):
        print("it was a redwing!")  
    else: print("it was a song thrush!")
else: print("it wasn't a thrush!")