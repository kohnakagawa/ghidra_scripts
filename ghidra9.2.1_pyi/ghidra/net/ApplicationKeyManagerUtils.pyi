from typing import List
import ghidra.net
import java.io
import java.lang
import java.security
import java.security.KeyStore
import java.security.cert
import javax.security.auth.x500
import sun.security.x509


class ApplicationKeyManagerUtils(object):
    """
    ApplicationKeyManagerUtils provides public methods for utilizing
     the application PKI key management, including access to trusted issuers
     (i.e., CA certificates), token signing and validation, and the ability to
     generate keystores for testing or when a self-signed certificate will
     suffice.

     NOTE: This class makes direct use of classes within the
     sun.security.x509 package thus breaking portability. While this is
     not preferred, the ability to generate X.509 certificates and keystores
     appears to be absent from the standard java/javax packages.
    """

    DEFAULT_AUTH_TYPE: unicode = u'RSA'
    DEFAULT_SIGNING_ALGORITHM: unicode = u'SHA1withRSA'







    @staticmethod
    def createKeyStore(keyFile: java.io.File, keystoreType: unicode, protectedPassphrase: List[int], alias: unicode, certExtensions: sun.security.x509.CertificateExtensions, dn: unicode, caSignerKeyEntry: java.security.KeyStore.PrivateKeyEntry, durationDays: int) -> java.security.KeyStore:
        """
        Generate self-signed PKI X509 keystore containing both a signing key/cert
         and an encrypting key/cert.  Default certificte extension specifies key usage of
         Signing which is appropriate for SSL DHE or ECDHE cipher suites.
        @param keyFile keystore file or null if not to be stored
        @param keystoreType keystore type (e.g., "JKS", "PKCS12")
        @param protectedPassphrase passphrase for protecting key and keystore
        @param alias for key/cert
        @param certExtensions specifies certificate extensions to be set or null for default
                    key usage extension. Only a single alias may be specified when
                    this argument is not null.
        @param dn distinguished name for principal key holder
        @param caSignerKeyEntry certificate issuer/authority (CA) private key entry or null
                    for self-signed
        @param durationDays number of days from now when certificate shall expire
        @return newly generated keystore
        @throws KeyStoreException error occurred generating keystore
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def exportKeystore(keystore: java.security.KeyStore, outFile: java.io.File, password: List[int]) -> None:
        """
        Export all X.509 certificates contained within keystore to the specified outFile.
        @param keystore
        @param outFile output file
        @param password keystore password
        @throws CertificateException
        @throws NoSuchAlgorithmException
        @throws FileNotFoundException
        @throws KeyStoreException
        @throws CertificateEncodingException
        """
        ...

    @staticmethod
    def exportX509Certificates(keystore: java.security.KeyStore, outFile: java.io.File) -> None:
        """
        Export all X.509 certificates contained within keystore to the specified outFile.
        @param keystore
        @param outFile output file
        @throws IOException
        @throws KeyStoreException
        @throws CertificateEncodingException
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getSignedToken(authorities: List[java.security.Principal], token: List[int]) -> ghidra.net.SignedToken:
        """
        Sign the supplied token byte array using an installed certificate from
         one of the specified authorities
        @param authorities trusted certificate authorities
        @param token token byte array
        @return signed token object
        @throws NoSuchAlgorithmException
        @throws SignatureException
        @throws CertificateException
        """
        ...

    @staticmethod
    def getTrustedIssuers() -> List[javax.security.auth.x500.X500Principal]:
        """
        Returns a list of trusted issuers (i.e., CA certificates) as established
         by the {@link ApplicationTrustManagerFactory}.
        @throws CertificateException
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isMySignature(authorities: List[java.security.Principal], token: List[int], signature: List[int]) -> bool:
        """
        Verify that the specified sigBytes reflect my signature of the specified
         token.
        @param authorities trusted certificate authorities
        @param token byte array token
        @param signature token signature
        @return true if signature is my signature
        @throws NoSuchAlgorithmException
        @throws SignatureException
        @throws CertificateException
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @staticmethod
    def validateClient(certChain: List[java.security.cert.X509Certificate], authType: unicode) -> None:
        """
        Validate a client certificate ensuring that it is not expired and is
         trusted based upon the active trust managers.
        @param certChain X509 certificate chain
        @param authType authentication type (i.e., "RSA")
        @throws CertificateException
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
