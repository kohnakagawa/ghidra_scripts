from typing import Iterator
import db
import java.lang


class AddressKeyRecordIterator(object, db.RecordIterator):
    """
    Returns a RecordIterator over records that are address keyed.  Various constructors allow
     the iterator to be restricted to an address range or address set and optionally to be
     positioned at some starting address.
    """





    @overload
    def __init__(self, table: db.Table, addrMap: ghidra.program.database.map.AddressMap):
        """
        Construcs a new AddressKeyRecordIterator that iterates over all records in ascending order.
         Memory addresses encoded as Absolute are not included.
        @param table the table to iterate.
        @param addrMap the address map
        @throws IOException if a database io error occurs.
        """
        ...

    @overload
    def __init__(self, table: db.Table, addrMap: ghidra.program.database.map.AddressMap, startAddr: ghidra.program.model.address.Address, before: bool):
        """
        Construcs a new AddressKeyRecordIterator that iterates over records starting at given
         start address.  Memory addresses encoded as Absolute are not included.
        @param table the table to iterate.
        @param addrMap the address map
        @param startAddr the address at which to position the iterator.  The iterator will be positioned
         either before or after the start address depending on the before parameter.
        @param before if true, the iterator will be positioned before the start address, otherwise
         it will be positioned after the start address.
        @throws IOException if a database io error occurs.
        """
        ...

    @overload
    def __init__(self, table: db.Table, addrMap: ghidra.program.database.map.AddressMap, set: ghidra.program.model.address.AddressSetView, startAddr: ghidra.program.model.address.Address, before: bool):
        """
        Construcs a new AddressKeyRecordIterator that iterates over records that are contained in
         an address set with an optional start address within that set.
         Memory addresses encoded as Absolute are not included.
        @param table the table to iterate.
        @param addrMap the address map
        @param set the address set to iterate over.
        @param startAddr the address at which to position the iterator.  The iterator will be positioned
         either before or after the start address depending on the before parameter. If this parameter
         is null, then the iterator will start either before the min address or after the max address
         depending on the before parameter.
        @param before if true, the iterator will be positioned before the start address, otherwise
         it will be positioned after the start address. If the start address is null, then if the before
         parameter is true, the iterator is positioned before the min. Otherwise the iterator is
         postioned after the max address.
        @throws IOException if a database io error occurs.
        """
        ...

    @overload
    def __init__(self, table: db.Table, addrMap: ghidra.program.database.map.AddressMap, minAddr: ghidra.program.model.address.Address, maxAddr: ghidra.program.model.address.Address, startAddr: ghidra.program.model.address.Address, before: bool):
        """
        Constructs a new AddressKeyRecordIterator that iterates over records that are within an
         address range with an optional start address within that range.
         Memory addresses encoded as Absolute are not included.
        @param table the table to iterate.
        @param addrMap the address map
        @param minAddr the minimum address in the range.
        @param maxAddr tha maximum address in the range.
        @param startAddr the address at which to position the iterator.  The iterator will be positioned
         either before or after the start address depending on the before parameter. If this parameter
         is null, then the iterator will start either before the min address or after the max address
         depending on the before parameter.
        @param before if true, the iterator will be positioned before the start address, otherwise
         it will be positioned after the start address. If the start address is null, then if the before
         parameter is true, the iterator is positioned before the min. Otherwise the iterator is
         positioned after the max address.
        @throws IOException if a database io error occurs.
        """
        ...



    def delete(self) -> bool:
        """
        @see db.RecordIterator#delete()
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool:
        """
        @see db.RecordIterator#hasNext()
        """
        ...

    def hasPrevious(self) -> bool:
        """
        @see db.RecordIterator#hasPrevious()
        """
        ...

    def hashCode(self) -> int: ...

    def iterator(self) -> Iterator[db.Record]: ...

    def next(self) -> db.Record:
        """
        @see db.RecordIterator#next()
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def previous(self) -> db.Record:
        """
        @see db.RecordIterator#previous()
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
