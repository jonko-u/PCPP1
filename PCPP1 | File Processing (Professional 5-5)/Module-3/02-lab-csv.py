"""
Objectives

    improving the student's skills in reading the CSV files;
    using the reader function or the DictReader class.

Scenario

When we buy a new phone, it's necessary to import old contacts. Why not import them from a CSV file? Look again at the familiar contacts.csv file, and then design your new phone as follows:

    create a class called PhoneContact representing a single contact. The PhoneContact class should contain the name and phone properties;
    create a class called Phone that will store your contacts. First, implement the method called load_contacts_from_csv, responsible for reading data from the CSV file into the class property called contacts. The contacts property should contain a list of PhoneContact objects;
    add to the Phone class a method called search_contacts, which accepts any phrase entered by the user from the keyboard, and then based on it perform a search for all matching contacts (case insensitive). If there are no results, print the message: "No contacts found".

Example input:

Search contacts: mother

Example output:

mother (222-555-101)
mother-in-law (222-555-104)

Example input:

Search contacts: 103

Example output:

wife (222-555-103)
"""
import csv

class PhoneContact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class Phone:
    def __init__(self):
        self.contacts = []

    def load_contacts_from_csv(self, filename):
        with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                name, phone = row
                contact = PhoneContact(name, phone)
                self.contacts.append(contact)

    def search_contacts(self, search_query):
        matching_contacts = []
        for contact in self.contacts:
            if search_query.lower() in contact.name.lower():
                matching_contacts.append(contact)
        if matching_contacts:
            for contact in matching_contacts:
                print(f"{contact.name} ({contact.phone})")
        else:
            print("No contacts found")

if __name__ == '__main__':
    phone = Phone()
    phone.load_contacts_from_csv('contacts.csv')
    search_query = input("Search contacts: ")
    phone.search_contacts(search_query)