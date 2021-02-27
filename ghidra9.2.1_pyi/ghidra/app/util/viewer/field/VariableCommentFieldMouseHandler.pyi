import ghidra.app.nav
import ghidra.app.util.viewer.field
import ghidra.framework.plugintool
import ghidra.program.util
import java.awt.event
import java.lang


class VariableCommentFieldMouseHandler(ghidra.app.util.viewer.field.CommentFieldMouseHandler):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def fieldElementClicked(self, clickedObject: object, sourceNavigatable: ghidra.app.nav.Navigatable, location: ghidra.program.util.ProgramLocation, mouseEvent: java.awt.event.MouseEvent, serviceProvider: ghidra.framework.plugintool.ServiceProvider) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getSupportedProgramLocations(self) -> java.lang.Class: ...

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
