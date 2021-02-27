from typing import List
import ghidra.app.util.bin.format.pe.debug
import java.lang


class OMFGlobal(object):
    """
    A class to represent the Object Module Format (OMF) Global data structure.
    """





    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getAddrHash(self) -> int: ...

    def getCbAddrHash(self) -> int: ...

    def getCbSymHash(self) -> int: ...

    def getCbSymbol(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getSymHash(self) -> int: ...

    def getSymbols(self) -> List[ghidra.app.util.bin.format.pe.debug.DebugSymbol]:
        """
        Returns the debug symbols in this OMF Global.
        @return the debug symbols in this OMF Global
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

    @property
    def addrHash(self) -> int: ...

    @property
    def cbAddrHash(self) -> int: ...

    @property
    def cbSymHash(self) -> int: ...

    @property
    def cbSymbol(self) -> int: ...

    @property
    def symHash(self) -> int: ...

    @property
    def symbols(self) -> List[object]: ...
