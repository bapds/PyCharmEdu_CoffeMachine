# our class Ship
class Ship:
    def __init__(self, name, capacity, country):
        self.name = name
        self.capacity = capacity
        self.cargo = 0
        self.country = country

    # the old sail method that you need to rewrite
    def sail(self):
        print("The {} has sailed for {}! ".format(self.name, self.country))


black_pearl = Ship.country("Argentina")
