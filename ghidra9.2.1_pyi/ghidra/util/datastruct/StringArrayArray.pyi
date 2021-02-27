from typing import List
import ghidra.util.datastruct
import java.io
import java.lang


class StringArrayArray(object, ghidra.util.datastruct.Array, java.io.Serializable):
    """
    Array of String[] that grows as needed.
    """





    def __init__(self):
        """
        Constructor for StringArrayArray.
        """
        ...



    def copyDataTo(self, index: int, table: ghidra.util.datastruct.DataTable, toIndex: int, toCol: int) -> None:
        """
        @see Array#copyDataTo(int, DataTable, int, int)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def get(self, index: int) -> List[unicode]:
        """
        Retrieves the String array stored at the given index.
        @param index the index at which to retrieve the array.
        @return String[] the String array at the index.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getLastNonEmptyIndex(self) -> int:
        """
        @see Array#getLastNonEmptyIndex()
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def put(self, index: int, value: List[unicode]) -> None:
        """
        Stores the string array at the given index.
        @param index the index to store the array
        @param value the array to store
        """
        ...

    def remove(self, index: int) -> None:
        """
        @see Array#remove(int)
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
