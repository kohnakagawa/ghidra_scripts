from typing import Iterator
import ghidra.util.datastruct
import java.lang
import java.util
import java.util.function
import java.util.stream


class CopyOnReadWeakSet(ghidra.util.datastruct.WeakSet):






    def __iter__(self): ...

    def add(self, t: object) -> None:
        """
        Add the given object to the set.
        """
        ...

    def clear(self) -> None:
        """
        Remove all elements from this data structure
        """
        ...

    def contains(self, t: object) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool: ...

    def iterator(self) -> Iterator[object]:
        """
        Returns an iterator over the elements in this data structure.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, t: object) -> None:
        """
        Remove the given object from the data structure
        """
        ...

    def size(self) -> int: ...

    def spliterator(self) -> java.util.Spliterator: ...

    def stream(self) -> java.util.stream.Stream:
        """
        Returns a stream of the values of this collection.
        @return a stream of the values of this collection.
        """
        ...

    def toString(self) -> unicode: ...

    def values(self) -> java.util.Collection: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def empty(self) -> bool: ...
