from typing import List
import ghidra.program.model.address
import ghidra.program.model.mem
import java.awt
import java.lang


class AddressPixelMap(object):








    def clear(self) -> None: ...

    def createMapping(self, width: int) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddress(self, pixel: int) -> ghidra.program.model.address.Address: ...

    def getBlockPosition(self, memoryBlock: ghidra.program.model.mem.MemoryBlock) -> java.awt.Rectangle: ...

    def getBlocks(self) -> List[ghidra.program.model.mem.MemoryBlock]: ...

    def getClass(self) -> java.lang.Class: ...

    def getPixel(self, address: ghidra.program.model.address.Address) -> int: ...

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
    def blocks(self) -> List[ghidra.program.model.mem.MemoryBlock]: ...
