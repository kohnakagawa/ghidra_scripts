import ghidra.app.util.bin.format.pef
import ghidra.program.model.address
import ghidra.program.model.mem
import ghidra.program.model.symbol
import java.lang


class ImportStateCache(object):




    def __init__(self, program: ghidra.program.model.listing.Program, header: ghidra.app.util.bin.format.pef.ContainerHeader): ...



    def createLibrarySymbol(self, library: ghidra.app.util.bin.format.pef.ImportedLibrary, symbolName: unicode, address: ghidra.program.model.address.Address) -> bool: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getMemoryBlockForSection(self, section: ghidra.app.util.bin.format.pef.SectionHeader) -> ghidra.program.model.mem.MemoryBlock:
        """
        Returns the memory block for the given section.
         Generally sections do not specify a preferred address
         and are not named. This map provides a way to lookup
         the block that was created for the given section.
        @param section the PEF section header
        @return the memory block for the given section
        """
        ...

    def getNamespace(self, library: ghidra.app.util.bin.format.pef.ImportedLibrary) -> ghidra.program.model.symbol.Namespace:
        """
        Returns a namespace for the given imported library.
        @param library the imported library
        @return a namespace for the given imported library
        """
        ...

    def getSymbol(self, symbolName: unicode, library: ghidra.app.util.bin.format.pef.ImportedLibrary) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the symbol object with the given name in the specified library.
        @param symbolName the desired symbol's name
        @param library the desired library
        @return the symbol object with the given name in the specified library
        """
        ...

    def getTVectNamespace(self) -> ghidra.program.model.symbol.Namespace: ...

    def getTocAddress(self) -> ghidra.program.model.address.Address: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setMemoryBlockForSection(self, section: ghidra.app.util.bin.format.pef.SectionHeader, block: ghidra.program.model.mem.MemoryBlock) -> None: ...

    def setTocAddress(self, tocAddress: ghidra.program.model.address.Address) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def TVectNamespace(self) -> ghidra.program.model.symbol.Namespace: ...

    @property
    def tocAddress(self) -> ghidra.program.model.address.Address: ...

    @tocAddress.setter
    def tocAddress(self, value: ghidra.program.model.address.Address) -> None: ...
