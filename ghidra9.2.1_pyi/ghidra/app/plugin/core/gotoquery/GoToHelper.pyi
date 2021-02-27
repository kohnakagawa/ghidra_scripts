import ghidra.app.nav
import ghidra.app.plugin.core.navigation
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.symbol
import ghidra.program.util
import java.lang


class GoToHelper(object):




    def __init__(self, __a0: ghidra.framework.plugintool.PluginTool): ...



    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLocation(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address, __a2: ghidra.program.model.address.Address) -> ghidra.program.util.ProgramLocation: ...

    def getOptions(self) -> ghidra.app.plugin.core.navigation.NavigationOptions: ...

    @staticmethod
    def getProgramLocationForAddress(__a0: ghidra.program.model.address.Address, __a1: ghidra.program.model.listing.Program) -> ghidra.program.util.ProgramLocation: ...

    def goTo(self, __a0: ghidra.app.nav.Navigatable, __a1: ghidra.program.util.ProgramLocation, __a2: ghidra.program.model.listing.Program) -> bool: ...

    def goToExternalLocation(self, __a0: ghidra.app.nav.Navigatable, __a1: ghidra.program.model.symbol.ExternalLocation, __a2: bool) -> bool: ...

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
    def options(self) -> ghidra.app.plugin.core.navigation.NavigationOptions: ...
