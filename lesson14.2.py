class Transprot(object):
    name  = 'Renault Logan'
    capacity = 50 

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
    
    def seating_capacity(self):
        print(f'Вместимость одного автобуса:{self.name}, {self.capacity}: пассажиров')

autobus = Transprot('Renault Logan', 50)
autobus.seating_capacity()