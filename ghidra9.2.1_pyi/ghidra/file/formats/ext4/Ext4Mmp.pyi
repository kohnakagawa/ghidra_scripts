from typing import List
import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class Ext4Mmp(object, ghidra.app.util.bin.StructConverter):
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

    def getMmp_bdevname(self) -> List[int]: ...

    def getMmp_check_interval(self) -> int: ...

    def getMmp_checksum(self) -> int: ...

    def getMmp_magic(self) -> int: ...

    def getMmp_nodename(self) -> List[int]: ...

    def getMmp_pad1(self) -> int: ...

    def getMmp_pad2(self) -> List[int]: ...

    def getMmp_seq(self) -> int: ...

    def getMmp_time(self) -> long: ...

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
    def mmp_bdevname(self) -> List[int]: ...

    @property
    def mmp_check_interval(self) -> int: ...

    @property
    def mmp_checksum(self) -> int: ...

    @property
    def mmp_magic(self) -> int: ...

    @property
    def mmp_nodename(self) -> List[int]: ...

    @property
    def mmp_pad1(self) -> int: ...

    @property
    def mmp_pad2(self) -> List[int]: ...

    @property
    def mmp_seq(self) -> int: ...

    @property
    def mmp_time(self) -> long: ...