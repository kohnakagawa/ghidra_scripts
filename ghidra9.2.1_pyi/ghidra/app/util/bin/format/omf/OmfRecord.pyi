import ghidra.app.util.bin
import ghidra.app.util.bin.format.omf
import java.lang


class OmfRecord(object):
    COMDEF: int = -80
    COMENT: int = -120
    EXTDEF: int = -116
    FIXUPP: int = -100
    GRPDEF: int = -102
    LCOMDEF: int = -72
    LEDATA: int = -96
    LEXTDEF: int = -76
    LHEADR: int = -126
    LIDATA: int = -94
    LINNUM: int = -108
    LNAMES: int = -106
    LPUBDEF: int = -74
    MODEND: int = -118
    PUBDEF: int = -112
    SEGDEF: int = -104
    THEADR: int = -128



    def __init__(self): ...



    def calcCheckSum(self, reader: ghidra.app.util.bin.BinaryReader) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getRecordLength(self) -> int: ...

    def getRecordType(self) -> int: ...

    def hasBigFields(self) -> bool: ...

    def hashCode(self) -> int: ...

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
    def recordLength(self) -> int: ...

    @property
    def recordType(self) -> int: ...
