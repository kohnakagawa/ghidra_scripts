from typing import List
import ghidra.util
import java.lang


class ObjectStorageStreamAdapter(object, ghidra.util.ObjectStorage):
    """
    Implementation for ObjectStorage to save and restore Strings and
     Java primitives using an ObjectOutputStream and ObjectInputStream,
     respectively.
    """





    @overload
    def __init__(self, in_: java.io.ObjectInputStream):
        """
        Constructor for new ObjectStorageStreamAdapter
        @param in input stream to read from
        """
        ...

    @overload
    def __init__(self, out: java.io.ObjectOutputStream):
        """
        Constructor for ObjectStorageStreamAdapter.
        @param out output stream to write to
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getBoolean(self) -> bool:
        """
        @see ghidra.util.ObjectStorage#getBoolean()
        """
        ...

    def getByte(self) -> int:
        """
        @see ghidra.util.ObjectStorage#getByte()
        """
        ...

    def getBytes(self) -> List[int]:
        """
        @see ghidra.util.ObjectStorage#getBytes()
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDouble(self) -> float:
        """
        @see ghidra.util.ObjectStorage#getDouble()
        """
        ...

    def getDoubles(self) -> List[float]:
        """
        @see ghidra.util.ObjectStorage#getDoubles()
        """
        ...

    def getFloat(self) -> float:
        """
        @see ghidra.util.ObjectStorage#getFloat()
        """
        ...

    def getFloats(self) -> List[float]:
        """
        @see ghidra.util.ObjectStorage#getFloats()
        """
        ...

    def getInt(self) -> int:
        """
        @see ghidra.util.ObjectStorage#getInt()
        """
        ...

    def getInts(self) -> List[int]:
        """
        @see ghidra.util.ObjectStorage#getInts()
        """
        ...

    def getLong(self) -> long:
        """
        @see ghidra.util.ObjectStorage#getLong()
        """
        ...

    def getLongs(self) -> List[long]:
        """
        @see ghidra.util.ObjectStorage#getLongs()
        """
        ...

    def getShort(self) -> int:
        """
        @see ghidra.util.ObjectStorage#getShort()
        """
        ...

    def getShorts(self) -> List[int]:
        """
        @see ghidra.util.ObjectStorage#getShorts()
        """
        ...

    def getString(self) -> unicode:
        """
        @see ghidra.util.ObjectStorage#getString()
        """
        ...

    def getStrings(self) -> List[unicode]:
        """
        @see ghidra.util.ObjectStorage#getStrings()
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def putBoolean(self, value: bool) -> None:
        """
        @see ghidra.util.ObjectStorage#putBoolean(boolean)
        """
        ...

    def putByte(self, value: int) -> None:
        """
        @see ghidra.util.ObjectStorage#putByte(byte)
        """
        ...

    def putBytes(self, value: List[int]) -> None:
        """
        @see ghidra.util.ObjectStorage#putBytes(byte[])
        """
        ...

    def putDouble(self, value: float) -> None:
        """
        @see ghidra.util.ObjectStorage#putDouble(double)
        """
        ...

    def putDoubles(self, value: List[float]) -> None:
        """
        @see ghidra.util.ObjectStorage#putDoubles(double[])
        """
        ...

    def putFloat(self, value: float) -> None:
        """
        @see ghidra.util.ObjectStorage#putFloat(float)
        """
        ...

    def putFloats(self, value: List[float]) -> None:
        """
        @see ghidra.util.ObjectStorage#putFloats(float[])
        """
        ...

    def putInt(self, value: int) -> None:
        """
        @see ghidra.util.ObjectStorage#putInt(int)
        """
        ...

    def putInts(self, value: List[int]) -> None:
        """
        @see ghidra.util.ObjectStorage#putInts(int[])
        """
        ...

    def putLong(self, value: long) -> None:
        """
        @see ghidra.util.ObjectStorage#putLong(long)
        """
        ...

    def putLongs(self, value: List[long]) -> None:
        """
        @see ghidra.util.ObjectStorage#putLongs(long[])
        """
        ...

    def putShort(self, value: int) -> None:
        """
        @see ghidra.util.ObjectStorage#putShort(short)
        """
        ...

    def putShorts(self, value: List[int]) -> None:
        """
        @see ghidra.util.ObjectStorage#putShorts(short[])
        """
        ...

    def putString(self, value: unicode) -> None:
        """
        @see ghidra.util.ObjectStorage#putString(String)
        """
        ...

    def putStrings(self, value: List[unicode]) -> None:
        """
        @see ghidra.util.ObjectStorage#putStrings(String[])
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
