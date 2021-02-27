from typing import List
import java.io
import java.lang


class ClosedException(java.io.IOException):
    """
    ClosedException indicates that the underlying resource has been
     closed and read/write operations have failed.
    """





    @overload
    def __init__(self):
        """
        Default constructor.  Message indicates 'File is closed'.
        """
        ...

    @overload
    def __init__(self, resourceName: unicode):
        """
        Constructor which indicates resource which has been closed.
         Message indicates '&lt;resourceName&gt; is closed'.
        @param resourceName name of closed resource.
        """
        ...



    def addSuppressed(self, __a0: java.lang.Throwable) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def fillInStackTrace(self) -> java.lang.Throwable: ...

    def getCause(self) -> java.lang.Throwable: ...

    def getClass(self) -> java.lang.Class: ...

    def getLocalizedMessage(self) -> unicode: ...

    def getMessage(self) -> unicode: ...

    def getResourceName(self) -> unicode:
        """
        @return name of resource which is closed.
        """
        ...

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

    @property
    def resourceName(self) -> unicode: ...
