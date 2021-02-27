from typing import List
import java.lang


class ObjectStorage(object):
    """
    Methods for saving and restoring Strings and Java primitives or arrays of
     Strings and primitives. The order in which the puts are done must the
     same order in which the gets are done.
    """









    def equals(self, __a0: object) -> bool: ...

    def getBoolean(self) -> bool:
        """
        Gets the boolean value.
        """
        ...

    def getByte(self) -> int:
        """
        Gets the byte value.
        """
        ...

    def getBytes(self) -> List[int]:
        """
        Gets the byte array.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDouble(self) -> float:
        """
        Gets the double value.
        """
        ...

    def getDoubles(self) -> List[float]:
        """
        Gets the double array.
        """
        ...

    def getFloat(self) -> float:
        """
        Gets the float value.
        """
        ...

    def getFloats(self) -> List[float]:
        """
        Gets the float array.
        """
        ...

    def getInt(self) -> int:
        """
        Gets the int value.
        """
        ...

    def getInts(self) -> List[int]:
        """
        Gets the int array.
        """
        ...

    def getLong(self) -> long:
        """
        Gets the long value.
        """
        ...

    def getLongs(self) -> List[long]:
        """
        Gets the long array.
        """
        ...

    def getShort(self) -> int:
        """
        Gets the short value.
        """
        ...

    def getShorts(self) -> List[int]:
        """
        Gets the short array.
        """
        ...

    def getString(self) -> unicode:
        """
        Gets the String value.
        """
        ...

    def getStrings(self) -> List[unicode]:
        """
        Gets the array of Strings
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def putBoolean(self, value: bool) -> None:
        """
        Store a boolean value.
        @param value The value in the name,value pair.
        """
        ...

    def putByte(self, value: int) -> None:
        """
        Store a byte value.
        @param value The value in the name,value pair.
        """
        ...

    def putBytes(self, value: List[int]) -> None:
        """
        Store a byte array.
        """
        ...

    def putDouble(self, value: float) -> None:
        """
        Store a double value.
        @param value The value in the name,value pair.
        """
        ...

    def putDoubles(self, value: List[float]) -> None:
        """
        Store a double array value.
        """
        ...

    def putFloat(self, value: float) -> None:
        """
        Store a float value.
        @param value The value in the name,value pair.
        """
        ...

    def putFloats(self, value: List[float]) -> None:
        """
        Store a float array.
        """
        ...

    def putInt(self, value: int) -> None:
        """
        Store an integer value.
        @param value The value in the name,value pair.
        """
        ...

    def putInts(self, value: List[int]) -> None:
        """
        Store an integer array.
        """
        ...

    def putLong(self, value: long) -> None:
        """
        Store a long value.
        @param value The value in the name,value pair.
        """
        ...

    def putLongs(self, value: List[long]) -> None:
        """
        Store a long array.
        """
        ...

    def putShort(self, value: int) -> None:
        """
        Store a short value.
        @param value The value in the name,value pair.
        """
        ...

    def putShorts(self, value: List[int]) -> None:
        """
        Store a short array.
        """
        ...

    def putString(self, value: unicode) -> None:
        """
        Store a String value.
        @param value The value in the name,value pair.
        """
        ...

    def putStrings(self, value: List[unicode]) -> None:
        """
        Store a String[] value.
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
