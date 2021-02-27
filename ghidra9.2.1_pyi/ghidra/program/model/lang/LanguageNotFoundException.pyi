from typing import List
import java.io
import java.lang


class LanguageNotFoundException(java.io.IOException):
    """
    Exception class used when the named language cannot be found.
    """





    @overload
    def __init__(self, message: unicode): ...

    @overload
    def __init__(self, languageID: ghidra.program.model.lang.LanguageID):
        """
        Language not found
        @param languageID
        """
        ...

    @overload
    def __init__(self, processor: ghidra.program.model.lang.Processor): ...

    @overload
    def __init__(self, languageID: ghidra.program.model.lang.LanguageID, msg: unicode):
        """
        Language not found
        @param languageID
        @param msg
        """
        ...

    @overload
    def __init__(self, languageID: ghidra.program.model.lang.LanguageID, compilerSpecID: ghidra.program.model.lang.CompilerSpecID): ...

    @overload
    def __init__(self, languageID: ghidra.program.model.lang.LanguageID, majorVersion: int, minorVersion: int):
        """
        Newer version of language required
        @param languageID
        @param majorVersion
        @param minorVersion
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
