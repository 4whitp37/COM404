#Modules - main

def wordinput():
    print("please enter a word")
    global word
    word = input()
    return word

wordinput()

def options():
    print("These are the options:")
    print("1 - under")
    print("2 - over")
    print("3 - both")
    print("4 - grid")
    print("please select an option 1- 4")

options()
option = str(input())

if option not in [ "1","2","3","4" ]:
    print("That is an invalid option")
    print()
    options()
elif option==str(1):
    from functions import under
elif option==str(2):
     from functions import over
elif option==str(3):
     from functions import both
else:
     from functions import grid
