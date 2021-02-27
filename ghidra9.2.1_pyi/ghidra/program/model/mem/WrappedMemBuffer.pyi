from typing import List
import ghidra.program.model.address
import ghidra.program.model.mem
import java.lang


class WrappedMemBuffer(object, ghidra.program.model.mem.MemBuffer):
    """
    WrappedMemBuffer implements a MemBuffer that provides a zero based index
     on top of an underlying membuffer with at a given address.  It can buffer N bytes
     at time using the constructor that takes a cache size.  However the default
     is to provide no buffering.  Use of the buffer can
     reduce the overall number of calls to Memory, greatly reducing
     the overhead of various error checks.  This implementation will not wrap
     if the end of the memory space is encountered.

     The #getByte(int), #getBytes(byte[], int) methods can cause the bytes in the
     buffer cache if the request is outside of the current cached bytes.

     WARNING: The underlying MemBuffer should not change its base address. Using a
     mutable MemBuffer can cause problematic behavior if not controlled carefully.

     WARNING: Not thread-safe.
    """





    @overload
    def __init__(self, buf: ghidra.program.model.mem.MemBuffer, baseOffset: int):
        """
        Construct a wrapped MemBuffer with an adjustable base offset
        @param buf memory buffer
        @param baseOffset offset relative to the underlying buffer's start address
                       (addr + baseOffset) will be the 0 index into this buffer
        @throws AddressOutOfBoundsException
        """
        ...

    @overload
    def __init__(self, buf: ghidra.program.model.mem.MemBuffer, bufferSize: int, baseOffset: int):
        """
        Construct a wrapped MemBuffer with an adjustable base offset
        @param buf memory buffer
        @param bufferSize size of cache buffer - specify 0 for no buffering
        @param baseOffset offset relative to the underlying buffer's start address
                       (addr + baseOffset) will be the 0 index into this buffer
        @throws AddressOutOfBoundsException
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address: ...

    def getBigInteger(self, offset: int, size: int, signed: bool) -> long: ...

    def getByte(self, offset: int) -> int: ...

    def getBytes(self, b: List[int], offset: int) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getInt(self, offset: int) -> int: ...

    def getLong(self, offset: int) -> long: ...

    def getMemory(self) -> ghidra.program.model.mem.Memory: ...

    def getShort(self, offset: int) -> int: ...

    def getUnsignedByte(self, __a0: int) -> int: ...

    def getUnsignedInt(self, __a0: int) -> long: ...

    def getUnsignedShort(self, __a0: int) -> int: ...

    def getVarLengthInt(self, __a0: int, __a1: int) -> int: ...

    def getVarLengthUnsignedInt(self, __a0: int, __a1: int) -> long: ...

    def hashCode(self) -> int: ...

    def isBigEndian(self) -> bool: ...

    def isInitializedMemory(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def bigEndian(self) -> bool: ...

    @property
    def initializedMemory(self) -> bool: ...

    @property
    def memory(self) -> ghidra.program.model.mem.Memory: ...
