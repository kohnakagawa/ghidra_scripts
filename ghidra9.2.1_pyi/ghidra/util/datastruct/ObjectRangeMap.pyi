import ghidra.util.datastruct
import java.lang


class ObjectRangeMap(object):
    """
    Associates objects with long index ranges.
    """





    def __init__(self):
        """
        Constructs a new ObjectRangeMap
        """
        ...



    def clearRange(self, start: long, end: long) -> None:
        """
        Clears any object associations within the given range.
        @param start the first index in the range to be cleared.
        @param end the last index in the range to be cleared.
        """
        ...

    def contains(self, index: long) -> bool:
        """
        Returns true if the associated index has an associated object even if the assocated object
         is null.
        @param index the index to check for an association.
        @return true if the associated index has an associated object even if the assocated object
         is null.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getIndexRangeIterator(self) -> ghidra.util.datastruct.IndexRangeIterator:
        """
        Returns an {@link IndexRangeIterator} over all ranges that have associated objects.
        @return an {@link IndexRangeIterator} over all ranges that have associated objects.
        """
        ...

    @overload
    def getIndexRangeIterator(self, start: long, end: long) -> ghidra.util.datastruct.IndexRangeIterator:
        """
        Returns an {@link IndexRangeIterator} over all ranges that have associated objects within
         the given range.  Object Ranges that overlap the beginning or end of the given range are
         included, but have thier start or end index adjusted to be in the given range.
        @param start the first index in the range to find all index ranges that have associated values.
        @param end the last index(inclusive) in the range to find all index ranges that have associated
          values.
        @return an {@link IndexRangeIterator} over all ranges that have associated objects within the
         given range.
        """
        ...

    def getObject(self, index: long) -> object:
        """
        Returns the object associated with the given index or null if no object is associated with
         the given index.  Note that null is a valid association so a null result could be either
         no association or an actual association of the index to null.  Use the contains() method
         first if the distinction is important.  If the contains() method returns true, the result
         is cached so the next call to getObject() will be fast.
        @param index the index at which to retrieve an assocated object.
        @return the object (which can be null) associated with the given index or null if no such
         association exists.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setObject(self, start: long, end: long, object: object) -> None:
        """
        Associates the given object with all indices in the given range. The object may be null,
         but an assocition is still established.  Use the clearRange() method to remove associations.
        @param start the start of the range.
        @param end the end (inclusive) of the range.
        @param object the object to associate with the given range.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def indexRangeIterator(self) -> ghidra.util.datastruct.IndexRangeIterator: ...
