"""
Objectives

    improving the student's skills in building an XML document;
    using the Element class and the SubElement function.

Scenario

You are a programmer working for an online store. Your task is to build an XML document containing information about the three vegan products available in the store:

<?xml version="1.0"?>
<shop>
    <category name="Vegan Products">
        <product name="Good Morning Sunshine">
            <type>cereals</type>
            <producer>OpenEDG Testing Service</producer>
            <price>9.90</price>
            <currency>USD</currency>
        </product>
        <product name="Spaghetti Veganietto">
            <type>pasta</type>
            <producer>Programmers Eat Pasta</producer>
            <price>15.49</price>
            <currency>EUR</currency>
        </product>
        <product name="Fantastic Almond Milk">
            <type>beverages</type>
            <producer>Drinks4Coders Inc.</producer>
            <price>19.75</price>
            <currency>USD</currency>
        </product>
    </category>
</shop>

Save the document to the shop.xml file. Use UTF-8 character encoding and don't forget to add the prolog to the beginning of the file. Good luck!
"""
import xml.etree.ElementTree as ET
from xml.dom import minidom

# create the root element
root = ET.Element("shop")

# create the category element and set its name attribute
category = ET.SubElement(root, "category", name="Vegan Products")

# create the product elements and their child elements
product1 = ET.SubElement(category, "product", name="Good Morning Sunshine")
ET.SubElement(product1, "type").text = "cereals"
ET.SubElement(product1, "producer").text = "OpenEDG Testing Service"
ET.SubElement(product1, "price").text = "9.90"
ET.SubElement(product1, "currency").text = "USD"

product2 = ET.SubElement(category, "product", name="Spaghetti Veganietto")
ET.SubElement(product2, "type").text = "pasta"
ET.SubElement(product2, "producer").text = "Programmers Eat Pasta"
ET.SubElement(product2, "price").text = "15.49"
ET.SubElement(product2, "currency").text = "EUR"

product3 = ET.SubElement(category, "product", name="Fantastic Almond Milk")
ET.SubElement(product3, "type").text = "beverages"
ET.SubElement(product3, "producer").text = "Drinks4Coders Inc."
ET.SubElement(product3, "price").text = "19.75"
ET.SubElement(product3, "currency").text = "USD"

# create the XML document with indentation, padding, sorting, and the XML declaration
xml_str = ET.tostring(root, encoding="UTF-8", method="xml")
xml_pretty_str = minidom.parseString(xml_str).toprettyxml(indent="\t")
xml_pretty_str = xml_pretty_str.replace('\t', '  ') # replace tabs with double spaces

# write the XML document to a file
with open("shop.xml", "w") as file:
    file.write(xml_pretty_str)