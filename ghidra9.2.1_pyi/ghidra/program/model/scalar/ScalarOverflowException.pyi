from typing import List
import java.io
import java.lang


class ScalarOverflowException(java.lang.RuntimeException):
    """
    A ScalarOverflowException indicates that some precision would
     be lost.  If the operation was signed, unused bits did not match the
     sign bit.  If the operation was unsigned, unsed bits were not all
     zero
    """





    @overload
    def __init__(self):
        """
        <p>Constructs a ScalarOverflowException with no detail message.<p>
        """
        ...

    @overload
    def __init__(self, message: unicode):
        """
        <p>Constructs a ScalarOverflowException with the specified
         detail message.<p>
        @param message The message.
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
