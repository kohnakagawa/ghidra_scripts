from typing import List
import java.io
import java.lang


class RollbackException(java.lang.RuntimeException):
    """
    Exception thrown when a transaction should be rolled back.
    """





    @overload
    def __init__(self, message: unicode):
        """
        Constructor
        @param message the message explaining what caused the exception.
        """
        ...

    @overload
    def __init__(self, cause: java.lang.Throwable):
        """
        Constructor
        @param cause cause of exception
        """
        ...

    @overload
    def __init__(self, message: unicode, cause: java.lang.Throwable):
        """
        Constructor
        @param message the message explaining what caused the exception.
        @param cause cause of exception
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
