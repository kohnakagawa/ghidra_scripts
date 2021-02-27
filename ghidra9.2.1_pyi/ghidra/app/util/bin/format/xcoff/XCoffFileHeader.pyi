import ghidra.app.util.bin
import ghidra.app.util.bin.format.xcoff
import ghidra.program.model.data
import java.lang


class XCoffFileHeader(object, ghidra.app.util.bin.StructConverter):
    """
    XCOFF File Header.
     Handles both 32 and 64 bit cases.
    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    SIZEOF: int = 20
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    def __init__(self, provider: ghidra.app.util.bin.ByteProvider): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFlags(self) -> int: ...

    def getMagic(self) -> int: ...

    def getOptionalHeader(self) -> ghidra.app.util.bin.format.xcoff.XCoffOptionalHeader: ...

    def getOptionalHeaderSize(self) -> int: ...

    def getSectionCount(self) -> int: ...

    def getSymbolTableEntries(self) -> int: ...

    def getSymbolTablePointer(self) -> long: ...

    def getTimeStamp(self) -> int: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def flags(self) -> int: ...

    @property
    def magic(self) -> int: ...

    @property
    def optionalHeader(self) -> ghidra.app.util.bin.format.xcoff.XCoffOptionalHeader: ...

    @property
    def optionalHeaderSize(self) -> int: ...

    @property
    def sectionCount(self) -> int: ...

    @property
    def symbolTableEntries(self) -> int: ...

    @property
    def symbolTablePointer(self) -> long: ...

    @property
    def timeStamp(self) -> int: ...
