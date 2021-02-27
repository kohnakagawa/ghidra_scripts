import ghidra.app.util.bin.format
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.mem
import ghidra.util.task
import java.lang


class MemorySectionResolver(object):




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

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

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

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def memory(self) -> ghidra.program.model.mem.Memory: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...
