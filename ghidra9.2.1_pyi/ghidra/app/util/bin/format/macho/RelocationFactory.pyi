import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.macho
import java.lang


class RelocationFactory(object):
    EXTERNAL: int = 3003
    LOCAL: int = 3276
    SECTION: int = 2730



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getRelocationDescription(header: ghidra.app.util.bin.format.macho.MachHeader, relocation: ghidra.app.util.bin.format.macho.RelocationInfo) -> unicode: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def readRelocation(reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader, is32bit: bool) -> ghidra.app.util.bin.format.macho.RelocationInfo: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
