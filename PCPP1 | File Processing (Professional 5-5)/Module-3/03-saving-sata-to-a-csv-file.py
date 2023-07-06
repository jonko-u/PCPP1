"""
Saving data to a CSV file (part 1)

As we mentioned before, saving data to a CSV file is done using the writer object provided by the csv module. To create it, we need to use a function called writer, which takes the same set of arguments as the reader function. Let's see how to save contacts to a CSV file. Look at the code in the editor.

In the example code, we first open the file for writing. The 'w' mode creates a file for us if it hasn't already been created. Next, we create a writer object that we use to add rows using the writerow method. The writerow method takes a list of values as an argument, and then saves them as one line in a CSV file.

Saving data to a CSV file (part 2)

Imagine a situation where you add a contact containing the separator used to separate the values in the CSV file. By default, these values are quoted, but you can change this with the quotechar argument, which must be a single character. Look at the code in the editor and notice how we explicitly set default arguments.

The code will save the following data to the exported_contacts.csv file:

Name,Phone
mother,222-555-101
father,222-555-102
wife,222-555-103
"grandmother, grandfather and auntie",222-555-105

The last argument called quoting, specifies what values should be quoted. The default value QUOTE_MINIMAL means that only values with special characters such as separator or quotechar will be quoted. In our case, it's the value of "grandmother, grandfather and auntie".

Below are other constants that we can use as the value of the quoting argument:

csv.QUOTE_ALL – quotes all values

csv.QUOTE_NONNUMERIC – quotes only non-numeric values

csv.QUOTE_NONE – doesn't quote any values. It's not a good idea to set this value if you have special characters that require quoting, because this will raise an error

NOTE: The quotechar and quoting parameters can also be used in the reader function. See the documentation for more information.


Saving data to a CSV file (part 3)

Do you remember how we read rows from the CSV file to OrderedDict objects? In the csv module, there is an analogous class called DictWriter with which we can map dictionaries to rows. Unlike the DictReader object, when creating the DictWriter object, we must define a header. Let's look at the example in the editor.

To create the DictWriter object, we use a file object and a list containing column names. Note that before saving the value, we first call the writeheader method, which adds the header to the first line of the file. After that we add rows with values by passing dictionaries to the writerow method.

"""
import csv
# Part1
# with open('exported_contacts.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=',')
#
#     writer.writerow(['Name', 'Phone'])
#     writer.writerow(['mother', '222-555-101'])
#     writer.writerow(['father', '222-555-102'])
#     writer.writerow(['wife', '222-555-103'])
#     writer.writerow(['mother-in-law', '222-555-104'])
# Part2
# with open('exported_contacts.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#
#     writer.writerow(['Name', 'Phone'])
#     writer.writerow(['mother', '222-555-101'])
#     writer.writerow(['father', '222-555-102'])
#     writer.writerow(['wife', '222-555-103'])
#     writer.writerow(['mother-in-law', '222-555-104'])
#     writer.writerow(['grandmother, grandfather', '222-555-105'])
# Part3
with open('exported_contacts.csv', 'w', newline='') as csvfile:
    fieldnames = ['Name', 'Phone']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Name': 'mother', 'Phone': '222-555-101'})
    writer.writerow({'Name': 'father', 'Phone': '222-555-102'})
    writer.writerow({'Name': 'wife', 'Phone': '222-555-103'})
    writer.writerow({'Name': 'mother-in-law', 'Phone': '222-555-104'})
    writer.writerow({'Name': 'grandmother, grandfather and auntie', 'Phone': '222-555-105'})