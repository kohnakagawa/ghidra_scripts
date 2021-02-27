from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.coff
import ghidra.program.model.data
import java.lang


class CoffSymbol(object, ghidra.app.util.bin.StructConverter):
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







    def equals(self, __a0: object) -> bool: ...

    def getAuxiliaryCount(self) -> int: ...

    def getAuxiliarySymbols(self) -> List[ghidra.app.util.bin.format.coff.CoffSymbolAux]: ...

    def getBasicType(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getDerivedType(self, derivedIndex: int) -> int: ...

    def getName(self) -> unicode: ...

    def getSectionNumber(self) -> int: ...

    def getStorageClass(self) -> int: ...

    def getValue(self) -> long: ...

    def hashCode(self) -> int: ...

    def isSection(self) -> bool:
        """
        Returns true if this symbol represents a section.
        @return true if this symbol represents a section
        """
        ...

    def move(self, offset: int) -> None:
        """
        Adds offset to the value; this must be performed before
         relocations in order to achieve the proper result.
        @param offset the offset to add to the value
        """
        ...

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
    def auxiliaryCount(self) -> int: ...

    @property
    def auxiliarySymbols(self) -> List[object]: ...

    @property
    def basicType(self) -> int: ...

    @property
    def name(self) -> unicode: ...

    @property
    def section(self) -> bool: ...

    @property
    def sectionNumber(self) -> int: ...

    @property
    def storageClass(self) -> int: ...

    @property
    def value(self) -> long: ...
