"""
Building an XML document (part 1)

During this course, you haven’t had the opportunity to create an Element object yourself. Let's see how to build an XML document in Python.

The Element class constructor takes two arguments. The first is the name of the tag to be created, while the second (optional) is the attribute dictionary. In the example in the editor, we've created the root element represented by a data tag with no attributes - look at the code.

Result:

<data />

In the example above, we use the dump method, which allows us to debug either the whole tree or a single element.

Building an XML document (part 2)

In addition to the Element class, the xml.etree.ElementTree module offers a function for creating child elements called SubElement. The SubElement function takes three arguments.

The first one defines the parent element, the second one defines the tag name, and the third (optional) defines the attributes of the element. Let's see how it looks in action and analyze the code in the editor.

Result:

<data><movie rate="5" title="The Little Prince" /><movie rate="5" title="Hamlet" /></data>

In the example, we've added two child elements called movie to the root element. The created elements are objects of the Element class, so we can use all of the methods that we learned about during this course.

NOTE: To save a document using the write method, we need to have an ElementTree object. To do this, pass our root element to its constructor:

tree = ET.ElementTree(root)

"""
import xml.etree.ElementTree as ET

# Part1
# root = ET.Element('data')
# ET.dump(root)
# Part2
root = ET.Element('data')
movie_1 = ET.SubElement(root, 'movie', {'title': 'The Little Prince', 'rate': '5'})
movie_2 = ET.SubElement(root, 'movie', {'title': 'Hamlet', 'rate': '5'})
ET.dump(root)
