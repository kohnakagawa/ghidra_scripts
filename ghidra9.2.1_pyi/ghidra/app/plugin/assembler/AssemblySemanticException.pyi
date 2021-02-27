from typing import List
import ghidra.app.plugin.assembler
import java.io
import java.lang
import java.util


class AssemblySemanticException(ghidra.app.plugin.assembler.AssemblyException):
    """
    Thrown when all resolutions of an assembly instruction result in semantic errors.

     For SLEIGH, semantic errors amount to incompatible contexts
    """





    @overload
    def __init__(self, message: unicode): ...

    @overload
    def __init__(self, errors: java.util.Set):
        """
        Construct a semantic exception with the associated semantic errors
        @param errors the associated semantic errors
        """
        ...



    def addSuppressed(self, __a0: java.lang.Throwable) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def fillInStackTrace(self) -> java.lang.Throwable: ...

    def getCause(self) -> java.lang.Throwable: ...

    def getClass(self) -> java.lang.Class: ...

    def getErrors(self) -> java.util.Collection:
        """
        Get the collection of associated semantic errors
        @return the collection
        """
        ...

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
    def errors(self) -> java.util.Collection: ...
