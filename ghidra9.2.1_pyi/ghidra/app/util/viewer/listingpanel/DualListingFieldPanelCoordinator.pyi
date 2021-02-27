import docking.widgets.fieldpanel
import docking.widgets.fieldpanel.listener
import ghidra.program.util
import java.lang


class DualListingFieldPanelCoordinator(docking.widgets.fieldpanel.listener.ViewListener, object):
    """
    Coordinates the locations between the left and right sides of a dual listing panel.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def leftLocationChanged(self, leftLocation: ghidra.program.util.ProgramLocation) -> None:
        """
        Method that gets called when the location changes in the left side's program listing.
        @param leftLocation the new location in the left side.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def rightLocationChanged(self, rightLocation: ghidra.program.util.ProgramLocation) -> None:
        """
        Method that gets called when the location changes in the right side's program listing.
        @param rightLocation the new location in the right side.
        """
        ...

    def toString(self) -> unicode: ...

    def viewChanged(self, __a0: docking.widgets.fieldpanel.FieldPanel, __a1: long, __a2: int, __a3: int) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
