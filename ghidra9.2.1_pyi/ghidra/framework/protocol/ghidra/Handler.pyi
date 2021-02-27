import java.lang
import java.net


class Handler(java.net.URLStreamHandler):
    """
    Handler provides a "ghidra" URL protocol handler which
     corresponds to the GhidraURLConnection implementation.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isSupportedURL(url: java.net.URL) -> bool:
        """
        Determine if the specified url is supported and that any required
         protocol extensions are recognized.
        @param url
        @return true if support ghidra URL
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def registerHandler() -> None:
        """
        Register the "ghidra" URL protocol Handler.
         Alternatively, the protocol handler can be explicitly used when instantiating
         a ghidra URL:
         <pre>
           URL url = new URL(null, "ghidra://myGhidraServer/Test", new ghidra.framework.protocol.ghidra.Handler());
         </pre>
         It is also important that a <code>ClientAuthenticator</code> also be registered.
        @see ClientUtil#setClientAuthenticator(ghidra.framework.client.ClientAuthenticator)
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
