from typing import List
import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class Ext4XattrHeader(object, ghidra.app.util.bin.StructConverter):
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

    def getClass(self) -> java.lang.Class: ...

    def getH_blocks(self) -> int: ...

    def getH_checksum(self) -> int: ...

    def getH_hash(self) -> int: ...

    def getH_magic(self) -> int: ...

    def getH_refcount(self) -> int: ...

    def getH_reserved(self) -> List[int]: ...

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
    def h_blocks(self) -> int: ...

    @property
    def h_checksum(self) -> int: ...

    @property
    def h_hash(self) -> int: ...

    @property
    def h_magic(self) -> int: ...

    @property
    def h_refcount(self) -> int: ...

    @property
    def h_reserved(self) -> List[int]: ...
