from typing import List
import ghidra.util
import java.lang


class BigEndianDataConverter(object, ghidra.util.DataConverter):
    """
    Helper class to convert a byte array to Java primitives and primitives to a
     byte array in Big endian.
    """

    INSTANCE: ghidra.util.BigEndianDataConverter = ghidra.util.BigEndianDataConverter@629f078e



    def __init__(self):
        """
        Don't use this constructor to create new instances of this class.  Use the static {@link #INSTANCE} instead.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    @overload
    def getBigInteger(self, __a0: List[int], __a1: int, __a2: bool) -> long: ...

    @overload
    def getBigInteger(self, b: List[int], offset: int, size: int, signed: bool) -> long: ...

    @overload
    def getBytes(self, __a0: long) -> List[int]: ...

    @overload
    def getBytes(self, __a0: int) -> List[int]: ...

    @overload
    def getBytes(self, __a0: int) -> List[int]: ...

    @overload
    def getBytes(self, __a0: long, __a1: int) -> List[int]: ...

    @overload
    def getBytes(self, __a0: long, __a1: List[int]) -> None: ...

    @overload
    def getBytes(self, __a0: int, __a1: List[int]) -> None: ...

    @overload
    def getBytes(self, __a0: int, __a1: List[int]) -> None: ...

    @overload
    def getBytes(self, __a0: long, __a1: List[int], __a2: int) -> None: ...

    @overload
    def getBytes(self, __a0: int, __a1: List[int], __a2: int) -> None: ...

    @overload
    def getBytes(self, __a0: int, __a1: List[int], __a2: int) -> None: ...

    @overload
    def getBytes(self, __a0: long, __a1: int, __a2: List[int], __a3: int) -> None: ...

    @overload
    def getBytes(self, __a0: long, __a1: int, __a2: List[int], __a3: int) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getInstance(__a0: bool) -> ghidra.util.DataConverter: ...

    @overload
    def getInt(self, __a0: List[int]) -> int: ...

    @overload
    def getInt(self, b: List[int], offset: int) -> int: ...

    @overload
    def getLong(self, __a0: List[int]) -> long: ...

    @overload
    def getLong(self, b: List[int], offset: int) -> long: ...

    @overload
    def getShort(self, __a0: List[int]) -> int: ...

    @overload
    def getShort(self, b: List[int], offset: int) -> int: ...

    @overload
    def getSignedValue(self, __a0: List[int], __a1: int) -> long: ...

    @overload
    def getSignedValue(self, __a0: List[int], __a1: int, __a2: int) -> long: ...

    @overload
    def getValue(self, __a0: List[int], __a1: int) -> long: ...

    @overload
    def getValue(self, b: List[int], offset: int, size: int) -> long: ...

    def hashCode(self) -> int: ...

    def isBigEndian(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def putBigInteger(self, __a0: List[int], __a1: int, __a2: long) -> None: ...

    @overload
    def putBigInteger(self, b: List[int], offset: int, size: int, value: long) -> None: ...

    @overload
    def putInt(self, __a0: List[int], __a1: int) -> None: ...

    @overload
    def putInt(self, b: List[int], offset: int, value: int) -> None: ...

    @overload
    def putLong(self, __a0: List[int], __a1: long) -> None: ...

    @overload
    def putLong(self, __a0: List[int], __a1: int, __a2: long) -> None: ...

    @overload
    def putShort(self, __a0: List[int], __a1: int) -> None: ...

    @overload
    def putShort(self, b: List[int], offset: int, value: int) -> None: ...

    def putValue(self, value: long, size: int, b: List[int], offset: int) -> None: ...

    @staticmethod
    def swapBytes(__a0: long, __a1: int) -> long: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def bigEndian(self) -> bool: ...
