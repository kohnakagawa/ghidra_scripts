import ghidra.util.datastruct
import java.lang


class WeakDataStructureFactory(object):
    """
    Factory for creating containers to use in various threading environments
    """





    def __init__(self): ...



    @staticmethod
    def createCopyOnReadWeakSet() -> ghidra.util.datastruct.WeakSet:
        """
        Use when mutations outweigh iterations.
        @return a new WeakSet
        @see CopyOnReadWeakSet
        """
        ...

    @staticmethod
    def createCopyOnWriteWeakSet() -> ghidra.util.datastruct.WeakSet:
        """
        Use when iterations outweigh mutations.
        @return a new WeakSet
        @see CopyOnWriteWeakSet
        """
        ...

    @staticmethod
    def createSingleThreadAccessWeakSet() -> ghidra.util.datastruct.WeakSet:
        """
        Use when all access are on a single thread, such as the Swing thread.
        @return a new WeakSet
        """
        ...

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
