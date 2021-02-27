from typing import Iterator
import ghidra.util.datastruct
import java.lang
import java.util
import java.util.function
import java.util.stream


class CopyOnWriteWeakSet(ghidra.util.datastruct.WeakSet):
    """
    A set that avoids ConcurrentModificationExceptions by copying the internal storage
     for every mutation operation.  Thus, this data structure is only efficient when the
     number of event notification operations significantly out numbers mutations to this structure
     (e.g., adding and removing items.

     An example use cases where using this class is a good fit would be a listener list where
     listeners are added during initialization, but not after that.   Further, this hypothetical
     list fires a large number of events.

     A bad use of this class would be as a container to store widgets where the container the
     contents are changed often, but iterated over very little.

     Finally, if this structure is only ever used from a single thread, like the Swing thread, then
     you do not need the overhead of this class, as the Swing thread synchronous access guarantees
     that the structure cannot be mutated while it is being iterated.  See
     WeakDataStructureFactory#createSingleThreadAccessWeakSet().
    """





    def __init__(self): ...

    def __iter__(self): ...

    def add(self, t: object) -> None: ...

    def clear(self) -> None: ...

    def contains(self, t: object) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool: ...

    def iterator(self) -> Iterator[object]: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, t: object) -> None: ...

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
