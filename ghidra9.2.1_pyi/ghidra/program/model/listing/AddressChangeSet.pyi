import ghidra.framework.model
import ghidra.program.model.address
import java.lang


class AddressChangeSet(ghidra.framework.model.ChangeSet, object):
    """
    Interface for an Address Change set.  Objects that implements this interface track
     various change information on a set of addresses where the program has changed.
    """









    def add(self, addrSet: ghidra.program.model.address.AddressSetView) -> None:
        """
        Adds the address set to the set addresses where changes occurred.
        @param addrSet the set of addresses to add as changes.
        """
        ...

    def addRange(self, addr1: ghidra.program.model.address.Address, addr2: ghidra.program.model.address.Address) -> None:
        """
        Adds the range of addresses to the set addresses where changes occurred.
        @param addr1 the first address in the range
        @param addr2 the last address in the range. (inclusive)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAddressSet(self) -> ghidra.program.model.address.AddressSetView:
        """
        Returns the address set of all addresses where the listing has changed.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

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
    def addressSet(self) -> ghidra.program.model.address.AddressSetView: ...
