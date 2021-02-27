from typing import List
import java.io
import java.lang
import javax.security.auth.callback


class SSHSignatureCallback(object, javax.security.auth.callback.Callback, java.io.Serializable):
    """
    SSHSignatureCallback provides a Callback implementation used
     to perform SSH authentication.  This callback is instantiated
     by the server with a random token which must be signed using the
     user's SSH private key.

     It is the responsibility of the callback handler to invoke the
     sign method and return this object in response
     to the callback.
    """

    serialVersionUID: long = 0x1L



    def __init__(self, token: List[int], serverSignature: List[int]):
        """
        Construct callback with a random token to be signed by the client.
        @param token random bytes to be signed
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getServerSignature(self) -> List[int]:
        """
        @return the server's signature of the token bytes.
        """
        ...

    def getSignature(self) -> List[int]:
        """
        @return signed token bytes set by callback handler.
        """
        ...

    def getToken(self) -> List[int]:
        """
        @return token to be signed using user certificate.
        """
        ...

    def hashCode(self) -> int: ...

    def isSigned(self) -> bool:
        """
        @return true if callback has been signed
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def sign(self, sshPrivateKey: object) -> None:
        """
        Sign this challenge with the specified SSH private key.
        @param sshPrivateKey RSAPrivateKey or DSAPrivateKey
        @throws IOException if signature generation failed
        @see RSAPrivateKey
        @see DSAPrivateKey
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
    def serverSignature(self) -> List[int]: ...

    @property
    def signature(self) -> List[int]: ...

    @property
    def signed(self) -> bool: ...

    @property
    def token(self) -> List[int]: ...
