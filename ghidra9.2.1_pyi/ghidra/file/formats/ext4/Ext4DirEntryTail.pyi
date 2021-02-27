import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class Ext4DirEntryTail(object, ghidra.app.util.bin.StructConverter):
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

    def getDet_checksum(self) -> int: ...

    def getDet_rec_len(self) -> int: ...

    def getDet_reserved_ft(self) -> int: ...

    def getDet_reserved_zero1(self) -> int: ...

    def getDet_reserved_zero2(self) -> int: ...

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
    def det_checksum(self) -> int: ...

    @property
    def det_rec_len(self) -> int: ...

    @property
    def det_reserved_ft(self) -> int: ...

    @property
    def det_reserved_zero1(self) -> int: ...

    @property
    def det_reserved_zero2(self) -> int: ...
