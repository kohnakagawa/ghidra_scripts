from typing import List
import ghidra.framework.data
import ghidra.framework.model
import ghidra.framework.store
import ghidra.util.task
import java.io
import java.lang
import java.util
import javax.swing


class DomainFile(java.lang.Comparable, object):
    """
    DomainFile provides a storage interface for project
     files.  A DomainFile is an immutable reference to
     a file contained within a project.  The state of a DomainFile
     object does not track name/parent changes made to the referenced project file.
    """

    DEFAULT_VERSION: int = -1
    READ_ONLY_PROPERTY: unicode = u'READ_ONLY'







    def addToVersionControl(self, comment: unicode, keepCheckedOut: bool, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Adds this private file to version control.
        @param comment new version comment
        @param keepCheckedOut if true, the file will be initially checked-out
        @param monitor progress monitor
        @throws FileInUseException if this file is in-use.
        @throws IOException thrown if an IO or access error occurs.  Also
         thrown if file is not private.
        @throws CancelledException if the monitor cancelled the operation
        """
        ...

    def canAddToRepository(self) -> bool:
        """
        Returns true if this private file may be added to the
         associated repository.
        """
        ...

    def canCheckin(self) -> bool:
        """
        Returns true if this file may be checked-in to the associated repository.
        """
        ...

    def canCheckout(self) -> bool:
        """
        Returns true if this file may be checked-out from the associated repository.
         User's with read-only repository access will not have checkout ability.
        """
        ...

    def canMerge(self) -> bool:
        """
        Returns true if this file can be merged with the current versioned file.
        """
        ...

    def canRecover(self) -> bool:
        """
        Prior to invoking getDomainObject, this method can be used to determine if
         unsaved changes can be recovered on the next open.
        @return true if recovery data exists.
        """
        ...

    def canSave(self) -> bool:
        """
        Return whether this domain object can be saved (i.e., updated/overwritten).
        @return true if the user is the owner AND the file is in
         the active project AND the file is not read-only.
        """
        ...

    def checkin(self, checkinHandler: ghidra.framework.data.CheckinHandler, okToUpgrade: bool, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Performs check in to associated repository.  File must be checked-out
         and modified since checkout.
        @param checkinHandler provides user input data to complete checkin process.
        @param okToUpgrade if true an upgrade will be performed if needed
        @param monitor the TaskMonitor.
        @throws IOException if an IO or access error occurs
        @throws VersionException if unable to handle domain object version in versioned filesystem.
         If okToUpgrade was false, check exception to see if it can be upgraded
         sometime after doing a checkout.
        @throws CancelledException if task monitor cancelled operation
        """
        ...

    def checkout(self, exclusive: bool, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Checkout this file for update.  If this file is already
         private, this method does nothing.
        @param exclusive if true an exclusive checkout will be requested
        @param monitor progress monitor
        @return true if checkout successful, false if an exclusive checkout was not possible
         due to other users having checkouts of this file.  A request for a non-exclusive checkout
         will never return false.
        @throws IOException thrown if an IO or access error occurs.
        @throws CancelledException if task monitor cancelled operation.
        """
        ...

    def compareTo(self, __a0: object) -> int: ...

    def copyTo(self, newParent: ghidra.framework.model.DomainFolder, monitor: ghidra.util.task.TaskMonitor) -> ghidra.framework.model.DomainFile:
        """
        Copy this file into the newParent folder as a private file.
        @param newParent new parent folder
        @param monitor task monitor
        @return newly created domain file
        @throws FileInUseException if this file is in-use / checked-out.
        @throws IOException thrown if an IO or access error occurs.
        @throws CancelledException if task monitor cancelled operation.
        """
        ...

    def copyVersionTo(self, version: int, destFolder: ghidra.framework.model.DomainFolder, monitor: ghidra.util.task.TaskMonitor) -> ghidra.framework.model.DomainFile:
        """
        Copy a specific version of this file to the specified destFolder.
        @param version version to copy
        @param destFolder destination parent folder
        @param monitor task monitor
        @throws IOException thrown if an IO or access error occurs.
        @throws CancelledException if task monitor cancelled operation.
        """
        ...

    @overload
    def delete(self) -> None:
        """
        Delete the entire database for this file, including any version files.
        @throws FileInUseException if this file is in-use / checked-out.
        @throws UserAccessException if the user does not have permission to delete the file.
        @throws IOException thrown if an IO or access error occurs.
        """
        ...

    @overload
    def delete(self, version: int) -> None:
        """
        Deletes a specific version of a file from the versioned filesystem.
        @param version specific version to be deleted.  The version must either
         be the oldest or latest, or -1 which will attempt to remove all versions.
         When deleting the latest version, this method could take a long time
         to return since the previous version must be reconstructed within the
         versioned filesystem.
        @throws IOException if an IO error occurs, including the inability
         to delete a version because this item is checked-out, the user does
         not have permission, or the specified version is not the oldest or
         latest.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def exists(self) -> bool:
        """
        Check for existence of domain file.
        @return true if file exists.  A proxy domain file will always return false.
        """
        ...

    def getChangesByOthersSinceCheckout(self) -> ghidra.framework.model.ChangeSet:
        """
        Returns changes made to versioned file by others since checkout was performed.
        @return change set or null
        @throws VersionException latest version was created with a newer version of software
        @throws IOException if a folder item access error occurs or change set was
         produced by newer version of software and can not be read
        """
        ...

    def getCheckoutStatus(self) -> ghidra.framework.store.ItemCheckoutStatus:
        """
        Get checkout status associated with a versioned file.
        @return checkout status or null if not checked-out to current associated project.
        @throws IOException if an IO or access error occurs
        """
        ...

    def getCheckouts(self) -> List[ghidra.framework.store.ItemCheckoutStatus]:
        """
        Get a list of checkouts by all users for the associated versioned file.
        @return list of checkouts
        @throws IOException if an IO or access error occurs
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getConsumers(self) -> java.util.ArrayList:
        """
        Get the list of consumers (Objects) for this domain file.
        @return empty array list if there are no consumers
        """
        ...

    def getContentType(self) -> unicode:
        """
        Returns content-type string
        """
        ...

    def getDomainObject(self, consumer: object, okToUpgrade: bool, okToRecover: bool, monitor: ghidra.util.task.TaskMonitor) -> ghidra.framework.model.DomainObject:
        """
        Opens and returns the current domain object.  If the domain object is already opened,
         then the existing open domain object is returned.
        @param consumer consumer of the domain object which is responsible for
         releasing it after use. When all the consumers using the domain object release it, then
         the object is closed and its resources released.
        @param okToUpgrade if true, allows the system to upgrade out of data domain objects to
         be in compliance with the current version of Ghidra. A Version exception will be thrown
         if the domain object cannot be upgraded OR okToUpgrade is false and the domain object is
         out of date.
        @param okToRecover if true, allows the system to recover unsaved file changes which
         resulted from a crash.  If false, any existing recovery data will be deleted.
         This flag is only relevant if project is open for update (isInProject) and the file can be
         opened for update.
        @param monitor permits monitoring of open progress.
        @return an open domain object can be modified and saved. (Not read-only)
        @throws VersionException if the domain object could not be read due
         to a version format change.  If okToUpgrade is true, then a VersionException indicates
         that the domain object cannot be upgraded to the current format.  If okToUpgrade is false,
         then the VersionException only means the object is not in the current format - it
         may or may not be possible to upgrade.
        @throws IOException thrown if an IO or access error occurs.
        @throws CancelledException if monitor cancelled operation
        """
        ...

    def getDomainObjectClass(self) -> java.lang.Class:
        """
        Returns the underlying Class for the domain object in this
         domain file.
        """
        ...

    def getFileID(self) -> unicode:
        """
        Returns a unique file-ID
        @return
        """
        ...

    def getIcon(self, disabled: bool) -> javax.swing.Icon:
        """
        Get the state based Icon image for the domain file based upon its content class.
        @param disabled true if the icon return should be rendered as
         not enabled
        @return image icon
        """
        ...

    def getImmutableDomainObject(self, consumer: object, version: int, monitor: ghidra.util.task.TaskMonitor) -> ghidra.framework.model.DomainObject:
        """
        Returns a new DomainObject that cannot be changed or saved to its original file.
        @param consumer consumer of the domain object which is responsible for
         releasing it after use.
        @param version the domain object version requested.  DEFAULT_VERSION should be
         specified to open the current version.
        @param monitor permits monitoring of open progress.
        @return a new domain object that is disassociated from its original domain file
         and cannot be modified
        @throws VersionException if the domain object could not be read due
         to a version format change.
        @throws FileNotFoundException if the stored file/version was not found.
        @throws IOException thrown if an IO or access error occurs.
        @throws CancelledException if monitor cancelled operation
        """
        ...

    def getLastModifiedTime(self) -> long:
        """
        Get a long value representing the time when the data was last modified.
        """
        ...

    def getLatestVersion(self) -> int:
        """
        Return the latest version
        """
        ...

    def getMetadata(self) -> java.util.Map:
        """
        Returns an ordered map containting the metadata that has been associated with the corresponding domain object.
         The map contains key,value pairs and are ordered by their insertion order.
        @return a map containting the metadata that has been associated with the corresponding domain object.
        """
        ...

    def getName(self) -> unicode:
        """
        Get the name of the StoredObj that is associated with
         the data.
        """
        ...

    def getOpenedDomainObject(self, consumer: object) -> ghidra.framework.model.DomainObject:
        """
        Returns the domainObject for this DomainFile only if it is already open.
        @param consumer the consumer that will use the object.
        @return the already opened domainObject or null if it is not currently open.
        """
        ...

    def getParent(self) -> ghidra.framework.model.DomainFolder:
        """
        Get the parent domain folder for this domain file.
        """
        ...

    def getPathname(self) -> unicode:
        """
        Returns the path name to the domain object.
        """
        ...

    def getProjectLocator(self) -> ghidra.framework.model.ProjectLocator:
        """
        Returns the local storage location for the project that this DomainFile belongs to.
        """
        ...

    def getReadOnlyDomainObject(self, consumer: object, version: int, monitor: ghidra.util.task.TaskMonitor) -> ghidra.framework.model.DomainObject:
        """
        Returns a "read-only" version of the domain object.  "Read-only" means that the domain
         object cannot be saved back into its original domain object. It can still be modified
         and saved to a new domain file.  The domain object will be assigned a temporary domain
         file that will not allow a "save" operation. The user must do a "save as"
         to a new filename.
        @param consumer consumer of the domain object which is responsible for
         releasing it after use.
        @param version the domain object version requested.  DEFAULT_VERSION should be
         specified to open the current version.
        @param monitor permits monitoring of open progress.
        @return a new domain object that is disassociated from its original domain file.
        @throws VersionException if the domain object could not be read due
         to a version format change.
        @throws FileNotFoundException if the stored file/version was not found.
        @throws IOException thrown if an IO or access error occurs.
        @throws CancelledException if monitor cancelled operation
        """
        ...

    def getVersion(self) -> int:
        """
        Return either the latest version if the file is not checked-out or the version that
         was checked-out or a specific version that was requested.
        """
        ...

    def getVersionHistory(self) -> List[ghidra.framework.store.Version]:
        """
        Returns list of all available versions.
        """
        ...

    def hashCode(self) -> int: ...

    def isBusy(self) -> bool:
        """
        Returns true if the domain object in this domain file exists and has an open transaction.
        """
        ...

    def isChanged(self) -> bool:
        """
        Return whether the domain object in this domain file has changed.
        """
        ...

    def isCheckedOut(self) -> bool:
        """
        Returns true if this is a checked-out file.
        """
        ...

    def isCheckedOutExclusive(self) -> bool:
        """
        Returns true if this a checked-out file with exclusive access.
        """
        ...

    def isHijacked(self) -> bool:
        """
        Returns true if the file is versioned but a private copy also exists.
        """
        ...

    def isInWritableProject(self) -> bool:
        """
        Returns true if this file is in a writable project.
        """
        ...

    def isLatestVersion(self) -> bool:
        """
        Returns true if this file represents the latest version of the
         associated domain object.
        """
        ...

    def isOpen(self) -> bool:
        """
        Returns true if there is an open domainObject for this file.
        """
        ...

    def isReadOnly(self) -> bool:
        """
        Returns whether the object is read-only. From a
         framework point of view a read-only object can never be
         changed.
        """
        ...

    def isVersionControlSupported(self) -> bool:
        """
        Returns true if the versioned filesystem can be used to store
         this files content type.
        """
        ...

    def isVersioned(self) -> bool:
        """
        Return true if this is a versioned database, else false
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

    def merge(self, okToUpgrade: bool, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Performs merge from current version of versioned file into local checked-out file.
        @param okToUpgrade if true an upgrade will be performed if needed
        @param monitor task monitor
        @throws IOException if an IO or access error occurs
        @throws VersionException if unable to handle domain object version in versioned filesystem.
         If okToUpgrade was false, check exception to see if it can be upgraded
        @throws CancelledException if task monitor cancelled operation
        """
        ...

    def modifiedSinceCheckout(self) -> bool:
        """
        Returns true if this is a checked-out file which has been modified
         since it was checked-out.
        """
        ...

    def moveTo(self, newParent: ghidra.framework.model.DomainFolder) -> ghidra.framework.model.DomainFile:
        """
        Move this file into the newParent folder.
        @param newParent new parent folder within the same project
        @return the newly relocated domain file (the original DomainFile object becomes invalid since it is immutable)
        @throws DuplicateFileException if a file with the same name
         already exists in newParent folder.
        @throws FileInUseException if this file is in-use / checked-out.
        @throws IOException thrown if an IO or access error occurs.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def packFile(self, file: java.io.File, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Pack domain file into specified file.
         Specified file will be overwritten if it already exists.
        @param file destination file
        @param monitor
        @throws IOException
        @throws CancelledException if monitor cancels operation
        """
        ...

    def save(self, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Save the <CODE>DomainObject</CODE> associated with this file.
        @param monitor monitor for the task that is doing the save on the file
        @throws FileInUseException if the file is open for update by someone else, or
         a transient-read is in progress.
        @throws IOException thrown if an IO error occurs.
        @throws CancelledException if monitor cancelled operation
        """
        ...

    def setName(self, newName: unicode) -> ghidra.framework.model.DomainFile:
        """
        Set the name on this domain file.
        @param newName domain file name
        @return renamed domain file (the original DomainFile object becomes invalid since it is immutable)
        @throws InvalidNameException if newName contains illegal characters
        @throws DuplicateFileException if a file named newName
         already exists in this files domain folder.
        @throws FileInUseException if this file is in-use / checked-out.
        @throws IOException thrown if an IO or access error occurs.
        """
        ...

    def setReadOnly(self, state: bool) -> None:
        """
        Sets the object to read-only.  This method may only be invoked
         for private files (i.e., not versioned).
        @param state if true file will be read-only and may not be updated, if false the
         file may be updated.
        @throws IOException thrown if an IO error occurs.
        """
        ...

    def takeRecoverySnapshot(self) -> bool:
        """
        If the file has an updateable domain object with unsaved changes, generate a
         recovery snapshot.
        @return true if snapshot successful or not needed, false if file is busy
         which prevents snapshot, or snapshot was cancelled.
        @throws IOException
        """
        ...

    def terminateCheckout(self, checkoutId: long) -> None:
        """
        Forcefully terminate a checkout for the associated versioned file.
         The user must be the owner of the checkout or have admin privilege
         on the versioned filesystem (i.e., repository).
        @param checkoutId checkout ID
        @throws IOException if an IO or access error occurs
        """
        ...

    def toString(self) -> unicode: ...

    def undoCheckout(self, keep: bool) -> None:
        """
        Undo "checked-out" file.  The original repository file is restored.
        @param keep if true, the private database will be renamed with a .keep
         extension.
        @throws FileInUseException if this file is in-use / checked-out.
        @throws IOException thrown if file is not checked-out or an IO / access error occurs.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def busy(self) -> bool: ...

    @property
    def changed(self) -> bool: ...

    @property
    def changesByOthersSinceCheckout(self) -> ghidra.framework.model.ChangeSet: ...

    @property
    def checkedOut(self) -> bool: ...

    @property
    def checkedOutExclusive(self) -> bool: ...

    @property
    def checkoutStatus(self) -> ghidra.framework.store.ItemCheckoutStatus: ...

    @property
    def checkouts(self) -> List[ghidra.framework.store.ItemCheckoutStatus]: ...

    @property
    def consumers(self) -> java.util.ArrayList: ...

    @property
    def contentType(self) -> unicode: ...

    @property
    def domainObjectClass(self) -> java.lang.Class: ...

    @property
    def fileID(self) -> unicode: ...

    @property
    def hijacked(self) -> bool: ...

    @property
    def inWritableProject(self) -> bool: ...

    @property
    def lastModifiedTime(self) -> long: ...

    @property
    def latestVersion(self) -> bool: ...

    @property
    def metadata(self) -> java.util.Map: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def open(self) -> bool: ...

    @property
    def parent(self) -> ghidra.framework.model.DomainFolder: ...

    @property
    def pathname(self) -> unicode: ...

    @property
    def projectLocator(self) -> ghidra.framework.model.ProjectLocator: ...

    @property
    def readOnly(self) -> bool: ...

    @readOnly.setter
    def readOnly(self, value: bool) -> None: ...

    @property
    def version(self) -> int: ...

    @property
    def versionControlSupported(self) -> bool: ...

    @property
    def versionHistory(self) -> List[ghidra.framework.store.Version]: ...

    @property
    def versioned(self) -> bool: ...
