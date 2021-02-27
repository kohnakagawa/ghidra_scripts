import ghidra.app.merge.listing
import java.lang


class AbstractFunctionMerger(object, ghidra.app.merge.listing.ListingMergeConstants):
    """
    Abstract class that other function mergers can extend to get basic constants and methods
     for merging function changes.
     Important: This class is intended to be used only for a single program
     version merge.
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
