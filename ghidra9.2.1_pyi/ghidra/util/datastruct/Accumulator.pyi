from typing import Iterator
import java.lang
import java.util
import java.util.function
import java.util.stream


class Accumulator(java.lang.Iterable, object):
    """
    The interface provides a mechanism for clients to pass around an object that is effectively
     a 'results object', into which data can be placed as it is discovered.

     Historically, clients that load data will return results, once fully loaded, in a
     Collection.  This has the drawback that the discovered data cannot be used until
     all searching is complete.  This interface can now be passed into such a method (as opposed
     to be returned by it) so that the client can make use of data as it is discovered.   This
     allows for long searching processes to report data as they work.
    """







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

    def iterator(self) -> java.util.Iterator: ...

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
