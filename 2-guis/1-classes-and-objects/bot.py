class Bot:
    def __init__(self, name, age, energy,shield):
        self.name = name
        self.age = age
        self.energy = energy
        self.shield = shield

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_energy(self):
        return self.energy

    def get_shield(self):
        return self.shield

    def decrement_energy(self):
        self.energy -= 1

    def decrement_shield(self):
        self.shield -= 1

    def display_name(self):
        print("--------")
        print("|", self.name, "|")
        print("--------")

    def display_age(self):
          print("     iiiiiiiiii")
          print("   |:",self.age,"today:|")
          print(" __|___________|__")
          print("|^^^^^^^^^^^^^^^^^|")
          print("|                 |")
          print("|                 |")
          print("~~~~~~~~~~~~~~~~~~~")

    def display_energy(self):
        for count in range(0,self.energy):
            print("▯ ",end='')
        print()

    def display_shield(self):
        print("|`-._/\_.-`|")
        print("|          |")
        print("|          |")
        print("|    ", self.shield,"   |")
        print("\   o\/o   /")
        print(" \   ||   /")
        print("  \  ||  /")

    def increment_age(self):
        self.age += 1

    def increment_energy(self):
        self.energy += 1

    def increment_shield(self):
        self.shield += 1

    def display_summary(self):
        self.display_name()
        print()
        self.display_age()
        print()
        self.display_energy()
        print()
        self.display_shield()
        print()

    def __str__(self):
        return "Name: {}, age: {}, energy: {}, shield: {}".format(self.name,self.age,self.energy,self.shield)
