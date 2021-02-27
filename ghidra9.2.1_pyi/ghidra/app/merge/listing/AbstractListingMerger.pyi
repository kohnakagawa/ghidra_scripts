import ghidra.app.merge.listing
import java.lang


class AbstractListingMerger(object, ghidra.app.merge.listing.ListingMerger, ghidra.app.merge.listing.ListingMergeConstants):
    """
    AbstractListingMerger is an abstract class that each type of
     listing merge manager can extend to gain access to commonly needed information
     such as the programs, the listing merge panel,
     Diffs for Latest-Original and My-Original and Latest-My, etc.
    """









    def equals(self, __a0: object) -> bool: ...

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
