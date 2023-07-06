# Objectives
#
#     improving the student's skills in creating classes representing candies;
#     improving the student's skills in operating with deepcopy() and copy.
#
# Scenario
#
# The previous task was a very easy one. Now let's rework the code a bit:
#
#     introduce the Delicacy class to represent a generic delicacy. The objects of this class will replace the old school dictionaries. Suggested attribute names: name, price, weight;
#     your class should implement the __str__() method to represent each object state;
#     experiment with the copy.copy() and deepcopy.copy() methods to see the difference in how each method copies objects .


import copy

class Delicacy:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight} g), price: {self.price}"

    def __repr__(self):
        return f"Delicacy('{self.name}', {self.price}, {self.weight})"

# Create the list of delicacies
warehouse = [
    Delicacy('Lolly Pop', 0.4, 133),
    Delicacy('Licorice', 0.1, 251),
    Delicacy('Chocolate', 1, 601),
    Delicacy('Sours', 0.01, 513),
    Delicacy('Hard candies', 0.3, 433)
]

# Print the original list of delicacies
print("Original list of delicacies:")
for item in warehouse:
    print(item)

# Create a shallow copy of the warehouse list
warehouse_copy = copy.copy(warehouse)

# Create a deep copy of the warehouse list
warehouse_deepcopy = copy.deepcopy(warehouse)

# Modify the weight of the first delicacy in the warehouse list
warehouse[0].weight = 200

# Print the original list of delicacies
print("\nOriginal list of delicacies:")
for item in warehouse:
    print(item)

# Print the shallow copy of the warehouse list
print("\nShallow copy of the warehouse list:")
for item in warehouse_copy:
    print(item)

# Print the deep copy of the warehouse list
print("\nDeep copy of the warehouse list:")
for item in warehouse_deepcopy:
    print(item)