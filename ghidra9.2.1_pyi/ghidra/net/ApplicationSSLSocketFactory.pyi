from typing import List
import java.io
import java.lang
import java.net
import javax.net
import javax.net.ssl


class ApplicationSSLSocketFactory(javax.net.ssl.SSLSocketFactory):
    """
    ApplicationSSLSocketFactory provides a replacement for the default
     SSLSocketFactory which utilizes the default SSLContext established
     by SSLContextInitializer.
    """





    def __init__(self):
        """
        ApplicationSSLSocketFactory constructor.
         SSLContext initialization will be performed using {@link SSLContextInitializer}.
        """
        ...



    @overload
    def createSocket(self) -> java.net.Socket: ...

    @overload
    def createSocket(self, host: unicode, port: int) -> java.net.Socket: ...

    @overload
    def createSocket(self, host: java.net.InetAddress, port: int) -> java.net.Socket: ...

    @overload
    def createSocket(self, __a0: java.net.Socket, __a1: java.io.InputStream, __a2: bool) -> java.net.Socket: ...

    @overload
    def createSocket(self, host: unicode, port: int, localHost: java.net.InetAddress, localPort: int) -> java.net.Socket: ...

    @overload
    def createSocket(self, address: java.net.InetAddress, port: int, localAddress: java.net.InetAddress, localPort: int) -> java.net.Socket: ...

    @overload
    def createSocket(self, s: java.net.Socket, host: unicode, port: int, autoClose: bool) -> java.net.Socket: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getDefault() -> javax.net.SocketFactory: ...

    def getDefaultCipherSuites(self) -> List[unicode]: ...

    def getSupportedCipherSuites(self) -> List[unicode]: ...

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
    def defaultCipherSuites(self) -> List[unicode]: ...

    @property
    def supportedCipherSuites(self) -> List[unicode]: ...
