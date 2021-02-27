import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class SparseHeader(object, ghidra.app.util.bin.StructConverter):
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

    def getBlk_sz(self) -> int: ...

    def getChunk_hdr_sz(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getFile_hdr_sz(self) -> int: ...

    def getImage_checksum(self) -> int: ...

    def getMagic(self) -> int: ...

    def getMajor_version(self) -> int: ...

    def getMinor_version(self) -> int: ...

    def getTotal_blks(self) -> int: ...

    def getTotal_chunks(self) -> int: ...

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
    def blk_sz(self) -> int: ...

    @property
    def chunk_hdr_sz(self) -> int: ...

    @property
    def file_hdr_sz(self) -> int: ...

    @property
    def image_checksum(self) -> int: ...

    @property
    def magic(self) -> int: ...

    @property
    def major_version(self) -> int: ...

    @property
    def minor_version(self) -> int: ...

    @property
    def total_blks(self) -> int: ...

    @property
    def total_chunks(self) -> int: ...
