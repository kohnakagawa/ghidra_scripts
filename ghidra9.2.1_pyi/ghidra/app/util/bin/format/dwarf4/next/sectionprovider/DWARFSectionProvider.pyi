from typing import List
import ghidra.app.util.bin
import java.io
import java.lang


class DWARFSectionProvider(java.io.Closeable, object):
    """
    A DWARFSectionProvider is responsible for allowing access to DWARF section data of
     a Ghidra program.

     Implementors of this interface should probably be registered in DWARFSectionProviderFactory
     so they can be auto-detected when queried and also need to implement the static method:

     public static DWARFSectionProvider createSectionProviderFor(Program program)

    """









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
