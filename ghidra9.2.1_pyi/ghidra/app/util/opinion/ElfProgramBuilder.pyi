import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.elf
import ghidra.app.util.importer
import ghidra.app.util.opinion
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.program.model.mem
import ghidra.program.model.symbol
import ghidra.util.task
import java.lang


class ElfProgramBuilder(ghidra.app.util.opinion.MemorySectionResolver, ghidra.app.util.bin.format.elf.ElfLoadHelper):




    def __init__(self, program: ghidra.program.model.listing.Program): ...



    def addInitializedMemorySection(self, key: ghidra.app.util.bin.format.MemoryLoadable, fileOffset: long, numberOfBytes: long, startAddress: ghidra.program.model.address.Address, sectionName: unicode, isReadable: bool, isWritable: bool, isExecutable: bool, comment: unicode, isFragmentationOK: bool, isLoadedSection: bool) -> None:
        """
        Add initialized memory "section" based upon a specified data source fileOffset.
         The last "section" defined will take precedence when resolving conflicts. Sections identified
         as loaded will take precedence over those that are non-loaded.
         placed into memory
        @param key the loadable section key which corresponds to this memory "section"
        @param fileOffset data source file offset.  It is assumed that all initialized
         "sections" draw from a single data source.
        @param numberOfBytes number of bytes within "section"
        @param startAddress desired physical start address of "section"
        @param sectionName name of "section"
        @param isReadable true if "section" has read privilege
        @param isWritable true if "section" has write privilege
        @param isExecutable true if "section" has execute privilege
        @param comment section comment (used as basis for block comment)
        @param isFragmentationOK if true this memory section may be fragmented due to
        @param isLoadedSection if true this memory section will take precedence over non-loaded sections
         conflict/overlap with other memory sections of higher precedence.
        @throws AddressOverflowException
        """
        ...

    def addUninitializedMemorySection(self, key: ghidra.app.util.bin.format.MemoryLoadable, numberOfBytes: long, startAddress: ghidra.program.model.address.Address, sectionName: unicode, isReadable: bool, isWritable: bool, isExecutable: bool, comment: unicode, isFragmentationOK: bool) -> None:
        """
        Add uninitialized memory "section".
         The last "section" defined will take precedence when resolving conflicts.
        @param key the loadable section key which corresponds to this memory "section"
        @param numberOfBytes number of bytes within "section"
        @param startAddress desired physical start address of "section"
        @param sectionName name of "section"
        @param isReadable true if "section" has read privilege
        @param isWritable true if "section" has write privilege
        @param isExecutable true if "section" has execute privilege
        @param comment section comment (used as basis for block comment)
        @param isFragmentationOK if true this memory section may be fragmented due to
         conflict/overlap with other memory sections of higher precedence.
        @throws AddressOverflowException
        """
        ...

    def allocateLinkageBlock(self, alignment: int, size: int, purpose: unicode) -> ghidra.program.model.address.AddressRange: ...

    def createData(self, address: ghidra.program.model.address.Address, dt: ghidra.program.model.data.DataType) -> ghidra.program.model.listing.Data: ...

    def createExternalFunctionLinkage(self, name: unicode, functionAddr: ghidra.program.model.address.Address, indirectPointerAddr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Function: ...

    def createOneByteFunction(self, name: unicode, address: ghidra.program.model.address.Address, isEntry: bool) -> ghidra.program.model.listing.Function: ...

    def createSymbol(self, addr: ghidra.program.model.address.Address, name: unicode, isPrimary: bool, pinAbsolute: bool, namespace: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.symbol.Symbol: ...

    def createUndefinedData(self, address: ghidra.program.model.address.Address, length: int) -> ghidra.program.model.listing.Data: ...

    def equals(self, __a0: object) -> bool: ...

    def findLoadAddress(self, section: ghidra.app.util.bin.format.MemoryLoadable, byteOffsetWithinSection: long) -> ghidra.program.model.address.Address: ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultAddress(self, addressableWordOffset: long) -> ghidra.program.model.address.Address: ...

    def getElfHeader(self) -> ghidra.app.util.bin.format.elf.ElfHeader: ...

    def getElfSymbolAddress(self, elfSymbol: ghidra.app.util.bin.format.elf.ElfSymbol) -> ghidra.program.model.address.Address: ...

    def getGOTValue(self) -> long: ...

    def getImageBaseWordAdjustmentOffset(self) -> long: ...

    def getLog(self) -> ghidra.app.util.importer.MessageLog: ...

    def getMemory(self) -> ghidra.program.model.mem.Memory:
        """
        Get program memory object
        @return program memory
        """
        ...

    def getProgram(self) -> ghidra.program.model.listing.Program:
        """
        Get program object
        @return program
        """
        ...

    def hashCode(self) -> int: ...

    @overload
    def log(self, msg: unicode) -> None: ...

    @overload
    def log(self, t: java.lang.Throwable) -> None: ...

    def markAsCode(self, address: ghidra.program.model.address.Address) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def resolve(self, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Perform final resolve of all defined memory "sections" to establish final memory mappings.
         This method will resolve all conflicts and create memory blocks within the associated program.
        @param monitor
        @throws CancelledException
        """
        ...

    def setElfSymbolAddress(self, elfSymbol: ghidra.app.util.bin.format.elf.ElfSymbol, address: ghidra.program.model.address.Address) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
