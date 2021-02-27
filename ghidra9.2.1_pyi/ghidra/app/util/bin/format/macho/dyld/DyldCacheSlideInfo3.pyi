from typing import List
import ghidra.app.util.bin.format.macho.dyld
import ghidra.program.model.data
import java.lang


class DyldCacheSlideInfo3(ghidra.app.util.bin.format.macho.dyld.DyldCacheSlideInfoCommon):
    """
    Represents a dyld_cache_slide_info3 structure.
    """





    def __init__(self, reader: ghidra.app.util.bin.BinaryReader):
        """
        Create a new {@link DyldCacheSlideInfo3}.
        @param reader A {@link BinaryReader} positioned at the start of a DYLD slide info 3
        @throws IOException if there was an IO-related problem creating the DYLD slide info 3
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getAuthValueAdd(self) -> long: ...

    def getClass(self) -> java.lang.Class: ...

    def getPageSize(self) -> int: ...

    def getPageStarts(self) -> List[int]: ...

    def getPageStartsCount(self) -> int: ...

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
    def authValueAdd(self) -> long: ...

    @property
    def pageSize(self) -> int: ...

    @property
    def pageStarts(self) -> List[int]: ...

    @property
    def pageStartsCount(self) -> int: ...
