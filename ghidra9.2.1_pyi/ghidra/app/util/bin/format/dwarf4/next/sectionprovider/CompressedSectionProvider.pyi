from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.dwarf4.next.sectionprovider
import java.lang


class CompressedSectionProvider(object, ghidra.app.util.bin.format.dwarf4.next.sectionprovider.DWARFSectionProvider):
    """
    Fetches DWARF section data that has been compressed from an underlying DWARFSectionProvider.

     Note, this code has not been tested against real data but is included here as it was in
     the original DWARF code base.  This section provider is not currently
     registered in the DWARFSectionProviderFactory and as such will not be
     used.

     TODO: the decompressed data should be stored in something other than in-memory byte arrays,
     probably should use tmp files.
    """





    def __init__(self, sp: ghidra.app.util.bin.format.dwarf4.next.sectionprovider.DWARFSectionProvider): ...



    def close(self) -> None: ...

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
