from typing import List
import ghidra.framework.store
import ghidra.framework.store.local
import ghidra.util.task
import java.io
import java.lang


class UnknownFolderItem(ghidra.framework.store.local.LocalFolderItem):
    """
    UnknownFolderItem acts as a LocalFolderItem place-holder for
     items of an unknown type.
    """

    UNKNOWN_CONTENT_TYPE: unicode = u'Unknown'







    def canRecover(self) -> bool: ...

    @overload
    def checkout(self, user: unicode) -> ghidra.framework.store.ItemCheckoutStatus: ...

    @overload
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

    def getContentType(self) -> unicode: ...

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

    def getVersions(self) -> List[ghidra.framework.store.Version]: ...

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

    def output(self, outputFile: java.io.File, version: int, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def refresh(self) -> ghidra.framework.store.local.LocalFolderItem: ...

    def resetFileID(self) -> unicode:
        """
        @see ghidra.framework.store.FolderItem#resetFileID()
        """
        ...

    @overload
    def setCheckout(self, checkoutId: long, checkoutVersion: int, localVersion: int) -> None: ...

    @overload
    def setCheckout(self, checkoutId: long, exclusive: bool, checkoutVersion: int, localVersion: int) -> None: ...

    def setContentTypeVersion(self, version: int) -> None: ...

    def setReadOnly(self, state: bool) -> None:
        """
        @see ghidra.framework.store.FolderItem#setReadOnly(boolean)
        """
        ...

    @overload
    def terminateCheckout(self, checkoutId: long) -> None: ...

    @overload
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
    def checkouts(self) -> List[ghidra.framework.store.ItemCheckoutStatus]: ...

    @property
    def contentType(self) -> unicode: ...

    @property
    def currentVersion(self) -> int: ...

    @property
    def versions(self) -> List[ghidra.framework.store.Version]: ...
