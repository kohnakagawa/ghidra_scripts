from typing import Iterator
import ghidra.program.model.address
import java.lang
import java.util
import java.util.function


class IndexedAddressIterator(object, ghidra.program.model.address.AddressIterator):
    """
    Iterates over a FieldIterator; the field is the address but not
     the key; the column for the field must be indexed.
    """





    def __init__(self, iter: db.DBFieldIterator, addrMap: ghidra.program.database.map.AddressMap, colIndex: int, errHandler: db.util.ErrorHandler):
        """
        Constructor
        @param iter field iterator that is the address
        @param addrMap address map to convert the longs to addresses
        @param colIndex indexed column in the record
        """
        ...

    def __iter__(self) -> Iterator[ghidra.program.model.address.Address]: ...

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

    def iterator(self) -> Iterator[ghidra.program.model.address.Address]: ...

    def next(self) -> ghidra.program.model.address.Address:
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
