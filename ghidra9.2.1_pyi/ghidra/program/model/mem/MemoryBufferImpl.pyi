from typing import List
import ghidra.program.model.address
import ghidra.program.model.mem
import java.lang


class MemoryBufferImpl(object, ghidra.program.model.mem.MutableMemBuffer):
    """
    MemBufferImpl implements the MemBuffer interface.  It buffers up N bytes
     at time, reducing the overall number of calls to Memory, greatly reducing
     the overhead of various error checks.  This implementation will not wrap
     if the end of the memory space is encountered.

     The #getByte(int) method can cause the buffer cache to adjust if
     outside the current cache range.  This is not the case for other methods which
     will simply defer to the underlying memory if outside the cache range.
    """





    @overload
    def __init__(self, mem: ghidra.program.model.mem.Memory, addr: ghidra.program.model.address.Address):
        """
        Construct a new MemoryBufferImpl
        @param mem memory associated with the given address
        @param addr start address
        """
        ...

    @overload
    def __init__(self, mem: ghidra.program.model.mem.Memory, addr: ghidra.program.model.address.Address, bufSize: int):
        """
        Construct a new MemoryBufferImpl
        @param mem memory associated with the given address
        @param addr start address
        @param bufSize the size of the memory buffer.
        """
        ...



    def advance(self, displacement: int) -> None: ...

    def clone(self) -> ghidra.program.model.mem.MemoryBufferImpl: ...

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

    def setPosition(self, addr: ghidra.program.model.address.Address) -> None: ...

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

    @property
    def position(self) -> None: ...  # No getter available.

    @position.setter
    def position(self, value: ghidra.program.model.address.Address) -> None: ...
