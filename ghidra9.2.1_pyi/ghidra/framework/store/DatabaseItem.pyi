from typing import List
import db.buffers
import ghidra.framework.store
import ghidra.util.task
import java.io
import java.lang


class DatabaseItem(ghidra.framework.store.FolderItem, object):
    """
    DatabaseItem corresponds to a private or versioned
     database within a FileSystem.  Methods are provided for opening
     the underlying database as a BufferFile.
    """

    DATABASE_FILE_TYPE: int = 0
    DATAFILE_FILE_TYPE: int = 1
    DEFAULT_CHECKOUT_ID: long = -0x1L
    LATEST_VERSION: int = -1
    UNKNOWN_FILE_TYPE: int = -1







    def canRecover(self) -> bool: ...

    def checkout(self, __a0: ghidra.framework.store.CheckoutType, __a1: unicode, __a2: unicode) -> ghidra.framework.store.ItemCheckoutStatus: ...

    def clearCheckout(self) -> None: ...

    def delete(self, __a0: int, __a1: unicode) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getCheckout(self, __a0: long) -> ghidra.framework.store.ItemCheckoutStatus: ...

    def getCheckoutId(self) -> long: ...

    def getCheckoutVersion(self) -> int: ...

    def getCheckouts(self) -> List[ghidra.framework.store.ItemCheckoutStatus]: ...

    def getClass(self) -> java.lang.Class: ...

    def getContentType(self) -> unicode: ...

    def getContentTypeVersion(self) -> int: ...

    def getCurrentVersion(self) -> int: ...

    def getFileID(self) -> unicode: ...

    def getLocalCheckoutVersion(self) -> int: ...

    def getName(self) -> unicode: ...

    def getParentPath(self) -> unicode: ...

    def getPathName(self) -> unicode: ...

    def getVersions(self) -> List[ghidra.framework.store.Version]: ...

    def hasCheckouts(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isCheckedOut(self) -> bool: ...

    def isCheckedOutExclusive(self) -> bool: ...

    def isCheckinActive(self) -> bool: ...

    def isReadOnly(self) -> bool: ...

    def isVersioned(self) -> bool: ...

    def lastModified(self) -> long: ...

    def length(self) -> long: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def open(self) -> db.buffers.ManagedBufferFile:
        """
        Open the current version of the stored database for non-update use.
         Change data will not be available.
         The returned BufferFile does not support the BufferMgr's Save operation.
        @throws IOException thrown if IO error occurs.
        """
        ...

    @overload
    def open(self, version: int) -> db.buffers.ManagedBufferFile:
        """
        Open a specific version of the stored database for non-update use.
         Change data will not be available.
         The returned BufferFile does not support the BufferMgr's Save operation.
        @param version database version
        @return buffer file
        @throws FileInUseException thrown if unable to obtain the required database lock(s).
        @throws IOException thrown if IO error occurs.
        """
        ...

    @overload
    def open(self, version: int, minChangeDataVer: int) -> db.buffers.ManagedBufferFile:
        """
        Open a specific version of the stored database for non-update use.
         Historical change data from minChangeDataVer through version is available.
         The returned BufferFile does not support the BufferMgr's Save operation.
        @param version database version
        @param minChangeDataVer indicates the oldest change data version to be
         included in change set.  A -1 indicates only the last change data buffer file is applicable.
        @return buffer file
        @throws FileInUseException thrown if unable to obtain the required database lock(s).
        @throws IOException thrown if IO error occurs.
        @see ManagedBufferFile#getNextChangeDataFile(boolean)
        """
        ...

    def openForUpdate(self, checkoutId: long) -> db.buffers.ManagedBufferFile:
        """
        Open the current version of the stored database for update use.
         The returned BufferFile supports the Save operation.
         If this item is on a shared file-system, this method initiates an
         item checkin.  If a changeSet is specified, it will be filled with
         all change data since the check-out version.  Change data will be
         read into the change set starting oldest to newest.
        @param checkoutId the associated checkoutId if this item is stored
         on a versioned file-system, otherwise DEFAULT_CHECKOUT_ID can be
         specified.
        @return buffer file
        @throws FileInUseException thrown if unable to obtain the required database lock(s).
        @throws IOException thrown if IO error occurs.
        """
        ...

    def output(self, __a0: java.io.File, __a1: int, __a2: ghidra.util.task.TaskMonitor) -> None: ...

    def refresh(self) -> ghidra.framework.store.FolderItem: ...

    def resetFileID(self) -> unicode: ...

    def setCheckout(self, __a0: long, __a1: bool, __a2: int, __a3: int) -> None: ...

    def setContentTypeVersion(self, __a0: int) -> None: ...

    def setReadOnly(self, __a0: bool) -> None: ...

    def terminateCheckout(self, __a0: long, __a1: bool) -> None: ...

    def toString(self) -> unicode: ...

    def updateCheckoutVersion(self, __a0: long, __a1: int, __a2: unicode) -> None: ...

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
