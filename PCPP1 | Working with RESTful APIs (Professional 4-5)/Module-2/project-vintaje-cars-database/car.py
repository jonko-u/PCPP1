

class Car:
    def __init__(self, make, model, year, id=None):
        self.make = make
        self.model = model
        self.year = year
        self.id = id


class CarDatabase:
    def __init__(self):
        self.cars = {}
        self.counter = 0

    def add_car(self, car):
        self.counter += 1
        car.id = str(self.counter)
        self.cars[car.id] = car

    def delete_car(self, car_id):
        if car_id in self.cars:
            del self.cars[car_id]

    def update_car(self, car_id, make=None, model=None, year=None):
        if car_id in self.cars:
            car = self.cars[car_id]
            car.make = make or car.make
            car.model = model or car.model
            car.year = year or car.year
            self.cars[car_id] = car

    def list_cars(self):
        return list(self.cars.values())


# Export the CarDatabase class
car_database = CarDatabase()
