from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.pe.cli.blobs
import ghidra.app.util.bin.format.pe.cli.blobs.CliAbstractSig
import ghidra.app.util.bin.format.pe.cli.streams
import ghidra.program.model.data
import java.lang


class CliSigMethodDef(ghidra.app.util.bin.format.pe.cli.blobs.CliAbstractSig):




    def __init__(self, blob: ghidra.app.util.bin.format.pe.cli.blobs.CliBlob): ...



    @staticmethod
    def convertTypeCodeToDataType(typeCode: ghidra.app.util.bin.format.pe.cli.blobs.CliAbstractSig.CliElementType) -> ghidra.program.model.data.DataType: ...

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

    def getContentsComment(self) -> unicode: ...

    def getContentsDataType(self) -> ghidra.program.model.data.DataType: ...

    def getContentsName(self) -> unicode: ...

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

    def getParamTypes(self) -> List[ghidra.app.util.bin.format.pe.cli.blobs.CliAbstractSig.CliParam]: ...

    @overload
    def getRepresentation(self) -> unicode: ...

    @overload
    def getRepresentation(self, stream: ghidra.app.util.bin.format.pe.cli.streams.CliStreamMetadata) -> unicode: ...

    def getReturnType(self) -> ghidra.app.util.bin.format.pe.cli.blobs.CliAbstractSig.CliRetType: ...

    @overload
    def getShortRepresentation(self) -> unicode: ...

    @overload
    def getShortRepresentation(self, stream: ghidra.app.util.bin.format.pe.cli.streams.CliStreamMetadata) -> unicode: ...

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

    def readCliType(self, reader: ghidra.app.util.bin.BinaryReader) -> ghidra.app.util.bin.format.pe.cli.blobs.CliAbstractSig.CliSigType: ...

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
    def contentsComment(self) -> unicode: ...

    @property
    def contentsDataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def contentsName(self) -> unicode: ...

    @property
    def paramTypes(self) -> List[ghidra.app.util.bin.format.pe.cli.blobs.CliAbstractSig.CliParam]: ...

    @property
    def returnType(self) -> ghidra.app.util.bin.format.pe.cli.blobs.CliAbstractSig.CliRetType: ...
