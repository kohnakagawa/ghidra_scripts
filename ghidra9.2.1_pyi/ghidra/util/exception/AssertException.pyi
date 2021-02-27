from typing import List
import java.io
import java.lang


class AssertException(java.lang.RuntimeException):
    """
    AssertException is used in situations that the programmer believes can't happen.
     If it does, then there is a programming error of some kind.
    """





    @overload
    def __init__(self):
        """
        Create a new AssertException with no message.
        """
        ...

    @overload
    def __init__(self, msg: unicode):
        """
        Create a new AssertException with the given message.
        @param msg the exception message.
        """
        ...

    @overload
    def __init__(self, t: java.lang.Throwable):
        """
        Create a new AssertException using another exception (Throwable) has occurred.
         The message for this exception will be derived from the Throwable.
        @param t the Throwable which caused this exception to be generated.
        """
        ...

    @overload
    def __init__(self, message: unicode, throwable: java.lang.Throwable):
        """
        Create a new AssertException with the given message.
        @param message the exception message.
        @param throwable the Throwable which caused this exception to be generated.
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
