import ghidra.app.util.bin
import ghidra.program.model.address
import ghidra.program.model.mem
import java.lang


class BinaryPropertyListUtil(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @overload
    @staticmethod
    def generateName(__a0: long) -> unicode: ...

    @overload
    @staticmethod
    def generateName(__a0: int) -> unicode: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @overload
    @staticmethod
    def isBinaryPropertyList(__a0: ghidra.app.util.bin.ByteProvider) -> bool: ...

    @overload
    @staticmethod
    def isBinaryPropertyList(__a0: ghidra.program.model.mem.Memory, __a1: ghidra.program.model.address.Address) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
