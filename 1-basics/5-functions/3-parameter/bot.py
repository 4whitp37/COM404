#function with parameter
def escape_by(plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    if plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    if plan == "going deeper":
        print("That might just work! Let's go deeper!")

escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")  