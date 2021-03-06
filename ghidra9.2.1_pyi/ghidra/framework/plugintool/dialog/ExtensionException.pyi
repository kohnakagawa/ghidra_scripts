from typing import List
import ghidra.framework.plugintool.dialog
import ghidra.framework.plugintool.dialog.ExtensionException
import ghidra.util.exception
import java.io
import java.lang


class ExtensionException(ghidra.util.exception.UsrException):
    """
    Defines an exception that can be thrown by ExtensionUtils. This is intended to provide
     detailed information about issues that arise during installation (or removal) of
     Extensions.
    """






    class ExtensionExceptionType(java.lang.Enum):
        COPY_ERROR: ghidra.framework.plugintool.dialog.ExtensionException.ExtensionExceptionType = COPY_ERROR
        DUPLICATE_FILE_ERROR: ghidra.framework.plugintool.dialog.ExtensionException.ExtensionExceptionType = DUPLICATE_FILE_ERROR
        INSTALL_CANCELLED: ghidra.framework.plugintool.dialog.ExtensionException.ExtensionExceptionType = INSTALL_CANCELLED
        INVALID_INSTALL_LOCATION: ghidra.framework.plugintool.dialog.ExtensionException.ExtensionExceptionType = INVALID_INSTALL_LOCATION
        ZIP_ERROR: ghidra.framework.plugintool.dialog.ExtensionException.ExtensionExceptionType = ZIP_ERROR







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.framework.plugintool.dialog.ExtensionException.ExtensionExceptionType: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.framework.plugintool.dialog.ExtensionException.ExtensionExceptionType]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    @overload
    def __init__(self, msg: unicode, exceptionType: ghidra.framework.plugintool.dialog.ExtensionException.ExtensionExceptionType): ...

    @overload
    def __init__(self, msg: unicode, exceptionType: ghidra.framework.plugintool.dialog.ExtensionException.ExtensionExceptionType, errorFile: java.io.File): ...



    def addSuppressed(self, __a0: java.lang.Throwable) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def fillInStackTrace(self) -> java.lang.Throwable: ...

    def getCause(self) -> java.lang.Throwable: ...

    def getClass(self) -> java.lang.Class: ...

    def getErrorFile(self) -> java.io.File: ...

    def getExceptionType(self) -> ghidra.framework.plugintool.dialog.ExtensionException.ExtensionExceptionType: ...

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

    @property
    def errorFile(self) -> java.io.File: ...

    @property
    def exceptionType(self) -> ghidra.framework.plugintool.dialog.ExtensionException.ExtensionExceptionType: ...
