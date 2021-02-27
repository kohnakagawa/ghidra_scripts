import ghidra.app.util.bin
import ghidra.app.util.bin.format.macos.asd
import java.lang


class EntryFactory(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getEntry(reader: ghidra.app.util.bin.BinaryReader, descriptor: ghidra.app.util.bin.format.macos.asd.EntryDescriptor) -> object: ...

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
