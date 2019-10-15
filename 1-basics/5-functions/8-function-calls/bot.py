#function-calls

word="Hello"

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
        
displaymirrored(word)