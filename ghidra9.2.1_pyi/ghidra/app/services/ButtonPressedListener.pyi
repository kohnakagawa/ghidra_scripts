import docking.widgets.fieldpanel.support
import ghidra.app.util.viewer.field
import ghidra.program.util
import java.awt.event
import java.lang


class ButtonPressedListener(object):
    """
    Listener that is notified when a mouse button is pressed.
    """









    def buttonPressed(self, location: ghidra.program.util.ProgramLocation, fieldLocation: docking.widgets.fieldpanel.support.FieldLocation, field: ghidra.app.util.viewer.field.ListingField, event: java.awt.event.MouseEvent) -> None:
        """
        Notification that a mouse button was pressed.
        @param location program location when the button was pressed
        @param fieldLocation locations within the FieldPanel
        @param field field from the ListingPanel
        @param event mouse event for the button pressed
        """
        ...

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
