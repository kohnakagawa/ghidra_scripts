import java.lang


class InetNameLookup(object):








    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getCanonicalHostName(host: unicode) -> unicode:
        """
        Gets the fully qualified domain name for this IP address or hostname.
         Best effort method, meaning we may not be able to return
         the FQDN depending on the underlying system configuration.
        @param host IP address or hostname
        @return the fully qualified domain name for this IP address,
            or if the operation is not allowed/fails
            the original host name specified.
        @throws UnknownHostException the forward lookup of the specified address
         failed
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isEnabled() -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def setDisableOnFailure(state: bool) -> None: ...

    @staticmethod
    def setLookupEnabled(enable: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
