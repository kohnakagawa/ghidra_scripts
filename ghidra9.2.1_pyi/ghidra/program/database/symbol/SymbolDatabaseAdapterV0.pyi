import ghidra.program.database.symbol
import java.lang


class SymbolDatabaseAdapterV0(ghidra.program.database.symbol.SymbolDatabaseAdapter):
    """
    SymbolDatabaseAdapterV0 handles symbol tables which were created
     prior to the addition of Namespace support and Function symbols.  Function symbols
     are synthesized for those functions whose entry point currently has a
     label symbol.  The ID of these synthesized function symbols is the max ID plus
     the function ID.  The function Namespace ID is the same as the Function ID.
     The upgrade of this version may also add additional Function symbols for which there
     is no corresponding label symbol.
    """





    def __init__(self): ...



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
