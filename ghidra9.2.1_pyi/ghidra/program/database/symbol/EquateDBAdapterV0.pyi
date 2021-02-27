import ghidra.program.database.symbol
import java.lang


class EquateDBAdapterV0(ghidra.program.database.symbol.EquateDBAdapter):
    """
    Implementation for Version 0 of the adapter that accesses the
     equate record that has the equate name and value.
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
