import docking.widgets.fieldpanel.field
import docking.widgets.fieldpanel.support
import ghidra.program.model.listing
import ghidra.program.util
import java.lang
import javax.swing


class HoverService(object):
    """
    HoverService provides the ability to popup data Windows over a Field viewer
     in response to the mouse hovering over a single Field.
    """









    def componentHidden(self) -> None:
        """
        Provides notification when this hover component is popped-down
        """
        ...

    def componentShown(self) -> None:
        """
        Provides notification when this hover component is popped-up
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getHoverComponent(self, program: ghidra.program.model.listing.Program, programLocation: ghidra.program.util.ProgramLocation, fieldLocation: docking.widgets.fieldpanel.support.FieldLocation, field: docking.widgets.fieldpanel.field.Field) -> javax.swing.JComponent:
        """
        Returns a component to be shown in a popup window that is relevant to the given parameters.
         Null is returned if there is no appropriate information to display.
        @param program the program that is being hovered over.
        @param programLocation the program location where the mouse is hovering.
        @param fieldLocation the precise mouse location within the field viewer
        @param field the field over which the mouse is hovering
        @return The component to be shown for the given location information.
        """
        ...

    def getPriority(self) -> int:
        """
        Returns the priority of this hover service.
        """
        ...

    def hashCode(self) -> int: ...

    def hoverModeSelected(self) -> bool:
        """
        Return whether hover mode is "on."
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def scroll(self, amount: int) -> None:
        """
        If this service's window supports scrolling, scroll by the specified amount.
        @param amount the amount to scroll
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def priority(self) -> int: ...
