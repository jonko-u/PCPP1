"""
Modifying an XML document (part 1)

You've already learned how to parse an XML document. Time for the next step. Let's modify the element tree and create a new XML file based on it with the following movie data:

<?xml version="1.0"?>
<data>
    <movie title="The Little Prince" rate="5"></movie>
    <movie title="Hamlet" rate="5"></movie>
</data>

Are you wondering if it will be difficult to convert book data to movie data? Thanks to the xml.etree.ElementTree module, it's a piece of cake.

books > movies

To change the tag of the Element object, we must assign a new value to its tag property. Look at the code in the editor.

Result:

movie {'title': 'The Little Prince'}
author : Antoine de Saint-Exupéry
year : 1943
movie {'title': 'Hamlet'}
author : William Shakespeare
year : 1603

In the example, during each iteration through the book elements, we replace them with the movie tag, and then make sure that all changes have gone through correctly.

Modifying an XML document (part 2)

Our XML has a few unnecessary elements, such as author and year. In order to remove them, we need to use the method called remove, provided by the Element class. Look at the code in the editor.

Result:

movie {'title': 'The Little Prince'}
movie {'title': 'Hamlet'}

The remove method removes the child element passed as its argument, which must be an Element object. Note that for this purpose we use the method called find, which you're already familiar with.

Modifying an XML document (part 3)

Do you remember the get method that gets the value of the attribute? The Element object also has a method called set, which allows you to set any attribute. Look at the code in the editor.

Result:

movie {'title': 'The Little Prince', 'rate': '5'}
movie {'title': 'Hamlet', 'rate': '5'}

The set method takes the attribute name and its value as arguments. In our case, we use it to set the highest rating for each of the movies.

Modifying an XML document (part 4)

You must have noticed that the modified XML document is not saved anywhere. To save all the changes we’ve made to the tree, we have to use the method called write.

The write method has only one required argument, which is a file name of the output XML file, or a file object opened for writing. In addition, we can define character encoding by using the second argument (the default is US-ASCII). To add a prolog to our document, we must pass True in the third argument.

Take a look at the example in the editor, in which we save the modified tree in a file called movies.xml.

The created file looks like this:

<?xml version='1.0' encoding='UTF-8'?>
<data><movie rate="5" title="The Little Prince" /><movie rate="5" title="Hamlet" /></data>
"""
import xml.etree.ElementTree as ET

tree = ET.parse('books.xml')
root = tree.getroot()

# Part1
# for child in root:
#     child.tag = 'movie'
#     print(child.tag, child.attrib)
#     for sub_child in child:
#         print(sub_child.tag, ':', sub_child.text)
# Part2
# for child in root:
#     child.tag = 'movie'
#     child.remove(child.find('author'))
#     child.remove(child.find('year'))
#     print(child.tag, child.attrib)
#     for sub_child in child:
#         print(sub_child.tag, ':', sub_child.text)
# Part3
# for child in root:
#     child.tag = 'movie'
#     child.remove(child.find('author'))
#     child.remove(child.find('year'))
#     child.set('rate', '5')
#     print(child.tag, child.attrib)
#     for sub_child in child:
#         print(sub_child.tag, ':', sub_child.text)
# Part5
for child in root:
    child.tag = 'movie'
    child.remove(child.find('author'))
    child.remove(child.find('year'))
    child.set('rate', '5')
    print(child.tag, child.attrib)
    for sub_child in child:
        print(sub_child.tag, ':', sub_child.text)

tree.write('movies.xml', 'UTF-8', True)

