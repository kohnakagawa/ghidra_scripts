from typing import List
import ghidra.program.model.address
import ghidra.program.model.listing
import java.lang


class AddressEvaluator(object):
    """
    The AddressEvaluator class provides a way to evaluate a string
     that represents an address and resolve it to an address for a particular program.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @overload
    @staticmethod
    def evaluate(p: ghidra.program.model.listing.Program, s: unicode) -> ghidra.program.model.address.Address:
        """
        Gets a legitimate address for the specified program as indicated by the string.
        @param p the program to use for determining the address.
        @param s string representation of the address desired.
        @return the address. Otherwise, return null if the string fails to evaluate
         to a legitimate address.
        """
        ...

    @overload
    @staticmethod
    def evaluate(p: ghidra.program.model.listing.Program, addrBytes: List[int]) -> ghidra.program.model.address.Address:
        """
        Utility method for creating an Address object from a byte array. The Address object may or may not
         be a legitimate Address in the program's address space. This method is meant to provide a way of
         creating an Address object from a sequence of bytes that can be used for additional tests and
         comparisons.
        @param p - program being analyzed.
        @param addrBytes - byte array to use containing the values the address will be constructed from.
        @return - Address object constructed from the addrBytes array. Returns null if the program is null,
         addrBytes is null, or the length of addrBytes does not match the default Pointer size or does not contain
         a valid offset.
        """
        ...

    @overload
    @staticmethod
    def evaluate(p: ghidra.program.model.listing.Program, baseAddr: ghidra.program.model.address.Address, s: unicode) -> ghidra.program.model.address.Address:
        """
        Gets a legitimate address for the specified program as indicated by the string.
        @param p the program to use for determining the address.
        @param baseAddr the base address to use for relative addressing.
        @param s string representation of the address desired.
        @return the address. Otherwise, return null if the string fails to evaluate
         to a unique legitimate address.
        """
        ...

    @staticmethod
    def evaluateToLong(s: unicode) -> long: ...

    def getClass(self) -> java.lang.Class: ...

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
