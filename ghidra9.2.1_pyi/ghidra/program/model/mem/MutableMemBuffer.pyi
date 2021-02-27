from typing import List
import ghidra.program.model.address
import ghidra.program.model.mem
import java.lang


class MutableMemBuffer(ghidra.program.model.mem.MemBuffer, object):
    """
    The MutableMemBuffer interface facilitates
     repositioning of a MemBuffer object.
    """









    def advance(self, displacement: int) -> None:
        """
        Advance the Address pointer.
        @param displacement the amount to adjust the pointer by.
        @throws AddressOverflowException if displacement would cause the buffer position to wrap.
        """
        ...

    def clone(self) -> ghidra.program.model.mem.MutableMemBuffer:
        """
        Create a cloned copy of this MutableMemBuffer
        @return new cloned instance of this buffer object
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address: ...

    def getBigInteger(self, __a0: int, __a1: int, __a2: bool) -> long: ...

    def getByte(self, __a0: int) -> int: ...

    def getBytes(self, __a0: List[int], __a1: int) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getInt(self, __a0: int) -> int: ...

    def getLong(self, __a0: int) -> long: ...

    def getMemory(self) -> ghidra.program.model.mem.Memory: ...

    def getShort(self, __a0: int) -> int: ...

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

    def setPosition(self, addr: ghidra.program.model.address.Address) -> None:
        """
        Sets the Address to which offset of 0 points to.
        @param addr the new base Address.
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
