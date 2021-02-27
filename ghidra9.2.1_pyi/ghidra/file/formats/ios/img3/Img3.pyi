from typing import List
import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class Img3(object, ghidra.app.util.bin.StructConverter):
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



    @overload
    def __init__(self, __a0: ghidra.app.util.bin.BinaryReader): ...

    @overload
    def __init__(self, __a0: ghidra.app.util.bin.ByteProvider): ...



    def equals(self, __a0: object) -> bool: ...

    def getCheckArea(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataSize(self) -> int: ...

    def getIdentifier(self) -> int: ...

    def getMagic(self) -> unicode: ...

    def getSize(self) -> int: ...

    @overload
    def getTags(self) -> List[object]: ...

    @overload
    def getTags(self, __a0: java.lang.Class) -> List[object]: ...

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
    def checkArea(self) -> int: ...

    @property
    def dataSize(self) -> int: ...

    @property
    def identifier(self) -> int: ...

    @property
    def magic(self) -> unicode: ...

    @property
    def size(self) -> int: ...

    @property
    def tags(self) -> List[object]: ...
