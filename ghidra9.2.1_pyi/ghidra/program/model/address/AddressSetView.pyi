from typing import Iterator
import ghidra.program.model.address
import java.lang
import java.util
import java.util.function


class AddressSetView(java.lang.Iterable, object):
    """
    Defines a read-only interface for an address set.
    """







    def __iter__(self): ...

    @overload
    def contains(self, addr: ghidra.program.model.address.Address) -> bool:
        """
        Test if the address is contained within this set.
         <P>
        @param addr address to test.
        @return true if addr exists in the set, false otherwise.
        """
        ...

    @overload
    def contains(self, rangeSet: ghidra.program.model.address.AddressSetView) -> bool:
        """
        Test if the given address set is a subset of this set.
         <P>
        @param rangeSet the set to test.
        @return true if the entire set is contained within this set,
                 false otherwise.
        """
        ...

    @overload
    def contains(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> bool:
        """
        Test if the given address range is contained in this set.
         <P>
        @param start the first address in the range.
        @param end the last address in the range.
        @return true if entire range is contained within the set,
                 false otherwise.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def findFirstAddressInCommon(self, set: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.Address:
        """
        Finds the first address in this collection that is also in the given addressSet.
        @param set the addressSet to search for the first (lowest) common address.
        @return the first address that is contained in this set and the given set.
        """
        ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    @overload
    def getAddressRanges(self) -> ghidra.program.model.address.AddressRangeIterator:
        """
        @return an iterator over the address ranges in this address set.
        """
        ...

    @overload
    def getAddressRanges(self, forward: bool) -> ghidra.program.model.address.AddressRangeIterator:
        """
        Returns an iterator over the ranges in the specified order
        @param forward the ranges are returned from lowest to highest, otherwise from
         highest to lowest
        @return an iterator over all the addresse ranges in the set.
        """
        ...

    @overload
    def getAddressRanges(self, start: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.address.AddressRangeIterator:
        """
        Returns an iterator of address ranges starting with the range that contains the given address.
         If there is no range containing the start address, then the the first range will be
         the next range greater than the start address if going forward, otherwise the range less than
         the start address
        @param start the address the the first range should contain.
        @param forward true iterators forward, false backwards
        @return the AddressRange iterator
        """
        ...

    @overload
    def getAddresses(self, forward: bool) -> ghidra.program.model.address.AddressIterator:
        """
        Returns an iterator over all addresses in this set.
        @param forward if true the address are return in increasing order, otherwise in
         decreasing order.
        @return an iterator over all addresses in this set.
        """
        ...

    @overload
    def getAddresses(self, start: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.address.AddressIterator:
        """
        Returns an iterator over the addresses in this address set
         starting at the start address
        @param start address to start iterating at in the address set
        @param forward if true address are return from lowest to highest, else from highest to lowest
        @return an iterator over the addresses in this address set
         starting at the start address
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFirstRange(self) -> ghidra.program.model.address.AddressRange:
        """
        Returns the first range in this set or null if the set is empty;
        @return the first range in this set or null if the set is empty;
        """
        ...

    def getLastRange(self) -> ghidra.program.model.address.AddressRange:
        """
        Returns the last range in this set or null if the set is empty;
        @return the last range in this set or null if the set is empty;
        """
        ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address:
        """
        @return the maximum address for this set. Returns null if the set is empty.
        """
        ...

    def getMinAddress(self) -> ghidra.program.model.address.Address:
        """
        @return the minimum address for this set. Returns null if the set is empty.
        """
        ...

    def getNumAddressRanges(self) -> int:
        """
        @return the number of address ranges in this set.
        """
        ...

    def getNumAddresses(self) -> long:
        """
        @return the number of addresses in this set.
        """
        ...

    def getRangeContaining(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressRange:
        """
        Returns the range that contains the given address
        @param address the address for which to find a range.
        @return the range that contains the given address.
        """
        ...

    def hasSameAddresses(self, view: ghidra.program.model.address.AddressSetView) -> bool:
        """
        Returns true if the given address set contains the same set of addresses
         as this set.
        @param view the address set to compare.
        @return true if the given set contains the same addresses as this set.
        """
        ...

    def hashCode(self) -> int: ...

    def intersect(self, view: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet:
        """
        Computes the intersection of this address set with the given address set.
         This method does not modify this address set.
        @param view the address set to intersect with.
        @return AddressSet a new address set that contains all addresses that are
         contained in both this set and the given set.
        """
        ...

    def intersectRange(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressSet:
        """
        Computes the intersection of this address set with the given address range.
         This method does not modify this address set.
        @param start start of range
        @param end end of range
        @return AddressSet a new address set that contains all addresses that are
         contained in both this set and the given range.
        """
        ...

    @overload
    def intersects(self, addrSet: ghidra.program.model.address.AddressSetView) -> bool:
        """
        Determine if this address set intersects with the specified address set.
        @param addrSet address set to check intersection with.
        @return true if this set intersects the specified addrSet else false
        """
        ...

    @overload
    def intersects(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> bool:
        """
        Determine if the start and end range
         intersects with the specified address set.
        @param start start of range
        @param end end of range
        @return true if the given range intersects this address set.
        """
        ...

    def isEmpty(self) -> bool:
        """
        @return true if this set is empty.
        """
        ...

    @overload
    def iterator(self) -> Iterator[ghidra.program.model.address.AddressRange]:
        """
        Returns an iterator over the address ranges in this address set.
        """
        ...

    @overload
    def iterator(self, forward: bool) -> Iterator[ghidra.program.model.address.AddressRange]:
        """
        Returns an iterator over the ranges in the specified order
        @param forward the ranges are returned from lowest to highest, otherwise from
         highest to lowest
        @return an iterator over all the addresse ranges in the set.
        """
        ...

    @overload
    def iterator(self, start: ghidra.program.model.address.Address, forward: bool) -> Iterator[ghidra.program.model.address.AddressRange]:
        """
        Returns an iterator of address ranges starting with the range that contains the given address.
         If there is no range containing the start address, then the the first range will be
         the next range greater than the start address if going forward, otherwise the range less than
         the start address
        @param start the address the the first range should contain.
        @param forward true iterators forward, false backwards
        @return the AddressRange iterator
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def spliterator(self) -> java.util.Spliterator: ...

    def subtract(self, addrSet: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet:
        """
        Computes the difference of this address set with the given address set
         (this - set).  Note that this is not the same as (set - this).  This
         method does not change this address set.
        @param addrSet the set to subtract from this set.
        @return AddressSet a new address set which contains all the addresses
         that are in this set, but not in the given set.
        """
        ...

    def toString(self) -> unicode: ...

    @staticmethod
    def trimEnd(set: ghidra.program.model.address.AddressSetView, addr: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressSetView:
        """
        Trim address set removing all addresses greater-than-or-equal to specified
         address based upon {@link Address#compareTo(Address)} behavior.
         The address set may contain address ranges from multiple
         address spaces.
        @param set address set to be trimmed
        @param addr trim point.  Only addresses less than this address will be returned.
        @return trimmed address set view
        """
        ...

    @staticmethod
    def trimStart(set: ghidra.program.model.address.AddressSetView, addr: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressSetView:
        """
        Trim address set removing all addresses less-than-or-equal to specified
         address based upon {@link Address#compareTo(Address)} behavior.
         The address set may contain address ranges from multiple
         address spaces.
        @param set address set to be trimmed
        @param addr trim point.  Only addresses greater than this address will be returned.
        @return trimmed address set view
        """
        ...

    def union(self, addrSet: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet:
        """
        Computes the union of this address set with the given address set.  This
         method does not change this address set.
        @param addrSet The address set to be unioned with this address set.
        @return AddressSet A new address set which contains all the addresses
         from both this set and the given set.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def xor(self, addrSet: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet:
        """
        Computes the exclusive-or of this address set with the given set. This
         method does not modify this address set.
        @param addrSet address set to exclusive-or with.
        @return AddressSet a new address set containing all addresses that are in
         either this set or the given set, but not in both sets
        """
        ...

    @property
    def addressRanges(self) -> ghidra.program.model.address.AddressRangeIterator: ...

    @property
    def empty(self) -> bool: ...

    @property
    def firstRange(self) -> ghidra.program.model.address.AddressRange: ...

    @property
    def lastRange(self) -> ghidra.program.model.address.AddressRange: ...

    @property
    def maxAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def minAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def numAddressRanges(self) -> int: ...

    @property
    def numAddresses(self) -> long: ...
