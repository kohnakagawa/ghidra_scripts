import ghidra.app.util.importer
import ghidra.program.model.address
import java.lang


class RelocationState(object):
    """
    This class maintains the running state while
     applying relocations.

     relocAddress
     Holds an address within the section where the relocations
     are to be performed. The initial value is the base address
     of the section to be relocated.

     importIndex
     Holds a symbol index, which is used to access an
     imported symbol's address. This address can then
     be used for relocations. The initial value is 0.

     sectionC
     Holds the memory address of an instantiated section
     within the PEF container, this variable is used by relocation
     instructions that relocate section addresses. The initial
     value is the memory address of section 0 (if that section
     is present and instantiated), otherwise it is 0.

     sectionD
     Holds the memory address of an instantiated section
     within the PEF container, this variable is used by relocation
     instructions that relocate section addresses. The initial
     value is the memory address of section 1 (if that section
     is present and instantiated), otherwise it is 0.
    """





    def __init__(self, header: ghidra.app.util.bin.format.pef.ContainerHeader, relocationHeader: ghidra.app.util.bin.format.pef.LoaderRelocationHeader, program: ghidra.program.model.listing.Program, importState: ghidra.app.util.bin.format.pef.ImportStateCache):
        """
        Constructs a new relocation state
        @param header the PEF container header
        @param relocationHeader the specific relocation header for this state
        @param program the program being relocated
        @param importState the current import state
        """
        ...



    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def fixupMemory(self, address: ghidra.program.model.address.Address, fixupAddress: ghidra.program.model.address.Address, log: ghidra.app.util.importer.MessageLog) -> None:
        """
        Adds the fixup address to the contents stored at address,
         then creates a pointer at address.
        @param address the address to fixup
        @param fixupAddress the value to use in fixup
        @param log message log for recording errors
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getImportIndex(self) -> int:
        """
        Returns the current import index.
        @return the current import index
        """
        ...

    def getRelocationAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the current relocation address.
        @return the current relocation address
        """
        ...

    def getSectionC(self) -> ghidra.program.model.address.Address:
        """
        Returns the current sectionC address.
        @return the current sectionC address
        """
        ...

    def getSectionD(self) -> ghidra.program.model.address.Address:
        """
        Returns the current sectionD address.
        @return the current sectionD address
        """
        ...

    def getSectionToBeRelocated(self) -> ghidra.program.model.address.Address:
        """
        Returns the base address of the section to be relocated.
        @return the base address of the section to be relocated
        """
        ...

    def hashCode(self) -> int: ...

    def incrementImportIndex(self) -> None:
        """
        Increments the import index by one.
        """
        ...

    def incrementRelocationAddress(self, addend: int) -> None:
        """
        Increments the relocation address by the given addend
        @param addend the amount to increment the relocation address
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def relocateMemoryAt(self, address: ghidra.program.model.address.Address, addend: int, log: ghidra.app.util.importer.MessageLog) -> None:
        """
        Increments the integer in memory at the specified address
        @param address the address to increment
        @param addend the value to add
        @param log a message log
        """
        ...

    def setImportIndex(self, importIndex: int) -> None:
        """
        Sets the import index.
        @param importIndex the new import index value
        """
        ...

    def setRelocationAddress(self, relocationAddress: ghidra.program.model.address.Address) -> None:
        """
        Sets the relocation address.
        @param relocationAddress the new relocation address
        """
        ...

    def setSectionC(self, sectionC: ghidra.program.model.address.Address) -> None:
        """
        Set the sectionC variable to given address.
        @param sectionC the new sectionC address
        """
        ...

    def setSectionD(self, sectionD: ghidra.program.model.address.Address) -> None:
        """
        Set the sectionD variable to given address.
        @param sectionD the new sectionD address
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
    def importIndex(self) -> int: ...

    @importIndex.setter
    def importIndex(self, value: int) -> None: ...

    @property
    def relocationAddress(self) -> ghidra.program.model.address.Address: ...

    @relocationAddress.setter
    def relocationAddress(self, value: ghidra.program.model.address.Address) -> None: ...

    @property
    def sectionC(self) -> ghidra.program.model.address.Address: ...

    @sectionC.setter
    def sectionC(self, value: ghidra.program.model.address.Address) -> None: ...

    @property
    def sectionD(self) -> ghidra.program.model.address.Address: ...

    @sectionD.setter
    def sectionD(self, value: ghidra.program.model.address.Address) -> None: ...

    @property
    def sectionToBeRelocated(self) -> ghidra.program.model.address.Address: ...
