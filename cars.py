class Car:
    manufacturer = "Skoda"

    def __init__(self, doorNum, wheelNum, color, cylNum):
        self.doors = doorNum
        self.wheels = wheelNum
        self.color = color
        self.cylinders = cylNum


def printCar(car):
    print(f'This car has {car.doors} doors, \
{car.wheels} wheels, \
its {car.color} and has {car.cylinders}. \
It is manufactured by {car.manufacturer}')


car1 = Car(4, 2, "red", 4)
printCar(car1)
