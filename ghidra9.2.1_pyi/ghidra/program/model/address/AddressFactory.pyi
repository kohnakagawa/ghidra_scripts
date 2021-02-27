from typing import List
import ghidra.program.model.address
import java.lang


class AddressFactory(object):








    def equals(self, o: object) -> bool:
        """
        @see java.lang.Object#equals(Object)
        """
        ...

    @overload
    def getAddress(self, addrString: unicode) -> ghidra.program.model.address.Address:
        """
        Create an address from String. Attempts to use the "default" address space
         first.  Otherwise loops through each addressSpace, returning the first valid
         address that any addressSpace creates from the string.
         Returns an Address if the string is valid, otherwise null.
        """
        ...

    @overload
    def getAddress(self, spaceID: int, offset: long) -> ghidra.program.model.address.Address:
        """
        Get an address using the addressSpace with the given id and having the given offset.
        @param spaceID the id of the address space to use to create the new address.
        @param offset the offset of the new address to be created.
        @return the new address.
        """
        ...

    @overload
    def getAddressSet(self) -> ghidra.program.model.address.AddressSet:
        """
        Returns an addressSet containing all possible "real" addresses for this address factory.
        """
        ...

    @overload
    def getAddressSet(self, min: ghidra.program.model.address.Address, max: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressSet:
        """
        Computes an address set from a start and end address that may span address spaces.  Although
         in general, it is not meaningful to compare addresses from multiple spaces, but since there
         is an absolute ordering of address spaces it can be useful for iterating over all addresses
         in a program with multiple address spaces.
        @param min the start address
        @param max the end address.
        @return an addressSet containing ranges that don't span address spaces.
        """
        ...

    @overload
    def getAddressSpace(self, spaceID: int) -> ghidra.program.model.address.AddressSpace:
        """
        Returns the space with the given spaceID or null if none exists
        """
        ...

    @overload
    def getAddressSpace(self, name: unicode) -> ghidra.program.model.address.AddressSpace:
        """
        Returns the space with the given name or null if no space
         exists with that name.
        """
        ...

    def getAddressSpaces(self) -> List[ghidra.program.model.address.AddressSpace]:
        """
        Get the array of all "physical" AddressSpaces.
        """
        ...

    def getAllAddressSpaces(self) -> List[ghidra.program.model.address.AddressSpace]:
        """
        Returns an array of all address spaces, including analysis spaces.
        @return an array of all the address spaces.
        """
        ...

    @overload
    def getAllAddresses(self, addrString: unicode) -> List[ghidra.program.model.address.Address]:
        """
        Generates all reasonable addresses that can be interpreted from
         the given string.  Each Address Space is given a change to parse
         the string and all the valid results are return in the array.
        @param addrString the address string to parse.
        @return Address[] The list of addresses generated from the string.
        """
        ...

    @overload
    def getAllAddresses(self, addrString: unicode, caseSensitive: bool) -> List[ghidra.program.model.address.Address]:
        """
        Generates all reasonable addresses that can be interpreted from
         the given string.  Each Address Space is given a change to parse
         the string and all the valid results are return in the array.
        @param addrString the address string to parse.
        @param caseSensitive determines if addressSpace names must be case sensitive to match.
        @return Address[] The list of addresses generated from the string.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getConstantAddress(self, offset: long) -> ghidra.program.model.address.Address:
        """
        Returns an address in "constant" space with the given offset.
        @param offset the offset in "constant" space for the new address.
        @return a new address in the "constant" space with the given offset.
        """
        ...

    def getConstantSpace(self) -> ghidra.program.model.address.AddressSpace:
        """
        Returns the "constant" address space.
        """
        ...

    def getDefaultAddressSpace(self) -> ghidra.program.model.address.AddressSpace:
        """
        Returns the default AddressSpace
        """
        ...

    def getIndex(self, addr: ghidra.program.model.address.Address) -> long:
        """
        Returns the index (old encoding) for the given address.
        @param addr the address to encode.
        """
        ...

    def getNumAddressSpaces(self) -> int:
        """
        Returns the number of physical AddressSpaces.
        """
        ...

    def getPhysicalSpace(self, space: ghidra.program.model.address.AddressSpace) -> ghidra.program.model.address.AddressSpace:
        """
        Gets the physical address space associated with the given address space. If
         the given space is physical, then it will be returned.
        @param space the addressSpace for which the physical space is requested.
        @return the physical address space associated with the given address space.
        """
        ...

    def getPhysicalSpaces(self) -> List[ghidra.program.model.address.AddressSpace]:
        """
        Returns an array of all the physical address spaces.
        @return an array of all the physical address spaces.
        """
        ...

    def getRegisterSpace(self) -> ghidra.program.model.address.AddressSpace:
        """
        Returns the "register" address space.
        """
        ...

    def getStackSpace(self) -> ghidra.program.model.address.AddressSpace:
        """
        Returns the "stack" address space.
        """
        ...

    def getUniqueSpace(self) -> ghidra.program.model.address.AddressSpace:
        """
        Returns the "unique" address space.
        """
        ...

    def hasMultipleMemorySpaces(self) -> bool:
        """
        Returns true if there is more than one memory address space
        """
        ...

    def hashCode(self) -> int: ...

    def isValidAddress(self, addr: ghidra.program.model.address.Address) -> bool:
        """
        Tests if the given address is valid for at least one of the
         Address Spaces in this factory
        @param addr The address to test
        @return boolean true if the address valid, false otherwise
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def oldGetAddressFromLong(self, value: long) -> ghidra.program.model.address.Address:
        """
        Returns the address using the old encoding format.
        @param value to decode into an address.
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
    def addressSet(self) -> ghidra.program.model.address.AddressSet: ...

    @property
    def addressSpaces(self) -> List[ghidra.program.model.address.AddressSpace]: ...

    @property
    def allAddressSpaces(self) -> List[ghidra.program.model.address.AddressSpace]: ...

    @property
    def constantSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    @property
    def defaultAddressSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    @property
    def numAddressSpaces(self) -> int: ...

    @property
    def physicalSpaces(self) -> List[ghidra.program.model.address.AddressSpace]: ...

    @property
    def registerSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    @property
    def stackSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    @property
    def uniqueSpace(self) -> ghidra.program.model.address.AddressSpace: ...
