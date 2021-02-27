from typing import List
import generic.continues
import ghidra.app.util.bin
import ghidra.app.util.bin.format.macho
import ghidra.app.util.bin.format.macho.commands
import ghidra.program.model.data
import java.lang


class MachHeader(object, ghidra.app.util.bin.StructConverter):
    """
    Represents a mach_header structure.
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



    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    @overload
    @staticmethod
    def createMachHeader(factory: generic.continues.GenericFactory, provider: ghidra.app.util.bin.ByteProvider) -> ghidra.app.util.bin.format.macho.MachHeader:
        """
        Assumes the MachHeader starts at index 0 in the ByteProvider.
        @param provider the ByteProvider
        @throws IOException if an I/O error occurs while reading from the ByteProvider
        @throws MachException if an invalid MachHeader is detected
        """
        ...

    @overload
    @staticmethod
    def createMachHeader(factory: generic.continues.GenericFactory, provider: ghidra.app.util.bin.ByteProvider, machHeaderStartIndexInProvider: long) -> ghidra.app.util.bin.format.macho.MachHeader:
        """
        Assumes the MachHeader starts at index <i>machHeaderStartIndexInProvider</i> in the ByteProvider.
        @param provider the ByteProvider
        @param machHeaderStartIndexInProvider the index into the ByteProvider where the MachHeader begins.
        @throws IOException if an I/O error occurs while reading from the ByteProvider
        @throws MachException if an invalid MachHeader is detected
        """
        ...

    @overload
    @staticmethod
    def createMachHeader(factory: generic.continues.GenericFactory, provider: ghidra.app.util.bin.ByteProvider, machHeaderStartIndexInProvider: long, isRemainingMachoRelativeToStartIndex: bool) -> ghidra.app.util.bin.format.macho.MachHeader:
        """
        Assumes the MachHeader starts at index <i>machHeaderStartIndexInProvider</i> in the ByteProvider.
        @param provider the ByteProvider
        @param machHeaderStartIndexInProvider the index into the ByteProvider where the MachHeader begins.
        @param isRemainingMachoRelativeToStartIndex TRUE if the rest of the macho uses relative indexing. This is common in UBI and kernel cache files.
                                                     FALSE if the rest of the file uses absolute indexing from 0. This is common in DYLD cache files.
        @throws IOException if an I/O error occurs while reading from the ByteProvider
        @throws MachException if an invalid MachHeader is detected
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAddressSize(self) -> int: ...

    def getAllSections(self) -> List[ghidra.app.util.bin.format.macho.Section]: ...

    def getAllSegments(self) -> List[ghidra.app.util.bin.format.macho.commands.SegmentCommand]: ...

    def getClass(self) -> java.lang.Class: ...

    def getCpuSubType(self) -> int: ...

    def getCpuType(self) -> int: ...

    def getDescription(self) -> unicode: ...

    def getFileType(self) -> int: ...

    def getFirstLoadCommand(self, classType: java.lang.Class) -> object: ...

    def getFlags(self) -> int: ...

    def getImageBase(self) -> long: ...

    @overload
    def getLoadCommands(self) -> List[ghidra.app.util.bin.format.macho.commands.LoadCommand]: ...

    @overload
    def getLoadCommands(self, classType: java.lang.Class) -> List[object]: ...

    def getMagic(self) -> int: ...

    def getNumberOfCommands(self) -> int: ...

    def getReserved(self) -> int: ...

    def getSection(self, segmentName: unicode, sectionName: unicode) -> ghidra.app.util.bin.format.macho.Section: ...

    def getSegment(self, segmentName: unicode) -> ghidra.app.util.bin.format.macho.commands.SegmentCommand: ...

    def getSizeOfCommands(self) -> int: ...

    def getStartIndexInProvider(self) -> long: ...

    def hashCode(self) -> int: ...

    def is32bit(self) -> bool: ...

    def isLittleEndian(self) -> bool: ...

    @staticmethod
    def isMachHeader(provider: ghidra.app.util.bin.ByteProvider) -> bool:
        """
        Returns true if the specified ByteProvider starts with a Mach header magic signature.
        @param provider {@link ByteProvider} to check
        @return boolean true if byte provider starts with a MachHeader
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def parse(self) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def 32bit(self) -> bool: ...

    @property
    def addressSize(self) -> int: ...

    @property
    def allSections(self) -> List[object]: ...

    @property
    def allSegments(self) -> List[object]: ...

    @property
    def cpuSubType(self) -> int: ...

    @property
    def cpuType(self) -> int: ...

    @property
    def description(self) -> unicode: ...

    @property
    def fileType(self) -> int: ...

    @property
    def flags(self) -> int: ...

    @property
    def imageBase(self) -> long: ...

    @property
    def littleEndian(self) -> bool: ...

    @property
    def loadCommands(self) -> List[object]: ...

    @property
    def magic(self) -> int: ...

    @property
    def numberOfCommands(self) -> int: ...

    @property
    def reserved(self) -> int: ...

    @property
    def sizeOfCommands(self) -> int: ...

    @property
    def startIndexInProvider(self) -> long: ...
