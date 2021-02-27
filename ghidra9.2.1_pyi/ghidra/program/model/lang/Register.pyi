from typing import List
import ghidra.program.model.address
import ghidra.program.model.lang
import java.io
import java.lang


class Register(object, java.io.Serializable, java.lang.Comparable):
    """
    Class to represent a processor register.  To sort of handle bit registers, a
     special addressing convention is used.  First the upper bit is set.  Second, the
     next 3 bits are used to specify what bit position within a byte that this register
     bit exists at.  Finally, the rest of the address is the address of the byte where
     the register bit lives.
    """

    TYPE_CONTEXT: int = 8
    TYPE_DOES_NOT_FOLLOW_FLOW: int = 64
    TYPE_FP: int = 1
    TYPE_HIDDEN: int = 32
    TYPE_NONE: int = 0
    TYPE_PC: int = 4
    TYPE_SP: int = 2
    TYPE_VECTOR: int = 128
    TYPE_ZERO: int = 16



    @overload
    def __init__(self, register: ghidra.program.model.lang.Register): ...

    @overload
    def __init__(self, name: unicode, description: unicode, address: ghidra.program.model.address.Address, numBytes: int, bigEndian: bool, typeFlags: int):
        """
        Constructs a new Register object.
        @param name the name of this Register.
        @param description the description of this Register
        @param address the address in register space of this register
        @param numBytes the size (in bytes) of this register
        @param bigEndian true if the most significant bytes are associated with the lowest register
         addresses, and false if the least significant bytes are associated with the lowest register
         addresses.
        @param typeFlags the type(s) of this Register  (TYPE_NONE, TYPE_FP, TYPE_SP,
         	TYPE_PC, TYPE_CONTEXT, TYPE_ZERO);)
        """
        ...

    @overload
    def __init__(self, name: unicode, description: unicode, address: ghidra.program.model.address.Address, numBytes: int, leastSignificantBit: int, bitLength: int, bigEndian: bool, typeFlags: int): ...



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

    @property
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def addressSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    @property
    def aliases(self) -> java.lang.Iterable: ...

    @property
    def baseMask(self) -> List[int]: ...

    @property
    def baseRegister(self) -> bool: ...

    @property
    def bigEndian(self) -> bool: ...

    @property
    def bitLength(self) -> int: ...

    @property
    def childRegisters(self) -> List[object]: ...

    @property
    def defaultFramePointer(self) -> bool: ...

    @property
    def description(self) -> unicode: ...

    @property
    def group(self) -> unicode: ...

    @property
    def hidden(self) -> bool: ...

    @property
    def laneSizes(self) -> List[int]: ...

    @property
    def leastSignificantBit(self) -> int: ...

    @property
    def leastSignificatBitInBaseRegister(self) -> int: ...

    @property
    def minimumByteSize(self) -> int: ...

    @property
    def name(self) -> unicode: ...

    @property
    def offset(self) -> int: ...

    @property
    def parentRegister(self) -> ghidra.program.model.lang.Register: ...

    @property
    def processorContext(self) -> bool: ...

    @property
    def programCounter(self) -> bool: ...

    @property
    def typeFlags(self) -> int: ...

    @property
    def vectorRegister(self) -> bool: ...

    @property
    def zero(self) -> bool: ...
