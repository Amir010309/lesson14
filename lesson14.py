class Transport(object):
    name = 'Renault Logan'
    max_speed = 120
    milage = 12


    def __init__(self, name, max_speed, mileage):
       self.name = name
       self.max_speed = max_speed
       self.mileage = mileage
    
    def hello(self):
        print(f'Название автомобиля:{self.name}, Скорость:{self.max_speed}, Пробег:{self.milage}')

autobus = Transport('Renault Logan', 120, 12)

autobus.hello()