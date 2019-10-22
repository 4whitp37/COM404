#Loop
count = 0

print("How many zones must I cross?")
zones = int(input())
print("Crossing zones...")
for count in range(zones,count,-1):
    print("...crossed zone " + (str(zones)))
    zones = zones -1
print("Crossed all zones. Jumanji!")


