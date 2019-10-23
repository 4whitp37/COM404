#Modules - Functions

from main import wordinput

word = wordinput()

length = len(word)
astericks = "*"
gridrepeat = astericks*length
n = 3

def under(word):
    print(word)
    for position in range(0, len(word), 1):
        print("*",end='')

#under(word)

def over(word):
    for position in range(0, len(word), 1):
        print("*",end='')
    print("\n" + word)

#over(word)

def both(word):
        for position in range(0, len(word), 1):
            print("*",end='')
        print("\n" + word)
        for position in range(0, len(word), 1):
            print("*",end='')
        print()

#both(word)

def grid(word,n):
        for count in range(0, n, 1):
            for number in range(0, n, 1):
                print(gridrepeat + " ",end="")
            print()
            for number in range(0, n, 1):
                print(word+"|",end="")
            print()
        for number in range(0, n, 1):
            print(gridrepeat + " ",end="")
        print()

#grid(word,n)
