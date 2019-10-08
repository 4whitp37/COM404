#while ascii
chargingbars = 0
message = str("Charging: █")
print("How many bars should be charged?")
bars = int(input())

while(chargingbars < bars):
    print(message)
    message = message + " █"
    chargingbars = chargingbars +1

if chargingbars==5:
    print()
    print("The battery is fully charged.")
    