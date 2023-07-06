import json

import requests

base_url = 'http://localhost:3000/cars'

def list_cars():
    response = requests.get(base_url)
    cars = response.json()
    print(cars)
    for car in cars:
        print_car(car)

def add_car():
    response = requests.get(base_url)
    get_json = response.json()
    # Get the length of the list of cars in the JSON data
    num_cars = len(get_json)
    print(num_cars)
    make = input('Make: ')
    model = input('Model: ')
    year = input('Year: ')
    data = {'id': num_cars+1, 'make': make, 'model': model, 'year': year}
    response = requests.post(base_url, json=data)
    car = response.json()
    print_car(car)

def delete_car():
    car_id = input('Car ID: ')
    url = f'{base_url}/{car_id}'
    response = requests.delete(url)
    if response.status_code == 200:
        print(f"Deleted car with ID {car_id}.")
    else:
        print('Error')

def update_car():
    car_id = input('Car ID: ')
    make = input('Make: ')
    model = input('Model: ')
    year = input('Year: ')
    data = {'id': int(car_id), 'make': make, 'model': model, 'year': year}
    url = f'{base_url}/{car_id}'
    response = requests.put(url, json=data)
    print(response.status_code)
    if response.status_code == 200:
        print(f"Updated car with ID {car_id}.")
    else:
        print('Error')

def print_car(car):
    print(f"ID: {car['id']}")
    print(f"Make: {car['make']}")
    print(f"Model: {car['model']}")
    print(f"Year: {car['year']}")
    print()

def print_menu():
    print("+-----------------------------------+")
    print("| Vintage Cars Database             |")
    print("+-----------------------------------+")
    print("M E N U\n")
    print("    1. List cars")
    print("    2. Add new car")
    print("    3. Delete car")
    print("    4. Update car")
    print("    5. Exit")

def main():
    while True:
        print_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            list_cars()
        elif choice == "2":
            add_car()
        elif choice == "3":
            delete_car()
        elif choice == "4":
            update_car()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()