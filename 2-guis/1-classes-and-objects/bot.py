class Bot:
    def __init__(self, name, age, energy,shield):
        self.__name = name
        self.__age = age
        self.__energy = energy
        self.__shield = shield

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_energy(self):
        return self.__energy

    def get_shield(self):
        return self.__shield

    def decrement_energy(self):
        self.__energy -= 1

    def decrement_shield(self):
        self.__shield -= 1

    def display_name(self):
        print("--------")
        print("|", self.__name, "|")
        print("--------")

    def display_age(self):
          print("     iiiiiiiiii")
          print("   |:",self.__age,"today:|")
          print(" __|___________|__")
          print("|^^^^^^^^^^^^^^^^^|")
          print("|                 |")
          print("|                 |")
          print("~~~~~~~~~~~~~~~~~~~")

    def display_energy(self):
        for count in range(0,self.__energy):
            print("▯ ",end='')
        print()

    def display_shield(self):
        print("|`-._/\_.-`|")
        print("|          |")
        print("|          |")
        print("|    ", self.__shield,"   |")
        print("\   o\/o   /")
        print(" \   ||   /")
        print("  \  ||  /")

    def increment_age(self):
        self.__age += 1

    def increment_energy(self):
        self.__energy += 1

    def increment_shield(self):
        self.__shield += 1

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
