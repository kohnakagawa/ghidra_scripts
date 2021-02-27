import ghidra.app.util.bin.format.pe
import ghidra.app.util.bin.format.pe.cli.tables
import ghidra.app.util.importer
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class CliTableProperty(ghidra.app.util.bin.format.pe.cli.tables.CliAbstractTable):
    """
    Describes the Property table. Each row describes a property. Indices into this table point to contiguous runs of properties
     ending with the next index from the PropertyMap table or with the end of this table.
    """





    def __init__(self, reader: ghidra.app.util.bin.BinaryReader, stream: ghidra.app.util.bin.format.pe.cli.streams.CliStreamMetadata, tableId: ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable): ...



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

    def getRowDataType(self) -> ghidra.program.model.data.StructureDataType: ...

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
    def rowDataType(self) -> ghidra.program.model.data.StructureDataType: ...
