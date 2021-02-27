from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.omf
import ghidra.app.util.importer
import ghidra.program.model.address
import ghidra.program.model.lang
import java.io
import java.lang


class OmfSegmentHeader(ghidra.app.util.bin.format.omf.OmfRecord):





    class SectionStream(java.io.InputStream):




        def __init__(self, __a0: ghidra.app.util.bin.format.omf.OmfSegmentHeader, __a1: ghidra.app.util.bin.BinaryReader, __a2: ghidra.app.util.importer.MessageLog): ...



        def available(self) -> int: ...

        def close(self) -> None: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def mark(self, __a0: int) -> None: ...

        def markSupported(self) -> bool: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        @staticmethod
        def nullInputStream() -> java.io.InputStream: ...

        @overload
        def read(self) -> int: ...

        @overload
        def read(self, __a0: List[int]) -> int: ...

        @overload
        def read(self, __a0: List[int], __a1: int, __a2: int) -> int: ...

        def readAllBytes(self) -> List[int]: ...

        @overload
        def readNBytes(self, __a0: int) -> List[int]: ...

        @overload
        def readNBytes(self, __a0: List[int], __a1: int, __a2: int) -> int: ...

        def reset(self) -> None: ...

        def skip(self, __a0: long) -> long: ...

        def toString(self) -> unicode: ...

        def transferTo(self, __a0: java.io.OutputStream) -> long: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self, reader: ghidra.app.util.bin.BinaryReader): ...



    def calcCheckSum(self, reader: ghidra.app.util.bin.BinaryReader) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddress(self, language: ghidra.program.model.lang.Language) -> ghidra.program.model.address.Address:
        """
        @param language is the Program language for this binary
        @return the starting Address for this segment
        """
        ...

    def getAlignment(self) -> int:
        """
        @return the alignment required for this segment
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getClassName(self) -> unicode:
        """
        @return the class name of this segment
        """
        ...

    def getCombine(self) -> int:
        """
        @return special combining rules for this segment
        """
        ...

    def getFrameDatum(self) -> int:
        """
        @return the segment selector needed for this object
        """
        ...

    def getName(self) -> unicode:
        """
        @return the name of this segment
        """
        ...

    def getOverlayName(self) -> unicode:
        """
        @return the name of the overlay, or the empty string
        """
        ...

    def getRawDataStream(self, reader: ghidra.app.util.bin.BinaryReader, log: ghidra.app.util.importer.MessageLog) -> java.io.InputStream:
        """
        Get an InputStream that reads in the raw data for this segment
        @param reader is the image file reader
        @param log the log
        @return the InputStream
        @throws IOException for problems reading from the image file
        """
        ...

    def getRecordLength(self) -> int: ...

    def getRecordType(self) -> int: ...

    def getSegmentLength(self) -> long:
        """
        @return the length of the segment in bytes
        """
        ...

    def getStartAddress(self) -> long:
        """
        @return the load image address for this segment
        """
        ...

    def hasBigFields(self) -> bool: ...

    def hasNonZeroData(self) -> bool:
        """
        @return true if this block uses filler other than zero bytes
        """
        ...

    def hashCode(self) -> int: ...

    def isCode(self) -> bool:
        """
        @return true if this is a code segment
        """
        ...

    def isExecutable(self) -> bool:
        """
        @return true if this segment is executable
        """
        ...

    def isReadable(self) -> bool:
        """
        @return true if this segment is readable
        """
        ...

    def isWritable(self) -> bool:
        """
        @return true if this segment is writable
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

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

    def toString(self) -> unicode: ...

    def validCheckSum(self, reader: ghidra.app.util.bin.BinaryReader) -> bool: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def alignment(self) -> int: ...

    @property
    def className(self) -> unicode: ...

    @property
    def code(self) -> bool: ...

    @property
    def combine(self) -> int: ...

    @property
    def executable(self) -> bool: ...

    @property
    def frameDatum(self) -> int: ...

    @property
    def name(self) -> unicode: ...

    @property
    def overlayName(self) -> unicode: ...

    @property
    def readable(self) -> bool: ...

    @property
    def segmentLength(self) -> long: ...

    @property
    def startAddress(self) -> long: ...

    @property
    def writable(self) -> bool: ...
