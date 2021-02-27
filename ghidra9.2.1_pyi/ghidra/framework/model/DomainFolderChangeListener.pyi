import ghidra.framework.model
import java.lang


class DomainFolderChangeListener(object):
    """
    Methods for notifications when changes are made to a domain folder or
     a domain file.
    """









    def domainFileAdded(self, file: ghidra.framework.model.DomainFile) -> None:
        """
        Notification that a file is added to parent folder. You can
         get the parent from the file.
        @param file domain file which was just added.
        """
        ...

    def domainFileMoved(self, file: ghidra.framework.model.DomainFile, oldParent: ghidra.framework.model.DomainFolder, oldName: unicode) -> None:
        """
        Notification that the domain file was moved.
        @param file the file (after move)
        @param oldParent original parent folder
        """
        ...

    def domainFileObjectClosed(self, file: ghidra.framework.model.DomainFile, object: ghidra.framework.model.DomainObject) -> None:
        """
        Notification that a domain file previously open for update is in the process of closing.
        @param file domain file
        @param object domain object which was open for update
        """
        ...

    def domainFileObjectOpenedForUpdate(self, file: ghidra.framework.model.DomainFile, object: ghidra.framework.model.DomainObject) -> None:
        """
        Notification that a domain file has been opened for update.
        @param file domain file
        @param object domain object open for update
        """
        ...

    def domainFileObjectReplaced(self, file: ghidra.framework.model.DomainFile, oldObject: ghidra.framework.model.DomainObject) -> None:
        """
        Notification that a new version of the domain object exists and the
         current one is no longer valid. Existing consumers should be immediately
         released and no additional use of the oldObject is permitted once this
         method returns.  This is only called for domain objects which were
         opened for update.
        @param file file whose object was replaced
        @param oldObject old object that was replaced
        """
        ...

    def domainFileRemoved(self, parent: ghidra.framework.model.DomainFolder, name: unicode, fileID: unicode) -> None:
        """
        Notification that a file was removed
        @param parent domain folder which contained the file that was just removed.
        @param name the name of the file that was removed.
        @param fileID file ID or null
        """
        ...

    def domainFileRenamed(self, file: ghidra.framework.model.DomainFile, oldName: unicode) -> None:
        """
        Notification that the domain file was renamed.
        @param file file that was renamed
        @param oldName old name of the file
        """
        ...

    def domainFileStatusChanged(self, file: ghidra.framework.model.DomainFile, fileIDset: bool) -> None:
        """
        Notification that the status for a domain file has changed.
        @param file file whose status has changed.
        @param fileIDset if true indicates that the previously missing fileID has been
         established for the specified file.
        """
        ...

    def domainFolderAdded(self, folder: ghidra.framework.model.DomainFolder) -> None:
        """
        Notification that a folder is added to parent.
        @param folder domain folder which was just added.
        """
        ...

    def domainFolderMoved(self, folder: ghidra.framework.model.DomainFolder, oldParent: ghidra.framework.model.DomainFolder) -> None:
        """
        Notification that the domain folder was moved.
        @param folder the folder (after move)
        @param oldParent original parent folder
        """
        ...

    def domainFolderRemoved(self, parent: ghidra.framework.model.DomainFolder, name: unicode) -> None:
        """
        Notification that a domain folder is removed.
        @param parent domain folder which contained the folder that was just removed.
        @param name the name of the folder that was removed.
        """
        ...

    def domainFolderRenamed(self, folder: ghidra.framework.model.DomainFolder, oldName: unicode) -> None:
        """
        Notify listeners when a domain folder is renamed.
        @param folder folder that was renamed
        @param oldName old name of folder
        """
        ...

    def domainFolderSetActive(self, folder: ghidra.framework.model.DomainFolder) -> None:
        """
        Notification that the setActive() method on the folder was called.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
