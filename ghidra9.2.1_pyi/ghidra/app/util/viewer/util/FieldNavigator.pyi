import docking.widgets.fieldpanel.support
import ghidra.app.services
import ghidra.app.util.viewer.field
import ghidra.program.util
import java.awt.event
import java.lang


class FieldNavigator(object, ghidra.app.services.ButtonPressedListener, ghidra.app.services.FieldMouseHandlerService):
    """
    Helper class to navigate to an address when user double clicks in a
     Field.  This class will find FieldMouseHandlerExtensions by using the ClassSearcher.
    """





    def __init__(self, serviceProvider: ghidra.framework.plugintool.ServiceProvider, navigatable: ghidra.app.nav.Navigatable): ...



    def addFieldMouseHandler(self, handler: ghidra.app.util.viewer.field.FieldMouseHandler) -> None: ...

    def buttonPressed(self, location: ghidra.program.util.ProgramLocation, fieldLocation: docking.widgets.fieldpanel.support.FieldLocation, field: ghidra.app.util.viewer.field.ListingField, event: java.awt.event.MouseEvent) -> None: ...

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
