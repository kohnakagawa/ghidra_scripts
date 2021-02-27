import ghidra.program.model.address
import java.lang


class OldGenericNamespaceAddress(ghidra.program.model.address.GenericAddress):
    """
    OldGenericNamespaceAddress provides a means of instantiating namespace
     oriented addresses which were previously used for External, Stack and Register addresses.
     This class is needed to facilitate an upgrade since this concept is no longer supported by Address.
    """

    OLD_MAX_NAMESPACE_ID: long = 0xfffffffL
    OLD_MIN_NAMESPACE_ID: long = 0x1L



    def __init__(self, addrSpace: ghidra.program.model.address.AddressSpace, offset: long, namespaceID: long): ...



    def add(self, displacement: long) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.address.Address#add(long)
        """
        ...

    @overload
    def addNoWrap(self, displacement: long) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.address.Address#addNoWrap(long)
        """
        ...

    @overload
    def addNoWrap(self, displacement: long) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.address.Address#addNoWrap(long)
        """
        ...

    def addWrap(self, displacement: long) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.address.Address#addWrap(long)
        """
        ...

    def addWrapSpace(self, displacement: long) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.address.Address#addWrapSpace(long)
        """
        ...

    @overload
    def compareTo(self, a: ghidra.program.model.address.Address) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, o: object) -> bool:
        """
        @see java.lang.Object#equals(java.lang.Object)
        """
        ...

    def getAddress(self, addrString: unicode) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.address.Address#getAddress(java.lang.String)
        """
        ...

    def getAddressSpace(self) -> ghidra.program.model.address.AddressSpace:
        """
        @see ghidra.program.model.address.Address#getAddressSpace()
        """
        ...

    def getAddressableWordOffset(self) -> long: ...

    def getClass(self) -> java.lang.Class: ...

    def getGlobalAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns global address (i.e., GenericAddress) for this address.
        """
        ...

    @staticmethod
    def getMaxAddress(addrSpace: ghidra.program.model.address.AddressSpace, namespaceID: long) -> ghidra.program.model.address.Address:
        """
        Returns maximum namespace address within the specified address space for upgrade iterators.
         For a signed stack space, the negative region is treated as positive for the purpose of
         identifying the maximum address key encoding.
        @param addrSpace address space
        @param namespaceID
        @return maximum address
        """
        ...

    @staticmethod
    def getMinAddress(addrSpace: ghidra.program.model.address.AddressSpace, namespaceID: long) -> ghidra.program.model.address.Address:
        """
        Returns minimum namespace address within the specified address space for upgrade iterators.
         A minimum offset of 0x0 is always assumed.
        @param addrSpace address space
        @param namespaceID
        @return minimum address
        """
        ...

    def getNamespaceID(self) -> long:
        """
        Returns the namespace ID assigned to this address.
         This namespace ID generally corresponds to a Function.
        """
        ...

    @overload
    def getNewAddress(self, byteOffset: long) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.address.Address#getNewAddress(long)
        """
        ...

    @overload
    def getNewAddress(self, addrOffset: long, isAddressableWordOffset: bool) -> ghidra.program.model.address.Address: ...

    def getNewTruncatedAddress(self, addrOffset: long, isAddressableWordOffset: bool) -> ghidra.program.model.address.Address: ...

    def getOffset(self) -> long:
        """
        @see ghidra.program.model.address.Address#getOffset()
        """
        ...

    def getOffsetAsBigInteger(self) -> long: ...

    def getPhysicalAddress(self) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.address.Address#getPhysicalAddress()
        """
        ...

    def getPointerSize(self) -> int:
        """
        @see ghidra.program.model.address.Address#getPointerSize()
        """
        ...

    def getSize(self) -> int:
        """
        @see ghidra.program.model.address.Address#getSize()
        """
        ...

    def getUnsignedOffset(self) -> long:
        """
        @see ghidra.program.model.address.Address#getUnsignedOffset()
        """
        ...

    def hasSameAddressSpace(self, addr: ghidra.program.model.address.Address) -> bool:
        """
        @see ghidra.program.model.address.Address#hasSameAddressSpace(ghidra.program.model.address.Address)
        """
        ...

    def hashCode(self) -> int:
        """
        @see java.lang.Object#hashCode()
        """
        ...

    def isConstantAddress(self) -> bool:
        """
        @see ghidra.program.model.address.Address#isConstantAddress()
        """
        ...

    def isExternalAddress(self) -> bool:
        """
        @see ghidra.program.model.address.Address#isExternalAddress()
        """
        ...

    def isHashAddress(self) -> bool:
        """
        @see ghidra.program.model.address.Address#isHashAddress()
        """
        ...

    def isLoadedMemoryAddress(self) -> bool: ...

    def isMemoryAddress(self) -> bool:
        """
        @see ghidra.program.model.address.Address#isMemoryAddress()
        """
        ...

    def isNonLoadedMemoryAddress(self) -> bool: ...

    def isRegisterAddress(self) -> bool:
        """
        @see ghidra.program.model.address.Address#isRegisterAddress()
        """
        ...

    def isStackAddress(self) -> bool:
        """
        @see ghidra.program.model.address.Address#isStackAddress()
        """
        ...

    def isSuccessor(self, addr: ghidra.program.model.address.Address) -> bool:
        """
        @see ghidra.program.model.address.Address#isSuccessor(ghidra.program.model.address.Address)
        """
        ...

    def isUniqueAddress(self) -> bool:
        """
        @see ghidra.program.model.address.Address#isUniqueAddress()
        """
        ...

    def isVariableAddress(self) -> bool:
        """
        @see ghidra.program.model.address.Address#isVariableAddress()
        """
        ...

    @staticmethod
    def max(__a0: ghidra.program.model.address.Address, __a1: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address: ...

    @staticmethod
    def min(__a0: ghidra.program.model.address.Address, __a1: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address: ...

    def next(self) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.address.Address#next()
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def previous(self) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.address.Address#previous()
        """
        ...

    @overload
    def subtract(self, displacement: long) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.address.Address#subtract(long)
        """
        ...

    @overload
    def subtract(self, addr: ghidra.program.model.address.Address) -> long:
        """
        @see ghidra.program.model.address.Address#subtract(ghidra.program.model.address.Address)
        """
        ...

    def subtractNoWrap(self, displacement: long) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.address.Address#subtractNoWrap(long)
        """
        ...

    def subtractWrap(self, displacement: long) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.address.Address#subtractWrap(long)
        """
        ...

    def subtractWrapSpace(self, displacement: long) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.address.Address#subtractWrapSpace(long)
        """
        ...

    @overload
    def toString(self) -> unicode:
        """
        @see java.lang.Object#toString()
        """
        ...

    @overload
    def toString(self, showAddressSpace: bool) -> unicode: ...

    @overload
    def toString(self, prefix: unicode) -> unicode:
        """
        @see ghidra.program.model.address.Address#toString(java.lang.String)
        """
        ...

    @overload
    def toString(self, showAddressSpace: bool, minNumDigits: int) -> unicode: ...

    @overload
    def toString(self, showAddressSpace: bool, pad: bool) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def globalAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def namespaceID(self) -> long: ...
