"""


The xml.etree.ElementTree module may be also used to create, modify and write XML files.

We’ll use it to remove one car from our offer (theFord Mustang) and add a new car to it – look at the editor and see how we did it.

Rocket sciencist


Some explanations will make the sample code clearer – here they go:

    line 1: no comment needed;
    line 3: parse the file and fetch an object storing all elements – we’ll name it tree;
    line 4: find the root of the tree and store it in cars_for_sale (in fact, this is the same step as done previously, but divided into two parts)
    line 5: let's traverse the tree...
    line 6: ...in order to search the car whose brand name is Ford and its model name is Mustang;
    line 7: yes! We've found it! Now we invoke the remove() method from within the car object and the whole element disappears from the tree;
    line 8: we can leave the loop immediately;
    line 9: we create a brand new and completely empty car element – it’s stored inside the new_car variable (note: the Element() method requires one argument: a string containing the element's (tag's) name;
    lines 10 through 13: we call the SubElement() method as many times as the number of sub-elements (the inner tags) we need; each invocation needs two arguments: a parent element object (new_car here) and a sub-element name (as a string); note: the function returns an object for the newly created element; in fact, we need it only once, for a very specific purpose: we use it to set the text associated with the tag – this is why we access the text property and set it with the desired value;
    line 14 is slightly different – can you see it? The invocation contains one more argument: a dictionary; the function will use is to embed an attribute (price) inside the sub-element;
    line 15: now we’re ready to append the newly created element into the tree, and we do it;
    line 16: the write() method invoked from within the tree object creates a new file and fills it with the modified XML document.


As you can see, working with XML doesn't require you to be a rocket scientist, but – if we’re being honest – JSON is more convenient and – last but most important – most currently implemented services use JSON, not XML. It's highly possible that you may encounter a server which implements communication on exchanging XML documents, but JSON is much more popular.

We think you can judge for yourself now where this section’s title came from.

"""
import xml.etree.ElementTree

tree = xml.etree.ElementTree.parse('cars.xml')
cars_for_sale = tree.getroot()
for car in cars_for_sale.findall('car'):
    if car.find('brand').text == 'Ford' and car.find('model').text == 'Mustang':
        cars_for_sale.remove(car)
        break
new_car = xml.etree.ElementTree.Element('car')
xml.etree.ElementTree.SubElement(new_car, 'id').text = '4'
xml.etree.ElementTree.SubElement(new_car, 'brand').text = 'Maserati'
xml.etree.ElementTree.SubElement(new_car, 'model').text = 'Mexico'
xml.etree.ElementTree.SubElement(new_car, 'production_year').text = '1970'
xml.etree.ElementTree.SubElement(new_car, 'price', {'currency': 'EUR'}).text = '61800'
cars_for_sale.append(new_car)
tree.write('newcars.xml', method='')
