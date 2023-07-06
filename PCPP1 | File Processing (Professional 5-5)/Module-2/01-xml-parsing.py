"""

XML parsing (part 1)

Processing XML files in Python is very easy thanks to the ElementTree class provided by the xml.etree.ElementTree module. The ElementTree object is responsible for presenting the XML document in the form of a tree on which we can move up or down.

First, we need to import the appropriate module and define an alias for it. It's common to use the alias ET, but of course you can give it any name you like. To create a tree (an ElementTree object) from an existing XML document, pass it to the parse method as follows:

import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()

The getroot method returns the root element. With access to the root element, we can reach any elements in the document. Each of these elements is represented by a class called Element.

In addition to the parse method, we can use the method called fromstring, which, as an argument, takes XML as a string:

import xml.etree.ElementTree as ET

root = ET.fromstring(your_xml_as_string)

NOTE: The fromstring method doesn't return the ElementTree object, but instead returns the root element represented by the Element class.

XML parsing (part 2)

You already know how to access the root element. Let's use it to visit the elements of our tree - look at the code in the editor.

Result:

The root tag is: data
The root has the following children:
book {'title': 'The Little Prince'}
book {'title': 'Hamlet'}

The root element and all its children are Element objects. In the example above, we use the following properties:

tag – this returns the tag name as a string

attrib – this returns all attributes in the tag as a dictionary. To retrieve the value of a single attribute, use its key, e.g., child.attrib ['title'].

XML parsing (part 3)

In addition to iterating over tree elements, we can access them directly using indexes. Take a look at the example below in which we use the current book element to retrieve text from its child elements. Look at the code in the editor.

Result:

My books:

Title:  The Little Prince
Author: Antoine de Saint-Exupéry
Year:  1943

Title:  Hamlet
Author: William Shakespeare
Year:  1603

During each iteration, we refer to the children of the book element by using indexes. Index 0 refers to the first child of the book element, while index 1 refers to its second child. Displaying text is possible thanks to the text property, available in the Element object.

NOTE: Indexes are also used in deeper nesting, e.g., root [0] [0] .text returns the first book element, and then displays the text placed in its first child.

XML parsing (part 4)

The xml.etree.ElementTree module, or more precisely, the Element class, provides several useful methods for finding elements in an XML document. Let's start with the method called iter.

The iter method returns all elements by having the tag passed as an argument. The element that calls it is treated as the main element from which the search starts. In order to find all matches, the iterator iterates recursively through all child elements and their nested elements.

Look at the code in the editor to see an example of a search for all items with the author tag.

Result:

Antoine de Saint-Exupéry
William Shakespeare

XML parsing (part 5)

The Element object has a method called findall to search for direct child elements. Unlike the iter method, the findall method only searches the children at the first nesting level. Take a look at the example in the editor.

The example doesn't return any results, because the findall method can only iterate over the book elements that are the closest children of the root element. The correct code looks like this:

import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()
for book in root.findall('book'):
    print(book.get('title'))

Result:

The Little Prince
Hamlet

To display the value of the title attributes, we use the get method, which looks much better than a book.attrib ['title'] call. Its use is very simple: just enter the name of the attribute and optionally (as a second argument) the value that will be returned if the attribute is not found (the default is None).

NOTE: The findall method also accepts an XPath expression. We encourage you to deepen your knowledge of XPath expressions and apply it to the example shown.

XML parsing (part 6)

Another useful method used to parse an XML document is a method called find. The find method returns the first child element containing the specified tag or matching XPath expression. Look at the code in the editor.

Result:

The Little Prince

In the example, we use the find method to find the first child element containing the book tag, and then display the value of its title attribute. Note that the element from which we start the search is the root element.

"""
import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()
# part2
# print('The root tag is:', root.tag)
# print('The root has the following children:')
# for child in root:
#     print(child.tag, child.attrib)
# part3
# print("My books:\n")
# for book in root:
#     print('Title: ', book.attrib['title'])
#     print('Author:', book[0].text)
#     print('Year: ', book[1].text, '\n')
# part4
# for author in root.iter('author'):
#     print(author.text)
# part5
# for book in root.findall('book'):
#     print(book.get('title'))
# part6
print(root.find('book').get('title'))


