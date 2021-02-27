import ghidra.app.util.bin.format.dwarf4.next.sectionprovider
import ghidra.program.model.listing
import java.lang


class DWARFSectionProviderFactory(object):
    """
    Auto-detects which DWARFSectionProvider matches a Ghidra program.
    """





    def __init__(self): ...



    @staticmethod
    def createSectionProviderFor(program: ghidra.program.model.listing.Program) -> ghidra.app.util.bin.format.dwarf4.next.sectionprovider.DWARFSectionProvider:
        """
        Iterates through the statically registered {@link #sectionProviderFactoryFuncs factory funcs},
         trying each factory method until one returns a {@link DWARFSectionProvider}
         that can successfully retrieve the {@link DWARFSectionNames#MINIMAL_DWARF_SECTIONS minimal}
         sections we need to do a DWARF import.
         <p>
         The resulting {@link DWARFSectionProvider} is {@link Closeable} and it is the caller's
         responsibility to ensure that the object is closed when done.
        @param program
        @return {@link DWARFSectionProvider} that should be closed by the caller or NULL if no
         section provider types match the specified program.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

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
