from typing import Iterator
import ghidra.program.model.address
import java.lang
import java.util
import java.util.function


class AddressRange(java.lang.Comparable, java.lang.Iterable, object):
    """
    The AddressRange interface is used by any object
     that represents a contiguous inclusive range of
     addresses from a minimum address to a maximum
     address.  The entire range must fall within a
     single address space.

    """







    def __iter__(self): ...

    @overload
    def compareTo(self, addr: ghidra.program.model.address.Address) -> int:
        """
        Compares the given address to this address range.
        @param addr the address to compare.
        @return a negative integer if the address is greater than the maximum range address,
                 zero if the address is in the range, and
                 a positive integer if the address is less than minimum range address.
        """
        ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def contains(self, addr: ghidra.program.model.address.Address) -> bool:
        """
        Returns true if the given address is contained in the range.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def getAddressSpace(self) -> ghidra.program.model.address.AddressSpace:
        """
        @return address space this range resides within
        """
        ...

    def getBigLength(self) -> long:
        """
        Returns the number of addresses as a BigInteger.
        @return the number of addresses as a BigInteger.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getLength(self) -> long:
        """
        Returns the number of addresses in the range.
        """
        ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address:
        """
        @return the maximum address in the range.
        """
        ...

    def getMinAddress(self) -> ghidra.program.model.address.Address:
        """
        @return the minimum address in the range.
        """
        ...

    def hashCode(self) -> int: ...

    def intersect(self, range: ghidra.program.model.address.AddressRange) -> ghidra.program.model.address.AddressRange:
        """
        Computes the intersection of this range with another.
        @param range the range to intersect this range with
        @return AddressRange the intersection or null if the ranges
         do not intersect.
        """
        ...

    def intersectRange(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressRange:
        """
        Computes the intersection of this range with another.
        @param start of range
        @param end end of range
        @return AddressRange the intersection or null if the ranges
         do not intersect.
        """
        ...

    @overload
    def intersects(self, range: ghidra.program.model.address.AddressRange) -> bool:
        """
        Returns true if the given range intersects this range.
        @param range the range to test for intersection with.
        """
        ...

    @overload
    def intersects(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> bool:
        """
        Returns true if the given range intersects this range.
        @param start the first address in the range to test for intersection.
        @param end the last address in the range to test for intersection.
        """
        ...

    def iterator(self) -> java.util.Iterator: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def spliterator(self) -> java.util.Spliterator: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addressSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    @property
    def bigLength(self) -> long: ...

    @property
    def length(self) -> long: ...

    @property
    def maxAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def minAddress(self) -> ghidra.program.model.address.Address: ...
