import ghidra.app.util.bin.format.elf
import ghidra.app.util.bin.format.elf.relocation
import ghidra.app.util.importer
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.classfinder
import java.lang
import java.util


class ElfRelocationHandler(object, ghidra.util.classfinder.ExtensionPoint):
    """
    ElfRelocationHandler provides the base class for processor specific
     ELF relocation handlers.
    """





    def __init__(self): ...



    def canRelocate(self, elf: ghidra.app.util.bin.format.elf.ElfHeader) -> bool: ...

    def createRelocationContext(self, loadHelper: ghidra.app.util.bin.format.elf.ElfLoadHelper, relocationTable: ghidra.app.util.bin.format.elf.ElfRelocationTable, symbolMap: java.util.Map) -> ghidra.app.util.bin.format.elf.relocation.ElfRelocationContext:
        """
        Relocation context for a specific Elf image and relocation table.  The relocation context
         is used to process relocations and manage any data required to process relocations.
        @param loadHelper Elf load helper
        @param relocationTable Elf relocation table
        @param symbolMap Elf symbol placement map
        @return relocation context or null if unsupported
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getRelrRelocationType(self) -> int:
        """
        Get the architecture-specific relative relocation type
         which should be applied to RELR relocations.  The
         default implementation returns 0 which indicates
         RELR is unsupported.
        @return RELR relocation type
        """
        ...

    def hashCode(self) -> int: ...

    @overload
    @staticmethod
    def markAsError(program: ghidra.program.model.listing.Program, relocationAddress: ghidra.program.model.address.Address, type: long, symbolName: unicode, msg: unicode, log: ghidra.app.util.importer.MessageLog) -> None:
        """
        Generate error log entry and bookmark at relocationAddress where
         import failed to be applied.
        @param program
        @param relocationAddress relocation address to be bookmarked
        @param type relocation type
        @param symbolName associated symbol name
        @param log import log
        """
        ...

    @overload
    @staticmethod
    def markAsError(program: ghidra.program.model.listing.Program, relocationAddress: ghidra.program.model.address.Address, type: unicode, symbolName: unicode, msg: unicode, log: ghidra.app.util.importer.MessageLog) -> None:
        """
        Generate error log entry and bookmark at relocationAddress where
         import failed to be applied.
        @param program
        @param relocationAddress relocation address to be bookmarked
        @param type relocation type
        @param symbolName associated symbol name
        @param msg additional error message
        @param log import log
        """
        ...

    @staticmethod
    def markAsUnhandled(program: ghidra.program.model.listing.Program, relocationAddress: ghidra.program.model.address.Address, type: long, symbolIndex: long, symbolName: unicode, log: ghidra.app.util.importer.MessageLog) -> None:
        """
        Generate error log entry and bookmark at relocationAddress indicating
         an unhandled relocation.
        @param program
        @param relocationAddress relocation address to be bookmarked
        @param type relocation type
        @param symbolIndex associated symbol index within symbol table
        @param symbolName associated symbol name
        @param log import log
        """
        ...

    @staticmethod
    def markAsUninitializedMemory(program: ghidra.program.model.listing.Program, relocationAddress: ghidra.program.model.address.Address, type: long, symbolIndex: long, symbolName: unicode, log: ghidra.app.util.importer.MessageLog) -> None:
        """
        Generate error log entry and bookmark at relocationAddress where
         import failed to transition block to initialized while processing relocation.
        @param program
        @param relocationAddress relocation address to be bookmarked
        @param type relocation type
        @param symbolIndex associated symbol index within symbol table
        @param symbolName associated symbol name
        @param log import log
        """
        ...

    @staticmethod
    def markAsUnsupportedRelr(program: ghidra.program.model.listing.Program, relocationAddress: ghidra.program.model.address.Address) -> None:
        """
        Generate error log entry and bookmark at relocationAddress indicating
         an unsupported RELR relocation.
        @param program
        @param relocationAddress relocation address to be bookmarked
        """
        ...

    @overload
    @staticmethod
    def markAsWarning(program: ghidra.program.model.listing.Program, relocationAddress: ghidra.program.model.address.Address, type: unicode, msg: unicode, log: ghidra.app.util.importer.MessageLog) -> None:
        """
        Generate warning log entry and bookmark at relocationAddress where
         import issue occurred.
        @param program
        @param relocationAddress relocation address to be bookmarked
        @param type relocation type
        @param msg message associated with warning
        @param log import log
        """
        ...

    @overload
    @staticmethod
    def markAsWarning(program: ghidra.program.model.listing.Program, relocationAddress: ghidra.program.model.address.Address, type: unicode, symbolName: unicode, symbolIndex: long, msg: unicode, log: ghidra.app.util.importer.MessageLog) -> None:
        """
        Generate warning log entry and bookmark at relocationAddress where
         import issue occurred.
        @param program
        @param relocationAddress relocation address to be bookmarked
        @param type relocation type
        @param symbolName symbol name
        @param symbolIndex symbol index
        @param msg message associated with warning
        @param log import log
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def relocate(self, elfRelocationContext: ghidra.app.util.bin.format.elf.relocation.ElfRelocationContext, relocation: ghidra.app.util.bin.format.elf.ElfRelocation, relocationAddress: ghidra.program.model.address.Address) -> None:
        """
        Perform relocation fixup
        @param elfRelocationContext relocation context
        @param relocation ELF relocation
        @param relocationAddress relocation target address (fixup location)
        @throws MemoryAccessException memory access failure
        @throws NotFoundException required relocation data not found
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def relrRelocationType(self) -> int: ...
