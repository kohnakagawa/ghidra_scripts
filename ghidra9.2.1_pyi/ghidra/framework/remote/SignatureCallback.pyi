from typing import List
import java.io
import java.lang
import java.security
import java.security.cert
import javax.security.auth.callback


class SignatureCallback(object, javax.security.auth.callback.Callback, java.io.Serializable):
    """
    SignatureCallback provides a Callback implementation used
     to perform PKI authentication.  This callback is instantiated
     by the server with a random token which must be signed using the
     user's certificate which contains one of the recognizedAuthorities
     within it certificate chain.

     It is the responsibility of the callback handler to invoke the
     sign(X509Certificate[], byte[]) and return this object in response
     to the callback.
    """

    serialVersionUID: long = 0x1L



    def __init__(self, recognizedAuthorities: List[javax.security.auth.x500.X500Principal], token: List[int], serverSignature: List[int]):
        """
        Construct callback with a random token to be signed by the client.
        @param recognizedAuthorities list of CA's from which one must occur
         within the certificate chain of the signing certificate.
        @param token random bytes to be signed
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getCertificateChain(self) -> List[java.security.cert.X509Certificate]:
        """
        Returns certificate chain used to sign token.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getRecognizedAuthorities(self) -> List[java.security.Principal]:
        """
        Returns list of approved certificate authorities.
        """
        ...

    def getServerSignature(self) -> List[int]:
        """
        Returns the server's signature of the token bytes.
        """
        ...

    def getSigAlg(self) -> unicode: ...

    def getSignature(self) -> List[int]:
        """
        Returns signed token bytes set by callback handler.
        """
        ...

    def getToken(self) -> List[int]:
        """
        Returns token to be signed using user certificate.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def sign(self, sigCertChain: List[java.security.cert.X509Certificate], certSignature: List[int]) -> None:
        """
        Set token signature data.  Method must be invoked by
         callback handler.
        @param sigCertChain certificate chain used to sign token.
        @param certSignature token signature
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
    def certificateChain(self) -> List[java.security.cert.X509Certificate]: ...

    @property
    def recognizedAuthorities(self) -> List[java.security.Principal]: ...

    @property
    def serverSignature(self) -> List[int]: ...

    @property
    def sigAlg(self) -> unicode: ...

    @property
    def signature(self) -> List[int]: ...

    @property
    def token(self) -> List[int]: ...
