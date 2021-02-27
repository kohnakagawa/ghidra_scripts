import ghidra.program.model.address
import java.lang


class SpecialAddress(ghidra.program.model.address.GenericAddress):
    """
    Class used represent "special addresses"
    """









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
    def toString(self, showAddressSpace: bool) -> unicode:
        """
        @see ghidra.program.model.address.Address#toString(boolean)
        """
        ...

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
