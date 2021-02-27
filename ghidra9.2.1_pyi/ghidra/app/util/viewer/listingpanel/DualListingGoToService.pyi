import ghidra.app.nav
import ghidra.app.services
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.symbol
import ghidra.program.util
import ghidra.util.task
import java.lang


class DualListingGoToService(object, ghidra.app.services.GoToService):
    """
    This is a GoToService for a dual listing panel. It allows the goTo to occur relative to the
     left or right listing panel of a dual listing panel, since the left and right sides can be
     displaying totally different addresses.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultNavigatable(self) -> ghidra.app.nav.Navigatable: ...

    def getOverrideService(self) -> ghidra.app.services.GoToOverrideService: ...

    @overload
    def goTo(self, goToAddress: ghidra.program.model.address.Address) -> bool: ...

    @overload
    def goTo(self, loc: ghidra.program.util.ProgramLocation) -> bool: ...

    @overload
    def goTo(self, navigatable: ghidra.app.nav.Navigatable, goToAddress: ghidra.program.model.address.Address) -> bool: ...

    @overload
    def goTo(self, currentAddress: ghidra.program.model.address.Address, goToAddress: ghidra.program.model.address.Address) -> bool: ...

    @overload
    def goTo(self, goToAddress: ghidra.program.model.address.Address, program: ghidra.program.model.listing.Program) -> bool: ...

    @overload
    def goTo(self, loc: ghidra.program.util.ProgramLocation, program: ghidra.program.model.listing.Program) -> bool: ...

    @overload
    def goTo(self, navigatable: ghidra.app.nav.Navigatable, loc: ghidra.program.util.ProgramLocation, program: ghidra.program.model.listing.Program) -> bool: ...

    @overload
    def goTo(self, navigatable: ghidra.app.nav.Navigatable, program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address, refAddress: ghidra.program.model.address.Address) -> bool: ...

    @overload
    def goToExternalLocation(self, extLoc: ghidra.program.model.symbol.ExternalLocation, checkNavigationOption: bool) -> bool: ...

    @overload
    def goToExternalLocation(self, navigatable: ghidra.app.nav.Navigatable, extLoc: ghidra.program.model.symbol.ExternalLocation, checkNavigationOption: bool) -> bool: ...

    @overload
    def goToQuery(self, fromAddr: ghidra.program.model.address.Address, queryData: ghidra.app.services.QueryData, listener: ghidra.app.services.GoToServiceListener, monitor: ghidra.util.task.TaskMonitor) -> bool: ...

    @overload
    def goToQuery(self, navigatable: ghidra.app.nav.Navigatable, fromAddr: ghidra.program.model.address.Address, queryData: ghidra.app.services.QueryData, listener: ghidra.app.services.GoToServiceListener, monitor: ghidra.util.task.TaskMonitor) -> bool: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setOverrideService(self, override: ghidra.app.services.GoToOverrideService) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
