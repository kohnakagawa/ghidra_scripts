from typing import Iterator
import ghidra.program.model.address
import java.lang
import java.util
import java.util.function


class EmptyAddressRangeIterator(object, ghidra.program.model.address.AddressRangeIterator):
    """
    Implementation for an AddressIterator that is empty.
    """





    def __init__(self): ...

    def __iter__(self) -> Iterator[ghidra.program.model.address.AddressRange]: ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def forEachRemaining(self, __a0: java.util.function.Consumer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool:
        """
        @see ghidra.program.model.address.AddressIterator#hasNext()
        """
        ...

    def hashCode(self) -> int: ...

    def iterator(self) -> Iterator[ghidra.program.model.address.AddressRange]: ...

    def next(self) -> ghidra.program.model.address.AddressRange:
        """
        @see ghidra.program.model.address.AddressIterator#next()
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self) -> None:
        """
        @see java.util.Iterator#remove()
        """
        ...

    def spliterator(self) -> java.util.Spliterator: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
