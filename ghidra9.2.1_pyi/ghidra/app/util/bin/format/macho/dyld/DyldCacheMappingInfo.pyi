import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class DyldCacheMappingInfo(object, ghidra.app.util.bin.StructConverter):
    """
    Represents a dyld_cache_mapping_info structure.
    """

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



    def __init__(self, reader: ghidra.app.util.bin.BinaryReader):
        """
        Create a new {@link DyldCacheImageInfo}.
        @param reader A {@link BinaryReader} positioned at the start of a DYLD mapping info
        @throws IOException if there was an IO-related problem creating the DYLD mapping info
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> long:
        """
        Gets the address of the start of the mapping.
        @return The address of the start of the mapping
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFileOffset(self) -> long:
        """
        Gets the file offset of the start of the mapping.
        @return The file offset of the start of the mapping
        """
        ...

    def getSize(self) -> long:
        """
        Gets the size of the mapping.
        @return The size of the mapping
        """
        ...

    def hashCode(self) -> int: ...

    def isExecute(self) -> bool:
        """
        Returns true if the initial protections include EXECUTE.
        @return true if the initial protections include EXECUTE
        """
        ...

    def isRead(self) -> bool:
        """
        Returns true if the initial protections include READ.
        @return true if the initial protections include READ
        """
        ...

    def isWrite(self) -> bool:
        """
        Returns true if the initial protections include WRITE.
        @return true if the initial protections include WRITE
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
    def address(self) -> long: ...

    @property
    def execute(self) -> bool: ...

    @property
    def fileOffset(self) -> long: ...

    @property
    def read(self) -> bool: ...

    @property
    def size(self) -> long: ...

    @property
    def write(self) -> bool: ...
