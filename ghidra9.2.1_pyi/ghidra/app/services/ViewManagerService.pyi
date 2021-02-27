import ghidra.app.plugin.core.programtree
import ghidra.app.services
import ghidra.program.model.address
import ghidra.program.util
import java.lang


class ViewManagerService(ghidra.app.services.ViewService, object):
    """
    Service to manage generic views; the view controls what shows up in the code
     browser.
    """









    def addToView(self, __a0: ghidra.program.util.ProgramLocation) -> ghidra.program.model.address.AddressSetView: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCurrentView(self) -> ghidra.program.model.address.AddressSetView: ...

    def getCurrentViewProvider(self) -> ghidra.app.plugin.core.programtree.ViewProviderService:
        """
        Get the current view provider.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setCurrentViewProvider(self, viewName: unicode) -> None:
        """
        Set the current view to the provider with the given name.
        @param viewName
        """
        ...

    def toString(self) -> unicode: ...

    def viewNameChanged(self, vps: ghidra.app.plugin.core.programtree.ViewProviderService, oldName: unicode) -> None:
        """
        Notification that a view name has changed.
        @param vps service whose name has changed
        @param oldName old name of the service
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def currentView(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def currentViewProvider(self) -> ghidra.app.plugin.core.programtree.ViewProviderService: ...
