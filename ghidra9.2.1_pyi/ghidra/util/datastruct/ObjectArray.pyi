import ghidra.util.datastruct
import java.io
import java.lang


class ObjectArray(object, ghidra.util.datastruct.Array, java.io.Serializable):
    """
    Array of objects that grows as needed.
    """





    @overload
    def __init__(self):
        """
        Creates a new Object array of a default size.
        """
        ...

    @overload
    def __init__(self, size: int):
        """
        Creates a new object array that is initially the size specified.
        @param size the initial size of the Object array.
        """
        ...



    def copyDataTo(self, index: int, table: ghidra.util.datastruct.DataTable, toIndex: int, toCol: int) -> None:
        """
        @see ghidra.util.datastruct.Array#copyDataTo(int, ghidra.util.datastruct.DataTable, int, int)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def get(self, index: int) -> object:
        """
        Returns the Object at the given index
        @param index index into the array
        @return The Object value at the given index. A null will
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

    def put(self, index: int, value: object) -> None:
        """
        Puts the given Object in the Object array at
         the given index
        @param index Index into the array.
        @param value value to store
        @throws IndexOutOfBoundsException if the index is negative
        """
        ...

    def remove(self, index: int) -> None:
        """
        Sets the value at the given index to null.
        @param index the index to set to null.
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
