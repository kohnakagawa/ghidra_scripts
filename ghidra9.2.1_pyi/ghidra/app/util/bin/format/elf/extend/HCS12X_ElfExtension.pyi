import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.elf
import ghidra.app.util.bin.format.elf.extend
import ghidra.program.model.address
import ghidra.util.task
import java.io
import java.lang
import java.util


class HCS12X_ElfExtension(ghidra.app.util.bin.format.elf.extend.ElfExtension):
    PT_HCS12_ARCHEXT: ghidra.app.util.bin.format.elf.ElfProgramHeaderType = PT_HCS12X_ARCHEXT(0x70000000)
    SHT_HCS12_ATTRIBUTES: ghidra.app.util.bin.format.elf.ElfSectionHeaderType = SHT_AHCS12_ATTRIBUTES(0x70000003)



    def __init__(self): ...



    def addDynamicTypes(self, __a0: java.util.Map) -> None: ...

    def addProgramHeaderTypes(self, __a0: java.util.Map) -> None: ...

    def addSectionHeaderTypes(self, __a0: java.util.HashMap) -> None: ...

    @overload
    def canHandle(self, __a0: ghidra.app.util.bin.format.elf.ElfHeader) -> bool: ...

    @overload
    def canHandle(self, __a0: ghidra.app.util.bin.format.elf.ElfLoadHelper) -> bool: ...

    def creatingFunction(self, __a0: ghidra.app.util.bin.format.elf.ElfLoadHelper, __a1: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address: ...

    def equals(self, __a0: object) -> bool: ...

    def evaluateElfSymbol(self, __a0: ghidra.app.util.bin.format.elf.ElfLoadHelper, __a1: ghidra.app.util.bin.format.elf.ElfSymbol, __a2: ghidra.program.model.address.Address, __a3: bool) -> ghidra.program.model.address.Address: ...

    def getAdjustedLoadSize(self, __a0: ghidra.app.util.bin.format.elf.ElfProgramHeader) -> long: ...

    def getAdjustedMemoryOffset(self, __a0: long, __a1: ghidra.program.model.address.AddressSpace) -> long: ...

    def getAdjustedMemorySize(self, __a0: ghidra.app.util.bin.format.elf.ElfProgramHeader) -> long: ...

    def getAdjustedSize(self, __a0: ghidra.app.util.bin.format.elf.ElfSectionHeader) -> long: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataTypeSuffix(self) -> unicode: ...

    def getDefaultAlignment(self, __a0: ghidra.app.util.bin.format.elf.ElfLoadHelper) -> int: ...

    def getExternalBlockReserveSize(self) -> int: ...

    def getFilteredLoadInputStream(self, __a0: ghidra.app.util.bin.format.elf.ElfLoadHelper, __a1: ghidra.app.util.bin.format.MemoryLoadable, __a2: ghidra.program.model.address.Address, __a3: long, __a4: java.io.InputStream) -> java.io.InputStream: ...

    def getLinkageBlockAlignment(self) -> int: ...

    def getPreferredExternalBlockSize(self) -> int: ...

    def getPreferredSectionAddress(self, __a0: ghidra.app.util.bin.format.elf.ElfLoadHelper, __a1: ghidra.app.util.bin.format.elf.ElfSectionHeader) -> ghidra.program.model.address.Address: ...

    def getPreferredSectionAddressSpace(self, __a0: ghidra.app.util.bin.format.elf.ElfLoadHelper, __a1: ghidra.app.util.bin.format.elf.ElfSectionHeader) -> ghidra.program.model.address.AddressSpace: ...

    def getPreferredSegmentAddress(self, __a0: ghidra.app.util.bin.format.elf.ElfLoadHelper, __a1: ghidra.app.util.bin.format.elf.ElfProgramHeader) -> ghidra.program.model.address.Address: ...

    def getPreferredSegmentAddressSpace(self, __a0: ghidra.app.util.bin.format.elf.ElfLoadHelper, __a1: ghidra.app.util.bin.format.elf.ElfProgramHeader) -> ghidra.program.model.address.AddressSpace: ...

    def getRelocationClass(self, __a0: ghidra.app.util.bin.format.elf.ElfHeader) -> java.lang.Class: ...

    def hasFilteredLoadInputStream(self, __a0: ghidra.app.util.bin.format.elf.ElfLoadHelper, __a1: ghidra.app.util.bin.format.MemoryLoadable, __a2: ghidra.program.model.address.Address) -> bool: ...

    def hashCode(self) -> int: ...

    def isSectionAllocated(self, __a0: ghidra.app.util.bin.format.elf.ElfSectionHeader) -> bool: ...

    def isSectionExecutable(self, __a0: ghidra.app.util.bin.format.elf.ElfSectionHeader) -> bool: ...

    def isSectionWritable(self, __a0: ghidra.app.util.bin.format.elf.ElfSectionHeader) -> bool: ...

    def isSegmentExecutable(self, __a0: ghidra.app.util.bin.format.elf.ElfProgramHeader) -> bool: ...

    def isSegmentReadable(self, __a0: ghidra.app.util.bin.format.elf.ElfProgramHeader) -> bool: ...

    def isSegmentWritable(self, __a0: ghidra.app.util.bin.format.elf.ElfProgramHeader) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def processElf(self, __a0: ghidra.app.util.bin.format.elf.ElfLoadHelper, __a1: ghidra.util.task.TaskMonitor) -> None: ...

    def processGotPlt(self, __a0: ghidra.app.util.bin.format.elf.ElfLoadHelper, __a1: ghidra.util.task.TaskMonitor) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def dataTypeSuffix(self) -> unicode: ...