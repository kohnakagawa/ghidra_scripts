from typing import List
import ghidra.util.exception
import java.io
import java.lang


class VariableSizeException(ghidra.util.exception.InvalidInputException):
    """
    VariableSizeException is thrown when a variable
     data-type exceeds storage constraints.
    """





    @overload
    def __init__(self, msg: unicode):
        """
        Constructor.
         The canForce value is assumed to be false.
        @param msg message text
        """
        ...

    @overload
    def __init__(self, msg: unicode, canForce: bool):
        """
        Constructor.
        @param msg message text
        @param canForce if true conveys to the user that the operation may
         be successful if forced.
        """
        ...



    def addSuppressed(self, __a0: java.lang.Throwable) -> None: ...

    def canForce(self) -> bool:
        """
        Returns true if the operation could be successful if forced.
        """
        ...

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
