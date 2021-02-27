from typing import List
import ghidra.program.model.address
import ghidra.program.model.lang
import java.lang


class UnknownRegister(ghidra.program.model.lang.Register):
    """
    UnknownRegister is used when a register is requested in the register space
     for an undefined location.
    """





    def __init__(self, name: unicode, description: unicode, address: ghidra.program.model.address.Address, numBytes: int, bigEndian: bool, typeFlags: int): ...



    @overload
    def compareTo(self, other: ghidra.program.model.lang.Register) -> int:
        """
        @see java.lang.Comparable#compareTo(java.lang.Object)
        """
        ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def contains(self, reg: ghidra.program.model.lang.Register) -> bool:
        """
        Determines if reg is contained within this register.
         Method does not work for bit registers (e.g., context-bits)
        @param reg another register
        @return true if reg equals this register or is contained
         within it.
        """
        ...

    def equals(self, o: object) -> bool:
        """
        @see java.lang.Object#equals(java.lang.Object)
        """
        ...

    def followsFlow(self) -> bool:
        """
        Returns true for a register whose context value should
         follow the disassembly flow.
        """
        ...

    def getAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the address of the register.
        """
        ...

    def getAddressSpace(self) -> ghidra.program.model.address.AddressSpace:
        """
        Returns the register address space
        """
        ...

    def getAliases(self) -> java.lang.Iterable:
        """
        Return register aliases.
         NOTE: This is generally only supported for
         context register fields.
        @return register aliases or null
        """
        ...

    def getBaseMask(self) -> List[int]:
        """
        Returns the mask that indicates which bits in the base register apply to this register.
        @return the mask that indicates which bits in the base register apply to this register
        """
        ...

    def getBaseRegister(self) -> ghidra.program.model.lang.Register: ...

    def getBitLength(self) -> int:
        """
        Gets the total number of bits for this Register.
        @return the total number of bits for this Register.
        """
        ...

    def getChildRegisters(self) -> List[ghidra.program.model.lang.Register]:
        """
        Returns list of children registers sorted by
         lest-significant bit-offset within this register.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode:
        """
        Get the description of the Register.
        @return the description of the register
        """
        ...

    def getGroup(self) -> unicode: ...

    def getLaneSizes(self) -> List[int]:
        """
        Returns the sorted array of lane sizes for this register, measured in bytes.
        @return array of lane sizes, or {@code null} if {@code this} is not a vector register or no lane sizes have been set.
        """
        ...

    def getLeastSignificantBit(self) -> int:
        """
        Returns the bit offset from the register address for this register.
        @return the bit offset from the register address for this register.
        """
        ...

    def getLeastSignificatBitInBaseRegister(self) -> int: ...

    def getMinimumByteSize(self) -> int:
        """
        Returns the minimum number of bytes required to store a value for this Register.
        """
        ...

    def getName(self) -> unicode:
        """
        Gets the name of this Register.
        @return the name of this Register.
        """
        ...

    def getOffset(self) -> int:
        """
        Returns the offset into the register space for this register
        """
        ...

    def getParentRegister(self) -> ghidra.program.model.lang.Register: ...

    def getTypeFlags(self) -> int: ...

    def hasChildren(self) -> bool: ...

    def hashCode(self) -> int:
        """
        @see java.lang.Object#hashCode()
        """
        ...

    def isBaseRegister(self) -> bool: ...

    def isBigEndian(self) -> bool: ...

    def isDefaultFramePointer(self) -> bool:
        """
        Returns true if this is the default frame pointer register
        """
        ...

    def isHidden(self) -> bool:
        """
        Returns true if this is a hidden register.
        """
        ...

    def isProcessorContext(self) -> bool:
        """
        Returns true if this is a processor state register
        """
        ...

    def isProgramCounter(self) -> bool:
        """
        Returns true if this is the program counter register
        """
        ...

    def isValidLaneSize(self, laneSizeInBytes: int) -> bool:
        """
        Determines whether {@code laneSizeInBytes} is a valid lane size for this register.
        @param laneSizeInBytes lane size to check, measured in bytes
        @return true precisely when {@code this} is a vector register and {@code laneSizeInBytes} is a valid lane size.
        """
        ...

    def isVectorRegister(self) -> bool:
        """
        Returns true if this is a vector register
        @return true precisely when {@code this} is a full vector register (i.e., a register that can be
         used as input or output for a SIMD operation).
        """
        ...

    def isZero(self) -> bool:
        """
        Returns true for a register that is always zero
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode:
        """
        @see java.lang.Object#toString()
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
