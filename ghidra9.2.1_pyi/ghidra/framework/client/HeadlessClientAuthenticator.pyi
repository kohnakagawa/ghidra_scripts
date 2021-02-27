from typing import List
import ghidra.framework.client
import ghidra.framework.remote
import java.awt
import java.lang
import java.net
import javax.security.auth.callback


class HeadlessClientAuthenticator(object, ghidra.framework.client.ClientAuthenticator):
    """
    HeadlessClientAuthenticator provides the ability to install a Ghidra Server
     authenticator needed when operating in a headless mode.
    """









    def equals(self, __a0: object) -> bool: ...

    def getAuthenticator(self) -> java.net.Authenticator: ...

    def getClass(self) -> java.lang.Class: ...

    def getKeyStorePassword(self, keystorePath: unicode, passwordError: bool) -> List[int]: ...

    def getNewPassword(self, parent: java.awt.Component, serverInfo: unicode, username: unicode) -> List[int]: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def installHeadlessClientAuthenticator(username: unicode, keystorePath: unicode, allowPasswordPrompt: bool) -> None:
        """
        Install headless client authenticator for Ghidra Server
        @param username optional username to be used with a Ghidra Server which
         allows username to be specified
        @param keystorePath optional PKI or SSH keystore path.  May also be specified
         as resource path for SSH key.
        @param allowPasswordPrompt if true the user may be prompted for passwords
         via the console (stdin).  Please note that the Java console will echo
         the password entry to the terminal which may be undesirable.
        @throws IOException if error occurs while opening specified keystorePath
        """
        ...

    def isSSHKeyAvailable(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def processPasswordCallbacks(self, title: unicode, serverType: unicode, serverName: unicode, nameCb: javax.security.auth.callback.NameCallback, passCb: javax.security.auth.callback.PasswordCallback, choiceCb: javax.security.auth.callback.ChoiceCallback, anonymousCb: ghidra.framework.remote.AnonymousCallback, loginError: unicode) -> bool: ...

    def processSSHSignatureCallbacks(self, serverName: unicode, nameCb: javax.security.auth.callback.NameCallback, sshCb: ghidra.framework.remote.SSHSignatureCallback) -> bool: ...

    def promptForReconnect(self, parent: java.awt.Component, message: unicode) -> bool: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def SSHKeyAvailable(self) -> bool: ...

    @property
    def authenticator(self) -> java.net.Authenticator: ...
