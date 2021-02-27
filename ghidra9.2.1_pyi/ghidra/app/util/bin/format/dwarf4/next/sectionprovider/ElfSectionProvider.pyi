from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.dwarf4.next.sectionprovider
import ghidra.program.model.listing
import java.lang


class ElfSectionProvider(object, ghidra.app.util.bin.format.dwarf4.next.sectionprovider.DWARFSectionProvider):
    """
    Fetches DWARF section data from ELF files, directly, without going through
     the Ghidra memory block api.  This section provider usually isn't needed as
     ELF sections are normally provided as Ghidra memory blocks.  In case of extra-
     large binaries, Ghidra may not be able to map the debug sections into memory
     and this section provider will allow the DWARF analyzer to still function.
    """





    def __init__(self, exeFile: java.io.File): ...



    def close(self) -> None: ...

    @staticmethod
    def createSectionProviderFor(program: ghidra.program.model.listing.Program) -> ghidra.app.util.bin.format.dwarf4.next.sectionprovider.ElfSectionProvider: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getSectionAsByteProvider(self, sectionName: unicode) -> ghidra.app.util.bin.ByteProvider: ...

    def hasSection(self, sectionNames: List[unicode]) -> bool: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
