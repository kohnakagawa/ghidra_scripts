from typing import List
import ghidra.program.model.address
import ghidra.program.util
import java.io
import java.lang


class AddressTranslationException(java.lang.RuntimeException):
    """
    Exception thrown when an attempt is made to translate an address
     from one program into an equivalent address in another program.
    """





    @overload
    def __init__(self):
        """
        Construct a new AddressTranslationException with no message
        """
        ...

    @overload
    def __init__(self, msg: unicode):
        """
        Construct a new AddressTranslationException with the given message
        @param msg the exception message
        """
        ...

    @overload
    def __init__(self, address: ghidra.program.model.address.Address, translator: ghidra.program.util.AddressTranslator):
        """
        Construct a new AddressTranslationException with the given address and translator.
         The message will indicate there is a conflict between the two data types.
        @param address the first of the two conflicting data types.
         (The new data type.)
        @param translator the second of the two conflicting data types.
         (The existing data type.)
        """
        ...



    def addSuppressed(self, __a0: java.lang.Throwable) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def fillInStackTrace(self) -> java.lang.Throwable: ...

    def getAddress(self) -> ghidra.program.model.address.Address: ...

    def getCause(self) -> java.lang.Throwable: ...

    def getClass(self) -> java.lang.Class: ...

    def getLocalizedMessage(self) -> unicode: ...

    def getMessage(self) -> unicode: ...

    def getStackTrace(self) -> List[java.lang.StackTraceElement]: ...

    def getSuppressed(self) -> List[java.lang.Throwable]: ...

    def getTranslator(self) -> ghidra.program.util.AddressTranslator: ...

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
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def translator(self) -> ghidra.program.util.AddressTranslator: ...
