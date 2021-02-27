import ghidra.app.nav
import ghidra.app.services
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.symbol
import ghidra.program.util
import ghidra.util.task
import java.lang


class GoToService(object):
    """
    The GoToService provides a general service for plugins to generate GoTo
     events.  The provider of this service will take care of interfacing with
     any history service that may be available.
    """

    VALID_GOTO_CHARS: List[int] = array('c', '.:*')







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultNavigatable(self) -> ghidra.app.nav.Navigatable: ...

    def getOverrideService(self) -> ghidra.app.services.GoToOverrideService: ...

    @overload
    def goTo(self, goToAddress: ghidra.program.model.address.Address) -> bool:
        """
        Generates a GoTo event to the gotoAddress.
        @param goToAddress the address to goto
        @return true if the go to was successful
        @see #goTo(Address, Program)
        """
        ...

    @overload
    def goTo(self, loc: ghidra.program.util.ProgramLocation) -> bool:
        """
        Generates a GoTo event and handles any history state that needs to be saved.  This method
         will attempt to find the program that contains the given ProgramLocation.
        @param loc location to go to
        @return true if the go to was successful
        @see #goTo(ProgramLocation, Program)
        """
        ...

    @overload
    def goTo(self, navigatable: ghidra.app.nav.Navigatable, goToAddress: ghidra.program.model.address.Address) -> bool: ...

    @overload
    def goTo(self, currentAddress: ghidra.program.model.address.Address, goToAddress: ghidra.program.model.address.Address) -> bool:
        """
        Generates a GoTo event to the goToAddress or symbol.  The currentAddress is used to
         determine if there is a specific symbol reference from the current address.
        @param currentAddress the current address
        @param goToAddress the address to goto
        @return true if the go to was successful
        """
        ...

    @overload
    def goTo(self, goToAddress: ghidra.program.model.address.Address, program: ghidra.program.model.listing.Program) -> bool:
        """
        Generates a GoTo event to the gotoAddress.   This overloaded version of
         {@link #goTo(Address)} uses the given program as the program within which to
         perform the GoTo.  If the given program does not contain the given address, then the
         GoTo will not be performed and false will be returned.  Passing <code>null</code> as the
         <code>program</code> parameter will cause this method to attempt to find
         a program that contains the given ProgramLocation.
        @param goToAddress the address to goto
        @param program the program within which to perform the GoTo
        @return true if the go to was successful
        @see #goTo(Address)
        """
        ...

    @overload
    def goTo(self, loc: ghidra.program.util.ProgramLocation, program: ghidra.program.model.listing.Program) -> bool:
        """
        Generates a GoTo event and handles any history state that needs to be saved.  This
         overloaded version of {@link #goTo(Address)} uses the given program as the program
         within which to perform the GoTo.  If the given program does not contain the given
         address, then the GoTo will not be performed and false will be returned.  Passing
         <code>null</code> as the <code>program</code> parameter will cause this method to attempt to find
         a program that contains the given ProgramLocation.
        @param loc location to go to
        @param program the program within which to perform the GoTo
        @return true if the go to was successful
        @see #goTo(ProgramLocation)
        """
        ...

    @overload
    def goTo(self, navigatable: ghidra.app.nav.Navigatable, loc: ghidra.program.util.ProgramLocation, program: ghidra.program.model.listing.Program) -> bool: ...

    @overload
    def goTo(self, navigatable: ghidra.app.nav.Navigatable, program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address, refAddress: ghidra.program.model.address.Address) -> bool: ...

    @overload
    def goToExternalLocation(self, externalLoc: ghidra.program.model.symbol.ExternalLocation, checkNavigationOption: bool) -> bool:
        """
        Navigate to either the external program location or address linkage location.
         Specific behavior may vary based upon implementation.
        @param externalLoc external location
        @param checkNavigationOption if true the service navigation
         option will be used to determine if navigation to the external program will be
         attempted, or if navigation to the external linkage location within the current
         program will be attempted.  If false, the implementations default behavior
         will be performed.
        @return true if either navigation to the external program or to a
         linkage location was completed successfully.
        """
        ...

    @overload
    def goToExternalLocation(self, navigatable: ghidra.app.nav.Navigatable, externalLoc: ghidra.program.model.symbol.ExternalLocation, checkNavigationOption: bool) -> bool:
        """
        Navigate to either the external program location or address linkage location.
         Specific behavior may vary based upon implementation.
        @param navigatable Navigatable
        @param externalLoc external location
        @param checkNavigationOption if true the service navigation
         option will be used to determine if navigation to the external program will be
         attempted, or if navigation to the external linkage location within the current
         program will be attempted.  If false, the implementations default behavior
         will be performed.
        @return true if either navigation to the external program or to a
         linkage location was completed successfully.
        """
        ...

    @overload
    def goToQuery(self, fromAddr: ghidra.program.model.address.Address, queryData: ghidra.app.services.QueryData, listener: ghidra.app.services.GoToServiceListener, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Parses the input string as either:
         	an address/symbol expression (0x1000+5,  or LAB1000+5)
          a symbol wildcard expression (LAB*,  LAB?100)
          a symbol lookup
          an address lookup

         If the query results in more than one location, a list of locations will be displayed.
         If the query results in only one location, then a goto event will be fired(except for a
         wildcard query in which case a list will still be displayed.

         The listener will be notified after query and will indicate the query status.
        @param fromAddr The address used to determine the scope of the query
        @param queryData the query input data
        @param listener the listener that will be notified when the query completes.
        @param monitor the task monitor
        @return true if the queryInput is found or appears to be a wildcard search.
        """
        ...

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

    @property
    def defaultNavigatable(self) -> ghidra.app.nav.Navigatable: ...

    @property
    def overrideService(self) -> ghidra.app.services.GoToOverrideService: ...

    @overrideService.setter
    def overrideService(self, value: ghidra.app.services.GoToOverrideService) -> None: ...
