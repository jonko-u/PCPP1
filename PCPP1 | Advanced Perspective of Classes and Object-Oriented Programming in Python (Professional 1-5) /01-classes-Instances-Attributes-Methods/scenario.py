# Level of difficulty
#
# Easy
# Objectives
#
#     creating classes, methods, and variables;
#     calling methods;
#     getting simple access to instance variables;
#
# Mobile phone
#
# Scenario
#
#     create a class representing a mobile phone;
#     your class should implement the following methods:
#         __init__ expects a number to be passed as an argument; this method stores the number in an instance variable self.number
#         turn_on() should return the message 'mobile phone {number} is turned on'. Curly brackets are used to mark the place to insert the object's number variable;
#         turn_off() should return the message 'mobile phone is turned off';
#         call(number) should return the message 'calling {number}'. Curly brackets are used to mark the place to insert the object's number variable;
#     create two objects representing two different mobile phones; assign any random phone numbers to them;
#     implement a sequence of method calls on the objects to turn them on, call any number. Print the methods' outcomes;
#     turn off both mobiles.
#
# Example output
# mobile phone 01632-960004 is turned on
# mobile phone 01632-960012 is turned on
# calling 555-34343
# mobile phone is turned off
# mobile phone is turned off
#

class Phone:
    def __init__(self, number):
        self.number = number
    def call(self, number):
        message = 'Calling {} using own number {}'.format(number, self.number)
        return message


phone_1 = Phone(901123123)
phone_2 = Phone(902123123)
print(f"mobile phone {phone_1.number} is turned on")
print(f"mobile phone {phone_2.number} is turned on")
print(phone_1.call(903123123))
