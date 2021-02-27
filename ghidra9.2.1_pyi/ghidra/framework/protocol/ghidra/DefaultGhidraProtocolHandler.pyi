import ghidra.framework.protocol.ghidra
import java.lang
import java.net


class DefaultGhidraProtocolHandler(ghidra.framework.protocol.ghidra.GhidraProtocolHandler):
    """
    DefaultGhidraProtocolHandler provides the default protocol
     handler which corresponds to the original RMI-based Ghidra Server
     and local file-based Ghidra projects.

    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getConnector(self, ghidraUrl: java.net.URL) -> ghidra.framework.protocol.ghidra.GhidraProtocolConnector: ...

    def hashCode(self) -> int: ...

    def isExtensionSupported(self, extProtocolName: unicode) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
