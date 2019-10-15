#multiple functions
def display_ladder(steps):
    for count in range(0,int(steps),1):
            print("| |")
            print("***")
            
def create_ladder():
    print("how many steps remain?")
    steps = input()
    display_ladder(steps)

create_ladder()