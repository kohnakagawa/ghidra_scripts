from typing import List
import ghidra.framework.store
import ghidra.framework.store.local
import ghidra.util.task
import java.io
import java.lang


class LocalFolderItem(object, ghidra.framework.store.FolderItem):
    """
    LocalFolderItem provides an abstract implementation of a folder
     item which resides on a local file-system.  An item is defined by a property file
     and generally has a hidden data directory which contains the actual data file(s).

     An item may be either private or shared (i.e., versioned) as defined by the
     associated file-system.  A shared item utilizes a CheckoutManager and HistoryManager
     for tracking version control data related to this item.
    """

    DATABASE_FILE_TYPE: int = 0
    DATAFILE_FILE_TYPE: int = 1
    DEFAULT_CHECKOUT_ID: long = -0x1L
    LATEST_VERSION: int = -1
    UNKNOWN_FILE_TYPE: int = -1







    def canRecover(self) -> bool: ...

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

    def lastModified(self) -> long:
        """
        @see ghidra.framework.store.FolderItem#lastModified()
        """
        ...

    def length(self) -> long: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def output(self, __a0: java.io.File, __a1: int, __a2: ghidra.util.task.TaskMonitor) -> None: ...

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
    def updateCheckout(self, item: ghidra.framework.store.FolderItem, checkoutVersion: int) -> None:
        """
        Update this non-versioned item with the contents of the specified item which must be
         within the same non-versioned fileSystem.  If successful, the specified item will be
         removed after its content has been moved into this item.
        @param item
        @param checkoutVersion
        @throws IOException if this file is not a checked-out non-versioned file
         or an IO error occurs.
        """
        ...

    @overload
    def updateCheckout(self, versionedFolderItem: ghidra.framework.store.FolderItem, updateItem: bool, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Update this non-versioned item with the latest version of the specified versioned item.
        @param versionedFolderItem versioned item which corresponds to this
         non-versioned item.
        @param updateItem if true this items content is updated using the versionedFolderItem
        @param monitor progress monitor for update
        @throws IOException if this file is not a checked-out non-versioned file
         or an IO error occurs.
        @throws CancelledException if monitor cancels operation
        """
        ...

    def updateCheckoutVersion(self, checkoutId: long, checkoutVersion: int, user: unicode) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def checkedOut(self) -> bool: ...

    @property
    def checkedOutExclusive(self) -> bool: ...

    @property
    def checkinActive(self) -> bool: ...

    @property
    def checkoutId(self) -> long: ...

    @property
    def checkoutVersion(self) -> int: ...

    @property
    def checkouts(self) -> List[ghidra.framework.store.ItemCheckoutStatus]: ...

    @property
    def contentType(self) -> unicode: ...

    @property
    def contentTypeVersion(self) -> int: ...

    @contentTypeVersion.setter
    def contentTypeVersion(self, value: int) -> None: ...

    @property
    def currentVersion(self) -> int: ...

    @property
    def fileID(self) -> unicode: ...

    @property
    def localCheckoutVersion(self) -> int: ...

    @property
    def name(self) -> unicode: ...

    @property
    def parentPath(self) -> unicode: ...

    @property
    def pathName(self) -> unicode: ...

    @property
    def readOnly(self) -> bool: ...

    @readOnly.setter
    def readOnly(self, value: bool) -> None: ...

    @property
    def versioned(self) -> bool: ...

    @property
    def versions(self) -> List[ghidra.framework.store.Version]: ...
