from typing import List
import ghidra.util.datastruct
import java.lang


class ManagedDataTable(ghidra.util.datastruct.DataTable):
    """
    Data table that keeps track of rows that are occupied.
    """





    def __init__(self): ...



    def copyRowTo(self, row: int, table: ghidra.util.datastruct.DataTable, toRow: int) -> None:
        """
        Copy one row to another row.
        @param row source row
        @param table table containing the data
        @param toRow destination row
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getBoolean(self, row: int, col: int) -> bool:
        """
        Returns the boolean at the given row, column.
        @param row the row in the table
        @param col the column in the table (field num)
        @return the boolean value in the table
        """
        ...

    def getByte(self, row: int, col: int) -> int:
        """
        Returns the byte at the given row, column.
        @param row the row in the table
        @param col the column in the table (field num)
        @return the byte value in the table
        """
        ...

    def getByteArray(self, row: int, col: int) -> List[int]:
        """
        Returns the byte array at the given row, column.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @return the int value.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDouble(self, row: int, col: int) -> float:
        """
        Returns the double at the given row, column.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @return the double value.
        """
        ...

    def getDoubleArray(self, row: int, col: int) -> List[float]:
        """
        Returns the double array at the given row, column.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @return the int value.
        """
        ...

    def getFloat(self, row: int, col: int) -> float:
        """
        Returns the float at the given row, column.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @return the float value.
        """
        ...

    def getFloatArray(self, row: int, col: int) -> List[float]:
        """
        Returns the float array at the given row, column.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @return the float[] value.
        """
        ...

    def getInt(self, row: int, col: int) -> int:
        """
        Returns the int at the given row, column.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @return the int value.
        """
        ...

    def getIntArray(self, row: int, col: int) -> List[int]:
        """
        Returns the int array at the given row, column.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @return the int value.
        """
        ...

    def getLong(self, row: int, col: int) -> long:
        """
        Returns the long at the given row, column.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @return the long value.
        """
        ...

    def getLongArray(self, row: int, col: int) -> List[long]:
        """
        Returns the long array at the given row, column.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @return the long[] value.
        """
        ...

    def getMaxRow(self) -> int:
        """
        Returns the max row that contains data.
        """
        ...

    def getObject(self, row: int, col: int) -> object:
        """
        Returns the Object at the given row, column.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @return the Object value.
        """
        ...

    def getShort(self, row: int, col: int) -> int:
        """
        Returns the short at the given row, column.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @return the short value.
        """
        ...

    def getShortArray(self, row: int, col: int) -> List[int]:
        """
        Returns the short array at the given row, column.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @return the int value.
        """
        ...

    def getString(self, row: int, col: int) -> unicode:
        """
        Returns the string at the given row, column.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @return the int value.
        """
        ...

    def getStringArray(self, row: int, col: int) -> List[unicode]:
        """
        Returns the String array at the given row, column.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @return the String[] value.
        """
        ...

    def hasRow(self, row: int) -> bool:
        """
        returns true if the given row contains an object
        @param row the row in the table
        @return true if the given row contains an object
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def putBoolean(self, row: int, col: int, value: bool) -> None:
        """
        Stores a boolean value in the table at the given row
         and column.  Note - all values in a given column must be
         of the same type.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @param value The value to store.
        """
        ...

    def putByte(self, row: int, col: int, value: int) -> None:
        """
        Stores a byte value in the table at the given row
         and column.  Note - all values in a given column must be
         of the same type.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @param value The value to store.
        """
        ...

    def putByteArray(self, row: int, col: int, value: List[int]) -> None:
        """
        Stores an byte array in the table at the given row
         and column.  Note - all values in a given column must be
         of the same type.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @param value The value to store.
        """
        ...

    def putDouble(self, row: int, col: int, value: float) -> None:
        """
        Stores a double value in the table at the given row
         and column.  Note - all values in a given column must be
         of the same type.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @param value The value to store.
        """
        ...

    def putDoubleArray(self, row: int, col: int, value: List[float]) -> None:
        """
        Stores a double array in the table at the given row
         and column.  Note - all values in a given column must be
         of the same type.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @param value The value to store.
        """
        ...

    def putFloat(self, row: int, col: int, value: float) -> None:
        """
        Stores a float value in the table at the given row
         and column.  Note - all values in a given column must be
         of the same type.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @param value The value to store.
        """
        ...

    def putFloatArray(self, row: int, col: int, value: List[float]) -> None:
        """
        Stores a float array in the table at the given row
         and column.  Note - all values in a given column must be
         of the same type.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @param value The value to store.
        """
        ...

    def putInt(self, row: int, col: int, value: int) -> None:
        """
        Stores an int value in the table at the given row
         and column.  Note - all values in a given column must be
         of the same type.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @param value The value to store.
        """
        ...

    def putIntArray(self, row: int, col: int, value: List[int]) -> None:
        """
        Stores an int array in the table at the given row
         and column.  Note - all values in a given column must be
         of the same type.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @param value The value to store.
        """
        ...

    def putLong(self, row: int, col: int, value: long) -> None:
        """
        Stores a long value in the table at the given row
         and column.  Note - all values in a given column must be
         of the same type.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @param value The value to store.
        """
        ...

    def putLongArray(self, row: int, col: int, value: List[long]) -> None:
        """
        Stores an long array in the table at the given row
         and column.  Note - all values in a given column must be
         of the same type.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @param value The value to store.
        """
        ...

    def putObject(self, row: int, col: int, value: object) -> None:
        """
        Stores an Object in the table at the given row
         and column.  Note - all values in a given column must be
         of the same type.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @param value The value to store.
        """
        ...

    def putShort(self, row: int, col: int, value: int) -> None:
        """
        Stores a short value in the table at the given row
         and column.  Note - all values in a given column must be
         of the same type.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @param value The value to store.
        """
        ...

    def putShortArray(self, row: int, col: int, value: List[int]) -> None:
        """
        Stores an short array in the table at the given row
         and column.  Note - all values in a given column must be
         of the same type.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @param value The value to store.
        """
        ...

    def putString(self, row: int, col: int, value: unicode) -> None:
        """
        Stores an String in the table at the given row
         and column.  Note - all values in a given column must be
         of the same type.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @param value The value to store.
        """
        ...

    def putStringArray(self, row: int, col: int, value: List[unicode]) -> None:
        """
        Stores a String array in the table at the given row
         and column.  Note - all values in a given column must be
         of the same type.
        @param row The row into the table (specifies which object)
        @param col The column of the table.  (specifies which field)
        @param value The value to store.
        """
        ...

    def removeRow(self, row: int) -> None:
        """
        Removes the given row from the table.
        @param row The row to be removed
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
    def maxRow(self) -> int: ...
