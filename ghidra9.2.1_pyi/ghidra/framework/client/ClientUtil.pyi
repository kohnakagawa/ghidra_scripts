import ghidra.framework.client
import ghidra.framework.remote
import java.awt
import java.lang


class ClientUtil(object):
    """
    ClientUtil allows a user to connect to a Repository Server and obtain its handle.
    """









    @staticmethod
    def changePassword(parent: java.awt.Component, handle: ghidra.framework.remote.RepositoryServerHandle, serverInfo: unicode) -> None:
        """
        Prompt user and change password on server (not initiated by user).
        @param parent dialog parent
        @param handle server handle
        @param serverInfo server information
        @throws IOException
        """
        ...

    @staticmethod
    def checkGhidraServer(host: unicode, port: int) -> None:
        """
        Connect to a Ghidra Server and verify compatibility.  This method can be used
         to affectively "ping" the Ghidra Server to verify the ability to connect.
         NOTE: Use of this method when PKI authentication is enabled is not supported.
        @param host server hostname
        @param port first Ghidra Server port (0=use default)
        @throws IOException thrown if an IO Error occurs (e.g., server not found).
        @throws RemoteException if server interface is incompatible or another server-side
         error occurs.
        """
        ...

    @staticmethod
    def clearRepositoryAdapter(host: unicode, port: int) -> None:
        """
        Eliminate the specified repository server from the connection cache
        @param host host name or IP address
        @param port port (0: use default port)
        @throws IOException
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getClientAuthenticator() -> ghidra.framework.client.ClientAuthenticator:
        """
        Get the currently installed client authenticator.  If one has not been
         installed, this will trigger the installation of a default instance.
        @return current client authenticator
        """
        ...

    @overload
    @staticmethod
    def getRepositoryServer(host: unicode, port: int) -> ghidra.framework.client.RepositoryServerAdapter:
        """
        Connect to a Repository Server and obtain a handle to it.
         Based upon the server authentication requirements, the user may be
         prompted for a password via a Swing dialog.  If a previous connection
         attempt to this server failed, the adapter may be returned in a
         disconnected state.
        @param host server name or address
        @param port server port, 0 indicates that default port should be used.
        @return repository server adapter
        """
        ...

    @overload
    @staticmethod
    def getRepositoryServer(host: unicode, port: int, forceConnect: bool) -> ghidra.framework.client.RepositoryServerAdapter:
        """
        Connect to a Repository Server and obtain a handle to it.
         Based upon the server authentication requirements, the user may be
         prompted for a password via a Swing dialog.
        @param host server name or address
        @param port server port, 0 indicates that default port should be used.
        @param forceConnect if true and the server adapter is disconnected, an
         attempt will be made to reconnect.
        @return repository server handle
        """
        ...

    @staticmethod
    def getUserName() -> unicode:
        """
        Returns default user login name.  Actual user name used by repository
         should be obtained from RepositoryServerAdapter.getUser
        """
        ...

    @overload
    @staticmethod
    def handleException(repository: ghidra.framework.client.RepositoryAdapter, exc: java.lang.Exception, operation: unicode, parent: java.awt.Component) -> None:
        """
        Displays an error dialog appropriate for the given exception. If the exception is a
         ConnectException or NotConnectedException, a prompt to reconnect to the Ghidra Server
         is displayed. The message states that the operation may have to be retried due to the
         failed connection.
        @param repository may be null if the exception is not a RemoteException
        @param exc exception that occurred
        @param operation operation that was being done when the exception occurred; this string
         is be used in the message for the error dialog if one should be displayed
        @param parent parent of the error dialog
        """
        ...

    @overload
    @staticmethod
    def handleException(repository: ghidra.framework.client.RepositoryAdapter, exc: java.lang.Exception, operation: unicode, mustRetry: bool, parent: java.awt.Component) -> None:
        """
        Displays an error dialog appropriate for the given exception. If the exception is a
         ConnectException or NotConnectedException, a prompt to reconnect to the Ghidra Server
         is displayed.
        @param repository may be null if the exception is not a RemoteException
        @param exc exception that occurred
        @param operation operation that was being done when the exception occurred; this string
         is be used in the message for the error dialog if one should be displayed
        @param mustRetry true if the message should state that the user should retry the operation
         because it may not have succeeded (if the exception was because a RemoteException); there
         may be cases where the operation succeeded; as a result of the operation, a bad connection
         to the server was detected (e.g., save a file). Note: this parameter is ignored if the
         exception is not a ConnectException or NotConnectedException.
        @param parent parent of the error dialog
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isSSHKeyAvailable() -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def promptForReconnect(repository: ghidra.framework.client.RepositoryAdapter, parent: java.awt.Component) -> None:
        """
        Prompt the user to reconnect to the Ghidra Server.
        @param repository repository to connect to
        @param parent parent of the dialog
        """
        ...

    @staticmethod
    def setClientAuthenticator(authenticator: ghidra.framework.client.ClientAuthenticator) -> None:
        """
        Set client authenticator
        @param authenticator
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
