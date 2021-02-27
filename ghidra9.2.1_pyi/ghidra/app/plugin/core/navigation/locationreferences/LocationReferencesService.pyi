import ghidra.app.nav
import ghidra.program.util
import ghidra.util
import java.lang


class LocationReferencesService(object):
    MENU_GROUP: unicode = u'References'







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getHelpLocation(self) -> ghidra.util.HelpLocation: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def showReferencesToLocation(self, __a0: ghidra.program.util.ProgramLocation, __a1: ghidra.app.nav.Navigatable) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def helpLocation(self) -> ghidra.util.HelpLocation: ...
