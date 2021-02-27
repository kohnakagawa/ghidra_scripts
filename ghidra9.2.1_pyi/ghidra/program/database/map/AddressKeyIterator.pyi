import db
import java.lang


class AddressKeyIterator(object, db.DBLongIterator):
    """
    Iterator of primary keys that are addresses. The longs returned are the address longs.
    """





    @overload
    def __init__(self):
        """
        Constructs an empty iterator.
        """
        ...

    @overload
    def __init__(self, table: db.Table, addrMap: ghidra.program.database.map.AddressMap, before: bool):
        """
        Constructs  new AddressKeyIterator that iterates over all addresses.
         Memory addresses encoded as Absolute are not included.
        @param table the database table key by addresses
        @param addrMap the address map
        @param before positions the iterator before the min value,otherwise after the max value.
        @throws IOException if a database error occurs.
        """
        ...

    @overload
    def __init__(self, table: db.Table, addrMap: ghidra.program.database.map.AddressMap, startAddr: ghidra.program.model.address.Address, before: bool):
        """
        Constructs  new AddressKeyIterator that iterates overal all addresses and is initially
         positioned at startAddr.  Memory addresses encoded as Absolute are not included.
        @param table the database table key by addresses
        @param addrMap the address map
        @param startAddr the address at which to position the iterator.
        @param before positions the iterator before the start address,otherwise after
         the start address. If the start address is null, then before positions the iterator before
         the lowest address, !before positions the iterater after the largest address.
        @throws IOException if a database error occurs.
        """
        ...

    @overload
    def __init__(self, table: db.Table, addrMap: ghidra.program.database.map.AddressMap, set: ghidra.program.model.address.AddressSetView, startAddr: ghidra.program.model.address.Address, before: bool):
        """
        Constructs  new AddressKeyIterator to iterate over an address set.
         Memory addresses encoded as Absolute are not included.
        @param table the database table key by addresses
        @param addrMap the address map
        @param set the address set to iterator over
        @param startAddr the address at which to position the iterator, can be null. The exact
         position of the iterator depends on the before parameter.
        @param before positions the iterator before the start address,otherwise after
         the start address. If the start address is null, then before positions the iterator before
         the lowest address, !before positions the iterater after the largest address.
        @throws IOException if a database error occurs.
        """
        ...

    @overload
    def __init__(self, table: db.Table, addrMap: ghidra.program.database.map.AddressMap, minAddr: ghidra.program.model.address.Address, maxAddr: ghidra.program.model.address.Address, startAddr: ghidra.program.model.address.Address, before: bool):
        """
        Constructs  new AddressKeyIterator that iterates over an address range.
         Memory addresses encoded as Absolute are not included.
        @param table the database table key by addresses
        @param addrMap the address map
        @param minAddr the first address in the range.
        @param maxAddr the last address in the range.
        @param startAddr the address at which to position the iterator, can be null. The exact
         position of the iterator depends on the before parameter.
        @param before positions the iterator before the start address,otherwise after
         the start address. If the start address is null, then before positions the iterator before
         the lowest address, !before positions the iterater after the largest address.
        @throws IOException if a database error occurs.
        """
        ...



    def delete(self) -> bool:
        """
        @see db.DBLongIterator#delete()
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool:
        """
        @see db.DBLongIterator#hasNext()
        """
        ...

    def hasPrevious(self) -> bool:
        """
        @see db.DBLongIterator#hasPrevious()
        """
        ...

    def hashCode(self) -> int: ...

    def next(self) -> long:
        """
        @see db.DBLongIterator#next()
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def previous(self) -> long:
        """
        @see db.DBLongIterator#previous()
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
