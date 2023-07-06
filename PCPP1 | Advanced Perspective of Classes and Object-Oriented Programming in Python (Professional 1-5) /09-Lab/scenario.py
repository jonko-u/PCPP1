# Level of difficulty
#
# Medium
# Objectives
#
#     improving the student's skills in operating with inheritance and composition
#
# Scenario
#
# Imagine that you are an automotive fan, and you are able to build a car from a limited set of components.
#
# Your task is to :
#
#     define classes representing:
#         tires (as a bundle needed by a car to operate); methods available: get_pressure(), pump(); attribute available: size
#         engine; methods available: start(), stop(), get_state(); attribute available: fuel type
#         vehicle; method available: __init__(VIN, engine, tires); attribute available: VIN
#     based on the classes defined above, create the following objects:
#         two sets of tires: city tires (size: 15), off-road tires (size: 18)
#         two engines: electric engine, petrol engine
#     instantiate two objects representing cars:
#         the first one is a city car, built of an electric engine and city tires
#         the second one is an all-terrain car build of a petrol engine and off-road tires
#     play with the cars by calling methods responsible for interaction with components.


class Tires:
    def __init__(self, size):
        self._size = size
        self._pressure = 0

    def get_pressure(self):
        return self._pressure

    def pump(self, pressure):
        self._pressure = pressure

    @property
    def size(self):
        return self._size


class Engine:
    def __init__(self, fuel_type):
        self._fuel_type = fuel_type
        self._state = "off"

    def start(self):
        self._state = "running"

    def stop(self):
        self._state = "off"

    def get_state(self):
        return self._state

    @property
    def fuel_type(self):
        return self._fuel_type


class Vehicle:
    def __init__(self, VIN, engine, tires):
        self._VIN = VIN
        self._engine = engine
        self._tires = tires

    @property
    def VIN(self):
        return self._VIN

    def start(self):
        self._engine.start()
        print("Vehicle started")

    def stop(self):
        self._engine.stop()
        print("Vehicle stopped")

    def get_engine_state(self):
        return self._engine.get_state()

    def get_tire_pressure(self):
        return self._tires.get_pressure()

    def pump_tires(self, pressure):
        self._tires.pump(pressure)

    @property
    def fuel_type(self):
        return self._engine.fuel_type

    @property
    def tire_size(self):
        return self._tires.size

# Create two sets of tires
city_tires = Tires(15)
off_road_tires = Tires(18)

# Create two engines
electric_engine = Engine("electric")
petrol_engine = Engine("petrol")

# Create two cars
city_car = Vehicle("ABC123", electric_engine, city_tires)
off_road_car = Vehicle("XYZ789", petrol_engine, off_road_tires)

# Start the city car
city_car.start()

# Print the state of the city car engine
print(city_car.get_engine_state())

# Print the tire pressure of the city car
print(city_car.get_tire_pressure())

# Pump the tires of the city car to 30 psi
city_car.pump_tires(30)

# Stop the city car
city_car.stop()

# Start the off-road car
off_road_car.start()

# Print the state of the off-road car engine
print(off_road_car.get_engine_state())

# Print the tire pressure of the off-road car
print(off_road_car.get_tire_pressure())

# Pump the tires of the off-road car to 40 psi
off_road_car.pump_tires(40)

# Stop the off-road car
off_road_car.stop()