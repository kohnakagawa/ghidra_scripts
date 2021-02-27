import ghidra.app.util.bin.format.elf
import ghidra.app.util.bin.format.elf.relocation
import ghidra.app.util.importer
import ghidra.program.model.address
import ghidra.program.model.listing
import java.lang
import java.util


class SPARC_ElfRelocationHandler(ghidra.app.util.bin.format.elf.relocation.ElfRelocationHandler):




    def __init__(self): ...



    def canRelocate(self, __a0: ghidra.app.util.bin.format.elf.ElfHeader) -> bool: ...

    def createRelocationContext(self, __a0: ghidra.app.util.bin.format.elf.ElfLoadHelper, __a1: ghidra.app.util.bin.format.elf.ElfRelocationTable, __a2: java.util.Map) -> ghidra.app.util.bin.format.elf.relocation.ElfRelocationContext: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getRelrRelocationType(self) -> int: ...

    def hashCode(self) -> int: ...

    @overload
    @staticmethod
    def markAsError(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address, __a2: long, __a3: unicode, __a4: unicode, __a5: ghidra.app.util.importer.MessageLog) -> None: ...

    @overload
    @staticmethod
    def markAsError(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address, __a2: unicode, __a3: unicode, __a4: unicode, __a5: ghidra.app.util.importer.MessageLog) -> None: ...

    @staticmethod
    def markAsUnhandled(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address, __a2: long, __a3: long, __a4: unicode, __a5: ghidra.app.util.importer.MessageLog) -> None: ...

    @staticmethod
    def markAsUninitializedMemory(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address, __a2: long, __a3: long, __a4: unicode, __a5: ghidra.app.util.importer.MessageLog) -> None: ...

    @staticmethod
    def markAsUnsupportedRelr(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address) -> None: ...

    @overload
    @staticmethod
    def markAsWarning(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address, __a2: unicode, __a3: unicode, __a4: ghidra.app.util.importer.MessageLog) -> None: ...

    @overload
    @staticmethod
    def markAsWarning(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address, __a2: unicode, __a3: unicode, __a4: long, __a5: unicode, __a6: ghidra.app.util.importer.MessageLog) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def relocate(self, __a0: ghidra.app.util.bin.format.elf.relocation.ElfRelocationContext, __a1: ghidra.app.util.bin.format.elf.ElfRelocation, __a2: ghidra.program.model.address.Address) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
