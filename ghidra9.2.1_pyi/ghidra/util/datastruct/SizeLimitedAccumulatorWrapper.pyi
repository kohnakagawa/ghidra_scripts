from typing import Iterator
import ghidra.util.datastruct
import java.lang
import java.util
import java.util.function
import java.util.stream


class SizeLimitedAccumulatorWrapper(object, ghidra.util.datastruct.Accumulator):




    def __init__(self, accumulator: ghidra.util.datastruct.Accumulator, maxSize: int):
        """
        Constructor.
        @param accumulator the accumulator to pass items to
        @param maxSize the maximum number of items this accumulator will hold
        """
        ...

    def __iter__(self): ...

    def add(self, t: object) -> None: ...

    def addAll(self, collection: java.util.Collection) -> None: ...

    def contains(self, t: object) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def get(self) -> java.util.Collection: ...

    def getClass(self) -> java.lang.Class: ...

    def hasReachedSizeLimit(self) -> bool:
        """
        Returns true if this size of this accumulator is greater than or equal to the given
         maximum size
        @return true if the max size has been reachged
        """
        ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool: ...

    def iterator(self) -> Iterator[object]: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def size(self) -> int: ...

    def spliterator(self) -> java.util.Spliterator: ...

    def stream(self) -> java.util.stream.Stream: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def empty(self) -> bool: ...
