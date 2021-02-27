from typing import List
import ghidra.framework.store
import ghidra.util.task
import java.io
import java.lang


class FolderItem(object):
    """
    FolderItem represents an individual file
     contained within a FileSystem and is uniquely identified
     by a path string.
    """

    DATABASE_FILE_TYPE: int = 0
    DATAFILE_FILE_TYPE: int = 1
    DEFAULT_CHECKOUT_ID: long = -0x1L
    LATEST_VERSION: int = -1
    UNKNOWN_FILE_TYPE: int = -1







    def canRecover(self) -> bool:
        """
        Returns true if unsaved file changes can be recovered.
        """
        ...

    def checkout(self, checkoutType: ghidra.framework.store.CheckoutType, user: unicode, projectPath: unicode) -> ghidra.framework.store.ItemCheckoutStatus:
        """
        Checkout this folder item.
        @param checkoutType type of checkout
        @param user user requesting checkout
        @param projectPath path of project where checkout was made
        @return checkout status or null if exclusive checkout request failed
        @throws IOException if an IO error occurs or this item is not versioned
        """
        ...

    def clearCheckout(self) -> None:
        """
        Clears the checkout data associated with this non-shared file.
         NOTE: This method is only valid for a local non-versioned file-system.
        @throws IOException
        """
        ...

    def delete(self, version: int, user: unicode) -> None:
        """
        Deletes the item or a specific version.  If a specific version
         is specified, it must either be the oldest or latest (i.e., current).
        @param version specific version to be deleted, or -1 to remove
         all versions.
        @param user user name
        @throws IOException if an IO error occurs, including the inability
         to delete a version because this item is checked-out, the user does
         not have permission, or the specified version is not the oldest or
         latest.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getCheckout(self, checkoutId: long) -> ghidra.framework.store.ItemCheckoutStatus:
        """
        Get the checkout status which corresponds to the specified checkout ID.
        @param checkoutId checkout ID
        @return checkout status or null if checkout ID not found.
        @throws IOException if an IO error occurs or this item is not versioned
        """
        ...

    def getCheckoutId(self) -> long:
        """
        Returns the checkoutId for this file.  A value of -1 indicates
         a private item.
         NOTE: This method is only valid for a local non-versioned file-system.
        @throws IOException if an IO error occurs
        """
        ...

    def getCheckoutVersion(self) -> int:
        """
        Returns the item version which was checked-out.  A value of -1 indicates
         a private item.
         NOTE: This method is only valid for a local non-versioned file-system.
        @throws IOException
        """
        ...

    def getCheckouts(self) -> List[ghidra.framework.store.ItemCheckoutStatus]:
        """
        Get all current checkouts for this item.
        @return array of checkouts
        @throws IOException if an IO error occurs or this item is not versioned
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getContentType(self) -> unicode:
        """
        Return The content type name for this item.
        """
        ...

    def getContentTypeVersion(self) -> int:
        """
        Returns the version of content type.  Note this is the version of the structure/storage
         for the content type, Not the users version of their data.
        """
        ...

    def getCurrentVersion(self) -> int:
        """
        Return the latest/current version.
        """
        ...

    def getFileID(self) -> unicode:
        """
        Return the file ID if one has been established or null
        @throws IOException thrown if IO or access error occurs
        """
        ...

    def getLocalCheckoutVersion(self) -> int:
        """
        Returns the local item version at the time the checkout was
         completed.  A value of -1 indicates a private item.
         NOTE: This method is only valid for a local non-versioned file-system.
        """
        ...

    def getName(self) -> unicode:
        """
        Return The display name for this item.
        """
        ...

    def getParentPath(self) -> unicode:
        """
        Returns the path of the parent folder.
        """
        ...

    def getPathName(self) -> unicode:
        """
        Return The concatenation of the pathname and the basename
         which can be used to uniquely identify a folder item.
        """
        ...

    def getVersions(self) -> List[ghidra.framework.store.Version]:
        """
        Returns list of all available versions or null
         if item is not versioned.
        @throws IOException thrown if an IO error occurs.
        """
        ...

    def hasCheckouts(self) -> bool:
        """
        Returns true if this item is versioned and has one or more checkouts.
        @throws IOException if an IO error occurs
        """
        ...

    def hashCode(self) -> int: ...

    def isCheckedOut(self) -> bool:
        """
        Returns true if this item is a checked-out copy from a versioned file system.
        """
        ...

    def isCheckedOutExclusive(self) -> bool:
        """
        Returns true if this item is a checked-out copy with exclusive access from a versioned file system.
        """
        ...

    def isCheckinActive(self) -> bool:
        """
        Returns true if this item is versioned and has a checkin in-progress.
        @throws IOException if an IO error occurs
        """
        ...

    def isReadOnly(self) -> bool:
        """
        Returns true if item can be overwritten/deleted.
        """
        ...

    def isVersioned(self) -> bool:
        """
        Return true if this is a versioned item, else false
        @throws IOException thrown if an IO error occurs.
        """
        ...

    def lastModified(self) -> long:
        """
        Return The time that this item was last modified.
        """
        ...

    def length(self) -> long:
        """
        Returns the length of this domain file.  This size is the minimum disk space
         used for storing this file, but does not account for additional storage space
         used to tracks changes, etc.
        @return file length
        @throws IOException thrown if IO or access error occurs
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def output(self, outputFile: java.io.File, version: int, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Serialize (i.e., pack) this item into the specified outputFile.
        @param outputFile packed output file to be created
        @param version if this item is versioned, specifies the version to be output, otherwise
         -1 should be specified.
        @param monitor progress monitor
        @throws IOException
        @throws CancelledException if monitor cancels operation
        """
        ...

    def refresh(self) -> ghidra.framework.store.FolderItem:
        """
        Returns this instance after refresh or null if item no longer exists
        """
        ...

    def resetFileID(self) -> unicode:
        """
        Assign a new file-ID to this local non-versioned file.
         NOTE: This method is only valid for a local non-versioned file-system.
        @return new file-ID
        @throws IOException thrown if IO or access error occurs
        """
        ...

    def setCheckout(self, checkoutId: long, exclusive: bool, checkoutVersion: int, localVersion: int) -> None:
        """
        Set the checkout data associated with this non-shared file.
         NOTE: This method is only valid for a local non-versioned file-system.
        @param checkoutId checkout ID (provided by ItemCheckoutStatus).
        @param exclusive true if checkout is exclusive
        @param checkoutVersion the item version which was checked-out (provided
         by ItemCheckoutStatus).
        @param localVersion the local item version at the time the checkout was
         completed.
        @throws IOException if an IO error occurs or item is
         stored on a shared file-system
        """
        ...

    def setContentTypeVersion(self, version: int) -> None:
        """
        Sets the version for the content type. This will change whenever the domain objects
         are upgraded.
        @param version the new version for the content type.
        @throws IOException if an IO error occurs or item is
         stored on a shared file-system
        """
        ...

    def setReadOnly(self, state: bool) -> None:
        """
        Set the state of the read-only indicator for this non-shared item.
        @param state read-only state
        @throws IOException if an IO error occurs or item is
         stored on a shared file-system
        """
        ...

    def terminateCheckout(self, checkoutId: long, notify: bool) -> None:
        """
        Terminates a checkout.  The checkout ID becomes invalid, therefore the
         associated checkout copy should either be removed or converted to a
         private file.
        @param checkoutId checkout ID
        @param notify if true item change notification will be sent
        @throws IOException if an IO error occurs or this item is not versioned
        """
        ...

    def toString(self) -> unicode: ...

    def updateCheckoutVersion(self, checkoutId: long, checkoutVersion: int, user: unicode) -> None:
        """
        Update the checkout version associated with this versioned item.
        @param checkoutId id corresponding to an existing checkout
        @param checkoutVersion
        @param user
        @throws IOException if an IO error occurs.
        """
        ...

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
