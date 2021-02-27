import ghidra.app.util.bin.format.elf
import ghidra.app.util.bin.format.elf.extend
import java.lang


class ElfExtensionFactory(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getLoadAdapter(elf: ghidra.app.util.bin.format.elf.ElfHeader) -> ghidra.app.util.bin.format.elf.extend.ElfLoadAdapter: ...

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
