"""
Objectives

    improving the student's skills in creating logs;
    improving the student's skills in creating their own handler and formatter.

Scenario

It's likely that the temperature of your phone battery can get pretty high. Check if that’s true. Write a program that will simulate the recording of battery temperatures with an interval of one minute. The simulation should contain 60 logs (the last hour).

To simulate temperatures, use one of the available random functions in Python. Temperatures should be drawn in the range of 20–40 degrees Celsius, and then saved in the following format:

LEVEL_NAME – TEMPERATURE_IN_CELSIUS UNIT => DEBUG – 20 C

The drawn temperatures should be assigned to the appropriate level depending on their value:

DEBUG = TEMPERATURE_IN_CELSIUS < 20
WARNING = TEMPERATURE_IN_CELSIUS >= 30 AND TEMPERATURE_IN_CELSIUS <= 35
CRITICAL = TEMPERATURE_IN_CELSIUS > 35

Put all logs in the battery_temperature.log file. The task will be completed when you implement your own handler and formatter.
"""
import logging
import random

class TemperatureFormatter(logging.Formatter):
    def format(self, record):
        temperature = record.temperature
        level_name = record.levelname
        unit = "\u00b0C" # degree Celsius symbol
        return f"{level_name} - {temperature} {unit} => {record.msg}"

class TemperatureHandler(logging.Handler):
    def emit(self, record):
        # Open the log file in append mode
        with open("battery_temperature.log", "a") as f:
            # Use the formatter to format the log message
            log_message = self.format(record)
            # Write the log message to the file
            f.write(log_message + "\n")

def simulate_battery_temperature():
    # Create a logger with the "battery_temperature" name
    logger = logging.getLogger("battery_temperature")
    logger.setLevel(logging.DEBUG)

    # Create a new TemperatureHandler and add it to the logger
    handler = TemperatureHandler()
    handler.setLevel(logging.DEBUG)
    formatter = TemperatureFormatter()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Generate 60 random temperatures and log them at random intervals
    for i in range(60):
        temperature = random.randint(20, 40)
        if temperature < 20:
            logger.debug("Temperature too low", extra={"temperature": temperature})
        elif temperature >= 20 and temperature < 30:
            logger.info("Temperature its okay", extra={"temperature": temperature})
        elif temperature >= 30 and temperature <= 35:
            logger.warning("Temperature within warning range", extra={"temperature": temperature})
        elif temperature > 35:
            logger.critical("Temperature too high", extra={"temperature": temperature})
        else:
            pass

if __name__ == "__main__":
    simulate_battery_temperature()