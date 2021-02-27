import ghidra.program.model.address
import java.lang


class ListingDisplayListener(object):
    """
    Interface for being notified whenever the set of visible addresses change in the listing.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    def visibleAddressesChanged(self, visibleAddresses: ghidra.program.model.address.AddressSetView) -> None:
        """
        Callback whenever the set of visible addresses change in the listing.
        @param visibleAddresses the current set of visible addresses in the listing.  If no
         visible addresses are in the listing view, then an empty AddressSetView will be passed.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
