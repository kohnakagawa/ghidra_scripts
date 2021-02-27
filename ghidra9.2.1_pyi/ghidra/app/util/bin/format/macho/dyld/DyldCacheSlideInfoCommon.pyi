import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class DyldCacheSlideInfoCommon(object, ghidra.app.util.bin.StructConverter):
    """
    Class for representing the common components of the various dyld_cache_slide_info structures.
     The intent is for the the full dyld_cache_slide_info structures to extend this and add their
     specific parts.
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
        Create a new {@link DyldCacheSlideInfoCommon}.
        @param reader A {@link BinaryReader} positioned at the start of a DYLD slide info
        @throws IOException if there was an IO-related problem creating the DYLD slide info
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getVersion(self) -> int:
        """
        Gets the version of the DYLD slide info.
        @return The version of the DYLD slide info.
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
    def version(self) -> int: ...
