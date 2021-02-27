from typing import List
import ghidra.framework.store
import ghidra.framework.store.local
import ghidra.util.task
import java.io
import java.lang


class LocalDataFile(ghidra.framework.store.local.LocalFolderItem, ghidra.framework.store.DataFileItem):
    """
    LocalDataFile provides a FolderItem implementation
     for a local serialized data file.  This implementation supports
     a non-versioned file-system only.

     This item utilizes a data directory for storing the serialized
     data file.
    """





    @overload
    def __init__(self, fileSystem: ghidra.framework.store.local.LocalFileSystem, propertyFile: ghidra.util.PropertyFile): ...

    @overload
    def __init__(self, fileSystem: ghidra.framework.store.local.LocalFileSystem, propertyFile: ghidra.util.PropertyFile, istream: java.io.InputStream, contentType: unicode, monitor: ghidra.util.task.TaskMonitor):
        """
        Create a new local data file item.
        @param fileSystem file system
        @param propertyFile serialized data property file
        @param istream data source input stream (should be a start of data and will be read to end of file).
         The invoker of this constructor is responsible for closing istream.
        @param contentType user content type
        @param monitor progress monitor (used for cancel support,
         progress not used since length of input stream is unknown)
        @throws IOException if an IO Error occurs
        @throws CancelledException if monitor cancels operation
        """
        ...



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

    @overload
    def getInputStream(self) -> java.io.InputStream: ...

    @overload
    def getInputStream(self, version: int) -> java.io.InputStream: ...

    def getLocalCheckoutVersion(self) -> int: ...

    def getName(self) -> unicode:
        """
        @see ghidra.framework.store.FolderItem#getName()
        """
        ...

    def getOutputStream(self) -> java.io.OutputStream: ...

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
    def inputStream(self) -> java.io.InputStream: ...

    @property
    def outputStream(self) -> java.io.OutputStream: ...
