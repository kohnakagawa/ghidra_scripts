import ghidra.program.model.address
import java.lang


class MultiAddressRangeIterator(object):
    """
    MultiAddressRangeIterator is a class for iterating through multiple
     address range iterators simultaneously. The next() method returns the next address range
     as determined from all the iterators.
    """





    @overload
    def __init__(self, iters: List[ghidra.program.model.address.AddressRangeIterator]):
        """
        Constructor of a multi address iterator for multiple forward address iterators.
        @param iters the address iterators.
        """
        ...

    @overload
    def __init__(self, iters: List[ghidra.program.model.address.AddressRangeIterator], forward: bool):
        """
        Constructor of a multi address range iterator.
         <br>Note: all iterators must iterate in the same direction (forwards or backwards).
        @param iters the address iterators. All must iterate in the direction indicated
         by the "forward" parameter.
        @param forward true indicates that forward iterators are in the array.
         false indicates backward iterators are in the array.
        """
        ...



    def backwardNext(self) -> ghidra.program.model.address.AddressRange:
        """
        Returns the next address for backward iterators. The next address could be from any
         one of the iterators.
        @return the next address.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def forwardNext(self) -> ghidra.program.model.address.AddressRange:
        """
        Returns the next address for forward iterators. The next address could be from any
         one of the iterators.
        @return the next address.
        """
        ...

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

    def next(self) -> ghidra.program.model.address.AddressRange:
        """
        Returns the next address. The next address could be from any
         one of the iterators.
        @return the next address.
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
