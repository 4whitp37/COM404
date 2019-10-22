#Modules - Functions

print("please enter a word")
word = input()
n = 3

def under(word):
    print(word)

    for position in range(0, len(word), 1):
        print("*",end='')
print()

#under(word)

def over(word):
    for position in range(0, len(word), 1):
        print("*",end='')
    print("\n" + word)

print()

#over(word)

def both(word):
        for position in range(0, len(word), 1):
            print("*",end='')
        print("\n" + word)
        for position in range(0, len(word), 1):
            print("*",end='')
        print()

#both(word)



#def grid(word,number):
for count in range(1, n, 1):
        both(word)
    #for count in range(1, n, 1):
        #for position in range(0,len(word),1):
        


            #print("*", end="")
    #print(" ")
            #print("\n" + word + " | ")
        #for position in range(0, len(word), 1):
         #   print("*",end='')

    #print()



#        for position in range(0, len(word), 1):
#            print("*",end='')
#        print("\n" + word + " | ")
#        for position in range(0, len(word), 1):
#            print("*",end='')
