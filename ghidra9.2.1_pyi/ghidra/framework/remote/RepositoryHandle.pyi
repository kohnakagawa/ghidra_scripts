from typing import List
import db.buffers
import ghidra.framework.remote
import ghidra.framework.store
import java.lang


class RepositoryHandle(object):
    """
    RepositoryHandle provides access to a repository.
    """

    CLIENT_CHECK_PERIOD: int = 30000







    def anonymousAccessAllowed(self) -> bool:
        """
        @return true if anonymous access allowed by this repository
        @throws IOException if an IO error occurs
        """
        ...

    def checkout(self, parentPath: unicode, itemName: unicode, checkoutType: ghidra.framework.store.CheckoutType, projectPath: unicode) -> ghidra.framework.store.ItemCheckoutStatus:
        """
        Perform a checkout on the specified item.
        @param parentPath parent folder path
        @param itemName name of item
        @param checkoutType checkout type.  If exclusive or transient, checkout is only successful
         if no other checkouts exist.  No new checkouts of item will be permitted while an
         exclusive/transient checkout is active.
        @param projectPath path of user's project
        @return checkout data
        @throws IOException if an IO error occurs
        """
        ...

    def close(self) -> None:
        """
        Notification to server that client is dropping handle.
        @throws IOException if error occurs
        """
        ...

    def createDatabase(self, parentPath: unicode, itemName: unicode, fileID: unicode, bufferSize: int, contentType: unicode, projectPath: unicode) -> db.buffers.ManagedBufferFileHandle:
        """
        Create a new empty database item within the repository.
        @param parentPath parent folder path
        @param itemName new item name
        @param fileID unique file ID
        @param bufferSize buffer file buffer size
        @param contentType application content type
        @param projectPath path of user's project
        @return initial buffer file open for writing
        @throws UserAccessException if user does not have adequate permission within the repository.
        @throws DuplicateFileException item path already exists within repository
        @throws IOException if an IO error occurs
        @throws InvalidNameException if itemName or parentPath contains invalid characters
        """
        ...

    def deleteItem(self, parentPath: unicode, itemName: unicode, version: int) -> None:
        """
        Delete the specified version of an item.
        @param parentPath parent folder path
        @param itemName name of item
        @param version oldest or latest version of item to be deleted, or -1
         to delete the entire item.  User must be Admin or owner of version to be
         deleted.
        @throws IOException if an IO error occurs
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def fileExists(self, parentPath: unicode, itemName: unicode) -> bool:
        """
        Returns true if the specified item exists.
        @param parentPath parent folder path
        @param itemName name of item
        @throws IOException if an IO error occurs
        """
        ...

    def folderExists(self, folderPath: unicode) -> bool:
        """
        Returns true if the specified folder path exists.
        @param folderPath folder path
        @throws IOException if an IO error occurs
        """
        ...

    def getCheckout(self, parentPath: unicode, itemName: unicode, checkoutId: long) -> ghidra.framework.store.ItemCheckoutStatus:
        """
        Returns specific checkout data for an item.
        @param parentPath parent folder path
        @param itemName name of item
        @param checkoutId checkout ID
        @return checkout data
        @throws IOException if an IO error occurs
        """
        ...

    def getCheckouts(self, parentPath: unicode, itemName: unicode) -> List[ghidra.framework.store.ItemCheckoutStatus]:
        """
        Get a list of all checkouts for an item.
        @param parentPath parent folder path
        @param itemName name of item
        @return checkout data list
        @throws IOException if an IO error occurs
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getEvents(self) -> List[ghidra.framework.remote.RepositoryChangeEvent]:
        """
        Get pending change events.  Call will block until an event is available.
        @return array of events
        @throws IOException if error occurs.
        """
        ...

    @overload
    def getItem(self, fileID: unicode) -> ghidra.framework.remote.RepositoryItem:
        """
        Returns the RepositoryItem with the given unique file ID
        @param fileID unique file ID
        @return item or null if not found
        @throws IOException if an IO error occurs
        @throws UnsupportedOperationException if file-system does not support this operation
        """
        ...

    @overload
    def getItem(self, parentPath: unicode, name: unicode) -> ghidra.framework.remote.RepositoryItem:
        """
        Returns the RepositoryItem in the given folder with the given name
        @param parentPath folder path
        @param name item name
        @return item or null if not found
        @throws IOException if an IO error occurs
        """
        ...

    def getItemCount(self) -> int:
        """
        Returns the number of folder items contained within this file-system.
        @throws IOException if an IO error occurs
        @throws UnsupportedOperationException if file-system does not support this operation
        """
        ...

    def getItemList(self, folderPath: unicode) -> List[ghidra.framework.remote.RepositoryItem]:
        """
        Get of all items found within the specified parent folder path.
        @param folderPath parent folder path
        @return list of items contained within specified parent folder
        @throws UserAccessException
        @throws FileNotFoundException if parent folder not found
        @throws IOException if an IO error occurs
        """
        ...

    def getLength(self, parentPath: unicode, itemName: unicode) -> long:
        """
        Returns the length of this domain file.  This size is the minimum disk space
         used for storing this file, but does not account for additional storage space
         used to tracks changes, etc.
        @param parentPath parent folder path
        @param itemName name of item
        @return file length
        @throws IOException if an IO error occurs
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of this repository.
        @throws IOException if an IO error occurs
        """
        ...

    def getServerUserList(self) -> List[unicode]:
        """
        Convenience method for obtaining a list of all users
         known to the server.
        @return list of user names.
        @throws IOException if an IO error occurs
        @see RemoteRepositoryServerHandle#getAllUsers
        """
        ...

    def getSubfolderList(self, folderPath: unicode) -> List[unicode]:
        """
        Get list of subfolders contained within the specified parent folder.
        @param folderPath parent folder path
        @return list of subfolder names
        @throws UserAccessException if user does not have adequate permission within the repository.
        @throws FileNotFoundException if specified parent folder path not found
        @throws IOException if an IO error occurs
        """
        ...

    def getUser(self) -> ghidra.framework.remote.User:
        """
        Returns user object associated with this handle.
        @throws IOException if an IO error occurs
        """
        ...

    def getUserList(self) -> List[ghidra.framework.remote.User]:
        """
        Returns a list of users authorized for this repository.
        @throws UserAccessException
        @throws IOException if an IO error occurs
        """
        ...

    def getVersions(self, parentPath: unicode, itemName: unicode) -> List[ghidra.framework.store.Version]:
        """
        Returns a list of all versions for the specified item.
        @param parentPath parent folder path
        @param itemName name of item
        @return version list
        @throws IOException if an IO error occurs
        """
        ...

    def hasCheckouts(self, parentPath: unicode, itemName: unicode) -> bool:
        """
        Returns true if the specified item has one or more checkouts.
        @param parentPath parent folder path
        @param itemName name of item
        """
        ...

    def hashCode(self) -> int: ...

    def isCheckinActive(self, parentPath: unicode, itemName: unicode) -> bool:
        """
        Returns true if the specified item has an active checkin.
        @param parentPath parent folder path
        @param itemName name of item
        """
        ...

    def moveFolder(self, oldParentPath: unicode, newParentPath: unicode, oldFolderName: unicode, newFolderName: unicode) -> None:
        """
        Move an entire folder
        @param oldParentPath current parent folder path
        @param newParentPath new parent folder path
        @param oldFolderName current folder name
        @param newFolderName new folder name
        @throws InvalidNameException if newFolderName is invalid
        @throws DuplicateFileException if target folder already exists
        @throws IOException if an IO error occurs
        """
        ...

    def moveItem(self, oldParentPath: unicode, newParentPath: unicode, oldItemName: unicode, newItemName: unicode) -> None:
        """
        Move an item to another folder
        @param oldParentPath current parent folder path
        @param newParentPath new parent folder path
        @param oldItemName current item name
        @param newItemName new item name
        @throws InvalidNameException if newItemName is invalid
        @throws DuplicateFileException if target item already exists
        @throws IOException if an IO error occurs
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def openDatabase(self, parentPath: unicode, itemName: unicode, checkoutId: long) -> db.buffers.ManagedBufferFileHandle:
        """
        Open the current version for checkin of new version.
        @param parentPath parent folder path
        @param itemName name of existing data file
        @param checkoutId checkout ID
        @return remote buffer file for updateable read-only use
        @throws UserAccessException if user does not have adequate permission within the repository.
        @throws FileNotFoundException if database version not found
        @throws IOException if an IO error occurs
        """
        ...

    @overload
    def openDatabase(self, parentPath: unicode, itemName: unicode, version: int, minChangeDataVer: int) -> db.buffers.ManagedBufferFileHandle:
        """
        Open an existing version of a database buffer file for non-update read-only use.
        @param parentPath parent folder path
        @param itemName name of existing data file
        @param version existing version of data file (-1 = latest version)
        @param minChangeDataVer indicates the oldest change data buffer file to be
         included.  A -1 indicates only the last change data buffer file is applicable.
        @return remote buffer file for non-update read-only use
        @throws UserAccessException if user does not have adequate permission within the repository.
        @throws FileNotFoundException if database version not found
        @throws IOException if an IO error occurs
        """
        ...

    def setUserList(self, users: List[ghidra.framework.remote.User], anonymousAccessAllowed: bool) -> None:
        """
        Set the list of authorized users for this repository.
        @param users list of user and access permissions.
        @param anonymousAccessAllowed true if anonymous access should be permitted to
         this repository
        @throws UserAccessException
        @throws IOException if an IO error occurs
        """
        ...

    def terminateCheckout(self, parentPath: unicode, itemName: unicode, checkoutId: long, notify: bool) -> None:
        """
        Terminate an existing item checkout.
        @param parentPath parent folder path
        @param itemName name of item
        @param checkoutId checkout ID
        @param notify notify listeners of item status change
        @throws IOException if an IO error occurs
        """
        ...

    def toString(self) -> unicode: ...

    def updateCheckoutVersion(self, parentPath: unicode, itemName: unicode, checkoutId: long, checkoutVersion: int) -> None:
        """
        Update checkout data for an item following an update of a local checkout file.
        @param parentPath parent folder path
        @param itemName name of item
        @param checkoutId checkout ID
        @param checkoutVersion item version used for update
        @throws IOException if error occurs
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def events(self) -> List[ghidra.framework.remote.RepositoryChangeEvent]: ...

    @property
    def itemCount(self) -> int: ...

    @property
    def name(self) -> unicode: ...

    @property
    def serverUserList(self) -> List[unicode]: ...

    @property
    def user(self) -> ghidra.framework.remote.User: ...

    @property
    def userList(self) -> List[ghidra.framework.remote.User]: ...
