import ghidra.app.nav
import ghidra.framework.plugintool
import ghidra.program.util
import java.awt.event
import java.lang


class FieldMouseHandler(object):








    def equals(self, __a0: object) -> bool: ...

    def fieldElementClicked(self, clickedObject: object, sourceNavigatable: ghidra.app.nav.Navigatable, programLocation: ghidra.program.util.ProgramLocation, mouseEvent: java.awt.event.MouseEvent, serviceProvider: ghidra.framework.plugintool.ServiceProvider) -> bool:
        """
        Called when a field {@link Field} has been clicked.  The object being passed in may be
         of any type, as returned by the clicked field.  The type is guaranteed to be one of the
         types returned in the call to {@link #getSupportedProgramLocations()}.
        @param clickedObject The object that was clicked
        @param sourceNavigatable The source navigatable that was clicked upon.
        @param programLocation The location at the time the click was made. Due to swing delay, this
         location may not be the same as you would get if you asked the navagatable for the current
         location.SC
        @param mouseEvent The mouse event that triggered the click
        @param serviceProvider A service provider used to access system resources.
        @return true if this handler wishes to have exclusive handling rights to processing the
                 <code>clickedObject</code>
        @see ListingField#getClickedObject(ghidra.util.bean.field.FieldLocation)
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getSupportedProgramLocations(self) -> java.lang.Class:
        """
        Returns an array of types that this handler wishes to handle.
        @return an array of types that this handler wishes to handle.
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
    def supportedProgramLocations(self) -> List[java.lang.Class]: ...
