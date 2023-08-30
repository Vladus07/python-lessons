class Machine:
    def __init__(self, material, mechanism):
        self.material = material
        self.mechanism = mechanism


class Bicycle(Machine):
    def __init__(self, material, date_of_production, durability):
        super().__init__(material, "Mechanical")
        self.date_of_production = date_of_production
        self.durability = durability


class Car(Machine):
    def __init__(self, material, brand, date_of_production, transmission):
        super().__init__(material, "Motor")
        self.brand = brand
        self.date_of_production = date_of_production
        self.transmission = transmission



