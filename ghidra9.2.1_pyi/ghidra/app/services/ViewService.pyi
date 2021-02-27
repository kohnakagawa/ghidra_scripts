import ghidra.program.model.address
import ghidra.program.util
import java.lang


class ViewService(object):
    """
    Base interface class for the view providers and view manager service.
    """









    def addToView(self, loc: ghidra.program.util.ProgramLocation) -> ghidra.program.model.address.AddressSetView:
        """
        Add the view that corresponds to the given program location.
        @param loc program location to be added to the view
        @return new addressSet for the added view
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCurrentView(self) -> ghidra.program.model.address.AddressSetView:
        """
        Get the current view.
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
    def currentView(self) -> ghidra.program.model.address.AddressSetView: ...
