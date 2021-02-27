import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class ElfDefaultGotPltMarkup(object):
    """
    ElfDefaultGotPltMarkup provides the legacy/default implementation of ELF GOT/PLT processing
     which handles a limited set of cases.  It is intended that over time this default implementation be
     eliminated although it may form the basis of an abstract implementation for specific processor
     extensions.
    """





    def __init__(self, elfLoadHelper: ghidra.app.util.bin.format.elf.ElfLoadHelper): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isValidPointer(pointerData: ghidra.program.model.listing.Data) -> bool:
        """
        Determine if pointerData refers to a valid memory address or symbol
        @param pointerData pointer data
        @return true if pointer data refers to valid memory address or symbol
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def process(self, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def processLinkageTable(self, pltName: unicode, minAddress: ghidra.program.model.address.Address, maxAddress: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Perform disassembly and markup of specified external linkage table which
         consists of thunks to external functions.  If symbols are defined within the
         linkage table, these will be transitioned to external functions.
        @param pltName name of PLT section for log messages
        @param minAddress minimum address of linkage table
        @param maxAddress maximum address of linkage table
        @param monitor task monitor
        @throws CancelledException task cancelled
        """
        ...

    @staticmethod
    def setConstant(data: ghidra.program.model.listing.Data) -> None:
        """
        Set specified data as constant if contained within a writable block.  It can be helpful
         to the decompiler results if constant pointers are marked as such (e.g., GOT entries)
        @param data program data
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
