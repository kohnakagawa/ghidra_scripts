import java.lang


class ApplicationTrustManagerFactory(object):
    """
    ApplicationTrustManagerFactory provides the ability to establish
     acceptable certificate authorities to be used with SSL connections and PKI
     authentication.

     The default behavior is for no trust authority to be established, in which case
     SSL peers will not be authenticated.  If CA certificates have been set, all SSL
     connections which leverage this factory will perform peer authentication.  If an error
     occurs while reading the CA certs file, all peer authentication will fail based upon the
     inability to choose a suitable client/server certificate.

     The application X.509 CA certificates file may be in the standard form (*.pem, *.crt,
     *.cer, *.der) or may be in a Java JKS form (*.jks). The path to this file may be
     established in one of two ways using the absolute file path:

     setting the system property ghidra.cacerts (takes precedence)
     setting the user preference ghidra.cacerts


     The application may choose to set the file path automatically based upon the presence of
     a cacerts file at a predetermined location.
    """

    GHIDRA_CACERTS_PATH_PROPERTY: unicode = u'ghidra.cacerts'







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def hasCertificateAuthorities() -> bool:
        """
        Determine if certificate authorities are in place.  If no certificate authorities
         have been specified via the "ghidra.cacerts" property, all certificates will be
         trusted.
        @return true if certificate authorities are in place, else false.
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
