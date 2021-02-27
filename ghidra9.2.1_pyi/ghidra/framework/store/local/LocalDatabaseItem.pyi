from typing import List
import db.buffers
import ghidra.framework.store
import ghidra.framework.store.local
import ghidra.util.task
import java.io
import java.lang


class LocalDatabaseItem(ghidra.framework.store.local.LocalFolderItem, ghidra.framework.store.DatabaseItem):
    """
    LocalDatabaseItem provides a FolderItem implementation
     for a local database.  This item wraps an underlying VersionedDatabase
     if the file-system is versioned, otherwise a PrivateDatabase is wrapped.

     This item utilizes a data directory for storing all files relating to the
     database as well as history and checkout data files if this item is versioned.
    """









    def canRecover(self) -> bool:
        """
        @see ghidra.framework.store.FolderItem#canRecover()
        """
        ...

    def checkout(self, checkoutType: ghidra.framework.store.CheckoutType, user: unicode, projectPath: unicode) -> ghidra.framework.store.ItemCheckoutStatus: ...

    def clearCheckout(self) -> None: ...

    def delete(self, version: int, user: unicode) -> None:
        """
        @see ghidra.framework.store.FolderItem#delete(int, java.lang.String)
        """
        ...

    def equals(self, obj: object) -> bool: ...

    def getCheckout(self, checkoutId: long) -> ghidra.framework.store.ItemCheckoutStatus: ...

    def getCheckoutId(self) -> long: ...

    def getCheckoutVersion(self) -> int: ...

    def getCheckouts(self) -> List[ghidra.framework.store.ItemCheckoutStatus]: ...

    def getClass(self) -> java.lang.Class: ...

    def getContentType(self) -> unicode:
        """
        @see ghidra.framework.store.FolderItem#getContentType()
        """
        ...

    def getContentTypeVersion(self) -> int: ...

    def getCurrentVersion(self) -> int: ...

    def getFileID(self) -> unicode:
        """
        @see ghidra.framework.store.FolderItem#getFileID()
        """
        ...

    def getLocalCheckoutVersion(self) -> int: ...

    def getMinimumVersion(self) -> int: ...

    def getName(self) -> unicode:
        """
        @see ghidra.framework.store.FolderItem#getName()
        """
        ...

    def getParentPath(self) -> unicode:
        """
        @see ghidra.framework.store.FolderItem#getParentPath()
        """
        ...

    def getPathName(self) -> unicode:
        """
        @see ghidra.framework.store.FolderItem#getPathName()
        """
        ...

    def getVersions(self) -> List[ghidra.framework.store.Version]:
        """
        @see ghidra.framework.store.FolderItem#getVersions()
        """
        ...

    def hasCheckouts(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isCheckedOut(self) -> bool:
        """
        @see ghidra.framework.store.FolderItem#isCheckedOut()
        """
        ...

    def isCheckedOutExclusive(self) -> bool: ...

    def isCheckinActive(self) -> bool: ...

    def isReadOnly(self) -> bool:
        """
        @see ghidra.framework.store.FolderItem#isReadOnly()
        """
        ...

    def isVersioned(self) -> bool:
        """
        @see ghidra.framework.store.FolderItem#isVersioned()
        """
        ...

    def lastModified(self) -> long: ...

    def length(self) -> long: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def open(self) -> db.buffers.LocalManagedBufferFile: ...

    @overload
    def open(self, version: int) -> db.buffers.LocalManagedBufferFile: ...

    @overload
    def open(self, version: int, minChangeDataVer: int) -> db.buffers.LocalManagedBufferFile: ...

    def openForUpdate(self, checkoutId: long) -> db.buffers.LocalManagedBufferFile:
        """
        Open the latest database version for update.
        @param checkoutId reqiured for update to a versioned item, otherwise set to -1 for
         a non-versioned private database.
        @return open database handle
        @throws IOException
        """
        ...

    def output(self, outputFile: java.io.File, version: int, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def refresh(self) -> ghidra.framework.store.local.LocalFolderItem: ...

    def resetFileID(self) -> unicode:
        """
        @see ghidra.framework.store.FolderItem#resetFileID()
        """
        ...

    def setCheckout(self, checkoutId: long, exclusive: bool, checkoutVersion: int, localVersion: int) -> None: ...

    def setContentTypeVersion(self, version: int) -> None: ...

    def setReadOnly(self, state: bool) -> None:
        """
        @see ghidra.framework.store.FolderItem#setReadOnly(boolean)
        """
        ...

    def terminateCheckout(self, checkoutId: long, notify: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def updateCheckout(self, item: ghidra.framework.store.FolderItem, checkoutVersion: int) -> None: ...

    @overload
    def updateCheckout(self, versionedFolderItem: ghidra.framework.store.FolderItem, updateItem: bool, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def updateCheckoutVersion(self, checkoutId: long, checkoutVersion: int, user: unicode) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def currentVersion(self) -> int: ...

    @property
    def minimumVersion(self) -> int: ...
