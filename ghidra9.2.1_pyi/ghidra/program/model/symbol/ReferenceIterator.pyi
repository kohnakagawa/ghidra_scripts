from typing import Iterator
import ghidra.program.model.symbol
import java.lang
import java.util
import java.util.function


class ReferenceIterator(java.util.Iterator, java.lang.Iterable, object):
    """
    Iterator that gives out MemReference objects.
    """







    def __iter__(self) -> Iterator[ghidra.program.model.symbol.Reference]: ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def forEachRemaining(self, __a0: java.util.function.Consumer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool:
        """
        Returns whether there is a next memory reference in the iterator.
        """
        ...

    def hashCode(self) -> int: ...

    def iterator(self) -> java.util.Iterator: ...

    def next(self) -> ghidra.program.model.symbol.Reference:
        """
        Get the next memory reference.
        @return null if there is no next reference
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self) -> None: ...

    def spliterator(self) -> java.util.Spliterator: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
