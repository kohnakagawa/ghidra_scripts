from typing import List
import db.buffers
import ghidra.framework.client
import ghidra.framework.model
import ghidra.framework.remote
import ghidra.framework.store
import java.lang


class RepositoryAdapter(object, ghidra.framework.client.RemoteAdapterListener):
    """
    RepositoryAdapter provides a persistent wrapper for a remote RepositoryHandle
     which may become invalid if the remote connection were to fail.  Connection recovery is provided
     by any method call which must communicate with the server.
    """





    def __init__(self, serverAdapter: ghidra.framework.client.RepositoryServerAdapter, name: unicode):
        """
        Construct.
        @param serverAdapter persistent server adapter
        @param name repository name
        """
        ...



    def addListener(self, listener: ghidra.framework.client.RemoteAdapterListener) -> None:
        """
        Add a listener to this remote adapter
        @param listener
        """
        ...

    def anonymousAccessAllowed(self) -> bool:
        """
        @return true if anonymous access allowed by this repository
        @throws IOException
        """
        ...

    def checkout(self, folderPath: unicode, itemName: unicode, checkoutType: ghidra.framework.store.CheckoutType, projectPath: unicode) -> ghidra.framework.store.ItemCheckoutStatus: ...

    def connect(self) -> None:
        """
        Attempt to connect to the server.
        """
        ...

    def connectionStateChanged(self, adapter: object) -> None:
        """
        Notification callback when server connection state changes.
        @see ghidra.framework.client.RemoteAdapterListener#connectionStateChanged(java.lang.Object)
        """
        ...

    def createDataFile(self, parentPath: unicode, itemName: unicode) -> None: ...

    def createDatabase(self, parentPath: unicode, itemName: unicode, bufferSize: int, contentType: unicode, fileID: unicode, projectPath: unicode) -> db.buffers.ManagedBufferFileAdapter:
        """
        @see RepositoryHandle#createDatabase(String, String, String, int, String, String)
        """
        ...

    def deleteItem(self, parentPath: unicode, itemName: unicode, version: int) -> None: ...

    def disconnect(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def fileExists(self, folderPath: unicode, itemName: unicode) -> bool: ...

    def folderExists(self, folderPath: unicode) -> bool: ...

    def getCheckout(self, parentPath: unicode, itemName: unicode, checkoutId: long) -> ghidra.framework.store.ItemCheckoutStatus: ...

    def getCheckouts(self, parentPath: unicode, itemName: unicode) -> List[ghidra.framework.store.ItemCheckoutStatus]: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getItem(self, fileID: unicode) -> ghidra.framework.remote.RepositoryItem: ...

    @overload
    def getItem(self, folderPath: unicode, itemName: unicode) -> ghidra.framework.remote.RepositoryItem: ...

    def getItemCount(self) -> int: ...

    def getItemList(self, folderPath: unicode) -> List[ghidra.framework.remote.RepositoryItem]: ...

    def getLength(self, parentPath: unicode, itemName: unicode) -> long: ...

    def getName(self) -> unicode:
        """
        Returns repository name
        """
        ...

    def getOpenFileHandleCount(self) -> int: ...

    def getServer(self) -> ghidra.framework.client.RepositoryServerAdapter:
        """
        Returns server adapter
        """
        ...

    def getServerInfo(self) -> ghidra.framework.model.ServerInfo:
        """
        Returns server information
        """
        ...

    def getServerUserList(self) -> List[unicode]:
        """
        Returns list of all users known to server.
        @throws IOException
        @throws UserAccessException user no longer has any permission to use repository.
        @throws NotConnectedException if server/repository connection is down (user already informed)
        @see RemoteRepositoryHandle#getServerUserList()
        """
        ...

    def getSubfolderList(self, folderPath: unicode) -> List[unicode]: ...

    def getUser(self) -> ghidra.framework.remote.User:
        """
        Returns repository user object.
        @throws UserAccessException user no longer has any permission to use repository.
        @throws NotConnectedException if server/repository connection is down (user already informed)
        @see ghidra.framework.remote.RemoteRepositoryHandle#getUser()
        """
        ...

    def getUserList(self) -> List[ghidra.framework.remote.User]:
        """
        Returns list of repository users.
        @throws IOException
        @throws UserAccessException user no longer has any permission to use repository.
        @throws NotConnectedException if server/repository connection is down (user already informed)
        @see RemoteRepositoryHandle#getUserList()
        """
        ...

    def getVersions(self, parentPath: unicode, itemName: unicode) -> List[ghidra.framework.store.Version]: ...

    def hadUnexpectedDisconnect(self) -> bool:
        """
        Returns true if connection recently was lost unexpectedly
        """
        ...

    def hasCheckouts(self, parentPath: unicode, itemName: unicode) -> bool: ...

    def hashCode(self) -> int: ...

    def isCheckinActive(self, parentPath: unicode, itemName: unicode) -> bool: ...

    def isConnected(self) -> bool:
        """
        Returns true if connected.
        """
        ...

    def moveFolder(self, oldParentPath: unicode, newParentPath: unicode, oldFolderName: unicode, newFolderName: unicode) -> None: ...

    def moveItem(self, oldParentPath: unicode, newParentPath: unicode, oldItemName: unicode, newItemName: unicode) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def openDataFile(self, parentPath: unicode, itemName: unicode, version: int) -> ghidra.framework.store.DataFileHandle: ...

    @overload
    def openDatabase(self, parentPath: unicode, itemName: unicode, checkoutId: long) -> db.buffers.ManagedBufferFileAdapter: ...

    @overload
    def openDatabase(self, parentPath: unicode, itemName: unicode, version: int, minChangeDataVer: int) -> db.buffers.ManagedBufferFileAdapter: ...

    def removeListener(self, listener: ghidra.framework.client.RemoteAdapterListener) -> None:
        """
        Remove a listener from this remote adapter
        @param listener
        """
        ...

    def setFileSystemListener(self, fsListener: ghidra.framework.store.FileSystemListener) -> None:
        """
        Set the file system listener associated with the remote repository.
        @param fsListener file system listener
        """
        ...

    def setUserList(self, users: List[ghidra.framework.remote.User], anonymousAccessAllowed: bool) -> None:
        """
        Set the list of authorized users for this repository.
        @param users list of user and access permissions.
        @param anonymousAccessAllowed true to permit anonymous access (also requires anonymous
         access to be enabled for server)
        @throws UserAccessException
        @throws IOException
        @throws NotConnectedException if server/repository connection is down (user already informed)
        @see RemoteRepositoryHandle#setUserList(User[], boolean)
        """
        ...

    def terminateCheckout(self, folderPath: unicode, itemName: unicode, checkoutId: long, notify: bool) -> None: ...

    def toString(self) -> unicode: ...

    def updateCheckoutVersion(self, parentPath: unicode, itemName: unicode, checkoutId: long, checkoutVersion: int) -> None: ...

    def verifyConnection(self) -> bool:
        """
        Verify that the connection is still valid.
        @return true if the connection is valid; false if the connection needs to be reestablished
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def connected(self) -> bool: ...

    @property
    def fileSystemListener(self) -> None: ...  # No getter available.

    @fileSystemListener.setter
    def fileSystemListener(self, value: ghidra.framework.store.FileSystemListener) -> None: ...

    @property
    def itemCount(self) -> int: ...

    @property
    def name(self) -> unicode: ...

    @property
    def openFileHandleCount(self) -> int: ...

    @property
    def server(self) -> ghidra.framework.client.RepositoryServerAdapter: ...

    @property
    def serverInfo(self) -> ghidra.framework.model.ServerInfo: ...

    @property
    def serverUserList(self) -> List[unicode]: ...

    @property
    def user(self) -> ghidra.framework.remote.User: ...

    @property
    def userList(self) -> List[ghidra.framework.remote.User]: ...
