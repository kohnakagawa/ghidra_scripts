from typing import List
import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.macho
import ghidra.app.util.bin.format.macho.commands
import ghidra.app.util.importer
import ghidra.program.flatapi
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class SymbolTableCommand(ghidra.app.util.bin.format.macho.commands.LoadCommand):
    """
    Represents a symtab_command structure.
    """





    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    @staticmethod
    def createSymbolTableCommand(reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader, header: ghidra.app.util.bin.format.macho.MachHeader) -> ghidra.app.util.bin.format.macho.commands.SymbolTableCommand: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCommandName(self) -> unicode: ...

    def getCommandSize(self) -> int:
        """
        Total size of command in bytes
        @return total size of command in bytes
        """
        ...

    def getCommandType(self) -> int:
        """
        Type of load command
        @return type of load command
        """
        ...

    def getNumberOfSymbols(self) -> int:
        """
        An integer indicating the number of entries in the symbol table.
        @return the number of entries in the symbol table
        """
        ...

    def getStartIndex(self) -> long:
        """
        Returns the binary start index of this load command.
        @return the binary start index of this load command
        """
        ...

    def getStringTableOffset(self) -> int:
        """
        An integer containing the byte offset from the start of the image to the
         location of the string table.
        @return string table offset
        """
        ...

    def getStringTableSize(self) -> int:
        """
        An integer indicating the size (in bytes) of the string table.
        @return string table size in bytes
        """
        ...

    def getSymbolAt(self, index: int) -> ghidra.app.util.bin.format.macho.commands.NList: ...

    def getSymbolOffset(self) -> int:
        """
        An integer containing the byte offset from the start
         of the file to the location of the symbol table entries.
         The symbol table is an array of nlist data structures.
        @return symbol table offset
        """
        ...

    def getSymbols(self) -> List[ghidra.app.util.bin.format.macho.commands.NList]: ...

    def hashCode(self) -> int: ...

    def markup(self, header: ghidra.app.util.bin.format.macho.MachHeader, api: ghidra.program.flatapi.FlatProgramAPI, baseAddress: ghidra.program.model.address.Address, isBinary: bool, parentModule: ghidra.program.model.listing.ProgramModule, monitor: ghidra.util.task.TaskMonitor, log: ghidra.app.util.importer.MessageLog) -> None: ...

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
    def commandName(self) -> unicode: ...

    @property
    def numberOfSymbols(self) -> int: ...

    @property
    def stringTableOffset(self) -> int: ...

    @property
    def stringTableSize(self) -> int: ...

    @property
    def symbolOffset(self) -> int: ...

    @property
    def symbols(self) -> List[object]: ...
