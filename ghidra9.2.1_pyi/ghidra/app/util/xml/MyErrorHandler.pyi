import java.lang
import org.xml.sax


class MyErrorHandler(object, org.xml.sax.ErrorHandler):








    def equals(self, __a0: object) -> bool: ...

    def error(self, exception: org.xml.sax.SAXParseException) -> None:
        """
        @see org.xml.sax.ErrorHandler#error(org.xml.sax.SAXParseException)
        """
        ...

    def fatalError(self, exception: org.xml.sax.SAXParseException) -> None:
        """
        @see org.xml.sax.ErrorHandler#fatalError(org.xml.sax.SAXParseException)
        """
        ...

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

    def warning(self, exception: org.xml.sax.SAXParseException) -> None:
        """
        @see org.xml.sax.ErrorHandler#warning(org.xml.sax.SAXParseException)
        """
        ...
