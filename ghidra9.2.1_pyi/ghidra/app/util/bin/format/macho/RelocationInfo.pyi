from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.macho
import ghidra.program.model.data
import java.lang


class RelocationInfo(object, ghidra.app.util.bin.StructConverter):
    """
    Represents a relocation_info structure.
    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    def __init__(self): ...



    @staticmethod
    def createRelocationInfo(reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader) -> ghidra.app.util.bin.format.macho.RelocationInfo: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getLength(self) -> int: ...

    def getSymbolIndex(self) -> int: ...

    def getType(self) -> int: ...

    def hashCode(self) -> int: ...

    def isExternal(self) -> bool: ...

    def isPcRelocated(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    def toValues(self) -> List[long]:
        """
        Returns the values array for storage into the program's relocation table.
        @return the values array for storage into the program's relocation table
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def address(self) -> int: ...

    @property
    def external(self) -> bool: ...

    @property
    def length(self) -> int: ...

    @property
    def pcRelocated(self) -> bool: ...

    @property
    def symbolIndex(self) -> int: ...

    @property
    def type(self) -> int: ...
