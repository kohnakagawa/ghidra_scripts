import ghidra.program.model.address
import java.lang


class Address(java.lang.Comparable, object):
    """
    An address represents a location in a program.  Conceptually, addresses consist
     of an "address space" and an offset within that space.  Many processors have only
     one "real" address space, but some have several spaces. Also, there are
     "artificial" address spaces used for analysis and representing other non-memory locations
     such as a register or an offset on the stack relative to a functions frame pointer.
    """

    EXT_FROM_ADDRESS: ghidra.program.model.address.Address = Entry Point
    NO_ADDRESS: ghidra.program.model.address.Address = NO ADDRESS
    SEPARATOR_CHAR: int = ':'







    def add(self, displacement: long) -> ghidra.program.model.address.Address:
        """
        Creates a new address (possibly in a new space) by adding the displacement to
         this address.
        @param displacement the amount to add to this offset.
        @return The new address.
        @throws AddressOutOfBoundsException if wrapping is not supported by the
         corresponding address space and the addition causes an out-of-bounds
         error
        """
        ...

    @overload
    def addNoWrap(self, displacement: long) -> ghidra.program.model.address.Address:
        """
        Creates a new Address with a displacement relative to this
          Address.  The Address will not wrap around!  An exception will be
         throw if the result is not within this address space.
        @param displacement the displacement to add.
        @return The new Address
        @throws AddressOverflowException if the offset in this Address would
          overflow (wrap around) due to this operation.
        """
        ...

    @overload
    def addNoWrap(self, displacement: long) -> ghidra.program.model.address.Address:
        """
        Creates a new Address with a displacement relative to this
          Address.  The Address will not wrap around!  An exception will be
         throw if the result is not within this address space.
        @param displacement the displacement to add.
        @return The new Address
        @throws AddressOverflowException if the offset in this Address would
          overflow (wrap around) due to this operation.
        """
        ...

    def addWrap(self, displacement: long) -> ghidra.program.model.address.Address:
        """
        Creates a new address by adding the displacement to the current
         address. The new address will wrap in a manner that depends on the
         address space. For a generic address space this will wrap at the
         extents of the address space. For a segmented address space it will
         wrap at the extents of the segment.
        @param displacement the displacement to add.
        @return The new Address formed by adding the displacement to this address's offset.
        """
        ...

    def addWrapSpace(self, displacement: long) -> ghidra.program.model.address.Address:
        """
        Creates a new address by adding the displacement to the current
         address. If the offset is greater than the max offset of the address space, the high
         order bits are masked off, making the address wrap.  For non-segmented addresses this
         will be the same as addWrap().  For segmented addresses, the address will wrap when
         the 20 bit (oxfffff) offset is exceeded, as opposed to when the segment offset is exceeded.
        @param displacement the displacement to add.
        @return The new Address formed by adding the displacement to this address's offset.
        """
        ...

    def compareTo(self, __a0: object) -> int: ...

    def equals(self, o: object) -> bool:
        """
        Compares this Address to the specified object.
         The result is <code>true</code> if and only if the argument is not
         <code>null</code> and is a <code>Address</code> object that represents
         the same address as this object.
        @param o the object to compare this <code>String</code>
                      against.
        @return <code>true</code> if the <code>Addresses</code>are equal;
                  <code>false</code> otherwise.
        """
        ...

    def getAddress(self, addrString: unicode) -> ghidra.program.model.address.Address:
        """
        Creates a new Address by parsing a String representation of an address. The
         string may be either a simple number (just the offset part of an address) or take
         the form "addressSpaceName:offset".  If the latter form is used, the
         "addressSpaceName" must match the name of the space for this address.
        @param addrString the String to parse.
        @return the new Address if the string is a legally formed address or null
         if the string contains an address space name that does not match this address's space.
        @throws AddressFormatException if the string cannot be parsed or the
         parsed offset is larger than the size for this address' space.
        """
        ...

    def getAddressSpace(self) -> ghidra.program.model.address.AddressSpace:
        """
        Returns the address space associated with this address.
        """
        ...

    def getAddressableWordOffset(self) -> long:
        """
        Get the addressable memory word offset which corresponds to this address.
        @return addressable memory word offset
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getNewAddress(self, byteOffset: long) -> ghidra.program.model.address.Address:
        """
        Creates a new Address in this address's space with the given byte offset.
        @param byteOffset the byte offset for the new address.
        @return the new Address.
        @throws AddressOutOfBoundsException if the offset is less than the minimum offset or
         greater than the max offset allowed for this space.
        """
        ...

    @overload
    def getNewAddress(self, offset: long, isAddressableWordOffset: bool) -> ghidra.program.model.address.Address:
        """
        Returns a new address in this address's space with the given offset.
         NOTE: for those spaces with an addressable unit size other than 1, the address
         returned may not correspond to an addressable unit/word boundary if a byte-offset
         is specified.
        @param offset the offset for the new address.
        @param isAddressableWordOffset if true the specified offset is an addressable unit/word offset,
         otherwise offset is a byte offset.  See {@link ghidra.program.model.address.AddressSpace#getAddressableUnitSize() AddressSpace#getAddressableUnitSize()} to understand the distinction
         (i.e., wordOffset = byteOffset * addressableUnitSize).
        @return address with given offset
        @throws AddressOutOfBoundsException if the offset is less than 0 or greater
         than the max offset allowed for this space.
        """
        ...

    def getNewTruncatedAddress(self, offset: long, isAddressableWordOffset: bool) -> ghidra.program.model.address.Address:
        """
        Returns a new address in this address's space with the given offset.  The specified
         offset will be truncated within the space and will not throw an exception.
         NOTE: for those spaces with an addressable unit size other than 1, the address
         returned may not correspond to a word boundary (addressable unit) if a byte-offset
         is specified.
        @param offset the offset for the new address.
        @param isAddressableWordOffset if true the specified offset is an addressable unit/word offset,
         otherwise offset is a byte offset.  See {@link ghidra.program.model.address.AddressSpace#getAddressableUnitSize() AddressSpace#getAddressableUnitSize()} to understand the distinction
         (i.e., wordOffset = byteOffset * addressableUnitSize).
        @return address with given byte offset truncated to the physical space size
        """
        ...

    def getOffset(self) -> long:
        """
        Get the offset of this Address.
        @return the offset of this Address.
        """
        ...

    def getOffsetAsBigInteger(self) -> long:
        """
        Get the offset of this Address as a BigInteger
        @return the offset of this Address.
        """
        ...

    def getPhysicalAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the physical Address that corresponds to this Address.
        @return address in a physical space corresponding to this
         address.
        """
        ...

    def getPointerSize(self) -> int:
        """
        Returns the number of bytes needed to form a pointer to this address.  The
         result will be one of {1,2,4,8}.
        @see DataOrganization#getPointerSize() for compiler-specific size of pointers stored in memory.
        """
        ...

    def getSize(self) -> int:
        """
        Returns the number of bits that are used to form the address.  Thus
         the maximum offset for this address space will be 2^size-1.
        """
        ...

    def getUnsignedOffset(self) -> long:
        """
        Get the address offset as an unsigned number.
         This may be useful when dealing with signed spaces (e.g. stack)
        @return unsigned address offset
        """
        ...

    def hasSameAddressSpace(self, addr: ghidra.program.model.address.Address) -> bool:
        """
        Return true if this address' address space is equal to the
         address space for addr.
        """
        ...

    def hashCode(self) -> int:
        """
        Returns a hashcode for this Address. The hashcode for an
         <code>Address</code> should be a value such that two Address
         objects which are equal will return the same hashcode.
         This method should generally return the same value as getLong().
        @return a hash code value for this object.
        """
        ...

    def isConstantAddress(self) -> bool:
        """
        Returns true if this address represents a location in constant space
        """
        ...

    def isExternalAddress(self) -> bool:
        """
        Returns true if this address represents an external location in the external address space
        """
        ...

    def isHashAddress(self) -> bool:
        """
        Returns true if this address represents a location in the HASH space
        """
        ...

    def isLoadedMemoryAddress(self) -> bool:
        """
        Returns true if this address represents an address in a loaded memory block
        """
        ...

    def isMemoryAddress(self) -> bool:
        """
        Returns true if this address represents a location in memory
        """
        ...

    def isNonLoadedMemoryAddress(self) -> bool:
        """
        Returns true if this address represents an address not loaded in real memory (i.e. OTHER)
        """
        ...

    def isRegisterAddress(self) -> bool:
        """
        Returns true if this address represents a location in register space.
        @deprecated use of this method is highly discouraged since since registers
         may also exist in a memory space. The address for such registers
         would return false from this method.
        """
        ...

    def isStackAddress(self) -> bool:
        """
        Returns true if this address represents a location in stack space
        """
        ...

    def isSuccessor(self, addr: ghidra.program.model.address.Address) -> bool:
        """
        Tests whether the given address immediately follows this address.
        @param addr the address to test.
        """
        ...

    def isUniqueAddress(self) -> bool:
        """
        Returns true if this address represents a location in unique space
        """
        ...

    def isVariableAddress(self) -> bool:
        """
        Returns true if this address represents a location in variable space
        """
        ...

    @staticmethod
    def max(a: ghidra.program.model.address.Address, b: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address:
        """
        Return the maximum of two addresses using Address.compareTo
        @param a first address
        @param b second address
        @return maximum of two addresses
        """
        ...

    @staticmethod
    def min(a: ghidra.program.model.address.Address, b: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address:
        """
        Return the minimum of two addresses using Address.compareTo
        @param a first address
        @param b second address
        @return minimum of two addresses
        """
        ...

    def next(self) -> ghidra.program.model.address.Address:
        """
        Returns the address's successor.  In most cases, this is equivalent
         to addr.add(1), but segmented addresses could span segments.  The result
         of calling this on the highest address will result in a null return value.
        @return the next higher address, or null if already at the
         highest address.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def previous(self) -> ghidra.program.model.address.Address:
        """
        Returns the address's predecessor.  In most cases, this is equivalent to
         addr.subtract(1), but segmented addresses could span segments.  The
         result of calling this on the lowest address will result in a null return value.
        @return the next lower address, or null if already at the
          lowest address.
        """
        ...

    @overload
    def subtract(self, displacement: long) -> ghidra.program.model.address.Address:
        """
        Creates a new address (possibly in a new space) by subtracting the displacement to
         this address.
        @param displacement the amount to subtract from this offset.
        @return The address using the subtracted offset.
        """
        ...

    @overload
    def subtract(self, addr: ghidra.program.model.address.Address) -> long:
        """
        Calculates the displacement between two addresses (<code>this - addr</code>)
        @param addr the Address to subtract from <code>this</code> address
        @return the difference (thisAddress.offset - thatAddress.offset)
        @throws IllegalArgumentException if the two addresses are not in the same address space
        """
        ...

    def subtractNoWrap(self, displacement: long) -> ghidra.program.model.address.Address:
        """
        Creates a new Address by subtracting displacement from the
         Address.  The Address will not wrap within the space and in fact will throw
         an exception if the result is less than the min address in this space or
         greater than the max address in this space.
        @param displacement the displacement to subtract.
        @return The new Address
        @throws AddressOverflowException if the offset in this Address would
          overflow due to this operation.
        """
        ...

    def subtractWrap(self, displacement: long) -> ghidra.program.model.address.Address:
        """
        Creates a new address by subtracting the displacement from the current
         address. The new address will wrap in a manner that depends on the
         address space. For a generic address space this will wrap at the
         extents of the address space. For a segmented address space it will
         wrap at the extents of the segment.
        @param displacement the displacement to subtract.
        @return The new Address formed by subtracting the displacement for the offset.
        """
        ...

    def subtractWrapSpace(self, displacement: long) -> ghidra.program.model.address.Address:
        """
        Creates a new address by subtracting the displacement from the current
         address. If the offset is greater than the max offset of the address space, the high
         order bits are masked off, making the address wrap.  For non-segmented addresses this
         will be the same as subtractWrap().  For segmented addresses, the address will wrap when
         the 20 bit (oxfffff) offset is exceeded, as opposed to when the segment offset is exceeded.
        @param displacement the displacement to add.
        @return The new Address formed by subtracting the displacement from this address's offset.
        """
        ...

    @overload
    def toString(self) -> unicode:
        """
        Returns a String representation of the address in hex and padded
         to the appropriate size.
        """
        ...

    @overload
    def toString(self, showAddressSpace: bool) -> unicode:
        """
        Returns a String representation that may include the address space name
        @param showAddressSpace true if the address space should be included in
         resulting string.
        @return String the string representation of the address
        """
        ...

    @overload
    def toString(self, prefix: unicode) -> unicode:
        """
        Returns a String representation of the address using the
         given string as a prefix.  Equivalent of prefix + ":" + toString(false)
        @param prefix the string to prepend to the address string.
        """
        ...

    @overload
    def toString(self, showAddressSpace: bool, minNumDigits: int) -> unicode:
        """
        Returns a String representation that may include the address space name and may or may
         not pad the address with leading zeros.
        @param showAddressSpace if true, the addressSpace name will be prepended to the address string.
        @param minNumDigits specifies the minimum number of digits to use.  If the address space size
         is less that minNumDigits, the address will be padded to the address space size.  If the address
         space size is larger that minNumDigits, the address will be displayed with as many digits as
         necessary, but will contain leading zeros to make the address string have at least minNumDigits.
        @return the address as a String.
        """
        ...

    @overload
    def toString(self, showAddressSpace: bool, pad: bool) -> unicode:
        """
        Returns a String representation that may include the address space name and may or may
         not pad the address with leading zeros.
        @param showAddressSpace if true, the addressSpace name will be prepended to the address string.
        @param pad if true, the address will be prepended with leading zeros to completely fill out
         the max digits the address could contain.  If false, the address will be prepended only to make
         the number of hex digits at least 4.
        @return the address as a String.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addressSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    @property
    def addressableWordOffset(self) -> long: ...

    @property
    def constantAddress(self) -> bool: ...

    @property
    def externalAddress(self) -> bool: ...

    @property
    def hashAddress(self) -> bool: ...

    @property
    def loadedMemoryAddress(self) -> bool: ...

    @property
    def memoryAddress(self) -> bool: ...

    @property
    def nonLoadedMemoryAddress(self) -> bool: ...

    @property
    def offset(self) -> long: ...

    @property
    def offsetAsBigInteger(self) -> long: ...

    @property
    def physicalAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def pointerSize(self) -> int: ...

    @property
    def registerAddress(self) -> bool: ...

    @property
    def size(self) -> int: ...

    @property
    def stackAddress(self) -> bool: ...

    @property
    def uniqueAddress(self) -> bool: ...

    @property
    def unsignedOffset(self) -> long: ...

    @property
    def variableAddress(self) -> bool: ...
