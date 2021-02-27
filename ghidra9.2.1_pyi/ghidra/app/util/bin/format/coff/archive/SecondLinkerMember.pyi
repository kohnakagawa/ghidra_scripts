from typing import List
import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class SecondLinkerMember(object, ghidra.app.util.bin.StructConverter):
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



    def __init__(self, reader: ghidra.app.util.bin.BinaryReader, header: ghidra.app.util.bin.format.coff.archive.CoffArchiveMemberHeader, skip: bool): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFileOffset(self) -> long: ...

    def getIndices(self) -> List[int]: ...

    def getNumberOfMembers(self) -> int: ...

    def getNumberOfSymbols(self) -> int: ...

    def getOffsets(self) -> List[int]: ...

    def getStringTable(self) -> List[unicode]: ...

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
    def fileOffset(self) -> long: ...

    @property
    def indices(self) -> List[int]: ...

    @property
    def numberOfMembers(self) -> int: ...

    @property
    def numberOfSymbols(self) -> int: ...

    @property
    def offsets(self) -> List[int]: ...

    @property
    def stringTable(self) -> List[object]: ...
