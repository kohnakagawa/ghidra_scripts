from typing import Iterator
import ghidra.util.datastruct
import java.lang
import java.util
import java.util.function
import java.util.stream


class CallbackAccumulator(object, ghidra.util.datastruct.Accumulator):
    """
    An implementation of Accumulator that allows clients to easily process items as
     they arrive.

     This class is different than normal accumulators in that the values are not
     stored internally.  As such, calls to #get(), #iterator() and
     #size() will reflect having no data.
    """





    def __init__(self, consumer: java.util.function.Consumer):
        """
        Constructor
        @param consumer the consumer that will get called each time an item is added
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
