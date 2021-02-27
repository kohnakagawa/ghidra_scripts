from typing import List
import ghidra.program.model.listing
import java.lang


class MultiCodeUnitIterator(object):
    """
    MultiCodeUnitIterator is a class for iterating through multiple
     code unit iterators simultaneously. The next() method returns an array
     of code units, since a code unit can be obtained from neither, either, or
     both of the original code unit iterators.
    """





    @overload
    def __init__(self, listings: List[ghidra.program.model.listing.Listing], addr: ghidra.program.model.address.Address, forward: bool):
        """
        Constructor of a multi-code unit iterator.
        @param listings an array of the program listings whose code units are to be iterated.
        @param addr the address where the iterator should start.
        @param forward true indicates a forward iterator.  false indicates a backwards iterator.
        """
        ...

    @overload
    def __init__(self, listings: List[ghidra.program.model.listing.Listing], addrs: ghidra.program.model.address.AddressSetView, forward: bool):
        """
        Constructor of a multi-code unit iterator.
        @param listings an array of the program listings whose code units are to be iterated.
        @param addrs the address set over which the code units should be iterated.
        @param forward true indicates a forward iterator.  false indicates a backwards iterator.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool:
        """
        Determines whether or not any of the iterators have a
          next code unit.
        @return true if the next code unit can be obtained from any of
         the code unit iterators.
        """
        ...

    def hashCode(self) -> int: ...

    def next(self) -> List[ghidra.program.model.listing.CodeUnit]:
        """
        Returns the next code unit(s). The next code unit could be from any one
         or more of the iterators. The array returns a code unit for each listing
         that has a code unit with a minimum address at the next iterator address.
         The code units in the array match up to the listings in the array passed
         to this classes constructor. The code unit will be null in the array if
         no code unit started at the next code unit address for that listing.
        @return an array with the next code unit(s).
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
