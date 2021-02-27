import ghidra.program.model.listing
import java.lang


class CoordinatedListingPanelListener(object):








    def activeProgramChanged(self, activeProgram: ghidra.program.model.listing.Program) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def listingClosed(self) -> bool:
        """
        Notifies the listener that it's associated listing panel should get closed.
        @return true if the listener actually closes a listing panel.
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
