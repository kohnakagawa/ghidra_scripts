import ghidra.program.model.address
import ghidra.program.model.listing
import java.lang


class JavaClassUtil(object):
    LOOKUP_ADDRESS: long = 0xe0000000L
    METHOD_INDEX_SIZE: long = 0x40000L



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isClassFile(__a0: ghidra.program.model.listing.Program) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def toLookupAddress(__a0: ghidra.program.model.listing.Program, __a1: int) -> ghidra.program.model.address.Address: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
