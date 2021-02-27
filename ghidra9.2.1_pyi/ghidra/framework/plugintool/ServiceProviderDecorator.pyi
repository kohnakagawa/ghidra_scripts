import ghidra.framework.plugintool
import ghidra.framework.plugintool.util
import java.lang


class ServiceProviderDecorator(object, ghidra.framework.plugintool.ServiceProvider):








    def addServiceListener(self, listener: ghidra.framework.plugintool.util.ServiceListener) -> None: ...

    @staticmethod
    def createEmptyDecorator() -> ghidra.framework.plugintool.ServiceProviderDecorator: ...

    @staticmethod
    def decorate(delegate: ghidra.framework.plugintool.ServiceProvider) -> ghidra.framework.plugintool.ServiceProviderDecorator: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getService(self, serviceClass: java.lang.Class) -> object: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def overrideService(self, serviceClass: java.lang.Class, service: object) -> None:
        """
        Adds a service that will override any service contained in the delegate
         {@link ServiceProvider}.

         <P>Note: this will not notify any clients that services have been changed.  This means
         that you should call this method before passing this service provider on to your clients.
        @param serviceClass the service class
        @param service the service implementation
        """
        ...

    def removeServiceListener(self, listener: ghidra.framework.plugintool.util.ServiceListener) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
