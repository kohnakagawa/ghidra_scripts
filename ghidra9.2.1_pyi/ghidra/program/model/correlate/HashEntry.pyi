import java.lang


class HashEntry(object):
    """
    Cross-reference container for different n-grams that share a particular hash
    """

    instList: java.util.LinkedList



    def __init__(self, h: ghidra.program.model.correlate.Hash): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hasDuplicateBlocks(self) -> bool:
        """
        @return true if any two InstructHash for this HashEntry share the same parent Block
        """
        ...

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
