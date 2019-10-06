#multiple nested decision
print("where should I look?")
location = input()
if location=="in the bedroom":
    print("where in the bedroom should I look?")
    bedroomlocation= input()
    if bedroomlocation == "under the bed":
        print("Found some shoes but no battery")
    else:
         print("Found some mess but no battery.")
if location=="in the bathroom":
    print("where in the bathroom should I look?")
    bathroomlocation= input()
    if bathroomlocation == "in the bathtub":
        print("Found a rubber duck but no battery")
    else:
         print("It is wet but I found no battery")
if location=="in the lab":
    print("where in the lab should I look?")
    lablocation= input()
    if lablocation == "on the table":
        print("Yes! I found my battery!")
    else:
         print("Found some tools but no battery")
else: print("I do not know where that is but I will keep looking.")