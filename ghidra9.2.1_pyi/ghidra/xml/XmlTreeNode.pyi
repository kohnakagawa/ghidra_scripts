from typing import Iterator
import ghidra.xml
import java.lang


class XmlTreeNode(object):
    """
    A class to represent a corresponding start and end tag. This value is one
     node on the XML parse tree.
    """





    def __init__(self, parser: ghidra.xml.XmlPullParser):
        """
        Constructs a new XML tree node given the specified parser.
        @param parser the XML parser
        @throws SAXParseException if an XML parser error occurs
        """
        ...



    def deleteChildNode(self, node: ghidra.xml.XmlTreeNode) -> None:
        """
        Deletes the specified child node.
        @param node the node to delete
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getChild(self, name: unicode) -> ghidra.xml.XmlTreeNode:
        """
        Returns the first child element with the specified name.
        @param name the name of the desired child element
        @return the first child element with the specified name
        """
        ...

    def getChildAt(self, index: int) -> ghidra.xml.XmlTreeNode: ...

    def getChildCount(self) -> int:
        """
        Returns the number of children below this node.
        @return the number of children below this node
        """
        ...

    @overload
    def getChildren(self) -> Iterator[ghidra.xml.XmlTreeNode]:
        """
        Returns an iterator over all of the children of this node.
        @return an iterator over all of the children of this node
        """
        ...

    @overload
    def getChildren(self, name: unicode) -> Iterator[ghidra.xml.XmlTreeNode]:
        """
        Returns an iterator over all of the children of this node with the
         specfied name.
        @param name the name of the desired children
        @return an iterator over all of the children of this node with the
                 specfied name
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getEndElement(self) -> ghidra.xml.XmlElement:
        """
        Returns the end element of this node.
        @return the end element of this node
        """
        ...

    def getStartElement(self) -> ghidra.xml.XmlElement:
        """
        Returns the start element of this node.
        @return the start element of this node
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def childCount(self) -> int: ...

    @property
    def children(self) -> java.util.Iterator: ...

    @property
    def endElement(self) -> ghidra.xml.XmlElement: ...

    @property
    def startElement(self) -> ghidra.xml.XmlElement: ...
