from typing import List
import ghidra.pcode.loadimage
import ghidra.program.model.address
import java.lang


class MemoryLoadImage(ghidra.pcode.loadimage.LoadImage, object):








    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def loadFill(self, __a0: List[int], __a1: int, __a2: ghidra.program.model.address.Address, __a3: int, __a4: bool) -> List[int]: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeBack(self, bytes: List[int], size: int, addr: ghidra.program.model.address.Address, offset: int) -> None: ...
