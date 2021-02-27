from typing import List
import ghidra.app.emulator.memory
import ghidra.program.model.address
import java.lang


class CompositeLoadImage(object, ghidra.app.emulator.memory.MemoryLoadImage):




    def __init__(self): ...



    def addProvider(self, provider: ghidra.app.emulator.memory.MemoryLoadImage, view: ghidra.program.model.address.AddressSetView) -> None: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def loadFill(self, buf: List[int], size: int, addr: ghidra.program.model.address.Address, bufOffset: int, generateInitializedMask: bool) -> List[int]: ...

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