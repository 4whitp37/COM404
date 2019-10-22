#function-calls

word="Hello"
timestorepeat = 5

def displaybox(word):
    print("------")
    print("|" + word + "|")
    print("------")

displaybox(word)

def displaylowercase(word):
        print(word.lower())

displaylowercase(word)

def displayuppercase(word):
        print(word.upper())

displayuppercase(word)

def displaymirrored(word):
    for position in range(len(word)-1,-1, -1):
        print(word[position], end='')
    print()
    print()
        
displaymirrored(word)

def displayrepeat(word, timestorepeat):
    for count in range(0,timestorepeat,1):
        print(word.lower()),(word.upper())
        

displayrepeat(word, timestorepeat) 

