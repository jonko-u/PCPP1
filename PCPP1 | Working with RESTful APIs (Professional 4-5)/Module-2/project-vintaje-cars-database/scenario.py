import json
import random
import secrets
import uuid

# Generate a list of dictionaries representing cars
cars = []
for i in range(10):
    car = {
        'id': i + 1,
        'make': random.choice(['Ford', 'Chevrolet', 'Toyota', 'Honda']),
        'model': random.choice(['Fusion', 'Cruze', 'Camry', 'Accord']),
        'year': random.randint(2000, 2022)
    }
    cars.append(car)

# Write the list of cars to a JSON file
with open('cars.json', 'w') as file:
    json.dump(cars, file, indent=4)

print('Cars saved to cars.json')