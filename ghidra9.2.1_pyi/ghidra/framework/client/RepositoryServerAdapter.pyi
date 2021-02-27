from typing import List
import ghidra.framework.client
import ghidra.framework.model
import java.lang


class RepositoryServerAdapter(object):
    """
    RepositoryServerAdapter provides a persistent wrapper for a
     RepositoryServerHandle which may become invalid if the
     remote connection were to fail.
    """









    def addListener(self, listener: ghidra.framework.client.RemoteAdapterListener) -> None:
        """
        Add a listener to this remote adapter
        @param listener
        """
        ...

    def anonymousAccessAllowed(self) -> bool:
        """
        @return true if server allows anonymous access.
         Individual repositories must grant anonymous access separately.
        @throws IOException
        @throws NotConnectedException if server connection is down (user already informed)
        @see ghidra.framework.remote.RemoteRepositoryServerHandle#anonymousAccessAllowed()
        """
        ...

    def canSetPassword(self) -> bool:
        """
        Returns true if this server allows the user to change their password.
        @see ghidra.framework.remote.RemoteRepositoryServerHandle#canSetPassword()
        """
        ...

    def connect(self) -> bool:
        """
        Attempt to connect or re-connect to the server.
        @return true if connect successful, false if cancelled by user
        @throws NotConnectedException if connect failed (error will be displayed to user)
        """
        ...

    def createRepository(self, name: unicode) -> ghidra.framework.client.RepositoryAdapter:
        """
        Create a new repository on the server.
        @param name repository name.
        @return handle to new repository.
        @throws DuplicateNameException
        @throws UserAccessException
        @throws IOException
        @throws NotConnectedException if server connection is down (user already informed)
        @see ghidra.framework.remote.RemoteRepositoryServerHandle#createRepository(String)
        """
        ...

    def deleteRepository(self, name: unicode) -> None:
        """
        Delete a repository.
        @param name repository name.
        @throws UserAccessException
        @throws IOException
        @throws NotConnectedException if server connection is down (user already informed)
        @see ghidra.framework.remote.RemoteRepositoryServerHandle#deleteRepository(java.lang.String)
        """
        ...

    def disconnect(self) -> None:
        """
        Force disconnect with server
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAllUsers(self) -> List[unicode]:
        """
        Returns a list of all known users.
        @throws IOException
        @throws NotConnectedException if server connection is down (user already informed)
        @see ghidra.framework.remote.RemoteRepositoryServerHandle#getAllUsers()
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getRepository(self, name: unicode) -> ghidra.framework.client.RepositoryAdapter:
        """
        Get a handle to an existing repository.  The repository adapter is
         initially disconnected - the connect() method or another repository
         action method must be invoked to establish a repository connection.
        @param name repository name.
        @return repository handle or null if repository not found.
        """
        ...

    def getRepositoryNames(self) -> List[unicode]:
        """
        Returns a list of all repository names defined to the server.
        @throws IOException
        @throws NotConnectedException if server connection is down (user already informed)
        @see ghidra.framework.remote.RemoteRepositoryServerHandle#getRepositoryNames()
        """
        ...

    def getServerInfo(self) -> ghidra.framework.model.ServerInfo:
        """
        Returns server information.  May be null if using fixed RepositoryServerHandle.
        """
        ...

    def getUser(self) -> unicode:
        """
        Returns user's server login identity
        """
        ...

    def hashCode(self) -> int: ...

    def isCancelled(self) -> bool:
        """
        Returns true if the connection was cancelled by the user.
        @return try if cancelled by user
        """
        ...

    def isConnected(self) -> bool:
        """
        Returns true if connected.
        """
        ...

    def isReadOnly(self) -> bool:
        """
        @return true if user has restricted read-only access to server (e.g., anonymous user)
        @throws IOException
        @throws NotConnectedException if server connection is down (user already informed)
        @see ghidra.framework.remote.RemoteRepositoryServerHandle#isReadOnly()
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeListener(self, listener: ghidra.framework.client.RemoteAdapterListener) -> None:
        """
        Remove a listener from this remote adapter
        @param listener
        """
        ...

    def setPassword(self, saltedSHA256PasswordHash: List[int]) -> bool:
        """
        Set the simple password for the user.
        @param saltedSHA256PasswordHash hex character representation of salted SHA256 hash of the password
        @return true if password changed
        @throws IOException if user data can't be written to file
        @throws NotConnectedException if server connection is down (user already informed)
        @see ghidra.framework.remote.RemoteRepositoryServerHandle#setPassword(char[])
        @see ghidra.util.HashUtilities#getSaltedHash(String, char[]) HashUtilities.getSaltedHash("SHA-256", char[])
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
    def allUsers(self) -> List[unicode]: ...

    @property
    def cancelled(self) -> bool: ...

    @property
    def connected(self) -> bool: ...

    @property
    def password(self) -> None: ...  # No getter available.

    @password.setter
    def password(self, value: List[int]) -> None: ...

    @property
    def readOnly(self) -> bool: ...

    @property
    def repositoryNames(self) -> List[unicode]: ...

    @property
    def serverInfo(self) -> ghidra.framework.model.ServerInfo: ...

    @property
    def user(self) -> unicode: ...
