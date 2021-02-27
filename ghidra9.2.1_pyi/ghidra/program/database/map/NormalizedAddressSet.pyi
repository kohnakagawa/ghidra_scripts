from typing import Iterator
import ghidra.program.model.address
import java.lang
import java.util
import java.util.function


class NormalizedAddressSet(object, ghidra.program.model.address.AddressSetView):
    """
    AddressSetView implementation that handles image base changes. NOTE: THIS IMPLEMENTATION
     ASSUMES THAT ONLY ADDRESS RANGES THAT ARE PART OF THE MEMORY MAP WILL BE ADDED TO THIS
     ADDRESS SET. IT IS INTENDED FOR USE BY THE CHANGE SET.
    """





    def __init__(self, addrMap: ghidra.program.database.map.AddressMap):
        """
        Constructs a NormalizedAddressSet
        @param addrMap the address map
        """
        ...

    def __iter__(self): ...

    @overload
    def add(self, addr: ghidra.program.model.address.Address) -> None:
        """
        Adds the address to the set.
        @param addr the address to add
        """
        ...

    @overload
    def add(self, range: ghidra.program.model.address.AddressRange) -> None:
        """
        Adds the address range to this set.
        @param range the range to add.
        """
        ...

    @overload
    def add(self, set: ghidra.program.model.address.AddressSetView) -> None:
        """
        Adds the addressSet to this set.
        @param set the set of addresses to add/
        """
        ...

    def addRange(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address) -> None:
        """
        Adds the address range to this set.
        @param startAddr the first address in the range to add.
        @param endAddr the last address in the range to add.
        """
        ...

    def clear(self) -> None:
        """
        Removes all addresses from this set.
        """
        ...

    @overload
    def contains(self, addr: ghidra.program.model.address.Address) -> bool:
        """
        @see ghidra.program.model.address.AddressSetView#contains(ghidra.program.model.address.Address)
        """
        ...

    @overload
    def contains(self, rangeSet: ghidra.program.model.address.AddressSetView) -> bool:
        """
        @see ghidra.program.model.address.AddressSetView#contains(ghidra.program.model.address.AddressSetView)
        """
        ...

    @overload
    def contains(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address) -> bool:
        """
        @see ghidra.program.model.address.AddressSetView#contains(ghidra.program.model.address.Address, ghidra.program.model.address.Address)
        """
        ...

    def delete(self, view: ghidra.program.model.address.AddressSetView) -> None:
        """
        REmoves all the addresses in the given address set from this set.
        @param view the set of addresses to remove.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def findFirstAddressInCommon(self, set: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.Address: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    @overload
    def getAddressRanges(self) -> ghidra.program.model.address.AddressRangeIterator:
        """
        @see ghidra.program.model.address.AddressSetView#getAddressRanges()
        """
        ...

    @overload
    def getAddressRanges(self, forward: bool) -> ghidra.program.model.address.AddressRangeIterator:
        """
        @see ghidra.program.model.address.AddressSetView#getAddressRanges(boolean)
        """
        ...

    @overload
    def getAddressRanges(self, start: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.address.AddressRangeIterator: ...

    @overload
    def getAddresses(self, forward: bool) -> ghidra.program.model.address.AddressIterator:
        """
        @see ghidra.program.model.address.AddressSetView#getAddresses(boolean)
        """
        ...

    @overload
    def getAddresses(self, start: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.address.AddressIterator:
        """
        @see ghidra.program.model.address.AddressSetView#getAddresses(ghidra.program.model.address.Address, boolean)
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFirstRange(self) -> ghidra.program.model.address.AddressRange: ...

    def getLastRange(self) -> ghidra.program.model.address.AddressRange: ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.address.AddressSetView#getMaxAddress()
        """
        ...

    def getMinAddress(self) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.address.AddressSetView#getMinAddress()
        """
        ...

    def getNumAddressRanges(self) -> int:
        """
        @see ghidra.program.model.address.AddressSetView#getNumAddressRanges()
        """
        ...

    def getNumAddresses(self) -> long:
        """
        @see ghidra.program.model.address.AddressSetView#getNumAddresses()
        """
        ...

    def getRangeContaining(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressRange: ...

    def hasSameAddresses(self, view: ghidra.program.model.address.AddressSetView) -> bool:
        """
        @see ghidra.program.model.address.AddressSetView#hasSameAddresses(ghidra.program.model.address.AddressSetView)
        """
        ...

    def hashCode(self) -> int: ...

    def intersect(self, view: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet:
        """
        @see ghidra.program.model.address.AddressSetView#intersect(ghidra.program.model.address.AddressSetView)
        """
        ...

    def intersectRange(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressSet:
        """
        @see ghidra.program.model.address.AddressSetView#intersectRange(ghidra.program.model.address.Address, ghidra.program.model.address.Address)
        """
        ...

    @overload
    def intersects(self, addrSet: ghidra.program.model.address.AddressSetView) -> bool:
        """
        @see ghidra.program.model.address.AddressSetView#intersects(ghidra.program.model.address.AddressSetView)
        """
        ...

    @overload
    def intersects(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> bool:
        """
        @see ghidra.program.model.address.AddressSetView#intersects(ghidra.program.model.address.Address, ghidra.program.model.address.Address)
        """
        ...

    def isEmpty(self) -> bool:
        """
        @see ghidra.program.model.address.AddressSetView#isEmpty()
        """
        ...

    @overload
    def iterator(self) -> Iterator[ghidra.program.model.address.AddressRange]: ...

    @overload
    def iterator(self, forward: bool) -> Iterator[ghidra.program.model.address.AddressRange]: ...

    @overload
    def iterator(self, start: ghidra.program.model.address.Address, forward: bool) -> Iterator[ghidra.program.model.address.AddressRange]: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def spliterator(self) -> java.util.Spliterator: ...

    def subtract(self, addrSet: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet:
        """
        @see ghidra.program.model.address.AddressSetView#subtract(ghidra.program.model.address.AddressSetView)
        """
        ...

    def toString(self) -> unicode:
        """
        @see java.lang.Object#toString()
        """
        ...

    @staticmethod
    def trimEnd(__a0: ghidra.program.model.address.AddressSetView, __a1: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressSetView: ...

    @staticmethod
    def trimStart(__a0: ghidra.program.model.address.AddressSetView, __a1: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressSetView: ...

    def union(self, addrSet: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet:
        """
        @see ghidra.program.model.address.AddressSetView#union(ghidra.program.model.address.AddressSetView)
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
        @see ghidra.program.model.address.AddressSetView#xor(ghidra.program.model.address.AddressSetView)
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
