"""
There are many possible Python tools allowing you to create, write, read, parse, and modify XML files. Most of them treat an XML document as a tree consisting of objects, while the objects represent elements.

One of these tools is a package named xml.etree and we’re going to show you two simple snippets that make use of it.

Look at the first snippet in the editor.
Cars for sale


Let’s comment on the code:

    line 1: import – nothing special;
    line 3: the parse() function reads the XML document, builds the tree, and returns it; we use the tree object to invoke its fundamental method named getroot() which returns what it promises – the root element of the tree;
    line 4: each tree element (i.e., each object containing the element) has a property named tag which stores the textual representation of the element's name – we use it to print the root element's name;
    line 5: now we start to traverse the tree using the findall() method of the root object; the method's arguments name the elements we are interested in;
    line 6: we print the tag's (element's) name – yes, we know that it's car (we wanted to find it so it isn't surprising)
    line 7: we initiate the iterations which should reveal all car's components
    line 8: we print the found tag's name...
    line 9: ...and if it is price...
    line 10: ...we make use of the attrib property which is, in fact, a Python dictionary grouping all of tag's attributes (as attributes occur in pairs, a dictionary is the best tool to store them)
    line 11: we print tag's content – it is available as a value returned from the text property.

The code produces the following output:

cars_for_sale
	 car
		 id = 1
		 brand = Ford
		 model = Mustang
		 production_year = 1972
		 price{'currency': 'USD'} = 35900
	 car
		 id = 2
		 brand = Aston Martin
		 model = Rapide
		 production_year = 2010
		 price{'currency': 'GBP'} = 32000
"""
import xml.etree.ElementTree

cars_for_sale = xml.etree.ElementTree.parse('cars.xml').getroot()
print(cars_for_sale.tag)
for car in cars_for_sale.findall('car'):
    print('\t', car.tag)
    for prop in car:
        print('\t\t', prop.tag, end='')
        if prop.tag == 'price':
            print(prop.attrib, end='')
        print(' =', prop.text)
