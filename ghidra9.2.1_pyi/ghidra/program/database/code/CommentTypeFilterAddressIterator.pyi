from typing import Iterator
import ghidra.program.model.address
import java.lang
import java.util
import java.util.function


class CommentTypeFilterAddressIterator(object, ghidra.program.model.address.AddressIterator):
    """
    Filters the given address iterator to only return addresses that have a comment of the given type
    """





    def __init__(self, program: ghidra.program.model.listing.Program, it: ghidra.program.model.address.AddressIterator, commentType: int):
        """
        Constructs a new CommentTypeFilterAddressIterator
        @param it an address iterator whose items are tested for the comment type.
        @param commentType the type of comment to search for.
        """
        ...

    def __iter__(self) -> Iterator[ghidra.program.model.address.Address]: ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def forEachRemaining(self, __a0: java.util.function.Consumer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool: ...

    def hashCode(self) -> int: ...

    def iterator(self) -> Iterator[ghidra.program.model.address.Address]: ...

    def next(self) -> ghidra.program.model.address.Address: ...

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
