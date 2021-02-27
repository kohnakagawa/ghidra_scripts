import ghidra.app.util.bin.format.coff
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.symbol
import ghidra.util.classfinder
import java.lang


class CoffRelocationHandler(object, ghidra.util.classfinder.ExtensionPoint):
    """
    An abstract class used to perform COFF relocations.  Classes should extend this class to
     provide relocations in a machine/processor specific way.
    """





    def __init__(self): ...



    def canRelocate(self, fileHeader: ghidra.app.util.bin.format.coff.CoffFileHeader) -> bool:
        """
        Checks to see whether or not an instance of this COFF relocation hander can handle
         relocating the COFF defined by the provided file header.
        @param fileHeader The file header associated with the COFF to relocate.
        @return True if this relocation handler can do the relocation; otherwise, false.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def relocate(self, program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address, symbol: ghidra.program.model.symbol.Symbol, relocation: ghidra.app.util.bin.format.coff.CoffRelocation) -> None:
        """
        Performs a relocation.
        @param program The program to relocate.
        @param address The address at which to perform the relocation.
        @param symbol The symbol used during relocation.
        @param relocation The relocation information to use to perform the relocation.
        @throws MemoryAccessException If there is a problem accessing memory during the relocation.
        @throws NotFoundException If this handler didn't find a way to perform the relocation.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
