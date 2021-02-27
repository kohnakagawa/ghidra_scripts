import ghidra.util.datastruct
import java.io
import java.lang


class IntArray(object, ghidra.util.datastruct.Array, java.io.Serializable):
    """
    Array of ints that grows as needed.
    """

    MIN_SIZE: int = 4



    def __init__(self):
        """
        Creates new intArray
        """
        ...



    def copyDataTo(self, index: int, table: ghidra.util.datastruct.DataTable, toIndex: int, toCol: int) -> None:
        """
        @see ghidra.util.datastruct.Array#copyDataTo(int, DataTable, int, int)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def get(self, index: int) -> int:
        """
        Returns the int at the given index
        @param index index into the array
        @return The int value at the given index. A 0 will
         be return for any index not initialized to
         another value.
        @throws IndexOutOfBoundsException if the index is negative
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getLastNonEmptyIndex(self) -> int:
        """
        @see ghidra.util.datastruct.Array#getLastNonEmptyIndex()
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def put(self, index: int, value: int) -> None:
        """
        Puts the given int value in the int array at
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
