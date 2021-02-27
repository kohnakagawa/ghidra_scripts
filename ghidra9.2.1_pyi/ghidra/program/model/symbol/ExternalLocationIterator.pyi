from typing import Iterator
import ghidra.program.model.symbol
import java.lang
import java.util
import java.util.function


class ExternalLocationIterator(java.util.Iterator, object):
    """
    Iterator interface for external locations.
    """







    def __iter__(self) -> Iterator[ghidra.program.model.symbol.ExternalLocation]: ...

    def equals(self, __a0: object) -> bool: ...

    def forEachRemaining(self, __a0: java.util.function.Consumer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool:
        """
        Returns true if another external location is available with the next() method.
        """
        ...

    def hashCode(self) -> int: ...

    def next(self) -> ghidra.program.model.symbol.ExternalLocation:
        """
        Returns the next external location
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
