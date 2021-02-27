import java.lang


class ApplicationKeyStore(object):
    """
    ApplicationKeyStore provides the ability to read X.509 certificates and
     keystores in various formats. Certificate files (e.g., cacerts) may be in a standard
     X.509 form (*.pem, *.crt, *.cer, *.der) or Java JKS (*.jks) form, while keystores
     for client/server may be in a PKCS12 form (*.p12, *.pks, *.pfx) or Java JKS (*.jks) form.
    """





    def __init__(self): ...



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
