import ghidra.app.util.bin
import ghidra.program.model.listing
import java.lang


class DyldCacheUtils(object):
    """
    Utilities methods for working with Mach-O DYLD shared cache binaries.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @overload
    @staticmethod
    def isDyldCache(signature: unicode) -> bool:
        """
        Determines if the given signature represents a DYLD cache signature with an architecture we
         support.
        @param signature The DYLD cache signature
        @return True if the given signature represents a DYLD cache signature with an architecture we
         support; otherwise, false
        """
        ...

    @overload
    @staticmethod
    def isDyldCache(provider: ghidra.app.util.bin.ByteProvider) -> bool:
        """
        Determines if the given {@link ByteProvider} is a DYLD cache.
        @param provider The {@link ByteProvider}
        @return True if the given {@link ByteProvider} is a DYLD cache; otherwise, false
        """
        ...

    @overload
    @staticmethod
    def isDyldCache(program: ghidra.program.model.listing.Program) -> bool:
        """
        Determines if the given {@link Program} is a DYLD cache.
        @param program The {@link Program}
        @return True if the given {@link Program} is a DYLD cache; otherwise, false
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
