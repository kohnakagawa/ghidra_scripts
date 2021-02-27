from typing import List
import ghidra.program.model.address
import java.lang


class MultiAddressIterator(object):
    """
    MultiAddressIterator is a class for iterating through multiple
     address iterators simultaneously. The next() method returns the next address
     as determined from all the iterators.
    """





    @overload
    def __init__(self, iters: List[ghidra.program.model.address.AddressIterator]):
        """
        Constructor of a multi address iterator for multiple forward address iterators.
        @param iters the address iterators.
        """
        ...

    @overload
    def __init__(self, iters: List[ghidra.program.model.address.AddressIterator], forward: bool):
        """
        Constructor of a multi address iterator.
         <br>Note: all iterators must iterate in the same direction (forwards or backwards).
        @param iters the address iterators. All must iterate in the direction indicated
         by the "forward" parameter.
        @param forward true indicates that forward iterators are in the array.
         false indicates backward iterators are in the array.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool:
        """
        Determines whether or not any of the original iterators has a
          next address.
        @return true if a next address can be obtained from any of
         the address iterators.
        """
        ...

    def hashCode(self) -> int: ...

    def next(self) -> ghidra.program.model.address.Address:
        """
        Returns the next address. The next address could be from any
         one of the iterators.
        @return the next address.
        """
        ...

    def nextAddresses(self) -> List[ghidra.program.model.address.Address]:
        """
        Returns the next address(es). The next address could be from any
         one or more of the iterators.
        @return an array with the next address(es). Each element in this array
         corresponds to each iterator passed to the constructor.
         Null is returned in an element if the next overall address is not the
         next address from the corresponding iterator.
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
