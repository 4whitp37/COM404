#function with return value
def sum_weights(Beep_weight,Bop_weight):
        total_weight = int(Beep_weight) + int(Bop_weight)
        return total_weight

def calc_avg_weight(Beep_weight,Bop_weight):
        avg_weight = (sum_weights(Beep_weight,Bop_weight) / 2)
        return avg_weight
    
def run():
    print("What is the weight of Beep?")
    Beep_weight = input()
    print("What is the weight of Bop?")
    Bop_weight = input()
    print("What would you like to calcluate (sum or average)?")
    calculate = input()

    if calculate == "sum":
        print("The " + calculate + " of Beep and Bop's weight is " + str(sum_weights(Beep_weight,Bop_weight)))
    if calculate == "average":
        print("The " + calculate + " of Beep and Bop's weight is " + str(calc_avg_weight(Beep_weight,Bop_weight)))
    
run()


