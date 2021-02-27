import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.pe.debug
import java.lang


class DebugCOFFLineNumber(object):
    """
    A class to represent the COFF Line number data structure.


     typedef struct _IMAGE_LINENUMBER {
        union {
            DWORD   SymbolTableIndex; // Symbol table index of function name if Linenumber is 0.
            DWORD   VirtualAddress;   // Virtual address of line number.
        } Type;
        WORD    Linenumber;           // Line number.
     } IMAGE_LINENUMBER;

    """

    IMAGE_SIZEOF_LINENUMBER: int = 6



    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    @staticmethod
    def createDebugCOFFLineNumber(reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader, index: int) -> ghidra.app.util.bin.format.pe.debug.DebugCOFFLineNumber: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLineNumber(self) -> int:
        """
        Returns the line number.
        @return the line number
        """
        ...

    def getSymbolTableIndex(self) -> int:
        """
        Returns the symbol table index of function name, if linenumber is 0.
        @return the symbol table index of function name, if linenumber is 0
        """
        ...

    def getVirtualAddress(self) -> int:
        """
        Returns the virtual address of the line number.
        @return the virtual address of the line number
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def lineNumber(self) -> int: ...

    @property
    def symbolTableIndex(self) -> int: ...

    @property
    def virtualAddress(self) -> int: ...
