from typing import List
import ghidra.util
import java.lang


class ObjectStorageAdapter(object, ghidra.util.ObjectStorage):
    """
    Convenience adapter implementation for saving and restoring Strings and
     Java primitives or arrays of Strings and primitives for a row of a data table.
     The order in which the puts are done must the same order in which the gets are done.
    """





    def __init__(self, table: ghidra.util.datastruct.DataTable, row: int):
        """
        Constructor for ObjectStorageAdapter.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getBoolean(self) -> bool:
        """
        @see ObjectStorage#getBoolean()
        """
        ...

    def getByte(self) -> int:
        """
        @see ObjectStorage#getByte()
        """
        ...

    def getBytes(self) -> List[int]:
        """
        @see ObjectStorage#getBytes()
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDouble(self) -> float:
        """
        @see ObjectStorage#getDouble()
        """
        ...

    def getDoubles(self) -> List[float]:
        """
        @see ObjectStorage#getDoubles()
        """
        ...

    def getFloat(self) -> float:
        """
        @see ObjectStorage#getFloat()
        """
        ...

    def getFloats(self) -> List[float]:
        """
        @see ObjectStorage#getFloats()
        """
        ...

    def getInt(self) -> int:
        """
        @see ObjectStorage#getInt()
        """
        ...

    def getInts(self) -> List[int]:
        """
        @see ObjectStorage#getInts()
        """
        ...

    def getLong(self) -> long:
        """
        @see ObjectStorage#getLong()
        """
        ...

    def getLongs(self) -> List[long]:
        """
        @see ObjectStorage#getLongs()
        """
        ...

    def getShort(self) -> int:
        """
        @see ObjectStorage#getShort()
        """
        ...

    def getShorts(self) -> List[int]:
        """
        @see ObjectStorage#getShorts()
        """
        ...

    def getString(self) -> unicode:
        """
        @see ObjectStorage#getString()
        """
        ...

    def getStrings(self) -> List[unicode]:
        """
        @see ObjectStorage#getStrings()
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def putBoolean(self, value: bool) -> None:
        """
        @see ObjectStorage#putBoolean(boolean)
        """
        ...

    def putByte(self, value: int) -> None:
        """
        @see ObjectStorage#putByte(byte)
        """
        ...

    def putBytes(self, value: List[int]) -> None:
        """
        @see ObjectStorage#putBytes(byte[])
        """
        ...

    def putDouble(self, value: float) -> None:
        """
        @see ObjectStorage#putDouble(double)
        """
        ...

    def putDoubles(self, value: List[float]) -> None:
        """
        @see ObjectStorage#putDoubles(double[])
        """
        ...

    def putFloat(self, value: float) -> None:
        """
        @see ObjectStorage#putFloat(float)
        """
        ...

    def putFloats(self, value: List[float]) -> None:
        """
        @see ObjectStorage#putFloats(float[])
        """
        ...

    def putInt(self, value: int) -> None:
        """
        @see ObjectStorage#putInt(int)
        """
        ...

    def putInts(self, value: List[int]) -> None:
        """
        @see ObjectStorage#putInts(int[])
        """
        ...

    def putLong(self, value: long) -> None:
        """
        @see ObjectStorage#putLong(long)
        """
        ...

    def putLongs(self, value: List[long]) -> None:
        """
        @see ObjectStorage#putLongs(long[])
        """
        ...

    def putShort(self, value: int) -> None:
        """
        @see ObjectStorage#putShort(short)
        """
        ...

    def putShorts(self, value: List[int]) -> None:
        """
        @see ObjectStorage#putShorts(short[])
        """
        ...

    def putString(self, value: unicode) -> None:
        """
        @see ObjectStorage#putString(String)
        """
        ...

    def putStrings(self, value: List[unicode]) -> None:
        """
        @see ObjectStorage#putStrings(String[])
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
    def boolean(self) -> bool: ...

    @property
    def byte(self) -> int: ...

    @property
    def bytes(self) -> List[int]: ...

    @property
    def double(self) -> float: ...

    @property
    def doubles(self) -> List[float]: ...

    @property
    def float(self) -> float: ...

    @property
    def floats(self) -> List[float]: ...

    @property
    def int(self) -> int: ...

    @property
    def ints(self) -> List[int]: ...

    @property
    def long(self) -> long: ...

    @property
    def longs(self) -> List[long]: ...

    @property
    def short(self) -> int: ...

    @property
    def shorts(self) -> List[int]: ...

    @property
    def string(self) -> unicode: ...

    @property
    def strings(self) -> List[unicode]: ...
