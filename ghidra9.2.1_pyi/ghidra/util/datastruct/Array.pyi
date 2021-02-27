import ghidra.util.datastruct
import java.lang


class Array(object):
    """
    Base interface for Defining methods for managing a "virtual" array of some data type.
     Any access of an Array with an index that has never been set will return 0
     (or something like that depending on the data type)
    """









    def copyDataTo(self, index: int, table: ghidra.util.datastruct.DataTable, toIndex: int, toCol: int) -> None:
        """
        Copies the underlying value for this array at the given index to the
         data table at the given index and column.  The data type at the column in
         the data table must be the same as the data in this array.
        @param index index into this array to copy the value from.
        @param table the data table object to copy the data to.
        @param toIndex the index into the destination data table to copy the
         value.
        @param toCol the data table column to store the value.  Must be the same
         type as this array.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLastNonEmptyIndex(self) -> int:
        """
        Returns the index of the last non-null or non-zero element in the array.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, index: int) -> None:
        """
        Removes the value at that index.  If the array is of primitive type (int, short, etc),
         then "removing" the value is equivilent to setting the value to 0;
        @param index int index into the array to remove.
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
    def lastNonEmptyIndex(self) -> int: ...
