from typing import List
import ghidra.program.model.mem
import ghidra.util
import java.lang


class GhidraDataConverter(ghidra.util.DataConverter, object):








    def equals(self, __a0: object) -> bool: ...

    @overload
    def getBigInteger(self, __a0: List[int], __a1: int, __a2: bool) -> long: ...

    @overload
    def getBigInteger(self, __a0: List[int], __a1: int, __a2: int, __a3: bool) -> long: ...

    @overload
    def getBigInteger(self, buf: ghidra.program.model.mem.MemBuffer, offset: int, size: int, signed: bool) -> long:
        """
        Generate a BigInteger value by invoking buf.getBytes at the specified offset.
        @param buf MemBuffer source of bytes
        @param offset offset in mem buffer to read
        @param size number of bytes
        @param signed boolean flag
        @return BigInteger value
        @throws MemoryAccessException if failed to read specified number of bytes
         at the specified offset
        """
        ...

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
    def getInstance(isBigEndian: bool) -> ghidra.util.GhidraDataConverter:
        """
        Returns the correct GhidraDataConverter static instance for the requested endian-ness.
        @param isBigEndian boolean flag, true means big endian
        @return static GhidraDataConverter instance
        """
        ...

    @overload
    def getInt(self, __a0: List[int]) -> int: ...

    @overload
    def getInt(self, __a0: List[int], __a1: int) -> int: ...

    @overload
    def getInt(self, buf: ghidra.program.model.mem.MemBuffer, offset: int) -> int:
        """
        Generate a int value by invoking buf.getBytes at the specified offset.
        @param buf MemBuffer source of bytes
        @param offset offset in mem buffer to read
        @return int value
        @throws MemoryAccessException if failed to read 4-bytes at the specified offset
        """
        ...

    @overload
    def getLong(self, __a0: List[int]) -> long: ...

    @overload
    def getLong(self, __a0: List[int], __a1: int) -> long: ...

    @overload
    def getLong(self, buf: ghidra.program.model.mem.MemBuffer, offset: int) -> long:
        """
        Generate a long value by invoking buf.getBytes at the specified offset.
        @param buf MemBuffer source of bytes
        @param offset offset in mem buffer to read
        @return long value
        @throws MemoryAccessException if failed to read 8-bytes at the specified offset
        """
        ...

    @overload
    def getShort(self, __a0: List[int]) -> int: ...

    @overload
    def getShort(self, __a0: List[int], __a1: int) -> int: ...

    @overload
    def getShort(self, buf: ghidra.program.model.mem.MemBuffer, offset: int) -> int:
        """
        Generate a short value by invoking buf.getBytes at the specified offset.
        @param buf MemBuffer source of bytes
        @param offset offset in mem buffer to read
        @return short value
        @throws MemoryAccessException if failed to read 2-bytes at the specified offset
        """
        ...

    @overload
    def getSignedValue(self, __a0: List[int], __a1: int) -> long: ...

    @overload
    def getSignedValue(self, __a0: List[int], __a1: int, __a2: int) -> long: ...

    @overload
    def getValue(self, __a0: List[int], __a1: int) -> long: ...

    @overload
    def getValue(self, __a0: List[int], __a1: int, __a2: int) -> long: ...

    def hashCode(self) -> int: ...

    def isBigEndian(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def putBigInteger(self, __a0: List[int], __a1: int, __a2: long) -> None: ...

    @overload
    def putBigInteger(self, __a0: List[int], __a1: int, __a2: int, __a3: long) -> None: ...

    @overload
    def putInt(self, __a0: List[int], __a1: int) -> None: ...

    @overload
    def putInt(self, __a0: List[int], __a1: int, __a2: int) -> None: ...

    @overload
    def putLong(self, __a0: List[int], __a1: long) -> None: ...

    @overload
    def putLong(self, __a0: List[int], __a1: int, __a2: long) -> None: ...

    @overload
    def putShort(self, __a0: List[int], __a1: int) -> None: ...

    @overload
    def putShort(self, __a0: List[int], __a1: int, __a2: int) -> None: ...

    def putValue(self, __a0: long, __a1: int, __a2: List[int], __a3: int) -> None: ...

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
