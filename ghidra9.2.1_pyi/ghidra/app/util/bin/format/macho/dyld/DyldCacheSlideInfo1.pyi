import ghidra.app.util.bin.format.macho.dyld
import ghidra.program.model.data
import java.lang


class DyldCacheSlideInfo1(ghidra.app.util.bin.format.macho.dyld.DyldCacheSlideInfoCommon):
    """
    Represents a dyld_cache_slide_info structure.
    """





    def __init__(self, reader: ghidra.app.util.bin.BinaryReader):
        """
        Create a new {@link DyldCacheSlideInfo1}.
        @param reader A {@link BinaryReader} positioned at the start of a DYLD slide info 1
        @throws IOException if there was an IO-related problem creating the DYLD slide info 1
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEntriesCount(self) -> int: ...

    def getEntriesOffset(self) -> int: ...

    def getEntriesSize(self) -> int: ...

    def getTocCount(self) -> int: ...

    def getTocOffset(self) -> int: ...

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
    def entriesCount(self) -> int: ...

    @property
    def entriesOffset(self) -> int: ...

    @property
    def entriesSize(self) -> int: ...

    @property
    def tocCount(self) -> int: ...

    @property
    def tocOffset(self) -> int: ...
