import generic.jar
import ghidra.xml
import java.io
import java.lang
import org.xml.sax


class XmlPullParserFactory(object):




    def __init__(self): ...



    @overload
    @staticmethod
    def create(file: generic.jar.ResourceFile, errHandler: org.xml.sax.ErrorHandler, validate: bool) -> ghidra.xml.XmlPullParser:
        """
        Constructs a new parser using the specified XML file.
        @param file the input XML file
        @param errHandler the XML error handler
        @param validate true if the parse should validate against the DTD
        @throws SAXException if an XML parse error occurs
        @throws IOException if an i/o error occurs
        """
        ...

    @overload
    @staticmethod
    def create(file: java.io.File, errHandler: org.xml.sax.ErrorHandler, validate: bool) -> ghidra.xml.XmlPullParser:
        """
        Constructs a new parser using the specified XML file.
        @param file the input XML file
        @param errHandler the XML error handler
        @param validate true if the parse should validate against the DTD
        @throws SAXException if an XML parse error occurs
        @throws IOException if an i/o error occurs
        """
        ...

    @overload
    @staticmethod
    def create(input: unicode, inputName: unicode, errHandler: org.xml.sax.ErrorHandler, validate: bool) -> ghidra.xml.XmlPullParser:
        """
        Constructs a new parser using the specified XML file.
        @param input A string that contains the XML input data
        @param inputName A descriptive name for the XML process (this will appear as the thread name)
        @param errHandler the XML error handler
        @param validate true if the parse should validate against the DTD
        @throws SAXException if an XML parse error occurs
        """
        ...

    @overload
    @staticmethod
    def create(input: java.io.InputStream, inputName: unicode, errHandler: org.xml.sax.ErrorHandler, validate: bool) -> ghidra.xml.XmlPullParser:
        """
        Constructs a new parser using the specified stream and name.
        @param input the input XML stream
        @param inputName the name of the stream
        @param errHandler the XML error handler
        @param validate true if the parse should validate against the DTD
        @throws SAXException if an XML parse error occurs
        @throws IOException
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def setCreateTracingParsers(xmlTracer: ghidra.xml.XmlTracer) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
