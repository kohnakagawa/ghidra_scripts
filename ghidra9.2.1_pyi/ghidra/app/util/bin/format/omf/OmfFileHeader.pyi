from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.omf
import ghidra.util.task
import java.lang
import java.util


class OmfFileHeader(ghidra.app.util.bin.format.omf.OmfRecord):




    def __init__(self, reader: ghidra.app.util.bin.BinaryReader): ...



    def calcCheckSum(self, reader: ghidra.app.util.bin.BinaryReader) -> int: ...

    @staticmethod
    def checkMagicNumber(reader: ghidra.app.util.bin.BinaryReader) -> bool:
        """
        Check that the file has the specific OMF magic number
        @param reader accesses the bytes of the file
        @return true if the magic number matches
        @throws IOException for problems reading bytes
        """
        ...

    @staticmethod
    def createReader(provider: ghidra.app.util.bin.ByteProvider) -> ghidra.app.util.bin.BinaryReader:
        """
        Create a reader for a specific OMF file
        @param provider is the underlying ByteProvider
        @return the new reader
        """
        ...

    @staticmethod
    def doLinking(__a0: long, __a1: java.util.ArrayList, __a2: java.util.ArrayList) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getExternalSymbols(self) -> List[ghidra.app.util.bin.format.omf.OmfExternalSymbol]:
        """
        @return the list of symbols that are external to this file
        """
        ...

    def getExtraSegments(self) -> List[ghidra.app.util.bin.format.omf.OmfSegmentHeader]:
        """
        @return the list of segments which are Borland extensions
        """
        ...

    def getFixups(self) -> List[ghidra.app.util.bin.format.omf.OmfFixupRecord]:
        """
        @return the list of relocation records for this file
        """
        ...

    def getGroups(self) -> List[ghidra.app.util.bin.format.omf.OmfGroupRecord]:
        """
        @return the list of group records for this file
        """
        ...

    def getLibraryModuleName(self) -> unicode:
        """
        The name of the object module (within a library)
        @return the name
        """
        ...

    def getMachineName(self) -> unicode:
        """
        @return the string identifying the architecture this object was compiled for
        """
        ...

    def getName(self) -> unicode:
        """
        This is usually the original source filename
        @return the name
        """
        ...

    def getPublicSymbols(self) -> List[ghidra.app.util.bin.format.omf.OmfSymbolRecord]:
        """
        @return the list of symbols exported by this file
        """
        ...

    def getRecordLength(self) -> int: ...

    def getRecordType(self) -> int: ...

    def getSegments(self) -> List[ghidra.app.util.bin.format.omf.OmfSegmentHeader]:
        """
        @return the list of segments in this file
        """
        ...

    def getTranslator(self) -> unicode:
        """
        If the OMF file contains a "translator" record, this is usually a string
         indicating the compiler which produced the file.
        @return the translator for this file
        """
        ...

    def hasBigFields(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isLittleEndian(self) -> bool:
        """
        @return true if the file describes the load image for a little endian architecture
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def parse(reader: ghidra.app.util.bin.BinaryReader, monitor: ghidra.util.task.TaskMonitor) -> ghidra.app.util.bin.format.omf.OmfFileHeader:
        """
        Parse the entire object file
        @param reader is the byte stream
        @param monitor is checked for cancel button
        @return the header record as root of object
        @throws IOException for problems reading data
        @throws OmfException for malformed records
        """
        ...

    def readCheckSumByte(self, reader: ghidra.app.util.bin.BinaryReader) -> None: ...

    @staticmethod
    def readIndex(reader: ghidra.app.util.bin.BinaryReader) -> int: ...

    @staticmethod
    def readInt1Or2(reader: ghidra.app.util.bin.BinaryReader, isBig: bool) -> int: ...

    @staticmethod
    def readInt2Or4(reader: ghidra.app.util.bin.BinaryReader, isBig: bool) -> int: ...

    @staticmethod
    def readRecord(reader: ghidra.app.util.bin.BinaryReader) -> ghidra.app.util.bin.format.omf.OmfRecord: ...

    def readRecordHeader(self, reader: ghidra.app.util.bin.BinaryReader) -> None: ...

    @staticmethod
    def readString(reader: ghidra.app.util.bin.BinaryReader) -> unicode:
        """
        Read the OMF string format,  1-byte length, followed by that many ascii characters
        @param reader
        @return
        @throws IOException
        """
        ...

    def resolveNames(self) -> None:
        """
        Resolve special names associated with each segment: segment, class, overlay names
         and group: group name
         For each segment, the read/write/execute permissions are also determined
        @throws OmfException if any name indices are malformed
        """
        ...

    def resolveSegment(self, index: int) -> ghidra.app.util.bin.format.omf.OmfSegmentHeader:
        """
        Given an index, retrieve the specific segment it refers to. This
         incorporates the special Borland segments, where the index has
         the bit 0x4000 set.
        @param index identifies the segment
        @return the corresponding OmfSegmentHeader
        @throws OmfException if the index is malformed
        """
        ...

    @staticmethod
    def scan(reader: ghidra.app.util.bin.BinaryReader, monitor: ghidra.util.task.TaskMonitor, initialCommentsOnly: bool) -> ghidra.app.util.bin.format.omf.OmfFileHeader:
        """
        Scan the object file, for the main header and comment records. Other records are parsed but not saved
        @param reader is the byte stream
        @param monitor is checked for cancellation
        @param initialCommentsOnly is true if we only want to scan the header and the initial comments,
        @return the header record
        @throws IOException for problems reading program data
        @throws OmfException for malformed records
        """
        ...

    def sortSegmentDataBlocks(self) -> None:
        """
        Sort the explicit data-blocks for each segment into address order.
        """
        ...

    def toString(self) -> unicode: ...

    def validCheckSum(self, reader: ghidra.app.util.bin.BinaryReader) -> bool: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def externalSymbols(self) -> java.util.ArrayList: ...

    @property
    def extraSegments(self) -> java.util.ArrayList: ...

    @property
    def fixups(self) -> java.util.ArrayList: ...

    @property
    def groups(self) -> java.util.ArrayList: ...

    @property
    def libraryModuleName(self) -> unicode: ...

    @property
    def littleEndian(self) -> bool: ...

    @property
    def machineName(self) -> unicode: ...

    @property
    def name(self) -> unicode: ...

    @property
    def publicSymbols(self) -> java.util.ArrayList: ...

    @property
    def segments(self) -> java.util.ArrayList: ...

    @property
    def translator(self) -> unicode: ...
