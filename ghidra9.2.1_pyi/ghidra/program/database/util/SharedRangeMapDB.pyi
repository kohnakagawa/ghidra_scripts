from typing import Iterator
import db
import ghidra.util.datastruct
import java.lang


class SharedRangeMapDB(object):
    """
    SharedRangeMapDB provides a long value range map backed by a database table.
     This map allows values to share a given range with other values.
    """





    def __init__(self, dbHandle: db.DBHandle, name: unicode, errHandler: db.util.ErrorHandler, create: bool):
        """
        Construct a shared range map.
        @param dbHandle database handle.
        @param name map name used in naming the underlying database table.
         This name must be unqiue across all shared range maps.
        @param errHandler database error handler.
        @param create if true the underlying database tables will be created.
        """
        ...



    def add(self, start: long, end: long, value: long) -> None:
        """
        Add a value to this map over the specified range.
        @param start the start of the range.
        @param end the end of the range.
        @param value the value to associate with the range.
        """
        ...

    def dispose(self) -> None:
        """
        Frees resources used by this map.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getValueIterator(self, start: long, end: long) -> Iterator[db.Field]:
        """
        Get a LongField value iterator over the specified range.
         List is pre-calculated such that any changes made to the map
         after invoking this method will not be reflected by the iterator
         and invalid function keys may be returned.
         The implementation assumes a small set of values exist over the
         range.
        @param start
        @param end
        @return Iterator of unique LongField values occuring within the
         specified range.
        """
        ...

    def getValueRangeIterator(self, value: long) -> ghidra.util.datastruct.IndexRangeIterator:
        """
        Get an index range iterator for a specified value.
        @param value the value for which to iterator indexes over.
        @return IndexRangeIterator
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, value: long) -> None:
        """
        Remove a value from this map.
        @param value the value to remove.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
