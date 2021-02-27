from typing import List
import java.io
import java.lang


class DemangledException(java.lang.Exception):
    """
    A class to handle exceptions that occur demangling.
    """





    @overload
    def __init__(self, invalidMangledName: bool):
        """
        Use this constructor to indicate the demangler failed
         because the string to demangle does not appear to represent
         a valid mangled name.
        @param invalidMangledName true to indicate the string to
         demangle does not appear to represent a valid mangled name
        """
        ...

    @overload
    def __init__(self, message: unicode):
        """
        Use this constructor to indicate a demangler exception
         due to some general invalid or unsupported mangled string
         characteristic. For example, unrecognized datatype.
        @param message the invalid or unsupported mangled message
        """
        ...

    @overload
    def __init__(self, cause: java.lang.Exception):
        """
        Use this constructor to indicate a demangler exception
         due to an exception thrown during the demangling process.
        @param cause the exception thrown during the demangling process
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

    def isInvalidMangledName(self) -> bool:
        """
        Returns true if the string to demangle does not appear to represent
         a valid mangled name
        @return true if the string to demangle does not appear to represent
         a valid mangled name
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
    def invalidMangledName(self) -> bool: ...
