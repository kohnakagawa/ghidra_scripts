from typing import List
import java.io
import java.lang


class OptionException(java.lang.Exception):
    """
    Exception thrown if there was a problem accessing an Option, or if
     an informational message is to be conveyed.
    """





    @overload
    def __init__(self, msg: unicode):
        """
        Construct a new OptionException.
        @param msg reason for the exception
        """
        ...

    @overload
    def __init__(self, msg: unicode, isInfo: bool):
        """
        Construct a new OptionException that may be an informational message
         if isValid is true.
        @param msg message to display
        @param isInfo true if the msg is in informational message
        """
        ...



    def addSuppressed(self, __a0: java.lang.Throwable) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def fillInStackTrace(self) -> java.lang.Throwable: ...

    def getCause(self) -> java.lang.Throwable: ...

    def getClass(self) -> java.lang.Class: ...

    def getLocalizedMessage(self) -> unicode: ...

    def getMessage(self) -> unicode: ...

    def getStackTrace(self) -> List[java.lang.StackTraceElement]: ...

    def getSuppressed(self) -> List[java.lang.Throwable]: ...

    def hashCode(self) -> int: ...

    def initCause(self, __a0: java.lang.Throwable) -> java.lang.Throwable: ...

    def isInfoMessage(self) -> bool:
        """
        Return whether the message associated with this exception is
         informational.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def printStackTrace(self) -> None: ...

    @overload
    def printStackTrace(self, __a0: java.io.PrintStream) -> None: ...

    @overload
    def printStackTrace(self, __a0: java.io.PrintWriter) -> None: ...

    def setStackTrace(self, __a0: List[java.lang.StackTraceElement]) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def infoMessage(self) -> bool: ...
