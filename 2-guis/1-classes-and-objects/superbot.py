from bot import Bot

class SuperBot(Bot):
    def __init__(self, name, age, energy,shield,super_power_level):
        super().__init__(name, age, energy,shield)
        self.__super_power_level = super_power_level

        def get_super_power_level(self):
            return self.__super_power_level
