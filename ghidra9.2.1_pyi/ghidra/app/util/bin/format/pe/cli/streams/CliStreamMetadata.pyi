import ghidra.app.util.bin.format.pe
import ghidra.app.util.bin.format.pe.cli
import ghidra.app.util.bin.format.pe.cli.streams
import ghidra.app.util.bin.format.pe.cli.tables
import ghidra.app.util.importer
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class CliStreamMetadata(ghidra.app.util.bin.format.pe.cli.streams.CliAbstractStream):
    """
    The Metadata stream is giant and complicated.  It is made up of CliAbstractTables.
    """





    def __init__(self, header: ghidra.app.util.bin.format.pe.cli.CliStreamHeader, guidStream: ghidra.app.util.bin.format.pe.cli.streams.CliStreamGuid, userStringsStream: ghidra.app.util.bin.format.pe.cli.streams.CliStreamUserStrings, stringsStream: ghidra.app.util.bin.format.pe.cli.streams.CliStreamStrings, blobStream: ghidra.app.util.bin.format.pe.cli.streams.CliStreamBlob, fileOffset: long, rva: int, reader: ghidra.app.util.bin.BinaryReader):
        """
        Creates a new Metadata stream.
        @param header The stream header associated with this stream.
        @param guidStream The GUID stream.
        @param userStringsStream The user strings stream.
        @param stringsStream The strings stream.
        @param blobStream The blob stream.
        @param fileOffset The file offset where this stream starts.
        @param rva The relative virtual address where this stream starts.
        @param reader A reader that is set to the start of the stream.
        @throws IOException if there is a problem reading the stream.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getBlobIndexDataType(self) -> ghidra.program.model.data.DataType:
        """
        Gets the data type of the index into the Blob stream.  Will be either
         {@link DWordDataType} or {@link WordDataType}.
        @return The data type of the index into the string stream.
        """
        ...

    def getBlobStream(self) -> ghidra.app.util.bin.format.pe.cli.streams.CliStreamBlob:
        """
        Gets the blob stream.
        @return The blob stream.  Could be null if one doesn't exist.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getGuidIndexDataType(self) -> ghidra.program.model.data.DataType:
        """
        Gets the data type of the index into the GUID stream.  Will be either
         {@link DWordDataType} or {@link WordDataType}.
        @return The data type of the index into the string stream.
        """
        ...

    def getGuidStream(self) -> ghidra.app.util.bin.format.pe.cli.streams.CliStreamGuid:
        """
        Gets the GUID stream.
        @return The GUID stream.  Could be null if one doesn't exist.
        """
        ...

    def getMajorVersion(self) -> int:
        """
        Gets the major version.
        @return The major version.
        """
        ...

    def getMinorVersion(self) -> int:
        """
        Gets the minor version.
        @return The minor version.
        """
        ...

    @staticmethod
    def getName() -> unicode:
        """
        Gets the name of this stream.
        @return The name of this stream.
        """
        ...

    def getNumberRowsForTable(self, tableType: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable) -> int:
        """
        Gets the number of rows in the table with the given table type.
        @param tableType The type of table to get the number of rows of.
        @return The number of rows in the table with the given table type.  Could be 0 if
           the table of the given type was not found.
        """
        ...

    def getSorted(self) -> long:
        """
        Gets the sorted field.
        @return The sorted field.
        """
        ...

    def getStreamHeader(self) -> ghidra.app.util.bin.format.pe.cli.CliStreamHeader:
        """
        Gets this stream's header.
        @return This stream's header.
        """
        ...

    @staticmethod
    def getStreamMarkupAddress(program: ghidra.program.model.listing.Program, isBinary: bool, monitor: ghidra.util.task.TaskMonitor, log: ghidra.app.util.importer.MessageLog, ntHeader: ghidra.app.util.bin.format.pe.NTHeader, stream: ghidra.app.util.bin.format.pe.cli.streams.CliAbstractStream, streamIndex: int) -> ghidra.program.model.address.Address:
        """
        Gets the markup address of an offset in a given stream.
        @param program
        @param isBinary
        @param monitor
        @param log
        @param ntHeader
        @param stream The stream to offset into.
        @param streamIndex The index into the stream.
        @return The markup address of the given offset in the provided stream.
        """
        ...

    def getStringIndexDataType(self) -> ghidra.program.model.data.DataType:
        """
        Gets the data type of the index into the string stream.  Will be either
         {@link DWordDataType} or {@link WordDataType}.
        @return The data type of the index into the string stream.
        """
        ...

    def getStringsStream(self) -> ghidra.app.util.bin.format.pe.cli.streams.CliStreamStrings:
        """
        Gets the strings stream.
        @return The strings stream.  Could be null if one doesn't exist.
        """
        ...

    @overload
    def getTable(self, tableId: int) -> ghidra.app.util.bin.format.pe.cli.tables.CliAbstractTable:
        """
        Gets the table with the provided table type id from the metadata stream.
        @param tableId The id of the table type to get.
        @return The table with the provided table id.  Could be null if it doesn't exist.
        """
        ...

    @overload
    def getTable(self, tableType: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable) -> ghidra.app.util.bin.format.pe.cli.tables.CliAbstractTable:
        """
        Gets the table with the provided table type from the metadata stream.
        @param tableType The type of table to get.
        @return The table with the provided table type.  Could be null if it doesn't exist.
        """
        ...

    def getTableIndexDataType(self, table: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable) -> ghidra.program.model.data.DataType:
        """
        Gets the data type of the index into a metadata table.  Will be either
         {@link DWordDataType} or {@link WordDataType}.
        @return The data type of the index into the string stream.
        """
        ...

    def getUserStringsStream(self) -> ghidra.app.util.bin.format.pe.cli.streams.CliStreamUserStrings:
        """
        Gets the user strings stream.
        @return The user strings stream.  Could be null if one doesn't exist.
        """
        ...

    def getValid(self) -> long:
        """
        Gets the valid field.
        @return The valid field.
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
    def blobIndexDataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def blobStream(self) -> ghidra.app.util.bin.format.pe.cli.streams.CliStreamBlob: ...

    @property
    def guidIndexDataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def guidStream(self) -> ghidra.app.util.bin.format.pe.cli.streams.CliStreamGuid: ...

    @property
    def majorVersion(self) -> int: ...

    @property
    def minorVersion(self) -> int: ...

    @property
    def sorted(self) -> long: ...

    @property
    def stringIndexDataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def stringsStream(self) -> ghidra.app.util.bin.format.pe.cli.streams.CliStreamStrings: ...

    @property
    def userStringsStream(self) -> ghidra.app.util.bin.format.pe.cli.streams.CliStreamUserStrings: ...

    @property
    def valid(self) -> long: ...
