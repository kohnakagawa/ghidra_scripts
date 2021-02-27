from typing import List
import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class BTreeNodeDescriptor(object, ghidra.app.util.bin.StructConverter):
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

    def getBLink(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getFLink(self) -> int: ...

    def getHeight(self) -> int: ...

    def getKind(self) -> int: ...

    def getNumRecords(self) -> int: ...

    def getRecordOffsets(self) -> List[object]: ...

    def getRecords(self) -> List[object]: ...

    def getReserved(self) -> int: ...

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
    def BLink(self) -> int: ...

    @property
    def FLink(self) -> int: ...

    @property
    def height(self) -> int: ...

    @property
    def kind(self) -> int: ...

    @property
    def numRecords(self) -> int: ...

    @property
    def recordOffsets(self) -> List[object]: ...

    @property
    def records(self) -> List[object]: ...

    @property
    def reserved(self) -> int: ...
