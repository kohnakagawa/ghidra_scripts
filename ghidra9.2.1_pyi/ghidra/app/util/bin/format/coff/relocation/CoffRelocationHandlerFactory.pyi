import ghidra.app.util.bin.format.coff
import ghidra.app.util.bin.format.coff.relocation
import java.lang


class CoffRelocationHandlerFactory(object):
    """
    A class that gets the appropriate COFF relocation handler for a specific COFF.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getHandler(fileHeader: ghidra.app.util.bin.format.coff.CoffFileHeader) -> ghidra.app.util.bin.format.coff.relocation.CoffRelocationHandler:
        """
        Gets the appropriate COFF relocation handler that is capable of relocating the COFF that is
         defined by the given COFF file header.
        @param fileHeader The file header associated with the COFF to relocate.
        @return The appropriate COFF relocation handler that is capable of relocating the COFF that
             is defined by the given COFF file header.  Could return null if there if no such handler
             was found.
        """
        ...

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
