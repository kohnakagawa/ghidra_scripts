import ghidra.security
import java.lang
import javax.security.auth.x500


class ApplicationKeyManagerFactory(object):
    """
    ApplicationKeyManagerFactory provides application keystore management
     functionality and the ability to generate X509KeyManager's for use with an SSLContext
     or other PKI related operations.  Access to keystore data (other than keystore path)
     is restricted to package access.  Certain public operations are exposed via the
     ApplicationKeyManagerUtils class.
    """

    CERTIFICATE_FILE_FILTER: ghidra.util.filechooser.GhidraFileFilter = ghidra.util.filechooser.ExtensionFileFilter@79bf6696
    DEFAULT_PASSWORD: unicode = u'changeme'
    KEYSTORE_PASSWORD_PROPERTY: unicode = u'ghidra.password'
    KEYSTORE_PATH_PROPERTY: unicode = u'ghidra.keystore'







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getKeyStore() -> unicode:
        """
        Get the keystore path associated with the active key manager or the
         preferred keystore path if not yet initialized.
        """
        ...

    @staticmethod
    def getPreferredKeyStore() -> unicode:
        """
        If the system property <i>ghidra.keystore</i> takes precedence in establishing
         the ketsore.  If using a GUI and the system property has not been set, the
         user preference with the same name will be used.
        @return active keystore path or null if currently not running with a keystore or
         one has not been set.
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def initialize() -> bool:
        """
        Initialize key manager if needed.  Doing this explicitly independent of an SSL connection
         allows application to bail before initiating connection.  This will get handshake failure
         if user forgets keystore password or other keystore problem.
        @return true if key manager initialized, otherwise false
        """
        ...

    @staticmethod
    def invalidateKeyManagers() -> None:
        """
        Invalidate the key managers associated with this factory
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def setDefaultIdentity(identity: javax.security.auth.x500.X500Principal) -> None:
        """
        Set the default self-signed principal identity to be used during initialization
         if no keystore defined.  Current application key manager will be invalidated.
        @param identity if not null and a KeyStore path has not be set, this
         identity will be used to generate a self-signed certificate and private key
         (NOTE: this is intended for server use only when client will not be performing
         CA validation).
        """
        ...

    @staticmethod
    def setKeyStore(path: unicode, savePreference: bool) -> None:
        """
        Set user keystore file path (e.g., certificate file with private key).
         This method will have no effect if the keystore had been set via the system
         property and an error will be displayed.  Otherwise, the keystore will
         be updated and the key manager re-initialized.  The user preference will be
         updated unless a failure occurred while attempting to open the keystore.
         This change will take immediate effect for the current executing application,
         however, it may still be superseded by a system property setting when running
         the application in the future. See {@link #getKeyStore()}.
        @param path keystore file path
        @param savePreference if true will be saved as user preference
        @throws IOException if file or certificate error occurs
        """
        ...

    @staticmethod
    def setKeyStorePasswordProvider(provider: ghidra.security.KeyStorePasswordProvider) -> None:
        """
        Set the active keystore password provider
        @param provider keystore password provider
        """
        ...

    def toString(self) -> unicode: ...

    @staticmethod
    def usingGeneratedSelfSignedCertificate() -> bool:
        """
        Determine if active key manager is utilizing a generated self-signed certificate.
        @return true if using self-signed certificate.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
