"""
Download and open the following XML file in your favorite text editor:

nyse.xml

It's a small excerpt of the New York Stock Exchange quotes list. Take a look at it and analyze its structure. You need to do this as your task is to write a code which reads the data and presents it in a form similar to this one:

Command prompt -- Stock Exchange

Hints:

    don't forget to handle at least two possible exceptions: FileNotFoundError and xml.etree.ElementTree.ParseError;
    feel free to improve and beautify the output — we know perfectly well that ours is not very sophisticated and rather ugly.
    object.
"""
import argparse
import xml.etree.ElementTree as ET

class XMLAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.tree = None
        self.root = None

    def load_xml(self):
        try:
            self.tree = ET.parse(self.filename)
            self.root = self.tree.getroot()
        except FileNotFoundError:
            print("File not found.")
        except ET.ParseError:
            print("Error parsing XML.")

    def analyze(self, element_name, *attribute_names):
        if self.root is None:
            self.load_xml()

        if self.root is not None:
            # Define column widths
            name_width = 30
            attr_width = 15

            # Print header
            header = f"{'Element':<{name_width}} " + ' '.join([f"{attr_name:>{attr_width}}" for attr_name in attribute_names])
            print(header)

            # Print separator
            separator = f"{'-'*name_width} " + ' '.join(['-'*attr_width for _ in attribute_names])
            print(separator)

            # Print elements and attributes
            for element in self.root.iter(element_name):
                name = element.text[:name_width]
                attrs = [element.get(attr_name, '').rjust(attr_width) for attr_name in attribute_names]
                row = f"{name:<{name_width}} " + ' '.join(attrs)
                print(row)

if __name__ == '__main__':
    # Command line argument parsing
    parser = argparse.ArgumentParser(description='XML Analyzer Tool')
    parser.add_argument('files', metavar='file', type=str, nargs='+', help='XML file(s) to analyze')
    parser.add_argument('-e', '--element', type=str, default='quote', help='Name of the element to analyze')
    parser.add_argument('-a', '--attributes', type=str, nargs='+', default=['last', 'change', 'min', 'max'], help='Name(s) of the attribute(s) to analyze')
    args = parser.parse_args()

    # Analyze each XML file
    for filename in args.files:
        analyzer = XMLAnalyzer(filename)
        analyzer.analyze(args.element, *args.attributes)
