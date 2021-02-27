from typing import Iterator
import ghidra.program.model.address
import java.lang
import java.util
import java.util.function


class AddressIterator(java.util.Iterator, java.lang.Iterable, object):
    """
    AddressIterator is used to iterate over some set of addresses.

     Note: The next and previous methods return Addresss.

    """







    def __iter__(self) -> Iterator[ghidra.program.model.address.Address]: ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def forEachRemaining(self, __a0: java.util.function.Consumer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool:
        """
        Checks if there is a next address in the iteration.
        @return true if there is a next address.
        """
        ...

    def hashCode(self) -> int: ...

    def iterator(self) -> java.util.Iterator: ...

    def next(self) -> ghidra.program.model.address.Address:
        """
        Get the next address.
        @return the next address in the iteration.
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
