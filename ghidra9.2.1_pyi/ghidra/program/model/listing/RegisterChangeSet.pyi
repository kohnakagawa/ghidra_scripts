import ghidra.framework.model
import ghidra.program.model.address
import java.lang


class RegisterChangeSet(ghidra.framework.model.ChangeSet, object):
    """
    Interface for a Register Change set.  Objects that implements this interface track
     various change information on a set of addresses where the program register values have changed.
    """









    def addRegisterRange(self, addr1: ghidra.program.model.address.Address, addr2: ghidra.program.model.address.Address) -> None:
        """
        Adds the ranges of addresses that have register changes.
        @param addr1 the first address in the range.
        @param addr2 the last address in the range.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getRegisterAddressSet(self) -> ghidra.program.model.address.AddressSetView:
        """
        Returns the set of Addresses containing register changes.
        """
        ...

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
    def registerAddressSet(self) -> ghidra.program.model.address.AddressSetView: ...
