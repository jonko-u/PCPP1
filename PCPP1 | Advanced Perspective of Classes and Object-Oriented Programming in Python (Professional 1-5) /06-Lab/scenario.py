# Level of difficulty
#
# Easy
# Objectives
#
#     improving the student's skills in operating with static and class methods
#
# Scenario
#
#     Create a class representing a luxury watch;
#     The class should allow you to hold a number of watches created in the watches_created class variable. The number could be fetched using a class method named get_number_of_watches_created;
#     the class may allow you to create a watch with a dedicated engraving (text). As this is an extra option, the watch with the engraving should be created using an alternative constructor (a class method), as a regular __init__ method should not allow ordering engravings;
#     the regular __init__ method should only increase the value of the appropriate class variable;
#
# The text intended to be engraved should follow some restrictions:
#
#     it should not be longer than 40 characters;
#     it should consist of alphanumerical characters, so no space characters are allowed;
#     if the text does not comply with restrictions, an exception should be raised;
#
# before engraving the desired text, the text should be validated against restrictions using a dedicated static method.
#
#     Create a watch with no engraving
#     Create a watch with correct text for engraving
#     Try to create a watch with incorrect text, like 'foo@baz.com'. Handle the exception
#     After each watch is created, call class method to see if the counter variable was increased


class LuxuryWatch:
    watches_created = 0

    def __init__(self):
        LuxuryWatch.watches_created += 1

    @classmethod
    def get_number_of_watches_created(cls):
        return cls.watches_created

    @classmethod
    def create_engraved_watch(cls, engraving_text):
        if not cls.validate_engraving_text(engraving_text):
            raise ValueError("Engraving text must be alphanumeric and no more than 40 characters long")
        watch = cls()
        watch.engraving_text = engraving_text
        return watch

    @staticmethod
    def validate_engraving_text(text):
        if len(text) > 40:
            return False
        if not text.isalnum():
            return False
        return True

# Create a watch with no engraving
watch_no_engraving_1 = LuxuryWatch()
print(LuxuryWatch.get_number_of_watches_created())  # Output: 1

# Create a watch with correct text for engraving
watch_with_engraving_2 = LuxuryWatch.create_engraved_watch("HappyBirthday")
print(LuxuryWatch.get_number_of_watches_created())  # Output: 2

# Try to create a watch with incorrect text
try:
    invalid_watch = LuxuryWatch.create_engraved_watch("foo@baz.com")
except ValueError as e:
    print(str(e))  # Output: Engraving text must be alphanumeric and no more than 40 characters long
print(LuxuryWatch.get_number_of_watches_created())  # Output: 2