# Level of difficulty
#
# Medium
# Objectives
#
#     improving the student's skills in operating with metaclasses;
#     improving the student's skills in operating with class variables and class methods.
#
# Scenario
#
#     Imagine you’ve been given a task to clean up the code of a system developed in Python – the code should be treated as legacy code;
#     the system was created by a group of volunteers who worked with no clear “clean coding” rules;
#     the system suffers from a problem: we don’t know in which order the classes are created, so it causes multiple dependency problems;
#     your task is to prepare a metaclass that is responsible for:
#         equipping all newly instantiated classes with time stamps, persisted in a class attribute named instantiation_time;
#         equipping all newly instantiated classes with the get_instantiation_time() method. The method should return the value of the class attribute instantiation_time.
#
# * The metaclass should have its own class variable (a list) that contains a list of the names of the classes instantiated by the metaclass (tip: append the class name in the __new__ method).
#
#     Your metaclass should be used to create a few distinct legacy classes;
#     create objects based on the classes;
#     list the class names that are instantiated by your metaclass.

import datetime

class LegacyMeta(type):
    instantiated_classes = []

    def __new__(cls, name, bases, attrs):
        attrs['instantiation_time'] = datetime.datetime.now()
        attrs['get_instantiation_time'] = lambda self: self.instantiation_time
        cls.instantiated_classes.append(name)
        return super().__new__(cls, name, bases, attrs)
class LegacyClass1(metaclass=LegacyMeta):
    pass

class LegacyClass2(metaclass=LegacyMeta):
    pass

class LegacyClass3(metaclass=LegacyMeta):
    pass

obj1 = LegacyClass1()
obj2 = LegacyClass2()
obj3 = LegacyClass3()

print(obj1.get_instantiation_time())
print(obj2.get_instantiation_time())
print(obj3.get_instantiation_time())
print(LegacyMeta.instantiated_classes)