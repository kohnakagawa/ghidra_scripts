import docking.widgets.fieldpanel.support
import ghidra.app.util.viewer.util
import ghidra.program.model.address
import java.lang


class AddressIndexMapConverter(ghidra.app.util.viewer.util.AddressIndexMap):




    def __init__(self, addressIndexMap: ghidra.app.util.viewer.util.AddressIndexMap, mapProgram: ghidra.program.model.listing.Program, otherProgram: ghidra.program.model.listing.Program): ...



    def equals(self, __a0: object) -> bool: ...

    def getAddress(self, index: long) -> ghidra.program.model.address.Address: ...

    def getAddressSet(self, sel: docking.widgets.fieldpanel.support.FieldSelection) -> ghidra.program.model.address.AddressSet: ...

    def getClass(self) -> java.lang.Class: ...

    def getFieldSelection(self, set: ghidra.program.model.address.AddressSetView) -> docking.widgets.fieldpanel.support.FieldSelection: ...

    def getIndex(self, addr: ghidra.program.model.address.Address) -> long: ...

    def getIndexAtOrAfter(self, addr: ghidra.program.model.address.Address) -> long:
        """
        Returns the index for the given address.  If the address is not mapped, the result is
         defined as follows:
            if the address is less than the smallest address in the map, then null is returned
            if the address is greater the the largest address in the map, then a value one bigger than
                 the index of the largest address in the map.
            if the address is in a "gap", then the index of the next largest address that is in the
            		map is returned.
        @param addr the address for which to retrieve the index.
        @return the associated index for the given address or if there is none, then the index
                 of then next address greater than the given address or null if there is none.
        """
        ...

    def getIndexCount(self) -> long:
        """
        Returns the total number of addresses
        @return the number of addresses in the view
        """
        ...

    def getIndexedAddressSet(self) -> ghidra.program.model.address.AddressSetView: ...

    def getMaxIndex(self, addr: ghidra.program.model.address.Address) -> long: ...

    def getMinIndex(self, addr: ghidra.program.model.address.Address) -> long: ...

    def getMiniumUnviewableGapSize(self) -> long:
        """
        Returns the suggested minimum size of address ranges that contain no viewable code units (i.e.
         collapsed data).  Ranges larger that this should be removed from the index mapping to get
         better scrollbar behavior. Currently this is 1% of the total viewed address space.
        @return the suggested minimum size for a range of addresses with no viewable content.
        """
        ...

    def getOriginalAddressSet(self) -> ghidra.program.model.address.AddressSetView: ...

    def hashCode(self) -> int: ...

    def isGapAddress(self, address: ghidra.program.model.address.Address) -> bool:
        """
        Returns true if the given address is the first address after gap of missing addresses.
        @param address the address to check for being a gap address
        @return true if the given address is the first address after gap of missing addresses.
        """
        ...

    def isGapIndex(self, index: long) -> bool:
        """
        Returns true if address of the given index is not the successor of the
         previous index's address.
        @param index the index to test for gap in the address set.
        @return true if the given index represents the first address after a gap in the address set.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeUnviewableAddressRanges(self, addressSet: ghidra.program.model.address.AddressSet) -> None:
        """
        Removes the given addresses from the set of addresses that get mapped into indexes.  This
         is used to remove large number of addresses that are contained in closed data in order to
         make scrollbars scroll smoothly.
         <P>
         The original address set is maintained to determine the gap addresses and also for resetting
         the index map to the entire set of addresses
        @param addressSet the set of addresses to remove from the set of addresses that get mapped.
        """
        ...

    def reset(self) -> ghidra.app.util.viewer.util.AddressIndexMap:
        """
        Resets the mapping to the entire original address set.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def indexedAddressSet(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def originalAddressSet(self) -> ghidra.program.model.address.AddressSetView: ...
