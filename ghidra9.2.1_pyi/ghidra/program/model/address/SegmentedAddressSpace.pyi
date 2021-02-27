import ghidra.program.model.address
import java.lang


class SegmentedAddressSpace(ghidra.program.model.address.GenericAddressSpace):
    """
    Address Space for dealing with (intel) segmented address spaces.
     It understands the mapping between the segmented encoding (seg:offset) and
     the flat address encoding necessary to produce an Address object that can be
     used by other analyses.  This mapping is inherent in protected methods:
       - getDefaultOffsetFromFlat
       - getDefaultSegmentFromFlat
       - getFlatOffset
       - getOffsetFromFlat
       - getAddressInSegment

     These 5 methods can be overridden to get a different mapping. This base class is
     set up to map as for x86 16-bit real-mode.
    """





    def __init__(self, name: unicode, unique: int):
        """
        Constructs a new Segmented AddressSpace for x86 real-mode, with 21-bit addresses.
        @param name is the name of the space
        @param unique is the unique id for the space.
        """
        ...



    def add(self, addr: ghidra.program.model.address.Address, displacement: long) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.address.AddressSpace#add(ghidra.program.model.address.Address,
              long)
        """
        ...

    @overload
    def addNoWrap(self, addr: ghidra.program.model.address.Address, displacement: long) -> ghidra.program.model.address.Address: ...

    @overload
    def addNoWrap(self, addr: ghidra.program.model.address.GenericAddress, displacement: long) -> ghidra.program.model.address.Address: ...

    def addWrap(self, addr: ghidra.program.model.address.Address, displacement: long) -> ghidra.program.model.address.Address: ...

    def addWrapSpace(self, addr: ghidra.program.model.address.Address, displacement: long) -> ghidra.program.model.address.Address: ...

    @overload
    def compareTo(self, space: ghidra.program.model.address.AddressSpace) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool: ...

    @overload
    def getAddress(self, byteOffset: long) -> ghidra.program.model.address.SegmentedAddress:
        """
        @see ghidra.program.model.address.AddressSpace#getAddress(long)
        """
        ...

    @overload
    def getAddress(self, addrString: unicode) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.address.AddressSpace#getAddress(java.lang.String)
        """
        ...

    @overload
    def getAddress(self, segment: int, segmentOffset: int) -> ghidra.program.model.address.SegmentedAddress:
        """
        Generates a segmented address with the given segment, offset, and overlay id.
        @param segment the segment
        @param segmentOffset the offset in the segment
        @return SegmentedAddress the newly created segmented address.
        """
        ...

    @overload
    def getAddress(self, offset: long, isAddressableWordOffset: bool) -> ghidra.program.model.address.Address: ...

    @overload
    def getAddress(self, addrString: unicode, caseSensitive: bool) -> ghidra.program.model.address.Address: ...

    def getAddressInThisSpaceOnly(self, byteOffset: long) -> ghidra.program.model.address.SegmentedAddress:
        """
        @see ghidra.program.model.address.AddressSpace#getAddressInThisSpaceOnly(long)
        """
        ...

    def getAddressableUnitSize(self) -> int: ...

    def getAddressableWordOffset(self, byteOffset: long) -> long: ...

    def getClass(self) -> java.lang.Class: ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address: ...

    def getMinAddress(self) -> ghidra.program.model.address.Address: ...

    def getName(self) -> unicode: ...

    def getNextOpenSegment(self, addr: ghidra.program.model.address.Address) -> int:
        """
        Get the segment index for the first segment whose start address
         comes after the given address
        @param addr is the given address
        @return the segment index
        """
        ...

    def getOverlayAddress(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address:
        """
        No overlay translation necessary, this is a base addressSpace.

          (non-Javadoc)
        @see ghidra.program.model.address.AddressSpace#getOverlayAddress(ghidra.program.model.address.Address)
        """
        ...

    def getPhysicalSpace(self) -> ghidra.program.model.address.SegmentedAddressSpace:
        """
        @see ghidra.program.model.address.AddressSpace#getPhysicalSpace()
        """
        ...

    def getPointerSize(self) -> int:
        """
        @see ghidra.program.model.address.AddressSpace#getPointerSize()
        """
        ...

    def getSize(self) -> int: ...

    def getSpaceID(self) -> int: ...

    def getTruncatedAddress(self, offset: long, isAddressableWordOffset: bool) -> ghidra.program.model.address.Address: ...

    def getType(self) -> int: ...

    def getUnique(self) -> int:
        """
        Returns the unique id value for this space.
        """
        ...

    def hasMappedRegisters(self) -> bool: ...

    def hasSignedOffset(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isConstantSpace(self) -> bool: ...

    def isExternalSpace(self) -> bool: ...

    def isHashSpace(self) -> bool: ...

    def isLoadedMemorySpace(self) -> bool: ...

    def isMemorySpace(self) -> bool: ...

    def isNonLoadedMemorySpace(self) -> bool: ...

    def isOverlaySpace(self) -> bool: ...

    def isRegisterSpace(self) -> bool: ...

    def isStackSpace(self) -> bool: ...

    def isSuccessor(self, addr1: ghidra.program.model.address.Address, addr2: ghidra.program.model.address.Address) -> bool: ...

    def isUniqueSpace(self) -> bool: ...

    def isValidRange(self, byteOffset: long, length: long) -> bool: ...

    def isVariableSpace(self) -> bool: ...

    def makeValidOffset(self, offset: long) -> long: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setHasMappedRegisters(self, hasRegisters: bool) -> None:
        """
        Tag this memory space as having memory mapped registers
        @param hasRegisters true if it has registers, false otherwise
        """
        ...

    def setShowSpaceName(self, b: bool) -> None: ...

    def showSpaceName(self) -> bool: ...

    @overload
    def subtract(self, addr: ghidra.program.model.address.Address, displacement: long) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.address.AddressSpace#subtract(ghidra.program.model.address.Address,
              long)
        """
        ...

    @overload
    def subtract(self, addr1: ghidra.program.model.address.Address, addr2: ghidra.program.model.address.Address) -> long: ...

    def subtractNoWrap(self, addr: ghidra.program.model.address.Address, displacement: long) -> ghidra.program.model.address.Address: ...

    def subtractWrap(self, addr: ghidra.program.model.address.Address, displacement: long) -> ghidra.program.model.address.Address: ...

    def subtractWrapSpace(self, addr: ghidra.program.model.address.Address, displacement: long) -> ghidra.program.model.address.Address: ...

    def toString(self) -> unicode: ...

    def truncateAddressableWordOffset(self, wordOffset: long) -> long: ...

    def truncateOffset(self, offset: long) -> long: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def physicalSpace(self) -> ghidra.program.model.address.SegmentedAddressSpace: ...

    @property
    def pointerSize(self) -> int: ...
