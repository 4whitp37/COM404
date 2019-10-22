#functions
#hero1 = "Wonder Woman"
#hero2 = "Superman"

def  is_league_united(hero1, hero2):
    if (hero1 =="Superman" or hero2=="Superman") and (hero1 =="Wonder Woman" or hero2 == "Wonder Woman"):
        return "True"
    else: 
        return "False"

#is_league_united(hero1,hero2)

def decide_plan(hero1,hero2):
    if is_league_united(hero1, hero2) == "True":
        print("Time to save the world!")
    else: print("We must unite the league!")

#decide_plan(hero1,hero2)

def run():
    print("Please enter the first hero's name")
    hero1 = input()
    print("Please enter the second hero's name")
    hero2 =  input()
    print("League or Plan?")
    answer = input()

    if answer=="League":
        print(is_league_united(hero1,hero2))
    elif answer== "Plan":
        decide_plan(hero1,hero2)

# Run the program
run()




