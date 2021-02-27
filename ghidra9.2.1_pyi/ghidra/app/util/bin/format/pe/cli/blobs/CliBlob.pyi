from typing import List
import ghidra.app.util.bin
import ghidra.program.model.data
import java.lang


class CliBlob(object, ghidra.app.util.bin.StructConverter):
    """
    Describes a blob in the #Blob heap. Format is a coded size then the blob contents.

     Paraphrasing from ISO 23271:2012 11.24.2.4 (p272):
     - If the first one byte of the 'blob' is 0bbbbbbb_2: size is bbbbbbb_2 bytes.
     -
     -
     The first entry in the heap is the empty 'blob' consisting of a single zero byte.
    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    PATH: unicode = u'/PE/CLI/Blobs'
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    def __init__(self, streamIndex: int, reader: ghidra.app.util.bin.BinaryReader):
        """
        Creates a new blob from the given reader, which should be positioned at the start
         of the blob.  The reader will be positioned directly after the blob upon completion
         of the constructor.
        @param streamIndex The blob's stream index.
        @param reader The reader to use to read the blob.
        @throws IOException if there was a problem reading the blob.
        """
        ...



    @overload
    @staticmethod
    def decodeCompressedSigned(codedSize: int) -> int: ...

    @overload
    @staticmethod
    def decodeCompressedSigned(codedSize: int) -> int: ...

    @overload
    @staticmethod
    def decodeCompressedSigned(codedSize: int) -> int: ...

    @staticmethod
    def decodeCompressedSignedInt(reader: ghidra.app.util.bin.BinaryReader) -> int: ...

    @overload
    @staticmethod
    def decodeCompressedUnsigned(codedSize: int) -> int: ...

    @overload
    @staticmethod
    def decodeCompressedUnsigned(codedSize: int) -> int: ...

    @overload
    @staticmethod
    def decodeCompressedUnsigned(codedSize: int) -> int: ...

    @staticmethod
    def decodeCompressedUnsignedInt(reader: ghidra.app.util.bin.BinaryReader) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getContents(self) -> List[int]:
        """
        Gets the blob's contents.
        @return the blob's contents.  Could be null if there was a problem reading the
           contents.
        """
        ...

    def getContentsComment(self) -> unicode:
        """
        Gets the comment associated with this blob's contents.
        @return The comment associated with this blob's contents.
        """
        ...

    def getContentsDataType(self) -> ghidra.program.model.data.DataType:
        """
        Gets the data type associated with this blob's contents.
        @return The data type associated with this blob's contents.
        """
        ...

    def getContentsName(self) -> unicode:
        """
        Gets the name associated with this blob's contents.
        @return The name associated with this blob's contents.
        """
        ...

    def getContentsReader(self) -> ghidra.app.util.bin.BinaryReader:
        """
        Gets a new binary reader positioned at the start of this blob's contents.
        @return A new binary reader positioned at the start of this blob's contents.
        """
        ...

    def getContentsSize(self) -> int:
        """
        Gets the blob's contents size in bytes.
        @return The blob's contents size in bytes.
        """
        ...

    @staticmethod
    def getDataTypeForBytes(numBytes: int) -> ghidra.program.model.data.DataType: ...

    def getName(self) -> unicode:
        """
        Gets the name of this blob.
        @return The name of this blob.
        """
        ...

    def getRepresentation(self) -> unicode:
        """
        Gets the string representation of this blob.
        @return The string representation of this blob.
        """
        ...

    def getSize(self) -> int:
        """
        Gets the blob's size in bytes (includes all fields).
        @return The blob's size in bytes.
        """
        ...

    def getSizeDataType(self) -> ghidra.program.model.data.DataType:
        """
        Gets the proper data type for the blob's size field.
        @return The proper data type for the blob's size field.
        """
        ...

    def getStreamIndex(self) -> int:
        """
        Gets the index into the blob stream of this blob.
        @return The index into the blob stream of this blob.
        """
        ...

    def hashCode(self) -> int: ...

    def isLittleEndian(self) -> bool:
        """
        Checks to see whether or not this blob is little endian.
        @return True if this blob is little endian; false if big endian.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def testSizeDecoding() -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def contents(self) -> List[int]: ...

    @property
    def contentsComment(self) -> unicode: ...

    @property
    def contentsDataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def contentsName(self) -> unicode: ...

    @property
    def contentsReader(self) -> ghidra.app.util.bin.BinaryReader: ...

    @property
    def contentsSize(self) -> int: ...

    @property
    def littleEndian(self) -> bool: ...

    @property
    def name(self) -> unicode: ...

    @property
    def representation(self) -> unicode: ...

    @property
    def size(self) -> int: ...

    @property
    def sizeDataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def streamIndex(self) -> int: ...
