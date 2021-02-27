import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class DyldCacheImageInfo(object, ghidra.app.util.bin.StructConverter):
    """
    Represents a dyld_cache_image_info structure.
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
        @param reader A {@link BinaryReader} positioned at the start of a DYLD image info
        @throws IOException if there was an IO-related problem creating the DYLD image info
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> long:
        """
        Gets the address the start of the image.
        @return The address of the start of the image
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getPath(self) -> unicode:
        """
        Gets the path of the image.
        @return The path of the image
        """
        ...

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
    def address(self) -> long: ...

    @property
    def path(self) -> unicode: ...
