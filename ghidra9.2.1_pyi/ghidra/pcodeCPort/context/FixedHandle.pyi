import java.lang


class FixedHandle(object):
    offset_offset: long
    offset_size: int
    offset_space: ghidra.pcodeCPort.space.AddrSpace
    size: int
    space: ghidra.pcodeCPort.space.AddrSpace
    temp_offset: long
    temp_space: ghidra.pcodeCPort.space.AddrSpace



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

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
