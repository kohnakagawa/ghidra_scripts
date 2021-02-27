from typing import List
import ghidra.util.datastruct
import java.io
import java.lang


class FloatArrayArray(object, ghidra.util.datastruct.Array, java.io.Serializable):
    """
    Array of float[] that grows as needed.
    """

    serialVersionUID: long = 0x1L



    def __init__(self):
        """
        Creates new floatArrayArray
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
        Returns the float at the given index
        @param index index into the array
        @return The float array at the given index. An empty array will
         be returned for any index not initialized to
         another value.
        @throws IndexOutOfBoundsException if the index is negative
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
        Puts the given float value in the float array at
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
        @throws IndexOutOfBoundsException if the index is negative
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
