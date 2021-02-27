import ghidra.framework.protocol.ghidra
import ghidra.util.classfinder
import java.lang
import java.net


class GhidraProtocolHandler(object, ghidra.util.classfinder.ExtensionPoint):
    """
    GhidraProtocolHandler provides the extension point for
     Ghidra protocol extensions.  A Ghidra protocol extension will be identified
     within by the optional extProtocolName appearing within a Ghidra URL:
      In the absence of a protocol extension
     the DefaultGhidraProtocolHandler will be used.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getConnector(self, ghidraUrl: java.net.URL) -> ghidra.framework.protocol.ghidra.GhidraProtocolConnector:
        """
        Get the Ghidra protocol connector for a Ghidra URL which requires this
         extension.
        @param ghidraUrl Ghidra protocol URL
        @return Ghidra protocol connector
        @throws MalformedURLException if URL is invalid
        """
        ...

    def hashCode(self) -> int: ...

    def isExtensionSupported(self, extProtocolName: unicode) -> bool:
        """
        Determine if this protocol handler is responsible for handling the
         specified named protocol extension.  One handler may support multiple
         protocol extension names (e.g., http and https).
        @param extProtocolName protocol extension name
        @return true if this handler supports the specified protocol extension name
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
