from typing import List
import ghidra.app.util.bin.format.elf
import ghidra.app.util.bin.format.elf.relocation
import java.lang


class ElfRelocationHandlerFactory(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getHandler(elf: ghidra.app.util.bin.format.elf.ElfHeader) -> ghidra.app.util.bin.format.elf.relocation.ElfRelocationHandler: ...

    @staticmethod
    def getHandlers() -> List[ghidra.app.util.bin.format.elf.relocation.ElfRelocationHandler]: ...

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
