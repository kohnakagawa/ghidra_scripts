import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.pe.debug
import java.lang


class DebugSymbolSelector(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def selectSymbol(reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader, ptr: int) -> ghidra.app.util.bin.format.pe.debug.DebugSymbol: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
