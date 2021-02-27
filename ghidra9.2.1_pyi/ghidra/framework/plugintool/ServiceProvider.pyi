import ghidra.framework.plugintool.util
import java.lang


class ServiceProvider(object):
    """
    Interface for providing Services
    """









    def addServiceListener(self, listener: ghidra.framework.plugintool.util.ServiceListener) -> None:
        """
        Adds a listener that will be called as services are added and removed from this
         ServiceProvider.
        @param listener The listener to add.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getService(self, serviceClass: java.lang.Class) -> object:
        """
        Returns the Service object that implements the given service interface.
        @param serviceClass the interface class.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeServiceListener(self, listener: ghidra.framework.plugintool.util.ServiceListener) -> None:
        """
        Removes the given listener from this ServiceProvider.  This method does nothing if the
         given listener is not contained by this ServiceProvider.
        @param listener
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
