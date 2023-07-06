"""
Objectives

    improving the student's skills in parsing XML documents;
    using known methods of the Element object;

Scenario

Have you seen the weather forecast for the coming week? It’ll be an extremely sunny and warm week. Familiarize yourself with the data in the forecast.xml file and then complete the following tasks:

    Create a class named TemperatureConverter and its convert_celsius_to_fahrenheit method. The convert_celsius_to_fahrenheit method should convert the temperature from Celsius to Fahrenheit. Use the following formula:

    F = 9/5 * C + 32.

    Create a class named ForecastXmlParser and its parse method responsible for reading data from forecast.xml. Use the TemperatureConverter class to convert the temperature from Celsius to Fahrenheit (rounded to one decimal place). The parse method should print the following results:

    Monday: 28 Celsius, 82.4 Fahrenheit
    Tuesday: 27 Celsius, 80.6 Fahrenheit
    Wednesday: 28 Celsius, 82.4 Fahrenheit
    Thursday: 29 Celsius, 84.2 Fahrenheit
    Friday: 29 Celsius, 84.2 Fahrenheit
    Saturday: 32 Celsius, 89.6 Fahrenheit
    Sunday: 33 Celsius, 91.4 Fahrenheit

NOTE: The forecast.xml file is available in your working directory at Edube Interactive. If you want to download the file and work with it locally, you can do it here: forecast.xml
"""
import argparse
import xml.etree.ElementTree as ET
class TemperatureConverter:
    @staticmethod
    def convert_celsius_to_fahrenheit(celsius_temp):
        fahrenheit_temp = 9/5 * celsius_temp + 32
        return round(fahrenheit_temp, 1)


class ForecastXmlParser:
    @staticmethod
    def parse(xml_file, day_element, temp_element):
        # parse the XML file
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # iterate over the item tags and convert the temperature
        for item in root.findall('item'):
            day = item.find(day_element).text
            celsius_temp = int(item.find(temp_element).text)
            fahrenheit_temp = TemperatureConverter.convert_celsius_to_fahrenheit(celsius_temp)
            print(f"{day}: {celsius_temp} Celsius, {fahrenheit_temp} Fahrenheit")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Parse an XML file and convert Celsius temperatures to Fahrenheit.')
    parser.add_argument('xml_file', help='the input XML file')
    parser.add_argument('day_element', help='the name of the day element')
    parser.add_argument('temp_element', help='the name of the temperature element')

    args = parser.parse_args()

    ForecastXmlParser.parse(args.xml_file, args.day_element, args.temp_element)