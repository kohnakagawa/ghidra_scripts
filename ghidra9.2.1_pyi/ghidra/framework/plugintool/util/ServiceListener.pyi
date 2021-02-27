import java.lang


class ServiceListener(object):
    """
    Notifications for when services are added to or removed from a PluginTool.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def serviceAdded(self, interfaceClass: java.lang.Class, service: object) -> None:
        """
        Notifies the listener that a service has been added to the tool.
        @param interfaceClass the interface class that the given service implements.
        @param service the implementation of the service.
        """
        ...

    def serviceRemoved(self, interfaceClass: java.lang.Class, service: object) -> None:
        """
        Notifies the listener that a service has been removed from the tool.
        @param interfaceClass the interface class that the given service implements.
        @param service the implementation of the service.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
