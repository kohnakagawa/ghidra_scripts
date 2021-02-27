import ghidra.program.model.address
import ghidra.util.task
import java.lang


class AddressRangeObjectMap(object):
    """
    Associates objects with address ranges.
    """





    def __init__(self):
        """
        Constructs a new ObjectRangeMap
        """
        ...



    def clearAll(self) -> None:
        """
        Clears all objects from map
        """
        ...

    def clearRange(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> None:
        """
        Clears any object associations within the given range.
        @param start the first index in the range to be cleared.
        @param end the last index in the range to be cleared.
        """
        ...

    def contains(self, address: ghidra.program.model.address.Address) -> bool:
        """
        Returns true if the associated address has an associated object even if the assocated object
         is null.
        @param address the index to check for an association.
        @return true if the associated index has an associated object even if the assocated object
         is null.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAddressRangeContaining(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressRange:
        """
        Get the value or hole range containing the specified address
        @param addr
        """
        ...

    @overload
    def getAddressRangeIterator(self) -> ghidra.program.model.address.AddressRangeIterator:
        """
        Returns an {@link AddressRangeIterator} over all ranges that have associated objects.
        @return an {@link AddressRangeIterator} over all ranges that have associated objects.
        """
        ...

    @overload
    def getAddressRangeIterator(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressRangeIterator:
        """
        Returns an {@link AddressRangeIterator} over all ranges that have associated objects within
         the given range.  Object Ranges that overlap the beginning or end of the given range are
         included, but have thier start or end index adjusted to be in the given range.
        @param start the first Address in the range to find all index ranges that have associated values.
        @param end the last Address(inclusive) in the range to find all index ranges that have associated
          values.
        @return an {@link AddressRangeIterator} over all ranges that have associated objects within the
         given range.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getObject(self, address: ghidra.program.model.address.Address) -> object:
        """
        Returns the object associated with the given index or null if no object is associated with
         the given index.  Note that null is a valid association so a null result could be either
         no association or an actual association of the index to null.  Use the contains() method
         first if the distinction is important.  If the contains() method returns true, the result
         is cached so the next call to getObject() will be fast.
        @param address the index at which to retrieve an assocated object.
        @return the object (which can be null) associated with the given index or null if no such
         association exists.
        """
        ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool: ...

    def moveAddressRange(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, length: long, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Move all values within an address range to a new range.
        @param fromAddr the first address of the range to be moved.
        @param toAddr the address where to the range is to be moved.
        @param length the number of addresses to move.
        @param monitor the task monitor.
        @throws CancelledException if the user canceled the operation via the task monitor.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setObject(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, object: object) -> None:
        """
        Associates the given object with all indices in the given range. The object may be null,
         but an association is still established.  Use the clearRange() method to remove associations.
        @param start the start of the range.
        @param end the end (inclusive) of the range.
        @param object the object to associate with the given range.
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
    def addressRangeIterator(self) -> ghidra.program.model.address.AddressRangeIterator: ...

    @property
    def empty(self) -> bool: ...
