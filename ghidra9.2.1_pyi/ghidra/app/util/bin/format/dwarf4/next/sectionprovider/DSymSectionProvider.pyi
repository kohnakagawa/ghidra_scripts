from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.dwarf4.next.sectionprovider
import ghidra.program.model.listing
import java.io
import java.lang


class DSymSectionProvider(object, ghidra.app.util.bin.format.dwarf4.next.sectionprovider.DWARFSectionProvider):
    """
    Fetches DWARF section data for a MachO program with co-located .dSYM folder. (ie. Mac OSX
     binaries)
    """





    def __init__(self, dsymFile: java.io.File): ...



    def close(self) -> None: ...

    @staticmethod
    def createSectionProviderFor(program: ghidra.program.model.listing.Program) -> ghidra.app.util.bin.format.dwarf4.next.sectionprovider.DSymSectionProvider: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getDSYMForProgram(program: ghidra.program.model.listing.Program) -> java.io.File: ...

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
