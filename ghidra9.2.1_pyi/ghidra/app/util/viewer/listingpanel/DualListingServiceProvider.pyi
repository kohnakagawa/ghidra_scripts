import ghidra.framework.plugintool
import ghidra.framework.plugintool.util
import java.lang


class DualListingServiceProvider(object, ghidra.framework.plugintool.ServiceProvider):
    """
    This provides services, but overrides and implements its own goTo for one of the listing
     panels in a dual listing code comparison panel.
     If a goTo service is requested, this provides a goTo service that limits where you can go.
     It constrains the goTo to addresses that are currently in the indicated listing panel of
     the dual listing code comparison panel.
    """









    def addServiceListener(self, listener: ghidra.framework.plugintool.util.ServiceListener) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getService(self, serviceClass: java.lang.Class) -> object: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeServiceListener(self, listener: ghidra.framework.plugintool.util.ServiceListener) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
