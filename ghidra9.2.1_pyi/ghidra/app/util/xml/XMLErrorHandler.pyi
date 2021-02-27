import java.lang
import org.xml.sax


class XMLErrorHandler(object, org.xml.sax.ErrorHandler):
    """
    An implemenation of the basic interface for SAX error handlers.
     Per the documentation, this class is required to prevent the SAX
     parser from squelching all parse exceptions.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def error(self, exception: org.xml.sax.SAXParseException) -> None: ...

    def fatalError(self, exception: org.xml.sax.SAXParseException) -> None: ...

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

    def warning(self, exception: org.xml.sax.SAXParseException) -> None: ...
