import java.lang


class SignedToken(object):
    """
    SignedToken provides the result of a signed token byte array.
    """

    algorithm: unicode
    certChain: List[java.security.cert.X509Certificate]
    signature: List[int]
    token: List[int]







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

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
