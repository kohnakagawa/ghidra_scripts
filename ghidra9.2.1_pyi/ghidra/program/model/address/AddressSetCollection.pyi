import ghidra.program.model.address
import java.lang


class AddressSetCollection(object):
    """
    This interface represents a collection of AddressSets (actually AddressSetViews).
      It defines a set of methods that can efficiently be performed on a collection
      of one or more AddressSets.
    """









    def contains(self, address: ghidra.program.model.address.Address) -> bool:
        """
        Test if the address is contained within any of the addressSets in this collection.
         <P>
        @param address address to test.
        @return true if addr exists in the set, false otherwise.
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

    def getClass(self) -> java.lang.Class: ...

    def getCombinedAddressSet(self) -> ghidra.program.model.address.AddressSet:
        """
        Returns a single AddressSet containing the union of all the addressSetViews in the collection.
        """
        ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the largest address in this collection or null if the collection is empty.
        @return the largest address in this collection or null if the collection is empty.
        """
        ...

    def getMinAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the smallest address in this collection or null if the collection is empty.
        @return the smallest address in this collection or null if the collection is empty.
        """
        ...

    def hasFewerRangesThan(self, rangeThreshold: int) -> bool:
        """
        Tests whether this collection of addressSets has approximately fewer ranges than
         the given threshold. This is probably estimated by adding up the number of ranges
         in each AddressSet in this collections. Returns true if the total is less than the
         given threshold.
        @param rangeThreshold the number of ranges to test against.
        @return true if the max possible ranges is less than the given threshold.
        """
        ...

    def hashCode(self) -> int: ...

    @overload
    def intersects(self, addrSet: ghidra.program.model.address.AddressSetView) -> bool:
        """
        Determine if any AddressSet in this collection intersects with the specified address set.
        @param addrSet address set to check intersection with.
        """
        ...

    @overload
    def intersects(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> bool:
        """
        Determine if range specified by start and end intersects with any of the AddressSets
         in this collection.
        @param start start of range
        @param end end of range
        @return true if the given range intersects this address set collection.
        """
        ...

    def isEmpty(self) -> bool:
        """
        Returns true if all the AddressSets in this collection are empty.
        @return true if all the AddressSets in this collection are empty.
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

    @property
    def combinedAddressSet(self) -> ghidra.program.model.address.AddressSet: ...

    @property
    def empty(self) -> bool: ...

    @property
    def maxAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def minAddress(self) -> ghidra.program.model.address.Address: ...
