"""
Objectives

Learn how to:

    use the json module and its basic facilities;
    encode and decode JSON strings from/to Python objects.

Scenario

Take a look at these two screenshots. They present two different use cases of the same program:
python project.py
Press 1 to produce a JSON string describing a vehicle
Press 2 to decode a JSON string into vehicle data
Your choice: 1
Registration number: PC389272
Year of production: 2018
Passenger [y/n]: n
Vehicle mass: 1543.2
Resulting JSON string is:
{"registration_number": "PC389272", "year_of_production": 2018, "passenger": false, "mass": 1543.2}
Done

Your choice: 2
Enter vehicle JSON string: {"registration_number": "PC389272", "year_of_production": 2018, "passenger": false, "mass": 1543.2}
{'registration_number': 'PC389272', 'year_of_production': 2018, 'passenger': False, 'mass': 1543.2}

Your task is to write a code which has exactly the same conversation with the user and:

    defines a class named Vehicle, whose objects can carry the vehicle data shown above (the structure of the class should be deducted from the above dialog — call it "reverse engineering" if you want)
    defines a class able to encode the Vehicle object into an equivalent JSON string;
    defines a class able to decode the JSON string into the newly created Vehicle object.

Of course, some basic data validity checks should be done, too. We're sure you're careful enough to protect your code from reckless users.
"""
import json

class Vehicle:
    def __init__(self, registration_number, year_of_production, passenger, mass):
        self.registration_number = registration_number
        self.year_of_production = year_of_production
        self.passenger = passenger
        self.mass = mass

class VehicleEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Vehicle):
            return {
                "registration_number": obj.registration_number,
                "year_of_production": obj.year_of_production,
                "passenger": obj.passenger,
                "mass": obj.mass,
            }
        return super().default(obj)

class VehicleDecoder(json.JSONDecoder):
    def decode(self, s, _w=json.decoder.WHITESPACE.match):
        dict_obj = super().decode(s, _w)
        return Vehicle(
            dict_obj["registration_number"],
            dict_obj["year_of_production"],
            dict_obj["passenger"],
            dict_obj["mass"],
        )

def validate_registration_number(registration_number):
    if len(registration_number) != 8:
        raise ValueError("Registration number must be 8 characters long.")
    if not registration_number.isalnum():
        raise ValueError("Registration number can only contain letters and digits.")

def validate_year_of_production(year_of_production):
    if not isinstance(year_of_production, int):
        raise ValueError("Year of production must be an integer.")
    if year_of_production < 1900 or year_of_production > 2100:
        raise ValueError("Year of production must be between 1900 and 2100.")

def validate_passenger(passenger):
    if not isinstance(passenger, bool):
        raise ValueError("Passenger must be a boolean value.")

def validate_mass(mass):
    if not isinstance(mass, float):
        raise ValueError("Mass must be a floating point number.")
    if mass <= 0:
        raise ValueError("Mass must be greater than zero.")

def get_vehicle_from_user_input():
    registration_number = input("Registration number: ")
    validate_registration_number(registration_number)

    year_of_production = int(input("Year of production: "))
    validate_year_of_production(year_of_production)

    passenger_input = input("Passenger [y/n]: ")
    if passenger_input.lower() == "y":
        passenger = True
    elif passenger_input.lower() == "n":
        passenger = False
    else:
        raise ValueError("Passenger input must be 'y' or 'n'.")
    validate_passenger(passenger)

    mass = float(input("Vehicle mass: "))
    validate_mass(mass)

    return Vehicle(registration_number, year_of_production, passenger, mass)

def main():
    print("Press 1 to produce a JSON string describing a vehicle")
    print("Press 2 to decode a JSON string into vehicle data")
    choice = input("Your choice: ")

    if choice == "1":
        vehicle = get_vehicle_from_user_input()
        json_string = json.dumps(vehicle, cls=VehicleEncoder)
        print(f"Resulting JSON string is:\n{json_string}")
    elif choice == "2":
        json_string = input("Enter vehicle JSON string: ")
        vehicle = json.loads(json_string, cls=VehicleDecoder)
        print(vehicle.__dict__)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()