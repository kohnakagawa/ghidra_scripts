from typing import Iterator
from typing import List
import ghidra.program.model.listing
import java.lang
import java.util
import java.util.function


class DataKeyIterator(object, ghidra.program.model.listing.DataIterator):
    """
    Converts a DBLongIterator into a DataIterator
    """

    EMPTY: ghidra.program.model.listing.DataIterator = ghidra.program.model.listing.DataIterator$IteratorWrapper@5433d286



    def __init__(self, codeMgr: ghidra.program.database.code.CodeManager, addrMap: ghidra.program.database.map.AddressMap, it: db.DBLongIterator):
        """
        Constructs a new DataKeyIterator
        @param codeMgr the code manager
        @param addrMap the address map to convert keys to addresses.
        @param it DBLongIterator
        """
        ...

    def __iter__(self) -> Iterator[ghidra.program.model.listing.Data]: ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def forEachRemaining(self, __a0: java.util.function.Consumer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool:
        """
        @see ghidra.program.model.listing.CodeUnitIterator#hasNext()
        """
        ...

    def hashCode(self) -> int: ...

    def iterator(self) -> java.util.Iterator: ...

    def next(self) -> ghidra.program.model.listing.Data:
        """
        @see ghidra.program.model.listing.CodeUnitIterator#next()
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
