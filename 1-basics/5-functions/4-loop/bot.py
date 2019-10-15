#loop with function
def cross_bridge(steps):
    for count in range(0,steps,1):
        print("crossed step")
    if steps < 6:
        print("The bridge is collapsing!")
    else: print("We must keep going!")

cross_bridge(3)
cross_bridge(6)
