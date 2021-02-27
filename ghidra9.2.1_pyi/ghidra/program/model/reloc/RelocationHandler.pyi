import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.mem
import ghidra.program.model.reloc
import ghidra.util.classfinder
import ghidra.util.task
import java.lang


class RelocationHandler(ghidra.util.classfinder.ExtensionPoint, object):
    """
    NOTE:  ALL RelocationHandler CLASSES MUST END IN "RelocationHandler".  If not,
     the ClassSearcher will not find them.
    """









    def canRelocate(self, program: ghidra.program.model.listing.Program) -> bool:
        """
        Returns true if this relocation handler can relocate the
         given program. For example, an ELF program requires
         an ELF-specific relocation handler.
        @param program the program to relocation
        @return true if this relocation handler can relocate the given program
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def performRelocation(self, program: ghidra.program.model.listing.Program, relocation: ghidra.program.model.reloc.Relocation, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    @overload
    def relocate(self, program: ghidra.program.model.listing.Program, newImageBase: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        @param program
        @param newImageBase
        @param monitor
        @throws MemoryAccessException
        """
        ...

    @overload
    def relocate(self, program: ghidra.program.model.listing.Program, block: ghidra.program.model.mem.MemoryBlock, newStartAddress: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Relocates the memory block to the new start address.
         All relocations in the memory block will be fixed-up.
        @param program
        @param block
        @param newStartAddress
        @param monitor
        @throws MemoryAccessException
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
