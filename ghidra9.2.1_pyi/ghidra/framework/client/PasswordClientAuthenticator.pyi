from typing import List
import ghidra.framework.client
import ghidra.framework.remote
import java.awt
import java.lang
import java.net
import javax.security.auth.callback


class PasswordClientAuthenticator(object, ghidra.framework.client.ClientAuthenticator):
    """
    PasswordClientAuthenticator provides a fixed username/password
     authentication response when connecting to any Ghidra Server or accessing
     a protected PKI keystore.  The use of this authenticator is intended for
     headless applications in which the user is unable to respond to such
     prompts.  SSH authentication is not currently supported.  Anonymous user
     access is not supported.

     If a PKI certificate has been installed, a password may be required
     to access the certificate keystore independent of any other password which may be required
     for accessing SSH keys or server password authentication.  In such headless situations,
     the PKI certificate path/password should be specified via a property since it is unlikely
     that the same password will apply.
    """





    @overload
    def __init__(self, password: unicode): ...

    @overload
    def __init__(self, username: unicode, password: unicode): ...



    def equals(self, __a0: object) -> bool: ...

    def getAuthenticator(self) -> java.net.Authenticator: ...

    def getClass(self) -> java.lang.Class: ...

    def getKeyStorePassword(self, keystorePath: unicode, passwordError: bool) -> List[int]: ...

    def getNewPassword(self, parent: java.awt.Component, serverInfo: unicode, user: unicode) -> List[int]: ...

    def hashCode(self) -> int: ...

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
