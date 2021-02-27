from typing import List
import ghidra.framework.remote
import ghidra.security
import java.awt
import java.lang
import java.net
import javax.security.auth.callback


class ClientAuthenticator(ghidra.security.KeyStorePasswordProvider, object):








    def equals(self, __a0: object) -> bool: ...

    def getAuthenticator(self) -> java.net.Authenticator:
        """
        Get a standard Java authenticator for HTTP and other standard network connections
        @return authenticator object
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getKeyStorePassword(self, __a0: unicode, __a1: bool) -> List[int]: ...

    def getNewPassword(self, parent: java.awt.Component, serverInfo: unicode, username: unicode) -> List[int]:
        """
        Get new user password
        @param parent dialog parent component or null if not applicable
        @param serverInfo server host info
        @param username
        @return new password or null if password should not be changed,
         if not null array will be cleared by caller
        """
        ...

    def hashCode(self) -> int: ...

    def isSSHKeyAvailable(self) -> bool:
        """
        @return true if SSH private key is available for authentication
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def processPasswordCallbacks(self, title: unicode, serverType: unicode, serverName: unicode, nameCb: javax.security.auth.callback.NameCallback, passCb: javax.security.auth.callback.PasswordCallback, choiceCb: javax.security.auth.callback.ChoiceCallback, anonymousCb: ghidra.framework.remote.AnonymousCallback, loginError: unicode) -> bool:
        """
        Process Ghidra Server password authentication callbacks.
        @param title password prompt title if GUI is used
        @param serverType type of server (label associated with serverName)
        @param serverName name of server
        @param nameCb provides storage for user login name.  A null indicates
         that the default user name will be used, @see ClientUtil#getUserName()
        @param passCb provides storage for user password, @see PasswordCallback#setPassword(char[])
        @param choiceCb specifies choice between NT Domain authentication (index=0) and local password
         file authentication (index=1).  Set selected index to specify authenticator to be used,
        @param anonymousCb may be used to request anonymous read-only access to
         the server.  A null is specified if anonymous access has not been enabed on the server.
        @param loginError previous login error message or null for first attempt
        @see ChoiceCallback#setSelectedIndex(int) A null is specified if no choice is available (password authenticator determined by server configuration).
        @see AnonymousCallback#setAnonymousAccessRequested(boolean)
        @return
        """
        ...

    def processSSHSignatureCallbacks(self, serverName: unicode, nameCb: javax.security.auth.callback.NameCallback, sshCb: ghidra.framework.remote.SSHSignatureCallback) -> bool:
        """
        Process Ghidra Server SSH authentication callbacks.
        @param serverName name of server
        @param nameCb provides storage for user login name.  A null indicates
         that the default user name will be used, @see ClientUtil#getUserName().
        @param sshCb provides authentication token to be signed with private key, @see SSHAuthenticationCallback#sign(SSHPrivateKey)
        @return
        """
        ...

    def promptForReconnect(self, parent: java.awt.Component, message: unicode) -> bool:
        """
        Prompt user for reconnect
        @param parent dialog parent component or null if not applicable
        @param message
        @return return true if reconnect should be attempted
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
    def SSHKeyAvailable(self) -> bool: ...

    @property
    def authenticator(self) -> java.net.Authenticator: ...
