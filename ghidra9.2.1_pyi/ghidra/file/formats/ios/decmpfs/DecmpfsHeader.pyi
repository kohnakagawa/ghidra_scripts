from typing import List
import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class DecmpfsHeader(object, ghidra.app.util.bin.StructConverter):
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



    def __init__(self, __a0: ghidra.app.util.bin.BinaryReader, __a1: int): ...



    def equals(self, __a0: object) -> bool: ...

    def getAttrBytes(self) -> List[int]: ...

    def getClass(self) -> java.lang.Class: ...

    def getCompressionMagic(self) -> unicode: ...

    def getCompressionType(self) -> int: ...

    def getUncompressedSize(self) -> long: ...

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
    def attrBytes(self) -> List[int]: ...

    @property
    def compressionMagic(self) -> unicode: ...

    @property
    def compressionType(self) -> int: ...

    @property
    def uncompressedSize(self) -> long: ...
