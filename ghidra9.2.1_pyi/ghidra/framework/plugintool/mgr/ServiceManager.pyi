from typing import List
import ghidra.framework.plugintool
import ghidra.framework.plugintool.util
import java.lang


class ServiceManager(object):
    """
    Class for managing plugin services. A plugin may provide a service, or
     it may depend on a service. The ServiceManager maintains a list of
     service names and plugins that provide those services. A plugin may
     dynamically add and remove services from the service registry. As services
     are added and removed, all the plugins (ServiceListener)
     in the tool are notified.
    """





    def __init__(self):
        """
        Construct a new Service Registry.
        """
        ...



    def addService(self, interfaceClass: java.lang.Class, service: object) -> None:
        """
        Add the service to the tool. Notify the service listeners if the
         notification indicator is true; otherwise, add the service to a list
         that will be used to notify listeners when notifications are
         turned on again.
        @param interfaceClass class of the service interface being added
        @param service implementation of the service; it may be a plugin or
         may be some object created by the plugin
        @see #setServiceAddedNotificationsOn(boolean)
        """
        ...

    def addServiceListener(self, listener: ghidra.framework.plugintool.util.ServiceListener) -> None:
        """
        Add listener that is notified when services are added or removed.
        @param listener listener to notify
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAllServices(self) -> List[ghidra.framework.plugintool.ServiceInterfaceImplementationPair]:
        """
        Returns a array of all service implementors.
        @return a array of all service implementors
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getService(self, interfaceClass: java.lang.Class) -> object:
        """
        Return the first implementation found for the given service class.
        @param interfaceClass interface class for the service
        @return null if the interfaceClass was not registered
        """
        ...

    def getServices(self, interfaceClass: java.lang.Class) -> List[object]:
        """
        Get an array of objects that implement the given interfaceClass.
        @param interfaceClass interface class for the service
        @return zero length array if the interfaceClass was not registered
        """
        ...

    def hashCode(self) -> int: ...

    def isService(self, serviceInterface: java.lang.Class) -> bool:
        """
        Returns true if the specified <code>serviceInterface</code>
         is a valid service that exists in this service manager.
        @param serviceInterface the service interface
        @return true if the specified <code>serviceInterface</code>
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeService(self, interfaceClass: java.lang.Class, service: object) -> None:
        """
        Remove the service from the tool.
        """
        ...

    def removeServiceListener(self, listener: ghidra.framework.plugintool.util.ServiceListener) -> None:
        """
        Remove the given listener from list of listeners notified when
         services are added or removed.
        @param listener listener to remove
        """
        ...

    def setServiceAddedNotificationsOn(self, b: bool) -> None:
        """
        Set the indicator for whether service listeners should be notified.
         While plugins are being restored from a tool state, this indicator
         is false, as a plugin may not be in the proper state to handle the
         notification.
        @param b true means to notify listeners of the services added to
         the tool
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def allServices(self) -> List[object]: ...

    @property
    def serviceAddedNotificationsOn(self) -> None: ...  # No getter available.

    @serviceAddedNotificationsOn.setter
    def serviceAddedNotificationsOn(self, value: bool) -> None: ...
