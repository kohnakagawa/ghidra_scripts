from typing import Iterator
import java.lang
import java.util
import java.util.function


class LongArrayListIterator(object, java.util.ListIterator):






    def __iter__(self) -> Iterator[long]: ...

    def add(self, __a0: object) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def forEachRemaining(self, __a0: java.util.function.Consumer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool: ...

    def hasPrevious(self) -> bool: ...

    def hashCode(self) -> int: ...

    def next(self) -> long: ...

    def nextIndex(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def previous(self) -> long: ...

    def previousIndex(self) -> int: ...

    def remove(self) -> None: ...

    def set(self, __a0: object) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...