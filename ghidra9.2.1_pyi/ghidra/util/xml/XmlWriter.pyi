import ghidra.util.xml
import java.lang


class XmlWriter(object):
    """
    A class for creating XML files.
    """





    @overload
    def __init__(self, file: java.io.File, dtdName: unicode):
        """
        Constructs a new XML writer.
        @param file the name of the output XML file
        @param dtdName the name of the DTD
        @throws IOException if an i/o error occurs
        """
        ...

    @overload
    def __init__(self, out: java.io.OutputStream, dtdName: unicode):
        """
        Constructs a new XML writer.
        @param out the output stream
        @param dtdName the name of the DTD
        @throws IOException if an i/o error occurs
        """
        ...



    def close(self) -> None:
        """
        Closes this XML writer.
        """
        ...

    def endElement(self, name: unicode) -> None:
        """
        Writes the specified end element.
        @param name the name of the end element
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCounter(self) -> ghidra.util.xml.Counter:
        """
        Returns the XML summary string.
        @return the XML summary string
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def startElement(self, name: unicode) -> None:
        """
        Writes the specified start element.
        @param name the name of the start element
        """
        ...

    @overload
    def startElement(self, name: unicode, attrs: ghidra.util.xml.XmlAttributes) -> None:
        """
        Writes the specified start element with the attributes.
        @param name the name of the start element
        @param attrs the attributes of the start element
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeDTD(self, dtdName: unicode) -> None:
        """
        Writes the specified DTD into the file.
        @param dtdName the name of the DTD
        @throws IOException if an i/o error occurs
        """
        ...

    @overload
    def writeElement(self, name: unicode, attrs: ghidra.util.xml.XmlAttributes) -> None:
        """
        Writes the specified element with the attributes.
        @param name the name of the start element
        @param attrs the attributes of the start element
        """
        ...

    @overload
    def writeElement(self, name: unicode, attrs: ghidra.util.xml.XmlAttributes, text: unicode) -> None:
        """
        Writes the specified element with the attributes and text.
        @param name the name of the element
        @param attrs the attributes of the element
        @param text the text of the element
        """
        ...

    @property
    def counter(self) -> ghidra.util.xml.Counter: ...
