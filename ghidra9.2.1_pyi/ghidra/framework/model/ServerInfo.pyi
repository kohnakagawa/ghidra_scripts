import java.io
import java.lang


class ServerInfo(object, java.io.Serializable):
    """
    Container for a host name and port number.
    """





    def __init__(self, host: unicode, portNumber: int):
        """
        Construct a new ServerInfo object
        @param host host name
        @param portNumber port number
        """
        ...



    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getPortNumber(self) -> int:
        """
        Get the port number.
        """
        ...

    def getServerName(self) -> unicode:
        """
        Get the server name.
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
    def portNumber(self) -> int: ...

    @property
    def serverName(self) -> unicode: ...
