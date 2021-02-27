import ghidra.pcodeCPort.space
import java.lang


class AddrSpaceToIdSymmetryMap(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getID(__a0: ghidra.pcodeCPort.space.AddrSpace) -> long: ...

    @staticmethod
    def getSpace(__a0: long) -> ghidra.pcodeCPort.space.AddrSpace: ...

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
