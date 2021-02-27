import java.lang


class RMIServerPortFactory(object):




    def __init__(self, basePort: int):
        """
        Construct port factory using specified basePort
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getRMIRegistryPort(self) -> int:
        """
        Returns RMI Registry port
        """
        ...

    def getRMISSLPort(self) -> int:
        """
        Returns the SSL-protected RMI port.
        """
        ...

    def getStreamPort(self) -> int:
        """
        Returns the SSL Stream port
        """
        ...

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
    def RMIRegistryPort(self) -> int: ...

    @property
    def RMISSLPort(self) -> int: ...

    @property
    def streamPort(self) -> int: ...
