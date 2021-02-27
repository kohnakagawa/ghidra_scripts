from typing import List
import ghidra.app.nav
import ghidra.app.util.viewer.field
import ghidra.framework.plugintool
import ghidra.program.util
import ghidra.util.classfinder
import java.awt.event
import java.lang


class FieldMouseHandlerExtension(ghidra.app.util.viewer.field.FieldMouseHandler, ghidra.util.classfinder.ExtensionPoint, object):
    """
    NOTE:  ALL FieldMouseHandlerExtension CLASSES MUST END IN "FieldMouseHandler".  If not,
     the ClassSearcher will not find them.

     An interface to signal that it can handle mouse clicks for registered objects.  To register
     the handler you need to return the class that the handler supports in the class array
     returned from #getSupportedProgramLocations().

     New handlers are automatically picked-up by Ghidra upon startup via the
     ClassSearcher mechanism.
    """









    def equals(self, __a0: object) -> bool: ...

    def fieldElementClicked(self, __a0: object, __a1: ghidra.app.nav.Navigatable, __a2: ghidra.program.util.ProgramLocation, __a3: java.awt.event.MouseEvent, __a4: ghidra.framework.plugintool.ServiceProvider) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getSupportedProgramLocations(self) -> List[java.lang.Class]: ...

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
