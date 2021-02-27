from typing import List
import ghidra.util.exception
import java.io
import java.lang


class InvalidDataTypeException(ghidra.util.exception.UsrException):
    """
    Exception thrown if a data type is not valid for the operation being performed.
    """





    @overload
    def __init__(self):
        """
        Constructor.
        """
        ...

    @overload
    def __init__(self, message: unicode):
        """
        Constructor
        @param message detailed message explaining exception
        """
        ...

    @overload
    def __init__(self, dt: ghidra.program.model.data.DataType):
        """
        Constructor
        @param dt the data type that is invalid for the operation being performed.
        """
        ...

    @overload
    def __init__(self, msg: unicode, cause: java.lang.Throwable):
        """
        Construct a new InvalidDataTypeException with the given message and cause
        @param msg the exception message
        @param cause the exception cause
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
