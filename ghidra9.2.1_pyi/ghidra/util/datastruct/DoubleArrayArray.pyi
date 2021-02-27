from typing import List
import ghidra.util.datastruct
import java.io
import java.lang


class DoubleArrayArray(object, ghidra.util.datastruct.Array, java.io.Serializable):
    """
    Array of double[] that grows as needed.
    """





    def __init__(self):
        """
        Creates new doubleArrayArray
        """
        ...



    def copyDataTo(self, index: int, table: ghidra.util.datastruct.DataTable, toIndex: int, toCol: int) -> None:
        """
        @see ghidra.util.datastruct.Array#copyDataTo(int, DataTable, int, int)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def get(self, index: int) -> List[float]:
        """
        Returns the double at the given index
        @param index index into the array
        @return The double array at the given index. An empty array will
         be returned for any index not initialized to
         another value.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getLastNonEmptyIndex(self) -> int:
        """
        Returns the index of the last non-null or non-zero element in the array.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def put(self, index: int, value: List[float]) -> None:
        """
        Puts the given double value in the double array at
         the given index
        @param index Index into the array.
        @param value value to store
        @throws IndexOutOfBoundsException if the index is negative
        """
        ...

    def remove(self, index: int) -> None:
        """
        Removes the array at the given index
        @param index index of the array to be removed
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
