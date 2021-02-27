import ghidra.program.model.correlate
import java.lang


class Hash(object, java.lang.Comparable):
    """
    This encodes the main hash value for an n-gram, and the number of Instructions hashed
    """

    ALTERNATE_SEED: int = 11111
    SEED: int = 22222



    def __init__(self, val: int, sz: int): ...



    @overload
    def compareTo(self, o: ghidra.program.model.correlate.Hash) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool: ...

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
