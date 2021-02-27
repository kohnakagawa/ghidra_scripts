from typing import Iterator
import ghidra.util.datastruct
import java.lang
import java.util
import java.util.function


class SortedRangeList(object, java.lang.Iterable):
    """
    Provides a list of integer ranges that are maintained in sorted order.
     When a range is added any ranges that overlap or are adjacent to one another
     will coalesce into a single range.
    """





    @overload
    def __init__(self):
        """
        Creates a new empty sorted range list.
        """
        ...

    @overload
    def __init__(self, list: ghidra.util.datastruct.SortedRangeList):
        """
        Creates a new sorted range list with ranges equivalent to those in the
         specified list.
        @param list the sorted range list to make an equivalent copy of.
        """
        ...

    def __iter__(self): ...

    def addRange(self, min: int, max: int) -> None:
        """
        Adds the range from min to max to this sorted range list.
         If the range is adjacent to or overlaps any other existing ranges,
         then those ranges will coalesce.
        @param min the range minimum
        @param max the range maximum (inclusive)
        """
        ...

    @overload
    def contains(self, value: int) -> bool:
        """
        Returns true if the value is contained in any ranges within this list.
        @param value the value to check for.
        """
        ...

    @overload
    def contains(self, min: int, max: int) -> bool:
        """
        Returns true if a single range contains all the values from min to max.
        @param min the minimum value
        @param max the maximum value
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getMax(self) -> int:
        """
        Returns the maximum int value in this sorted range list.
        @throws NoSuchElementException if the list is empty.
        """
        ...

    def getMin(self) -> int:
        """
        Returns the minimum int value in this sorted range list.
        @throws NoSuchElementException if the list is empty.
        """
        ...

    def getNumRanges(self) -> int:
        """
        Returns the number of ranges in the list.
        """
        ...

    def getNumValues(self) -> long:
        """
        Gets the total number of int values in this range.
        @return the number of int values.
        """
        ...

    def getRange(self, index: int) -> ghidra.util.datastruct.Range:
        """
        Gets the nth range in this list as indicated by the value of index.
        @param index value indicating which nth range to get.
        @return the range or null if there is no such range in this list.
        """
        ...

    def getRangeIndex(self, value: int) -> int:
        """
        Gets the range index for the range containing the specified value.
        @param value the value to look for.
        @return the range index or a negative value if the range list doesn't contain the value.
        """
        ...

    @overload
    def getRanges(self) -> Iterator[ghidra.util.datastruct.Range]:
        """
        Returns an iterator over all the ranges in this list.
        """
        ...

    @overload
    def getRanges(self, forward: bool) -> Iterator[ghidra.util.datastruct.Range]:
        """
        Returns an iterator over all the ranges in this list that iterates in the direction specified.
        @param forward true indicates to iterate forward from minimum to maximum range.
         false indicates backward iteration form maximum to minimum.
        """
        ...

    def hashCode(self) -> int: ...

    def intersect(self, other: ghidra.util.datastruct.SortedRangeList) -> ghidra.util.datastruct.SortedRangeList:
        """
        Creates a new SortedRangeList that is the intersection of this range list and the other range list specified.
        @param other the other range list
        @return the new SortedRangeList representing the intersection.
        """
        ...

    def intersects(self, min: int, max: int) -> bool:
        """
        Returns true if the range from min to max intersects (overlaps) any ranges in this sorted range list.
        @param min the range minimum value.
        @param max the range maximum value
        """
        ...

    def isEmpty(self) -> bool:
        """
        Returns true if the range list is empty.
        """
        ...

    def iterator(self) -> Iterator[ghidra.util.datastruct.Range]: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, other: ghidra.util.datastruct.SortedRangeList) -> None:
        """
        Removes all the ranges that are in the specified other list from this list.
        @param other the other sorted range list.
        """
        ...

    def removeRange(self, min: int, max: int) -> None:
        """
        Removes the indicated range of values from the list. This will remove
         any ranges or portion of ranges that overlap the indicated range.
        @param min the minimum value for the range to remove.
        @param max the maximum value for the range to remove.
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

    @property
    def empty(self) -> bool: ...

    @property
    def max(self) -> int: ...

    @property
    def min(self) -> int: ...

    @property
    def numRanges(self) -> int: ...

    @property
    def numValues(self) -> long: ...

    @property
    def ranges(self) -> java.util.Iterator: ...
