import ghidra.util.datastruct
import java.io
import java.lang


class BooleanArray(object, ghidra.util.datastruct.Array, java.io.Serializable):
    """
    Data structure to set bits to indicate in use.
    """





    def __init__(self):
        """
        Constructor
        """
        ...



    def copyDataTo(self, index: int, table: ghidra.util.datastruct.DataTable, toIndex: int, toCol: int) -> None:
        """
        @see ghidra.util.datastruct.Array#copyDataTo(int, ghidra.util.datastruct.DataTable, int, int)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def get(self, index: int) -> bool:
        """
        Returns the boolean at the given index
        @param index index into the array
        @return The boolean value at the given index. A false will
         be return for any non-negative index not initialized to
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

    def put(self, index: int, value: bool) -> None:
        """
        Puts the given boolean value in the boolean array at
         the given index
        @param index Index into the array.
        @param value value to store
        @throws IndexOutOfBoundsException if the index is negative
        """
        ...

    def remove(self, index: int) -> None:
        """
        Sets the value at the given index to 0.
        @param index the index to set to 0.
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
