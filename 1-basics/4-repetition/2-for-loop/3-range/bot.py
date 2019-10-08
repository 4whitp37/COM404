#for loop - range
brightnesslevel = str("**")
print("What level of brightness is required?")
brightness = int(input())

print("Adjusting brightness...")
print()

for count in range(1,brightness,2):
    Beepbrightness = ("Beep's brightness level: " + str(brightnesslevel))
    Bopbrightness = ("Bop's brightness level: " + str(brightnesslevel))
    print(Beepbrightness)
    print(Bopbrightness)
    brightnesslevel = brightnesslevel + str("**")
    
    ##beepbrightness = beepbrightness + beepbrightness

