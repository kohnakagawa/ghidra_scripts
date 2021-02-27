from typing import List
import java.lang


class XmlParserElement(object):
    """
    A class to represent the start or end tag from an XML file.
    """









    def equals(self, obj: object) -> bool: ...

    def getAttrNames(self) -> List[unicode]:
        """
        Returns an array containing the names of all attributes defined in this element.
        @return an array containing the names of all attributes defined in this element
        """
        ...

    def getAttrValue(self, attrName: unicode) -> unicode:
        """
        Returns the value of the specified attribute.
         Or, null if no attribute exists with the specified name.
        @param attrName the name of the attribute
        @return the value of the specified attribute
        """
        ...

    def getAttrValueAsBool(self, attrName: unicode) -> bool:
        """
        Returns the boolean value of the specified attribute.
        @param attrName the name of the attribute
        @return the boolean value of the specified attribute
        @throws XmlAttributeException if no attribute exists with the specified name
        """
        ...

    def getAttrValueAsDouble(self, attrName: unicode) -> float:
        """
        Returns the double value of the specified attribute.
        @param attrName the name of the attribute
        @return the double value of the specified attribute
        @throws XmlAttributeException if no attribute exists with the specified name
        """
        ...

    def getAttrValueAsInt(self, attrName: unicode) -> int:
        """
        Returns the integer value of the specified attribute.
        @param attrName the name of the attribute
        @return the integer value of the specified attribute
        @throws XmlAttributeException if no attribute exists with the specified name
        """
        ...

    def getAttrValueAsLong(self, attrName: unicode) -> long:
        """
        Returns the long value of the specified attribute.
        @param attrName the name of the attribute
        @return the long value of the specified attribute
        @throws XmlAttributeException if no attribute exists with the specified name
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getLineNum(self) -> int:
        """
        Returns the line number where this element was defined.
        @return the line number where this element was defined
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of this element/tag.
        @return the name of this element/tag
        """
        ...

    def getText(self) -> unicode:
        """
        Returns the text of this element. Or, null if no text existed
         in the XML.
        @return the text of this element
        """
        ...

    def hasAttr(self, attrName: unicode) -> bool:
        """
        Returns true if this element contains an attribute with the specified name.
        @param attrName the name of the attribute
        @return true if this element contains an attribute with the specified name
        """
        ...

    def hashCode(self) -> int: ...

    def isEnd(self) -> bool:
        """
        Returns true if this element represents an end tag.
        @return true if this element represents an end tag
        """
        ...

    def isStart(self) -> bool:
        """
        Returns true if this element represents a start tag.
        @return true if this element represents a start tag
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setAttribute(self, name: unicode, value: unicode) -> None:
        """
        Sets the value of the specified attribute.
        @param name the name of the attribute
        @param value the value of the attribute
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def attrNames(self) -> List[unicode]: ...

    @property
    def end(self) -> bool: ...

    @property
    def lineNum(self) -> int: ...

    @property
    def name(self) -> unicode: ...

    @property
    def start(self) -> bool: ...

    @property
    def text(self) -> unicode: ...
