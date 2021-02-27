from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.pe.cli.streams
import ghidra.app.util.bin.format.pe.cli.tables
import ghidra.app.util.bin.format.pe.cli.tables.indexes
import ghidra.program.model.data
import java.lang


class CliIndexMemberRefParent(ghidra.app.util.bin.format.pe.cli.tables.indexes.CliCodedIndexUtils):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    @staticmethod
    def getRowIndex(codedIndex: int) -> int: ...

    @overload
    @staticmethod
    def getRowIndex(codedIndex: int, bitsUsed: int) -> int: ...

    @overload
    @staticmethod
    def getTableName(codedIndex: int) -> ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable: ...

    @overload
    @staticmethod
    def getTableName(codedIndex: int, bitsUsed: int, tables: List[ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable]) -> ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    @staticmethod
    def readCodedIndex(reader: ghidra.app.util.bin.BinaryReader, stream: ghidra.app.util.bin.format.pe.cli.streams.CliStreamMetadata) -> int: ...

    @overload
    @staticmethod
    def readCodedIndex(reader: ghidra.app.util.bin.BinaryReader, stream: ghidra.app.util.bin.format.pe.cli.streams.CliStreamMetadata, bitsUsed: int, tables: List[ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable]) -> int: ...

    @overload
    @staticmethod
    def toDataType(stream: ghidra.app.util.bin.format.pe.cli.streams.CliStreamMetadata) -> ghidra.program.model.data.DataType: ...

    @overload
    @staticmethod
    def toDataType(stream: ghidra.app.util.bin.format.pe.cli.streams.CliStreamMetadata, bitsUsed: int, tables: List[ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable]) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
