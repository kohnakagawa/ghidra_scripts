import ghidra.security
import java.io
import java.lang


class SSHKeyManager(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    @staticmethod
    def getSSHPrivateKey(sshPrivateKeyFile: java.io.File) -> object:
        """
        Return the SSH private key corresponding to the specified key file.
         If the specified key file is encrypted the currently installed password
         provider will be used to obtain the decrypt password.
        @param sshPrivateKeyFile
        @return RSAPrivateKey or DSAPrivateKey
        @throws FileNotFoundException key file not found
        @throws IOException if key file not found or key parse failed
        @see RSAPrivateKey
        @see DSAPrivateKey
        """
        ...

    @overload
    @staticmethod
    def getSSHPrivateKey(sshPrivateKeyIn: java.io.InputStream) -> object:
        """
        Return the SSH private key corresponding to the specified key input stream.
         If the specified key is encrypted the currently installed password
         provider will be used to obtain the decrypt password.
        @param sshPrivateKeyIn
        @return RSAPrivateKey or DSAPrivateKey
        @throws FileNotFoundException key file not found
        @throws IOException if key file not found or key parse failed
        @see RSAPrivateKey
        @see DSAPrivateKey
        """
        ...

    @staticmethod
    def getSSHPublicKey(sshPublicKeyFile: java.io.File) -> object:
        """
        Attempt to instantiate an SSH public key from the specified file
         which contains a single public key.
        @param sshPublicKeyFile
        @return RSAPublicKey or DSAPublicKey
        @throws FileNotFoundException key file not found
        @throws IOException if key file not found or key parse failed
        @see RSAPublicKey
        @see DSAPublicKey
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def setProtectedKeyStorePasswordProvider(provider: ghidra.security.KeyStorePasswordProvider) -> None:
        """
        Set PKI protected keystore password provider
        @param provider
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
