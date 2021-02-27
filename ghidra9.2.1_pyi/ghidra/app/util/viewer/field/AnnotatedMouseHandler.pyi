import ghidra.framework.plugintool
import ghidra.program.util
import java.awt.event
import java.lang


class AnnotatedMouseHandler(object):
    """
    An interface for handling mouse clicks on ghidra.util.bean.field.AnnotatedTextFieldElements.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def handleMouseClick(self, location: ghidra.program.util.ProgramLocation, mouseEvent: java.awt.event.MouseEvent, serviceProvider: ghidra.framework.plugintool.ServiceProvider) -> bool:
        """
        Handles a mouse click for the given program location on an {@link ghidra.util.bean.field.AnnotatedTextFieldElement}.
        @param location The program location for the click
        @param mouseEvent The mouse event that triggered the mouse click
        @param serviceProvider A service provider used to access system services while processing
                the mouse click
        @return true if the handler wants to be the only handler processing the click.
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
