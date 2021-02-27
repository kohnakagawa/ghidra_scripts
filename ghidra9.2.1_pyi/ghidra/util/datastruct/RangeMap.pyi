import ghidra.util
import ghidra.util.datastruct
import java.io
import java.lang


class RangeMap(object, java.io.Serializable):
    """
    Stores ranges of int values throughout "long" space. Every "long" index has
     an associated int value (initially 0). Users can paint (set) ranges of
     indexes to a given integer value, overwriting any value that currently exists
     in that range.

     This class is implemented using an IntPropertyMap.  The first index
     (0) will always contain a value.  The value at any other given
     index will either be the value stored at that index, or if no
     value stored there, then the value stored at the nearest previous index
     that contains a value.
    """





    @overload
    def __init__(self):
        """
        Constructor for RangeMap with a default value of 0.
        """
        ...

    @overload
    def __init__(self, defaultValue: int):
        """
        Creates a new range map with spcified default value.
        @param defaultValue the default value
        """
        ...



    def clear(self) -> None:
        """
        Clears all current values from the range map and resets the default value.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getChangePointIterator(self, start: long, end: long) -> ghidra.util.LongIterator:
        """
        Returns an iterator over all indexes where the value changes.
        @param start the starting index to search.
        @param end the ending index to search.
        @return an iterator over all indexes where the value changes.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getIndexRangeIterator(self, index: long) -> ghidra.util.datastruct.IndexRangeIterator:
        """
        Returns an iterator over all occupied ranges in the map.
        @param index the index to start the iterator
        @return an iterator over all occupied ranges in the map.
        """
        ...

    def getValue(self, index: long) -> int:
        """
        Returns the int value associated with the given index.
        @param index the index at which to get the value.
        """
        ...

    def getValueRange(self, index: long) -> ghidra.util.datastruct.ValueRange:
        """
        Returns the value range containing the given index. The value range indicates
         the int value and the start and end index for the range.
        @param index the index at which to get the associated value range
        @return the value range
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def paintRange(self, start: long, end: long, value: int) -> None:
        """
        Associates the given value with every index from start to end (inclusive)
         Any previous associates are overwritten.
        @param start the start index of the range to fill.
        @param end the end index of the range to fill
        @param value the value to put at every index in the range.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
