import ghidra.program.model.address
import ghidra.program.model.listing
import java.lang


class ListingAddressCorrelation(object):
    """
    This is the interface for a correlator that associates addresses from one program with
     addresses from another program or it can associate addresses from one part of a program
     with addresses from another part of the same program. Given an address from the address set
     in the first program it determines the matching address from the address set for the second
     program if possible.
    """









    def equals(self, __a0: object) -> bool: ...

    def getAddressInFirst(self, addressInSecond: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address:
        """
        Determine the address from the first set that matches the specified address in the second set.
        @param addressInSecond the address in the second address set.
        @return the matching address in the first set or null if a match couldn't be determined.
        """
        ...

    def getAddressInSecond(self, addressInFirst: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address:
        """
        Determine the address from the second set that matches the specified address in the first set.
        @param addressInFirst the address in the first address set.
        @return the matching address in the second set or null if a match couldn't be determined.
        """
        ...

    def getAddressesInFirst(self) -> ghidra.program.model.address.AddressSetView:
        """
        Gets the first set of addresses for this correlator.
        @return the first set of addresses.
        """
        ...

    def getAddressesInSecond(self) -> ghidra.program.model.address.AddressSetView:
        """
        Gets the second set of addresses for this correlator.
        @return the second set of addresses.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFirstProgram(self) -> ghidra.program.model.listing.Program:
        """
        Gets the program containing the first set of addresses.
        @return the program for the first set of addresses.
        """
        ...

    def getSecondProgram(self) -> ghidra.program.model.listing.Program:
        """
        Gets the program containing the second set of addresses.
         This program may be different from or the same as the first program.
        @return the program for the second set of addresses.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addressesInFirst(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def addressesInSecond(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def firstProgram(self) -> ghidra.program.model.listing.Program: ...

    @property
    def secondProgram(self) -> ghidra.program.model.listing.Program: ...
