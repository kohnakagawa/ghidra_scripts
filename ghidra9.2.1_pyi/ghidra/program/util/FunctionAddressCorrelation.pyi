import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.util
import java.lang


class FunctionAddressCorrelation(ghidra.program.util.ListingAddressCorrelation, object):
    """
    This is the interface for a correlator that associates instructions from one function to
     instructions from another function. Given an address from one function it determines the matching
     address in the other function if possible.
    """









    def equals(self, __a0: object) -> bool: ...

    def getAddressInFirst(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address: ...

    def getAddressInSecond(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address: ...

    def getAddressesInFirst(self) -> ghidra.program.model.address.AddressSetView: ...

    def getAddressesInSecond(self) -> ghidra.program.model.address.AddressSetView: ...

    def getClass(self) -> java.lang.Class: ...

    def getFirstFunction(self) -> ghidra.program.model.listing.Function:
        """
        Gets the first function for this address correlator.
        @return the first function.
        """
        ...

    def getFirstProgram(self) -> ghidra.program.model.listing.Program: ...

    def getSecondFunction(self) -> ghidra.program.model.listing.Function:
        """
        Gets the second function for this address correlator.
        @return the second function.
        """
        ...

    def getSecondProgram(self) -> ghidra.program.model.listing.Program: ...

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
    def firstFunction(self) -> ghidra.program.model.listing.Function: ...

    @property
    def firstProgram(self) -> ghidra.program.model.listing.Program: ...

    @property
    def secondFunction(self) -> ghidra.program.model.listing.Function: ...

    @property
    def secondProgram(self) -> ghidra.program.model.listing.Program: ...
