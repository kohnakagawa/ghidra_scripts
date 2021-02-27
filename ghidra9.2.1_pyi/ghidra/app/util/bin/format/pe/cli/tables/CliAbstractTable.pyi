import ghidra.app.util.bin
import ghidra.app.util.bin.format.pe
import ghidra.app.util.bin.format.pe.cli.tables
import ghidra.app.util.importer
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class CliAbstractTable(object, ghidra.app.util.bin.StructConverter, ghidra.app.util.bin.format.pe.PeMarkupable):
    """
    Generic Metadata table.  Subclasses should provided implementations for the actual
     tables.
    """

    ASCII: ghidra.program.model.data.DataType = char
    BYTE: ghidra.program.model.data.DataType = byte
    DWORD: ghidra.program.model.data.DataType = dword
    IBO32: ghidra.program.model.data.DataType = ImageBaseOffset32
    PATH: unicode = u'/PE/CLI/Metadata/Tables'
    POINTER: ghidra.program.model.data.DataType = pointer
    QWORD: ghidra.program.model.data.DataType = qword
    STRING: ghidra.program.model.data.DataType = string
    UTF16: ghidra.program.model.data.DataType = unicode
    UTF8: ghidra.program.model.data.DataType = string-utf8
    VOID: ghidra.program.model.data.DataType = void
    WORD: ghidra.program.model.data.DataType = word



    def __init__(self, reader: ghidra.app.util.bin.BinaryReader, metadataStream: ghidra.app.util.bin.format.pe.cli.streams.CliStreamMetadata, tableType: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable):
        """
        Creates a new generic CLI metadata table.  This is intended to be called by a subclass
         metadata table during its creation.
        @param reader A reader that is used to read the table.
        @param metadataStream The metadata stream that the table lives in.
        @param tableType The type of table to create.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getNumRows(self) -> int:
        """
        Gets the number of rows in this table.

         return The number of rows in this table.
        """
        ...

    def getRow(self, rowIndex: int) -> ghidra.app.util.bin.format.pe.cli.tables.CliAbstractTableRow:
        """
        Gets the row at the given index.
         <p>
         NOTE: Per ISO/IEC 23271:2012(E) III.1.9, Row indices start from 1, while heap/stream indices start from 0.
        @param rowIndex The index of the row to get (starting at 1).
        @return The row at the given index.
        @throws IndexOutOfBoundsException if the row index is invalid.
        """
        ...

    def getRowDataType(self) -> ghidra.program.model.data.DataType:
        """
        Gets the data type of a row in this table.
        @return The data type of a row in this table.
        """
        ...

    def getRowSize(self) -> int:
        """
        Gets the size in bytes of a row in this table.

         return The size in bytes of a row in this table.
        """
        ...

    def getTableSize(self) -> int:
        """
        Gets the size in bytes of this table.
        @return The size in bytes of this table.
        """
        ...

    def getTableType(self) -> ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable:
        """
        Gets this table's table type.
        @return This table's table type.
        """
        ...

    def hashCode(self) -> int: ...

    def markup(self, program: ghidra.program.model.listing.Program, isBinary: bool, monitor: ghidra.util.task.TaskMonitor, log: ghidra.app.util.importer.MessageLog, ntHeader: ghidra.app.util.bin.format.pe.NTHeader) -> None: ...

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
    def numRows(self) -> int: ...

    @property
    def rowDataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def rowSize(self) -> int: ...

    @property
    def tableSize(self) -> int: ...

    @property
    def tableType(self) -> ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable: ...
