# Level of difficulty
#
# Medium
# Objectives
#
#     improving the student's skills in operating with special methods
#
# Scenario
#
#     Create a class representing a time interval;
#     the class should implement its own method for addition, subtraction on time interval class objects;
#     the class should implement its own method for multiplication of time interval class objects by an integer-type value;
#     the __init__ method should be based on keywords to allow accurate and convenient object initialization, but limit it to hours, minutes, and seconds parameters;
#     the __str__ method should return an HH:MM:SS string, where HH represents hours, MM represents minutes and SS represents the seconds attributes of the time interval object;
#     check the argument type, and in case of a mismatch, raise a TypeError exception.

class TimeInterval:
    def __init__(self, hours=0, minutes=0, seconds=0):
        if not isinstance(hours, int) or not isinstance(minutes, int) or not isinstance(seconds, int):
            raise TypeError("hours, minutes and seconds must be integers")
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __add__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError("unsupported operand type(s) for +: 'TimeInterval' and '{}'".format(type(other).__name__))
        total_seconds = self.to_seconds() + other.to_seconds()
        return TimeInterval.from_seconds(total_seconds)

    def __sub__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError("unsupported operand type(s) for -: 'TimeInterval' and '{}'".format(type(other).__name__))
        total_seconds = self.to_seconds() - other.to_seconds()
        return TimeInterval.from_seconds(total_seconds)

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError("unsupported operand type(s) for *: 'TimeInterval' and '{}'".format(type(other).__name__))
        total_seconds = self.to_seconds() * other
        return TimeInterval.from_seconds(total_seconds)

    def __str__(self):
        return "{:02d}:{:02d}:{:02d}".format(self.hours, self.minutes, self.seconds)

    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @classmethod
    def from_seconds(cls, seconds):
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        return cls(hours, minutes, seconds)

interval_1 = TimeInterval(10, 5, 2)
interval_2 = TimeInterval(5, 4, 3)
times = 4
print("Intervalo 1 :", interval_1.__str__())
print("Intervalo 2 :", interval_2.__str__())
print(f"Suma entre {interval_1.__str__()} y {interval_2.__str__()}", interval_1.__add__(interval_2))
print(f"Resta entre {interval_1.__str__()} y {interval_2.__str__()}", interval_1.__sub__(interval_2))
print(f"Multiplicación entre {interval_1.__str__()} y {times} :", interval_1.__mul__(times))