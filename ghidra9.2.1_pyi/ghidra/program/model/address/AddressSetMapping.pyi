import ghidra.program.model.address
import java.lang


class AddressSetMapping(object):
    """
    Class that provides random access to Addresses in an AddressSet, based on the index of the address in the set, not the Address#getOffset().

     For instance, a AddressSet containing addresses [0,1,2,3,4,90,91,92,93,94], #getAddress(int) will return an Address with an
     offset value of 1, but #getAddress(int) will return an Address instance with an offset value of 90.

     This collapses a sparse address space with holes into a contiguous list of addresses.
    """





    def __init__(self, set: ghidra.program.model.address.AddressSetView): ...



    def equals(self, __a0: object) -> bool: ...

    def getAddress(self, index: int) -> ghidra.program.model.address.Address:
        """
        Returns the Address at the specified position in the AddressSet.
        @param index the index into the ordered list of addresses within an AddressSet.
        @return the Address at the specified position.
        """
        ...

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
