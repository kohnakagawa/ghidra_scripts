import ghidra.util.datastruct
import java.io
import java.lang


class StringArray(object, ghidra.util.datastruct.Array, java.io.Serializable):
    """
    Array of Strings that grows as needed.
    """





    def __init__(self):
        """
        Creates new StringArray
        """
        ...



    def copyDataTo(self, index: int, table: ghidra.util.datastruct.DataTable, toIndex: int, toCol: int) -> None:
        """
        @see ghidra.util.datastruct.Array#copyDataTo(int, ghidra.util.datastruct.DataTable, int, int)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def get(self, index: int) -> unicode:
        """
        Returns the String at the given index
        @param index index into the array
        @return The String  at the given index. A null will
         be return for any index not initialized to
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

    def put(self, index: int, value: unicode) -> None:
        """
        Puts the given String value in the String array at
         the given index
        @param index Index into the array.
        @param value value to store
        """
        ...

    def remove(self, index: int) -> None:
        """
        Removes the string at the given index
        @param index index of the string to be removed
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
