from superbot import SuperBot

class FlyingBot(SuperBot):
    def __init__(self, name, age, energy,shield,super_power_level,hover_distance):
        super().__init__(name, age, energy,shield, super_power_level)
        self.__hover_distance = hover_distance

        def get_hover_distance(self):
            return self.__hover_distance