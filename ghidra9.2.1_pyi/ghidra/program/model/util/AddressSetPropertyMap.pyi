import ghidra.program.model.address
import java.lang


class AddressSetPropertyMap(object):
    """
    Defines methods to mark ranges in a property map.
    """









    @overload
    def add(self, addressSet: ghidra.program.model.address.AddressSetView) -> None:
        """
        Add the address set to the property map.
        @param addressSet address set to add
        """
        ...

    @overload
    def add(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> None:
        """
        Add the address range to the property map.
        @param start start of the range
        @param end end of the range
        """
        ...

    def clear(self) -> None:
        """
        Clear the property map.
        """
        ...

    def contains(self, addr: ghidra.program.model.address.Address) -> bool:
        """
        Return whether the property map contains the given address.
        @param addr address to check
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAddressRanges(self) -> ghidra.program.model.address.AddressRangeIterator:
        """
        Return an address range iterator over the property map.
        """
        ...

    def getAddressSet(self) -> ghidra.program.model.address.AddressSet:
        """
        Return the address set for the property map.
        """
        ...

    def getAddresses(self) -> ghidra.program.model.address.AddressIterator:
        """
        Return an address iterator over the property map.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def remove(self, addressSet: ghidra.program.model.address.AddressSetView) -> None:
        """
        Remove the address set from the property map.
        @param addressSet address set to remove
        """
        ...

    @overload
    def remove(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> None:
        """
        Remove the address range from the property map.
        @param start start of the range
        @param end end of the range
        """
        ...

    def set(self, addressSet: ghidra.program.model.address.AddressSetView) -> None:
        """
        Clear the property map and set it with the given address set.
        @param addressSet address set to use
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
    def addressRanges(self) -> ghidra.program.model.address.AddressRangeIterator: ...

    @property
    def addressSet(self) -> ghidra.program.model.address.AddressSet: ...

    @property
    def addresses(self) -> ghidra.program.model.address.AddressIterator: ...
