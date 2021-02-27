from typing import Iterator
import ghidra.program.model.address
import ghidra.program.util
import java.lang
import java.util
import java.util.function


class ProgramSelection(object, ghidra.program.model.address.AddressSetView):
    """
    Class to define a selection for a program.
    """





    @overload
    def __init__(self):
        """
        Construct a new empty ProgramSelection.
        """
        ...

    @overload
    def __init__(self, addressFactory: ghidra.program.model.address.AddressFactory):
        """
        Construct a new empty ProgramSelection.
        @param addressFactory the address factory for the address set
         associated with this program selection.
        """
        ...

    @overload
    def __init__(self, setView: ghidra.program.model.address.AddressSetView):
        """
        Construct a new ProgramSelection
        @param setView address set for the selection
        """
        ...

    @overload
    def __init__(self, sel: ghidra.program.util.InteriorSelection):
        """
        Construct a new ProgramSelection from the indicated interior selection.
        @param sel the interior selection
        """
        ...

    @overload
    def __init__(self, from_: ghidra.program.model.address.Address, to: ghidra.program.model.address.Address):
        """
        Constructor.
        @param from the start of the selection
        @param to the end of the selection
        """
        ...

    @overload
    def __init__(self, addressFactory: ghidra.program.model.address.AddressFactory, setView: ghidra.program.model.address.AddressSetView):
        """
        Construct a new ProgramSelection
        @param addressFactory the address factory for the address set
         associated with this program selection.
        @param setView address set for the selection
        """
        ...

    @overload
    def __init__(self, addressFactory: ghidra.program.model.address.AddressFactory, sel: ghidra.program.util.InteriorSelection):
        """
        Construct a new ProgramSelection from the indicated interior selection.
        @param addressFactory the address factory for the address set
         associated with this program selection.
        @param sel the interior selection
        """
        ...

    @overload
    def __init__(self, addressFactory: ghidra.program.model.address.AddressFactory, from_: ghidra.program.model.address.Address, to: ghidra.program.model.address.Address):
        """
        Constructor.
        @param addressFactory the address factory for the address set
         associated with this program selection.
        @param from the start of the selection
        @param to the end of the selection
        """
        ...

    def __iter__(self): ...

    @overload
    def contains(self, addr: ghidra.program.model.address.Address) -> bool:
        """
        Test if the address exists within this set.
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
        Test if the given address range is in the set.
         <P>
        @param start the first address in the range.
        @param end the last address in the range.
        @return true if entire range is contained within the set,
                 false otherwise.
        """
        ...

    def equals(self, obj: object) -> bool:
        """
        Return whether this ProgramSelection is equal to obj.
        """
        ...

    def findFirstAddressInCommon(self, set: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.Address: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    @overload
    def getAddressRanges(self) -> ghidra.program.model.address.AddressRangeIterator:
        """
        Returns an iterator over the address ranges in this address set.
        """
        ...

    @overload
    def getAddressRanges(self, atStart: bool) -> ghidra.program.model.address.AddressRangeIterator:
        """
        Returns an iterator over the address ranges in this address set.
        @param atStart if true, the iterator is positioned at the minimum address.
         if false, the iterator is positioned at the maximum address.
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

    def getInteriorSelection(self) -> ghidra.program.util.InteriorSelection:
        """
        Get the interior selection.
        @return null if there is no interior selection
        """
        ...

    def getLastRange(self) -> ghidra.program.model.address.AddressRange: ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address:
        """
        Return the maximum address for this set.
        """
        ...

    def getMinAddress(self) -> ghidra.program.model.address.Address:
        """
        Return the minimum address for this set.
        """
        ...

    def getNumAddressRanges(self) -> int:
        """
        Return the number of address ranges in this set.
        """
        ...

    def getNumAddresses(self) -> long:
        """
        Returns the number of addresses in this set.
        """
        ...

    def getRangeContaining(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressRange: ...

    def hasSameAddresses(self, asv: ghidra.program.model.address.AddressSetView) -> bool:
        """
        Returns true if and only if this set and the given
         address set contains exactly the same addresses.
        @param asv the address set to compare with this one.
        @return true if the specified set has the same addresses.
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
        Determine if this program selection intersects with the specified address set.
        @param addrSet address set to check intersection with.
        """
        ...

    @overload
    def intersects(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> bool:
        """
        @see AddressSetView#intersects(Address, Address)
        """
        ...

    def isEmpty(self) -> bool:
        """
        Returns true if this set is empty.
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

    def subtract(self, view: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet:
        """
        @see ghidra.program.model.address.AddressSetView#subtract(ghidra.program.model.address.AddressSetView)
        """
        ...

    def toString(self) -> unicode: ...

    @staticmethod
    def trimEnd(__a0: ghidra.program.model.address.AddressSetView, __a1: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressSetView: ...

    @staticmethod
    def trimStart(__a0: ghidra.program.model.address.AddressSetView, __a1: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressSetView: ...

    def union(self, view: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet:
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

    def xor(self, view: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet:
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
    def interiorSelection(self) -> ghidra.program.util.InteriorSelection: ...

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
