from typing import List
import ghidra.app.util.bin.format.macho
import ghidra.app.util.bin.format.macho.commands
import ghidra.app.util.importer
import ghidra.program.flatapi
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class DynamicSymbolTableCommand(ghidra.app.util.bin.format.macho.commands.LoadCommand):
    """
    Represents a dysymtab_command structure.
    """





    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



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

    def getExternalRelocationOffset(self) -> int:
        """
        Returns the byte index from the start of the file to the external relocation table.
        @return the byte index of the external relocation table
        """
        ...

    def getExternalRelocationSize(self) -> int:
        """
        Returns the number of entries in the external relocation table.
        @return the number of entries in the external relocation table
        """
        ...

    def getExternalRelocations(self) -> List[ghidra.app.util.bin.format.macho.RelocationInfo]: ...

    def getExternalSymbolCount(self) -> int:
        """
        Returns the total number of external symbols.
        @return the total number of external symbols
        """
        ...

    def getExternalSymbolIndex(self) -> int:
        """
        Returns the index of the first external symbol.
        @return the index of the first external symbol
        """
        ...

    def getIndirectSymbolTableOffset(self) -> int:
        """
        Returns the byte index from the start of the file to the indirect symbol table.
        @return the byte index of the indirect symbol table
        """
        ...

    def getIndirectSymbolTableSize(self) -> int:
        """
        Returns the number of entries in the indirect symbol table.
        @return the number of entries in the indirect symbol table
        """
        ...

    def getIndirectSymbols(self) -> List[int]: ...

    def getLocalRelocationOffset(self) -> int:
        """
        Returns the byte index from the start of the file to the local relocation table.
        @return the byte index of the local relocation table
        """
        ...

    def getLocalRelocationSize(self) -> int:
        """
        Returns the number of entries in the local relocation table.
        @return the number of entries in the local relocation table
        """
        ...

    def getLocalRelocations(self) -> List[ghidra.app.util.bin.format.macho.RelocationInfo]: ...

    def getLocalSymbolCount(self) -> int:
        """
        Returns the total number of local symbols.
        @return the total number of local symbols
        """
        ...

    def getLocalSymbolIndex(self) -> int:
        """
        Returns the index of the first local symbol.
        @return the index of the first local symbol
        """
        ...

    def getModuleList(self) -> List[ghidra.app.util.bin.format.macho.commands.DynamicLibraryModule]: ...

    def getModuleTableOffset(self) -> int:
        """
        Returns the byte index from the start of the file to the module table.
        @return the byte index of the module table
        """
        ...

    def getModuleTableSize(self) -> int:
        """
        Returns the number of entries in the module table.
        @return the number of entries in the module table
        """
        ...

    def getReferencedSymbolList(self) -> List[ghidra.app.util.bin.format.macho.commands.DynamicLibraryReference]: ...

    def getReferencedSymbolTableOffset(self) -> int:
        """
        Returns the byte index from the start of the file to the external reference table.
        @return the byte index of the external reference table
        """
        ...

    def getReferencedSymbolTableSize(self) -> int:
        """
        Returns the number of entries in the external reference table.
        @return the number of entries in the external reference table
        """
        ...

    def getStartIndex(self) -> long:
        """
        Returns the binary start index of this load command.
        @return the binary start index of this load command
        """
        ...

    def getTableOfContentsList(self) -> List[ghidra.app.util.bin.format.macho.commands.TableOfContents]: ...

    def getTableOfContentsOffset(self) -> int:
        """
        Returns the byte index from the start of the file to the table of contents (TOC).
        @return the byte index of the TOC
        """
        ...

    def getTableOfContentsSize(self) -> int:
        """
        Returns the number of entries in the table of contents.
        @return the number of entries in the table of contents
        """
        ...

    def getUndefinedSymbolCount(self) -> int:
        """
        Returns the total number of undefined symbols.
        @return the total number of undefined symbols
        """
        ...

    def getUndefinedSymbolIndex(self) -> int:
        """
        Returns the index of the first undefined symbol.
        @return the index of the first undefined symbol
        """
        ...

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
    def externalRelocationOffset(self) -> int: ...

    @property
    def externalRelocationSize(self) -> int: ...

    @property
    def externalRelocations(self) -> List[object]: ...

    @property
    def externalSymbolCount(self) -> int: ...

    @property
    def externalSymbolIndex(self) -> int: ...

    @property
    def indirectSymbolTableOffset(self) -> int: ...

    @property
    def indirectSymbolTableSize(self) -> int: ...

    @property
    def indirectSymbols(self) -> List[int]: ...

    @property
    def localRelocationOffset(self) -> int: ...

    @property
    def localRelocationSize(self) -> int: ...

    @property
    def localRelocations(self) -> List[object]: ...

    @property
    def localSymbolCount(self) -> int: ...

    @property
    def localSymbolIndex(self) -> int: ...

    @property
    def moduleList(self) -> List[object]: ...

    @property
    def moduleTableOffset(self) -> int: ...

    @property
    def moduleTableSize(self) -> int: ...

    @property
    def referencedSymbolList(self) -> List[object]: ...

    @property
    def referencedSymbolTableOffset(self) -> int: ...

    @property
    def referencedSymbolTableSize(self) -> int: ...

    @property
    def tableOfContentsList(self) -> List[object]: ...

    @property
    def tableOfContentsOffset(self) -> int: ...

    @property
    def tableOfContentsSize(self) -> int: ...

    @property
    def undefinedSymbolCount(self) -> int: ...

    @property
    def undefinedSymbolIndex(self) -> int: ...
