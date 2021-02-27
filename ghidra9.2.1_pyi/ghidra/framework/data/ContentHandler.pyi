import db
import ghidra.framework.data
import ghidra.framework.model
import ghidra.framework.store
import ghidra.util.classfinder
import ghidra.util.task
import java.lang
import javax.swing


class ContentHandler(ghidra.util.classfinder.ExtensionPoint, object):
    """
    NOTE:  ALL ContentHandler CLASSES MUST END IN "ContentHandler".  If not,
     the ClassSearcher will not find them.

     ContentHandler defines an application interface for converting
     between a specific domain object implementation and folder item storage.
     This interface also defines a method which provides an appropriate icon
     corresponding to the content.
    """

    MISSING_CONTENT: unicode = u'Missing-File'
    UNKNOWN_CONTENT: unicode = u'Unknown-File'







    def createFile(self, fs: ghidra.framework.store.FileSystem, userfs: ghidra.framework.store.FileSystem, path: unicode, name: unicode, domainObject: ghidra.framework.model.DomainObject, monitor: ghidra.util.task.TaskMonitor) -> long:
        """
        Creates a new folder item within a specified file-system.
         If fs is versioned, the resulting item is marked as checked-out
         within the versioned file-system.  The specified domainObj
         will become associated with the newly created database.
        @param fs the file system in which to create the folder item
        @param userfs file system which contains associated user data
        @param path the path of the folder item
        @param name the name of the new folder item
        @param domainObject the domain object to store in the newly created folder item
        @param monitor the monitor that allows the user to cancel
        @return checkout ID for new item
        @throws IOException if an i/o error occurs
        @throws InvalidNameException if the specified name contains invalid characters
        @throws CancelledException if the user cancels
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getChangeSet(self, versionedFolderItem: ghidra.framework.store.FolderItem, olderVersion: int, newerVersion: int) -> ghidra.framework.model.ChangeSet:
        """
        Returns the object change data which includes changes made to the specified
         olderVersion through to the specified newerVersion.
        @param versionedFolderItem versioned folder item
        @param olderVersion the older version number
        @param newerVersion the newer version number
        @return the set of changes that were made
        @throws VersionException if a database version change prevents reading of data.
        @throws IOException if a folder item access error occurs or change set was
         produced by newer version of software and can not be read
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getContentType(self) -> unicode:
        """
        Returns list of unique content-types supported.
         A minimum of one content-type will be returned. If more than one
         is returned, these are considered equivalent aliases.
        """
        ...

    def getContentTypeDisplayString(self) -> unicode:
        """
        A string that is meant to be presented to the user.
        """
        ...

    def getDefaultToolName(self) -> unicode:
        """
        Returns the name of the default tool that should be used to open this content type
        """
        ...

    def getDomainObject(self, item: ghidra.framework.store.FolderItem, userfs: ghidra.framework.store.FileSystem, checkoutId: long, okToUpgrade: bool, okToRecover: bool, consumer: object, monitor: ghidra.util.task.TaskMonitor) -> ghidra.framework.data.DomainObjectAdapter:
        """
        Open a folder item for update.  Changes made to the returned object may be
         saved to the original folder item.
        @param item stored folder item
        @param userfs file system which contains associated user data
        @param checkoutId an appropriate checout ID required to update the specified
         folder item.
        @param okToUpgrade if true a version upgrade to the content will be done
         if necessary.
        @param okToRecover if true an attempt to recover any unsaved changes resulting from
         a crash will be attempted.
        @param consumer consumer of the returned object
        @param monitor cancelable task monitor
        @return updateable domain object
        @throws IOException if a folder item access error occurs
        @throws CancelledException if operation is cancelled by user
        @throws VersionException if unable to handle file content due to version
         difference which could not be handled.
        """
        ...

    def getDomainObjectClass(self) -> java.lang.Class:
        """
        Returns domain object implementation class supported.
        """
        ...

    def getIcon(self) -> javax.swing.Icon:
        """
        Returns the Icon associated with this handlers content type.
        """
        ...

    def getImmutableObject(self, item: ghidra.framework.store.FolderItem, consumer: object, version: int, minChangeVersion: int, monitor: ghidra.util.task.TaskMonitor) -> ghidra.framework.data.DomainObjectAdapter:
        """
        Open a folder item for immutable use.  If any changes are attempted on the
         returned object, an IllegalStateException state exception may be thrown.
        @param item stored folder item
        @param consumer consumer of the returned object
        @param version version of the stored folder item to be opened.
         DomainFile.DEFAULT_VERSION (-1) should be specified when not opening a specific
         file version.
        @param minChangeVersion the minimum version which should be included in the
         change set for the returned object. A value of -1 indicates the default change
         set.
        @param monitor the monitor that allows the user to cancel
        @return immutable domain object
        @throws IOException if a folder item access error occurs
        @throws CancelledException if operation is cancelled by user
        @throws VersionException if unable to handle file content due to version
         difference which could not be handled.
        """
        ...

    def getMergeManager(self, resultsObj: ghidra.framework.model.DomainObject, sourceObj: ghidra.framework.model.DomainObject, originalObj: ghidra.framework.model.DomainObject, latestObj: ghidra.framework.model.DomainObject) -> ghidra.framework.data.DomainObjectMergeManager:
        """
        Get an instance of a suitable merge manager to be used during the merge of a Versioned
         object which has been modified by another user since it was last merged
         or checked-out.
        @param resultsObj object to which merge results should be written
        @param sourceObj object which contains user's changes to be merged
        @param originalObj object which corresponds to checked-out version state
        @param latestObj object which corresponds to latest version with which
         the sourceObj must be merged.
        @return merge manager
        """
        ...

    def getReadOnlyObject(self, item: ghidra.framework.store.FolderItem, version: int, okToUpgrade: bool, consumer: object, monitor: ghidra.util.task.TaskMonitor) -> ghidra.framework.data.DomainObjectAdapter:
        """
        Open a folder item for read-only use.  While changes are permitted on the
         returned object, the original folder item may not be overwritten / updated.
        @param item stored folder item
        @param version version of the stored folder item to be opened.
         DomainFile.DEFAULT_VERSION should be specified when not opening a specific
         file version.
        @param okToUpgrade if true a version upgrade to the content will be done
         if necessary.
        @param consumer consumer of the returned object
        @param monitor the monitor that allows the user to cancel
        @return read-only domain object
        @throws IOException if a folder item access error occurs
        @throws CancelledException if operation is cancelled by user
        @throws VersionException if unable to handle file content due to version
         difference which could not be handled.
        """
        ...

    def hashCode(self) -> int: ...

    def isPrivateContentType(self) -> bool:
        """
        Returns true if the content type is always private
         (i.e., can not be added to the versioned filesystem).
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeUserDataFile(self, item: ghidra.framework.store.FolderItem, userFilesystem: ghidra.framework.store.FileSystem) -> None:
        """
        Remove user data file associated with an existing folder item.
        @param item folder item
        @param userFilesystem
        @throws IOException if an access error occurs
        """
        ...

    def saveUserDataFile(self, associatedDomainObj: ghidra.framework.model.DomainObject, userDbh: db.DBHandle, userfs: ghidra.framework.store.FileSystem, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Create user data file associated with existing content.
         This facilitates the lazy creation of the user data file.
        @param associatedDomainObj associated domain object corresponding to this content handler
        @param userDbh user data handle
        @param userfs private user data filesystem
        @param monitor task monitor
        @throws IOException if an access error occurs
        @throws CancelledException if operation is cancelled by user
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
    def contentType(self) -> unicode: ...

    @property
    def contentTypeDisplayString(self) -> unicode: ...

    @property
    def defaultToolName(self) -> unicode: ...

    @property
    def domainObjectClass(self) -> java.lang.Class: ...

    @property
    def icon(self) -> javax.swing.Icon: ...

    @property
    def privateContentType(self) -> bool: ...
