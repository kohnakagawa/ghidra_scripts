import ghidra.app.util.bin
import ghidra.app.util.bin.format.pef
import java.lang


class RelocationFactory(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getRelocation(reader: ghidra.app.util.bin.BinaryReader) -> ghidra.app.util.bin.format.pef.Relocation: ...

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
