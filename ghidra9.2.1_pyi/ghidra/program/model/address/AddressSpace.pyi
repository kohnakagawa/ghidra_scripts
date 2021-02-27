import ghidra.program.model.address
import java.lang


class AddressSpace(java.lang.Comparable, object):
    """
    The AddressSpace class is used to represent a unique context for addresses.  Programs can
     have multiple address spaces and address 0 in one space is not the same as address 0 in
     another space.
    """

    DEFAULT_REGISTER_SPACE: ghidra.program.model.address.AddressSpace = REGISTER:
    EXTERNAL_SPACE: ghidra.program.model.address.AddressSpace = EXTERNAL:
    HASH_SPACE: ghidra.program.model.address.AddressSpace = HASH:
    ID_SIZE_MASK: int = 112
    ID_SIZE_SHIFT: int = 4
    ID_TYPE_MASK: int = 15
    ID_UNIQUE_SHIFT: int = 7
    OTHER_SPACE: ghidra.program.model.address.AddressSpace = OTHER:
    TYPE_CODE: int = 2
    TYPE_CONSTANT: int = 0
    TYPE_DELETED: int = 13
    TYPE_EXTERNAL: int = 10
    TYPE_IPTR_CONSTANT: int = 0
    TYPE_IPTR_INTERNAL: int = 3
    TYPE_IPTR_SPACEBASE: int = 5
    TYPE_JOIN: int = 6
    TYPE_NONE: int = 15
    TYPE_OTHER: int = 7
    TYPE_RAM: int = 1
    TYPE_REGISTER: int = 4
    TYPE_STACK: int = 5
    TYPE_SYMBOL: int = 9
    TYPE_UNIQUE: int = 3
    TYPE_UNKNOWN: int = 14
    TYPE_VARIABLE: int = 11
    VARIABLE_SPACE: ghidra.program.model.address.AddressSpace = VARIABLE:







    def add(self, addr: ghidra.program.model.address.Address, displacement: long) -> ghidra.program.model.address.Address:
        """
        Creates a new address (possibly in a new space) by adding the given
         displacement from the given address.
        @param addr original address being subtracted from
        @param displacement amount to subtract
        @return the new address
        @throws AddressOutOfBoundsException if the result does not correspond to any address.
        """
        ...

    @overload
    def addNoWrap(self, addr: ghidra.program.model.address.Address, displacement: long) -> ghidra.program.model.address.Address:
        """
        Creates a new address by adding displacement to the given address. The
         new address will NOT wrap!
        @param addr the original address.
        @param displacement the displacement to add.
        @return The new address created by adding displacement to addr.offset.
        @throws AddressOverflowException if the addition would cause a wrap,
        """
        ...

    @overload
    def addNoWrap(self, addr: ghidra.program.model.address.GenericAddress, displacement: long) -> ghidra.program.model.address.Address:
        """
        Creates a new address by adding displacement to the given address. The
         new address will NOT wrap!
        @param addr the original address.
        @param displacement the displacement to add.
        @return The new address created by adding displacement to addr.offset.
        @throws AddressOverflowException if the addition would cause a wrap,
        """
        ...

    def addWrap(self, addr: ghidra.program.model.address.Address, displacement: long) -> ghidra.program.model.address.Address:
        """
        Creates a new address by adding displacement to the given address. The
         resulting address may wrap. The new address will wrap in a manner that
         depends on the address space. For a generic address space this will wrap
         at the extents of the address space. For a segmented address space it
         will wrap at the extents of the segment.
        @param addr the original address.
        @param displacement the displacement to add.
        @return the new address created by adding displacement to addr.offset.
        """
        ...

    def addWrapSpace(self, addr: ghidra.program.model.address.Address, displacement: long) -> ghidra.program.model.address.Address:
        """
        Creates a new address by adding the displacement to the given
         address. If the offset is greater than the max offset of the address space, the high
         order bits are masked off, making the address wrap.  For non-segmented addresses this
         will be the same as addWrap().  For segmented addresses, the address will wrap when
         the 20 bit (oxfffff) offset is exceeded, as opposed to when the segment offset is exceeded.
        @param addr the address to add the displacement to.
        @param displacement the displacement to add.
        @return The new Address formed by adding the displacement to the specified addresst.
        """
        ...

    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    def getAddress(self, byteOffset: long) -> ghidra.program.model.address.Address:
        """
        Returns a new address in this space with the given byte offset.
         NOTE: This method is the same as invoking getAddress(long byteOffset, false).
        @param byteOffset the byte offset for the new address.
        @return address with given byte offset
        @throws AddressOutOfBoundsException if the offset is less than 0 or greater
         than the max offset allowed for this space.
        """
        ...

    @overload
    def getAddress(self, addrString: unicode) -> ghidra.program.model.address.Address:
        """
        Parses the String into an address.
        @param addrString the string to parse as an address.
        @return an address if the string parsed successfully or null if the
         AddressSpace specified in the addrString is not this space.
        @throws AddressFormatException if the string cannot be parsed or the
         parsed offset is larger than the size for this space.
        """
        ...

    @overload
    def getAddress(self, offset: long, isAddressableWordOffset: bool) -> ghidra.program.model.address.Address:
        """
        Returns a new address in this space with the given offset.
         NOTE: for those spaces with an addressable unit size other than 1, the address
         returned may not correspond to an addressable unit/word boundary if a byte-offset
         is specified.
        @param offset the offset for the new address.
        @param isAddressableWordOffset if true the specified offset is an addressable unit/word offset,
         otherwise offset is a byte offset.  See {@link #getAddressableUnitSize()}
         to understand the distinction (i.e., wordOffset = byteOffset * addressableUnitSize).
        @return address with given offset
        @throws AddressOutOfBoundsException if the offset is less than 0 or greater
         than the max offset allowed for this space.
        """
        ...

    @overload
    def getAddress(self, addrString: unicode, caseSensitive: bool) -> ghidra.program.model.address.Address:
        """
        Parses the String into an address.
        @param addrString the string to parse as an address.
        @param caseSensitive specifies if addressSpace names must match case.
        @return an address if the string parsed successfully or null if the
         AddressSpace specified in the addrString is not this space.
        @throws AddressFormatException if the string cannot be parsed or the
         parsed offset is larger than the size for this space.
        """
        ...

    def getAddressInThisSpaceOnly(self, byteOffset: long) -> ghidra.program.model.address.Address:
        """
        Get a byte address from this address space.  Don't allow overlay spaces
         to remap the address into a base space when the address is not
         contained in the bounds of the overlay region.
        @param byteOffset the byte offset for the new address.
        @return an address if the offset is valid.
        @throws AddressOutOfBoundsException if the offset is less than 0 or greater
         than the max offset allowed for this space.
        """
        ...

    def getAddressableUnitSize(self) -> int:
        """
        Returns the number of data bytes which correspond to each addressable
         location within this space (i.e., word-size in bytes).
         NOTE: When transforming a byte-offset to an addressable word
         offset the method {@link #getAddressableWordOffset(long)} should
         be used instead of simple division.  When transforming an addressable word-offset
         to a byte-offset simple multiplication may be used.  Neither of these
         transformations perform address space bounds checking.
         <pre>
           byteOffset = wordOffset * addressUnitSize
           wordOffset = getAddressableWordOffset(byteOffset)
         </pre>
        """
        ...

    def getAddressableWordOffset(self, byteOffset: long) -> long:
        """
        Get the addressable memory word offset which corresponds to the specified
         memory byte offset.  This method handles some of the issues of unsigned
         math when stuck using Java's signed long primitives. No space bounds
         checking is performed.
        @param byteOffset memory byte offset
        @return addressable memory word offset
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address:
        """
        Get the max address allowed for this AddressSpace.
        """
        ...

    def getMinAddress(self) -> ghidra.program.model.address.Address:
        """
        Get the min address allowed for this AddressSpace
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of this address space.
        """
        ...

    def getOverlayAddress(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address:
        """
        Get an address that is relative to this address space.
         If this is an overlay space and the address falls within
         this space, return an address based in this space.
        @param addr address possibly falling within this overlay space.
        @return an address relative to this overlay
        """
        ...

    def getPhysicalSpace(self) -> ghidra.program.model.address.AddressSpace:
        """
        Returns the physical space associated with an address space.  There
         is always exactly one physical space associated with an address
         space (it may be its own physical space).
        @return the associated physical space.
        """
        ...

    def getPointerSize(self) -> int:
        """
        Returns the absolute size of a pointer into this space (in bytes).
        @see Program#getDefaultPointerSize() for a user adjustable pointer size which is derived from the
         CompilerSpec store pointer size.
        """
        ...

    def getSize(self) -> int:
        """
        Returns the number of bits that are used to form the address.  Thus
         the maximum offset for this address space will be 2^size-1.
        """
        ...

    def getSpaceID(self) -> int:
        """
        Get the ID for this space
        @return space ID
        """
        ...

    def getTruncatedAddress(self, offset: long, isAddressableWordOffset: bool) -> ghidra.program.model.address.Address:
        """
        Returns a new address in this space with the given offset.  The specified
         offset will be truncated within the space and will not throw an exception.
         NOTE: for those spaces with an addressable unit size other than 1, the address
         returned may not correspond to a word boundary (addressable unit) if a byte-offset
         is specified.
        @param offset the offset for the new address.
        @param isAddressableWordOffset if true the specified offset is an addressable unit/word offset,
         otherwise offset is a byte offset.  See {@link #getAddressableUnitSize()}
         to understand the distinction (i.e., wordOffset = byteOffset * addressableUnitSize).
        @return address with given byte offset truncated to the physical space size
        """
        ...

    def getType(self) -> int:
        """
        Returns the type of this address space
        """
        ...

    def getUnique(self) -> int:
        """
        Returns the unique index for this address space
        """
        ...

    def hasMappedRegisters(self) -> bool:
        """
        Returns true if this space has registers that are mapped into it.
         This means that registers could actually have pointers to them.
        @return true if this space has any registers mapped in it.
        """
        ...

    def hasSignedOffset(self) -> bool:
        """
        Returns true if space uses signed offset
        """
        ...

    def hashCode(self) -> int: ...

    def isConstantSpace(self) -> bool:
        """
        Returns true if this space in the constant space
        """
        ...

    def isExternalSpace(self) -> bool:
        """
        Returns true if this space in the EXTERNAL_SPACE
        """
        ...

    def isHashSpace(self) -> bool:
        """
        Returns true if this space represents a location in the HASH space.
        """
        ...

    def isLoadedMemorySpace(self) -> bool:
        """
        Returns true if this space represents represents a Loaded Memory
         region (e.g., processor RAM).
        """
        ...

    def isMemorySpace(self) -> bool:
        """
        Returns true if this space represents a memory address.  NOTE: It is important to
         make the distinction between Loaded and Non-Loaded memory addresses.  Program importers
         may create memory blocks associated with Non-Loaded file content which are not associated
         with processor defined memory regions.  While Loaded file content is placed into
         memory blocks which are associated with specific memory address spaces defined
         by the processor language specification.
        @see #isLoadedMemorySpace()
        @see #isNonLoadedMemorySpace()
        """
        ...

    def isNonLoadedMemorySpace(self) -> bool:
        """
        Returns true if this space represents represents a Non-Loaded storage region
         for retaining non-loaded file data (e.g., OTHER)
        """
        ...

    def isOverlaySpace(self) -> bool:
        """
        Returns true if this addressSpace is an OverlayAddressSpace
        """
        ...

    def isRegisterSpace(self) -> bool:
        """
        Returns true if this space represents a register location
        """
        ...

    def isStackSpace(self) -> bool:
        """
        Returns true if this space represents a stack location
        """
        ...

    def isSuccessor(self, addr1: ghidra.program.model.address.Address, addr2: ghidra.program.model.address.Address) -> bool:
        """
        Tests whether addr2 immediately follows addr1.
        @param addr1 the first address.
        @param addr2 the second address.
        """
        ...

    def isUniqueSpace(self) -> bool:
        """
        Returns true if this space in the unique space
        """
        ...

    def isValidRange(self, byteOffset: long, length: long) -> bool:
        """
        Check the specified address range for validity within this space.
         Segmented spaces will restrict a range to a single segment.
        @param byteOffset
        @param length
        @return true if range is valid for this space
        """
        ...

    def isVariableSpace(self) -> bool:
        """
        Returns true if this space represents a variable location
        """
        ...

    def makeValidOffset(self, offset: long) -> long:
        """
        Tests if the offset if valid. If the space is signed, then it sign extends
         the offset.
        @param offset the offset to test and/or sign extend
        @return the valid positive offset or appropriate sign extended offset.
        @throws AddressOutOfBoundsException if offset is invalid
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def showSpaceName(self) -> bool:
        """
        Returns true if the address should display its addressSpace name.
        """
        ...

    @overload
    def subtract(self, addr: ghidra.program.model.address.Address, displacement: long) -> ghidra.program.model.address.Address:
        """
        Creates a new address (possibly in a new space) by subtracting the given
         displacement from the given address.
        @param addr original address being subtracted from
        @param displacement amount to subtract
        @return the new address
        @throws AddressOutOfBoundsException if the result does not correspond to any address.
        """
        ...

    @overload
    def subtract(self, addr1: ghidra.program.model.address.Address, addr2: ghidra.program.model.address.Address) -> long:
        """
        Calculates the displacement between addr1 and addr2 (addr1 - addr2)
        @param addr1 the address to subtract from.
        @param addr2 the address to subtract.
        @return the difference. (<code>addr1.offset - addr2.offset</code>).
        @throws IllegalArgumentException if the two addresses are not in the
         same address space.
        """
        ...

    def subtractNoWrap(self, addr: ghidra.program.model.address.Address, displacement: long) -> ghidra.program.model.address.Address:
        """
        Creates a new address by subtracting displacement from addr's offset.
         The new offset will NOT wrap!
        @param addr the original address
        @param displacement the displacement to subtract.
        @return The new address created by subtracting displacement from addr.offset.
        @throws AddressOverflowException if the subtraction would cause a wrap,
        """
        ...

    def subtractWrap(self, addr: ghidra.program.model.address.Address, displacement: long) -> ghidra.program.model.address.Address:
        """
        Creates a new address by subtracting displacement from addr's offset.
        @param addr the original address. The new address will wrap in a manner
         that depends on the address space. For a generic address space this will
         wrap at the extents of the address space. For a segmented address space
         it will wrap at the extents of the segment.
        @param displacement the displacement to subtract.
        @return a new address created by subtracting the displacement from addr.offset.
        """
        ...

    def subtractWrapSpace(self, addr: ghidra.program.model.address.Address, displacement: long) -> ghidra.program.model.address.Address:
        """
        Creates a new address by subtracting the displacement from the given
         address. If the offset is greater than the max offset of the address space, the high
         order bits are masked off, making the address wrap.  For non-segmented addresses this
         will be the same as subtractWrap().  For segmented addresses, the address will wrap when
         the 20 bit (oxfffff) offset is exceeded, as opposed to when the segment offset is exceeded.
        @param addr the address to subtract the displacement from.
        @param displacement the displacement to subtract.
        @return The new Address formed by subtracting the displacement from the specified address.
        """
        ...

    def toString(self) -> unicode: ...

    def truncateAddressableWordOffset(self, wordOffset: long) -> long:
        """
        Truncate the specified addressable unit/word offset within this space to produce a
         valid offset.
        @param wordOffset any addressable unit/word offset
        @return truncated word offset
        """
        ...

    def truncateOffset(self, byteOffset: long) -> long:
        """
        Truncate the specified byte offset within this space to produce a valid offset.
        @param byteOffset any byte offset
        @return truncated byte offset
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addressableUnitSize(self) -> int: ...

    @property
    def constantSpace(self) -> bool: ...

    @property
    def externalSpace(self) -> bool: ...

    @property
    def hashSpace(self) -> bool: ...

    @property
    def loadedMemorySpace(self) -> bool: ...

    @property
    def maxAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def memorySpace(self) -> bool: ...

    @property
    def minAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def name(self) -> unicode: ...

    @property
    def nonLoadedMemorySpace(self) -> bool: ...

    @property
    def overlaySpace(self) -> bool: ...

    @property
    def physicalSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    @property
    def pointerSize(self) -> int: ...

    @property
    def registerSpace(self) -> bool: ...

    @property
    def size(self) -> int: ...

    @property
    def spaceID(self) -> int: ...

    @property
    def stackSpace(self) -> bool: ...

    @property
    def type(self) -> int: ...

    @property
    def unique(self) -> int: ...

    @property
    def uniqueSpace(self) -> bool: ...

    @property
    def variableSpace(self) -> bool: ...
