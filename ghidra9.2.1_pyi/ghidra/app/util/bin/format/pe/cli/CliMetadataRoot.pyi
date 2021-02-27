import ghidra.app.util.bin
import ghidra.app.util.bin.format.pe
import ghidra.app.util.bin.format.pe.cli
import ghidra.app.util.bin.format.pe.cli.streams
import ghidra.app.util.importer
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util.task
import java.lang
import java.util


class CliMetadataRoot(object, ghidra.app.util.bin.StructConverter, ghidra.app.util.bin.format.pe.PeMarkupable):
    """
    The header of a CliMetadataDirectory.
    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    NAME: unicode = u'CLI_METADATA_HEADER'
    PATH: unicode = u'/PE/CLI'
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    def __init__(self, reader: ghidra.app.util.bin.BinaryReader, rva: int):
        """
        Constructs a new CLI Metadata Root datatype. Matches ISO 23271 II.24.2.
        @param reader A binary reader set to start reading at the start of this header.
        @param rva The RVA of this header.
        @throws IOException if there is a problem reading the header.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getBlobOffsetAtIndex(self, index: int) -> int: ...

    def getBlobStream(self) -> ghidra.app.util.bin.format.pe.cli.streams.CliStreamBlob:
        """
        Gets the blob stream.
        @return The blob stream.  Could be null if it did not parse correctly.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFileOffset(self) -> long:
        """
        Gets the file offset of this header.
        @return The file offset of this header.
        """
        ...

    def getFlags(self) -> int:
        """
        Gets the flags.
         <p>
         Should always be 0.
        @return The flags.
        """
        ...

    def getGuidStream(self) -> ghidra.app.util.bin.format.pe.cli.streams.CliStreamGuid:
        """
        Gets the GUID stream.
        @return The GUID stream.  Could be null if it did not parse correctly.
        """
        ...

    def getMajorVersion(self) -> int:
        """
        Gets the major version.
        @return The major version.
        """
        ...

    def getMetadataStream(self) -> ghidra.app.util.bin.format.pe.cli.streams.CliStreamMetadata:
        """
        Gets the Metadata stream.
        @return The Metadata stream.  Could be null if it did not parse correctly.
        """
        ...

    def getMinorVersion(self) -> int:
        """
        Gets the minor version.
        @return The minor version.
        """
        ...

    def getReserved(self) -> int:
        """
        Gets the reserved field.
         <p>
         Should always be 0.
        @return The reserved field.
        """
        ...

    def getRva(self) -> int:
        """
        Gets the relative virtual address of this header.
        @return The relative virtual address of this header.
        """
        ...

    def getSignature(self) -> int:
        """
        Gets the signature.
         <p>
         Should always be 0x424a5342.
        @return The signature.
        """
        ...

    def getStreamHeader(self, name: unicode) -> ghidra.app.util.bin.format.pe.cli.CliStreamHeader:
        """
        Gets the stream header with the given name.
        @param name The name of the stream header to get.
        @return The stream header that matches the given name, or null if it wasn't found.
        """
        ...

    def getStreamHeaders(self) -> java.util.Collection:
        """
        Gets the stream headers.
        @return A collection of stream headers.
        """
        ...

    def getStreamsCount(self) -> int:
        """
        Gets the number of streams present in the metadata.
        @return The number of streams present in the metadata.
        """
        ...

    def getStringsStream(self) -> ghidra.app.util.bin.format.pe.cli.streams.CliStreamStrings:
        """
        Gets the strings stream.
        @return The strings stream.  Could be null if it did not parse correctly.
        """
        ...

    def getUserStringsStream(self) -> ghidra.app.util.bin.format.pe.cli.streams.CliStreamUserStrings:
        """
        Gets the user strings stream.
        @return The user strings stream.  Could be null if it did not parse correctly.
        """
        ...

    def getVersion(self) -> unicode:
        """
        Gets the version string.
        @return The version string.  Could be null if the version length appeared
           too long during parsing of the header.
        """
        ...

    def getVersionLength(self) -> int:
        """
        Gets the length of the version string that follows the length field.
        @return The length of the version string that follows the length field.
        """
        ...

    def hashCode(self) -> int: ...

    def markup(self, program: ghidra.program.model.listing.Program, isBinary: bool, monitor: ghidra.util.task.TaskMonitor, log: ghidra.app.util.importer.MessageLog, ntHeader: ghidra.app.util.bin.format.pe.NTHeader) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def parse(self) -> bool: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def blobStream(self) -> ghidra.app.util.bin.format.pe.cli.streams.CliStreamBlob: ...

    @property
    def fileOffset(self) -> long: ...

    @property
    def flags(self) -> int: ...

    @property
    def guidStream(self) -> ghidra.app.util.bin.format.pe.cli.streams.CliStreamGuid: ...

    @property
    def majorVersion(self) -> int: ...

    @property
    def metadataStream(self) -> ghidra.app.util.bin.format.pe.cli.streams.CliStreamMetadata: ...

    @property
    def minorVersion(self) -> int: ...

    @property
    def reserved(self) -> int: ...

    @property
    def rva(self) -> int: ...

    @property
    def signature(self) -> int: ...

    @property
    def streamHeaders(self) -> java.util.Collection: ...

    @property
    def streamsCount(self) -> int: ...

    @property
    def stringsStream(self) -> ghidra.app.util.bin.format.pe.cli.streams.CliStreamStrings: ...

    @property
    def userStringsStream(self) -> ghidra.app.util.bin.format.pe.cli.streams.CliStreamUserStrings: ...

    @property
    def version(self) -> unicode: ...

    @property
    def versionLength(self) -> int: ...
