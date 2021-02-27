from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.macho.dyld
import ghidra.app.util.importer
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class DyldCacheHeader(object, ghidra.app.util.bin.StructConverter):
    """
    Represents a dyld_cache_header structure.
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
        Create a new {@link DyldCacheHeader}.
        @param reader A {@link BinaryReader} positioned at the start of a DYLD cache header
        @throws IOException if there was an IO-related problem creating the DYLD cache header
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getArchitecture(self) -> ghidra.app.util.bin.format.macho.dyld.DyldArchitecture:
        """
        Gets architecture information.
        @return architecture information
        """
        ...

    def getBaseAddress(self) -> long:
        """
        Gets the base address of the DYLD cache.  This is where the cache should be loaded in
         memory.
        @return The base address of the DYLD cache
        """
        ...

    def getBranchPoolAddresses(self) -> List[long]:
        """
        Gets the {@link List} of branch pool address.  Requires header to have been parsed.
        @return The {@link List} of branch pool address
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getImageInfos(self) -> List[ghidra.app.util.bin.format.macho.dyld.DyldCacheImageInfo]:
        """
        Gets the {@link List} of {@link DyldCacheImageInfo}s. Requires header to have been parsed.
        @return The {@link List} of {@link DyldCacheImageInfo}s
        """
        ...

    def getImagesCount(self) -> int:
        """
        Gets the number of {@link DyldCacheImageInfo}s.
        @return The number of {@link DyldCacheImageInfo}s
        """
        ...

    def getImagesOffset(self) -> int:
        """
        Gets the file offset to first {@link DyldCacheImageInfo}.
        @return The file offset to first {@link DyldCacheImageInfo}
        """
        ...

    def getLocalSymbolsInfo(self) -> ghidra.app.util.bin.format.macho.dyld.DyldCacheLocalSymbolsInfo:
        """
        Gets the {@link DyldCacheLocalSymbolsInfo}.
        @return The {@link DyldCacheLocalSymbolsInfo}.  Could be be null if it didn't parse.
        """
        ...

    def getMagic(self) -> List[int]:
        """
        Gets the magic bytes, which contain version information.
        @return The magic bytes
        """
        ...

    def getMappingInfos(self) -> List[ghidra.app.util.bin.format.macho.dyld.DyldCacheMappingInfo]:
        """
        Gets the {@link List} of {@link DyldCacheMappingInfo}s.  Requires header to have been parsed.
        @return The {@link List} of {@link DyldCacheMappingInfo}s
        """
        ...

    def getSlideInfo(self) -> ghidra.app.util.bin.format.macho.dyld.DyldCacheSlideInfoCommon:
        """
        Gets the {@link DyldCacheSlideInfoCommon}.
        @return the {@link DyldCacheSlideInfoCommon}.  Common, or particular version
        """
        ...

    def getSlideInfoOffset(self) -> long:
        """
        @return slideInfoOffset
        """
        ...

    def getSlideInfoSize(self) -> long:
        """
        @return slideInfoSize
        """
        ...

    def hashCode(self) -> int: ...

    def markup(self, program: ghidra.program.model.listing.Program, space: ghidra.program.model.address.AddressSpace, monitor: ghidra.util.task.TaskMonitor, log: ghidra.app.util.importer.MessageLog) -> None:
        """
        Marks up this {@link DyldCacheHeader} with data structures and comments.
        @param program The {@link Program} to mark up
        @param space The {@link Program}'s {@link AddressSpace}
        @param monitor A cancellable task monitor
        @param log The log
        @throws CancelledException if the user cancelled the operation
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def parseFromFile(self, parseSymbols: bool, log: ghidra.app.util.importer.MessageLog, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Parses the structures referenced by this {@link DyldCacheHeader} from a file.
        @param parseSymbols True if symbols should be parsed (could be very slow); otherwise, false
        @param log The log
        @param monitor A cancellable task monitor
        @throws CancelledException if the user cancelled the operation
        """
        ...

    def parseFromMemory(self, program: ghidra.program.model.listing.Program, space: ghidra.program.model.address.AddressSpace, log: ghidra.app.util.importer.MessageLog, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Parses the structures referenced by this {@link DyldCacheHeader} from memory.
        @param program The {@link Program} whose memory to parse
        @param space The {@link Program}'s {@link AddressSpace}
        @param log The log
        @param monitor A cancellable task monitor
        @throws CancelledException if the user cancelled the operation
        """
        ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def architecture(self) -> ghidra.app.util.bin.format.macho.dyld.DyldArchitecture: ...

    @property
    def baseAddress(self) -> long: ...

    @property
    def branchPoolAddresses(self) -> List[object]: ...

    @property
    def imageInfos(self) -> List[object]: ...

    @property
    def imagesCount(self) -> int: ...

    @property
    def imagesOffset(self) -> int: ...

    @property
    def localSymbolsInfo(self) -> ghidra.app.util.bin.format.macho.dyld.DyldCacheLocalSymbolsInfo: ...

    @property
    def magic(self) -> List[int]: ...

    @property
    def mappingInfos(self) -> List[object]: ...

    @property
    def slideInfo(self) -> ghidra.app.util.bin.format.macho.dyld.DyldCacheSlideInfoCommon: ...

    @property
    def slideInfoOffset(self) -> long: ...

    @property
    def slideInfoSize(self) -> long: ...
