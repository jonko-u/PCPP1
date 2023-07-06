# Level of difficulty
#
# Low
# Objectives
#
#     improving the student's skills in operating with the deepcopy() method on a list of dictionaries.
#
# Scenario
# Introduction
#
# Imagine you have been hired to help run a candy warehouse.
# The task
#
#     Your task is to write a code that will prepare a proposal of reduced prices for the candies whose total weight exceeds 300 units of weight (we don’t care whether those are kilograms or pounds)
#     Your input is a list of dictionaries; each dictionary represents one type of candy. Each type of candy contains a key entitled 'weight', which should lead you to the total weight details of the given delicacy. The input is presented in the editor;
#     Prepare a copy of the source list (this should be done with a one-liner) and then iterate over it to reduce the price of each delicacy by 20% if its weight exceeds the value of 300;
#     Present an original list of candies and a list that contains the proposals;
#     Check if your code works correctly when copying and modifying the candy item details.
#
#     Expected output
#     Source list of candies
#     {'name': 'Lolly Pop', 'price': 0.4, 'weight': 133}
#     {'name': 'Licorice', 'price': 0.1, 'weight': 251}
#     {'name': 'Chocolate', 'price': 1, 'weight': 601}
#     {'name': 'Sours', 'price': 0.01, 'weight': 513}
#     {'name': 'Hard candies', 'price': 0.3, 'weight': 433}
#     ******************
#     Price proposal
#     {'name': 'Lolly Pop', 'price': 0.4, 'weight': 133}
#     {'name': 'Licorice', 'price': 0.1, 'weight': 251}
#     {'name': 'Chocolate', 'price': 0.8, 'weight': 601}
#     {'name': 'Sours', 'price': 0.008, 'weight': 513}
#     {'name': 'Hard candies', 'price': 0.24, 'weight': 433}
#
#     If your code issues the same output, then you deserve a small reward:

# Define the warehouse list
warehouse = [
    {'name': 'Lolly Pop', 'price': 0.4, 'weight': 133},
    {'name': 'Licorice', 'price': 0.1, 'weight': 251},
    {'name': 'Chocolate', 'price': 1, 'weight': 601},
    {'name': 'Sours', 'price': 0.01, 'weight': 513},
    {'name': 'Hard candies', 'price': 0.3, 'weight': 433}
]

# Print the original list of candies
print("Original list of candies:")
for item in warehouse:
    print(item)

# Create a copy of the warehouse list with reduced prices for candies over 300 weight
proposal = [{'name': item['name'], 'price': item['price']*0.8, 'weight': item['weight']} if item['weight'] > 300 else item for item in warehouse]

# Print the proposal list of candies
print("\nProposal list of candies:")
for item in proposal:
    print(item)