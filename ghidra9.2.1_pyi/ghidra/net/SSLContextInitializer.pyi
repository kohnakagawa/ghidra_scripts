import ghidra.framework
import java.lang
import javax.net.ssl


class SSLContextInitializer(object, ghidra.framework.ModuleInitializer):
    """
    Initialize the default SSLContext for use by SSL connections (e.g., https).
     It is the responsibility of the Application to properly invoke this initializer
     so that the default SSLContext may be established. While HTTPS URL connections
     will make use of this default SSLContext, other SSL connections may need to
     specify the ApplicationSSLSocketFactory to leverage the applications
     default SSLContext.
    """






    class HttpsHostnameVerifier(object, javax.net.ssl.HostnameVerifier):




        def __init__(self): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def toString(self) -> unicode: ...

        def verify(self, __a0: unicode, __a1: javax.net.ssl.SSLSession) -> bool: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode: ...

    def hashCode(self) -> int: ...

    @overload
    @staticmethod
    def initialize() -> bool:
        """
        Initialize default SSLContext
        @return true if successful, else false (see logged error)
        """
        ...

    @overload
    @staticmethod
    def initialize(reset: bool) -> bool:
        """
        Initialize default SSLContext with optional reset.
         This method is primarily intended for testing.
        @param reset if true a complete reset will be done to force use of
         any new certificate or keystores previously used.
        @return true if successful, else false (see logged error)
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def run(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def name(self) -> unicode: ...
