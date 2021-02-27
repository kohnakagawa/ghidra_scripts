import ghidra.app.util.bin
import ghidra.app.util.bin.format.pe.cli.streams
import ghidra.app.util.bin.format.pe.cli.tables
import ghidra.program.model.data
import java.lang


class CliIndexResolutionScope(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getRowIndex(codedIndex: int) -> int: ...

    @staticmethod
    def getTableName(codedIndex: int) -> ghidra.app.util.bin.format.pe.cli.tables.CliTypeTable: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def readCodedIndex(reader: ghidra.app.util.bin.BinaryReader, stream: ghidra.app.util.bin.format.pe.cli.streams.CliStreamMetadata) -> int: ...

    @staticmethod
    def toDataType(stream: ghidra.app.util.bin.format.pe.cli.streams.CliStreamMetadata) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
