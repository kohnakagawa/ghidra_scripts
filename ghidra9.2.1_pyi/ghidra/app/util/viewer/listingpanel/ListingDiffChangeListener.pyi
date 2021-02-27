import java.lang


class ListingDiffChangeListener(object):
    """
    Interface defining a listener that gets notified when the ListingDiff's set of differences
     and unmatched addresses has changed.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def listingDiffChanged(self) -> None:
        """
        Called when the ListingDiff's set of differences and unmatched addresses has changed.
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
