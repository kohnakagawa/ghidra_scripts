from typing import List
import ghidra.app.util.bin.format.coff
import ghidra.program.model.data
import java.lang


class CoffSymbolAuxArray(object, ghidra.app.util.bin.format.coff.CoffSymbolAux):
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

    def getArraySize(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getFirstDimension(self) -> int: ...

    def getFourthDimension(self) -> int: ...

    def getLineNumber(self) -> int: ...

    def getSecondDimension(self) -> int: ...

    def getTagIndex(self) -> int: ...

    def getThirdDimension(self) -> int: ...

    def getUnused(self) -> List[int]: ...

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
    def arraySize(self) -> int: ...

    @property
    def firstDimension(self) -> int: ...

    @property
    def fourthDimension(self) -> int: ...

    @property
    def lineNumber(self) -> int: ...

    @property
    def secondDimension(self) -> int: ...

    @property
    def tagIndex(self) -> int: ...

    @property
    def thirdDimension(self) -> int: ...

    @property
    def unused(self) -> List[int]: ...
