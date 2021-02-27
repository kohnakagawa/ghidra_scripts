import ghidra.app.merge.listing
import java.lang


class CodeUnitMerger(ghidra.app.merge.listing.AbstractListingMerger):
    """
    Manages byte and code unit changes and conflicts between the latest versioned
     program and the modified program being checked into version control.
     Indirect conflicts include:

     bytes and code units
     bytes and equates
     code units and equates

     Important: This class is intended to be used only for a single program
     version merge. It should be constructed, followed by an autoMerge(), and lastly
     should call mergeConflicts() passing it ASK_USER for the conflictOption.
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
