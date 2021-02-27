from typing import List
import generic.jar
import java.io
import java.lang
import javax.xml.parsers
import org.jdom
import org.jdom.input
import org.xml.sax


class XmlUtilities(object):
    """
    A set of utility methods for working with XML.
    """

    FEATURE_DISALLOW_DTD: unicode = u'http://apache.org/xml/features/disallow-doctype-decl'
    FEATURE_EXTERNAL_GENERAL_ENTITIES: unicode = u'http://xml.org/sax/features/external-general-entities'
    FEATURE_EXTERNAL_PARAMETER_ENTITIES: unicode = u'http://xml.org/sax/features/external-parameter-entities'




    class ThrowingErrorHandler(object, org.xml.sax.ErrorHandler):




        def __init__(self): ...



        def equals(self, __a0: object) -> bool: ...

        def error(self, __a0: org.xml.sax.SAXParseException) -> None: ...

        def fatalError(self, __a0: org.xml.sax.SAXParseException) -> None: ...

        def getClass(self) -> java.lang.Class: ...

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

        def warning(self, __a0: org.xml.sax.SAXParseException) -> None: ...



    def __init__(self): ...



    @staticmethod
    def byteArrayToXml(bytes: List[int]) -> org.jdom.Element:
        """
        Converts the specified byte array into an XML element.
        @param bytes the XML bytes
        @return an XML element
        """
        ...

    @staticmethod
    def createSecureSAXBuilder(validate: bool, needsDTD: bool) -> org.jdom.input.SAXBuilder:
        """
        Create a {@link SAXBuilder} that is not susceptible to XXE.

         This configures the builder to ignore external entities.
        @param validate indicates whether validation should occur
        @param needsDTD false to disable doctype declarations altogether
        @return the configured builder
        """
        ...

    @staticmethod
    def createSecureSAXParserFactory(needsDTD: bool) -> javax.xml.parsers.SAXParserFactory:
        """
        Create a {@link SAXParserFactory} that is not susceptible to XXE.

         This configures the factory to ignore external entities.
        @param needsDTD false to disable doctype declarations altogether
        @return the configured factory
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def escapeElementEntities(xml: unicode) -> unicode:
        """
        Converts any special or reserved characters in the specified XML string
         into the equivalent Unicode encoding.
        @param xml the XML string
        @return the encoded XML string
        """
        ...

    @staticmethod
    def fromString(s: unicode) -> org.jdom.Element:
        """
        Convert a String into a JDOM {@link Element}.
         <p>
        @param s
        @return
        @throws JDOMException
        @throws IOException
        """
        ...

    @staticmethod
    def getChildren(ele: org.jdom.Element, childName: unicode) -> List[org.jdom.Element]:
        """
        Type-safe way of getting a list of {@link Element}s from JDom.
        @param ele the parent element
        @param childName the name of the children elements to return
        @return {@literal List<Element>} of elements
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def hasInvalidXMLCharacters(s: unicode) -> bool:
        """
        Tests a string for characters that would cause a problem if added to an
         xml attribute or element.
        @param s a string
        @return boolean true if the string will cause a problem if added to an
                 xml attribute or element.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def parseBoolean(boolStr: unicode) -> bool:
        """
        Parses the given string into a boolean value. Acceptable inputs are
         y,n,true,fase. A null input string will return false (useful if optional
         boolean attribute is false by default)
        @param boolStr the string to parse into a boolean value
        @return the boolean result.
        @throws XmlAttributeException if the string in not one of y,n,true,false
                     or null.
        """
        ...

    @staticmethod
    def parseBoundedInt(intStr: unicode, minValue: int, maxValue: int) -> int:
        """
        Parses the specified string as a decimal number, returning its integer
         value.
         <p>
        @param intStr String with integer digits
        @param minValue minimum value allowed (inclusive)
        @param maxValue maximum value allowed (inclusive)
        @return integer value of the intStr
        @throws NumberFormatException if intStr is null or empty or could not be
                     parsed or is out of range.
        """
        ...

    @staticmethod
    def parseBoundedIntAttr(ele: org.jdom.Element, attrName: unicode, minValue: int, maxValue: int) -> int:
        """
        Parses the required attribute as a decimal number, returning its integer
         value.
         <p>
        @param ele JDom element that contains the attribute
        @param attrName the name of the xml attribute to parse
        @param minValue minimum value allowed (inclusive)
        @param maxValue maximum value allowed (inclusive)
        @return integer value of the attribute
        @throws NumberFormatException if intStr could not be parsed or is out of
                     range.
        """
        ...

    @staticmethod
    def parseBoundedLong(longStr: unicode, minValue: long, maxValue: long) -> long:
        """
        Parses the specified string as a decimal number, returning its long
         integer value.
         <p>
         Note, using {@link Long#MIN_VALUE} and/or {@link Long#MAX_VALUE} as lower
         and upper bounds is problematic and should be avoided as the range check
         will become a NO-OP and always succeed.
         <p>
        @param longStr String with integer digits
        @param minValue minimum value allowed (inclusive)
        @param maxValue maximum value allowed (inclusive)
        @return long integer value of the longStr
        @throws NumberFormatException if intStr is null or empty or could not be
                     parsed or is out of range.
        """
        ...

    @staticmethod
    def parseBoundedLongAttr(ele: org.jdom.Element, attrName: unicode, minValue: long, maxValue: long) -> long:
        """
        Parses the required attribute as a decimal number, returning its long
         integer value.
         <p>
         Note, using {@link Long#MIN_VALUE} and/or {@link Long#MAX_VALUE} as lower
         and upper bounds is problematic and should be avoided as the range check
         will become a NO-OP and always succeed.
         <p>
        @param ele JDom element that contains the attribute
        @param attrName the name of the xml attribute to parse
        @param minValue minimum value allowed (inclusive)
        @param maxValue maximum value allowed (inclusive)
        @return long integer value of the attribute
        @throws NumberFormatException if intStr could not be parsed or is out of
                     range.
        """
        ...

    @overload
    @staticmethod
    def parseInt(intStr: unicode) -> int:
        """
        Parse the given string as either a hex number (if it starts with 0x) or a
         decimal number.
        @param intStr the string to parse into an integer
        @return the parsed integer.
        @throws NumberFormatException if the given string does not represent a
                     valid integer.
        """
        ...

    @overload
    @staticmethod
    def parseInt(intStr: unicode, defaultValue: int) -> int:
        """
        Parses the optional specified string as a decimal number, returning its
         integer value.
         <p>
        @param intStr string with integer digits, or empty or null
        @param defaultValue value to return if intStr is missing
        @return integer value of the intStr
        @throws NumberFormatException if intStr could not be parsed or the string
                     specifies a value outside the range of a signed 32 bit
                     integer.
        """
        ...

    @staticmethod
    def parseLong(longStr: unicode) -> long:
        """
        Parse the given string as either a hex number (if it starts with 0x) or a
         decimal number.
        @param longStr the string to parse into an long
        @return the parsed long.
        @throws NumberFormatException if the given string does not represent a
                     valid long.
        """
        ...

    @staticmethod
    def parseOptionalBooleanAttr(ele: org.jdom.Element, attrName: unicode, defaultValue: bool) -> bool:
        """
        Parses the optional attribute as a boolean value, returning its value or
         the specified defaultValue if missing.
        @param ele JDom element that contains the attribute
        @param attrName the name of the xml attribute to parse
        @param defaultValue boolean value to return if the attribute is not
                    defined
        @return boolean equiv of the attribute string value ("y", "true"/"n",
                 "false")
        @throws IOException if attribute value is not valid boolean string
        """
        ...

    @staticmethod
    def parseOptionalBoundedInt(intStr: unicode, defaultValue: int, minValue: int, maxValue: int) -> int:
        """
        Parses the optional specified string as a decimal number, returning its
         integer value, or defaultValue if the string is null.
         <p>
        @param intStr string with integer digits, or null.
        @param defaultValue value to return if intStr is null.
        @param minValue minimum value allowed (inclusive).
        @param maxValue maximum value allowed (inclusive).
        @return integer value of the intStr.
        @throws NumberFormatException if intStr could not be parsed or is out of
                     range.
        """
        ...

    @staticmethod
    def parseOptionalBoundedIntAttr(ele: org.jdom.Element, attrName: unicode, defaultValue: int, minValue: int, maxValue: int) -> int:
        """
        Parses an optional attribute as a decimal number, returning its integer
         value, or the defaultValue if the attribute is null.
         <p>
        @param ele JDOM element that contains the attribute.
        @param attrName the name of the xml attribute to parse.
        @param defaultValue the default value to return if attribute is missing.
        @param minValue minimum value allowed (inclusive).
        @param maxValue maximum value allowed (inclusive).
        @return integer value of the attribute.
        @throws NumberFormatException if the attribute value could not be parsed
                     or is out of range.
        """
        ...

    @staticmethod
    def parseOptionalBoundedLongAttr(ele: org.jdom.Element, attrName: unicode, defaultValue: long, minValue: long, maxValue: long) -> long:
        """
        Parses the required attribute as a decimal number, returning its long
         integer value.
         <p>
         Note, using {@link Long#MIN_VALUE} and/or {@link Long#MAX_VALUE} as lower
         and upper bounds is problematic and should be avoided as the range check
         will become a NO-OP and always succeed.
         <p>
        @param ele JDom element that contains the attribute.
        @param attrName the name of the xml attribute to parse.
        @param defaultValue the default value to return if attribute is missing.
        @param minValue minimum value allowed (inclusive).
        @param maxValue maximum value allowed (inclusive).
        @return long integer value of the attribute.
        @throws NumberFormatException if intStr could not be parsed or is out of
                     range.
        """
        ...

    @staticmethod
    def parseOverlayName(addrStr: unicode) -> unicode:
        """
        Parses the overlay name from the specified address string. Returns null
         if the address string does appear to represent an overlay.
        @param addrStr the address string
        @return the overlay name or null
        """
        ...

    @overload
    @staticmethod
    def readDocFromFile(f: generic.jar.ResourceFile) -> org.jdom.Document:
        """
        Read a File and convert to jdom xml doc.
         <p>
        @param f {@link ResourceFile} to read
        @return JDOM {@link Document}
        @throws JDOMException if text in file isn't valid XML
        @throws IOException if IO error when reading file.
        """
        ...

    @overload
    @staticmethod
    def readDocFromFile(f: java.io.File) -> org.jdom.Document:
        """
        Read a File and convert to jdom xml doc.
         <p>
        @param f {@link File} to read
        @return JDOM {@link Document}
        @throws JDOMException if text in file isn't valid XML
        @throws IOException if IO error when reading file.
        """
        ...

    @staticmethod
    def requireStringAttr(ele: org.jdom.Element, attrName: unicode) -> unicode:
        """
        Throws an {@link IOException} with a verbose explanation if the requested
         attribute is not present or is empty.
         <p>
        @param ele JDOM {@link Element} that contains the attribute
        @param attrName the attribute name
        @return String value of the attribute (never null or empty)
        @throws IOException if attribute is missing or empty
        """
        ...

    @staticmethod
    def setIntAttr(ele: org.jdom.Element, attrName: unicode, attrValue: int) -> None:
        """
        Sets an integer attribute on the specified element.
        @param ele JDom element
        @param attrName name of attribute
        @param attrValue value of attribute
        """
        ...

    @staticmethod
    def setStringAttr(ele: org.jdom.Element, attrName: unicode, attrValue: unicode) -> None:
        """
        Sets a string attribute on the specified element.
        @param ele JDom element
        @param attrName name of attribute
        @param attrValue value of attribute, null ok
        """
        ...

    @overload
    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def toString(root: org.jdom.Element) -> unicode:
        """
        Converts the specified XML element into a String.
        @param root the root element
        @return String translation of the given element
        """
        ...

    @staticmethod
    def unEscapeElementEntities(escapedXMLString: unicode) -> unicode:
        """
        Converts any escaped character entities into their unescaped character
         equivalents. This method is designed to be compatible with the output of
         {@link #escapeElementEntities(String)}.
        @param escapedXMLString The string with escaped data
        @return the unescaped string
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @staticmethod
    def writeDocToFile(doc: org.jdom.Document, dest: java.io.File) -> None:
        """
        Writes a JDOM XML {@link Document} to a {@link File}.
         <p>
        @param doc JDOM XML {@link Document} to write.
        @param dest {@link File} to write to.
        @throws IOException if error when writing file.
        """
        ...

    @staticmethod
    def writePrettyDocToFile(doc: org.jdom.Document, dest: java.io.File) -> None:
        """
        Writes a JDOM XML {@link Document} to a {@link File}, with a prettier
         format than {@link #writeDocToFile(Document, File)}.
         <p>
        @param doc JDOM XML {@link Document} to write.
        @param dest {@link File} to write to.
        @throws IOException if error when writing file.
        """
        ...

    @staticmethod
    def xmlToByteArray(root: org.jdom.Element) -> List[int]:
        """
        Converts the specified XML element into a byte array.
        @param root the root element
        @return the byte array translation of the given element
        """
        ...
