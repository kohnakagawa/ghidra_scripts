from typing import Iterator
from typing import List
import ghidra.program.model.listing
import java.lang
import java.util
import java.util.function


class DataFilteredCodeUnitIterator(object, ghidra.program.model.listing.DataIterator):
    """
    Converts a code unit iterator into a data iterator.
    """

    EMPTY: ghidra.program.model.listing.DataIterator = ghidra.program.model.listing.DataIterator$IteratorWrapper@5433d286



    def __init__(self, it: ghidra.program.model.listing.CodeUnitIterator):
        """
        Constructs a new DataFilteredCodeUnitIterator.
        @param it the codeunit iterator to filter on.
        """
        ...

    def __iter__(self) -> Iterator[ghidra.program.model.listing.Data]: ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def forEachRemaining(self, __a0: java.util.function.Consumer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool:
        """
        @see ghidra.program.model.listing.DataIterator#hasNext()
        """
        ...

    def hashCode(self) -> int: ...

    def iterator(self) -> java.util.Iterator: ...

    def next(self) -> ghidra.program.model.listing.Data:
        """
        @see ghidra.program.model.listing.DataIterator#next()
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def of(__a0: List[ghidra.program.model.listing.Data]) -> ghidra.program.model.listing.DataIterator: ...

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
