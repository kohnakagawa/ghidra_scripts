import ghidra.framework.model
import java.lang


class DomainFolderListenerAdapter(object, ghidra.framework.model.DomainFolderChangeListener):
    """
    Adapter for the domain folder change listener.
    """









    def domainFileAdded(self, file: ghidra.framework.model.DomainFile) -> None: ...

    def domainFileMoved(self, file: ghidra.framework.model.DomainFile, oldParent: ghidra.framework.model.DomainFolder, oldName: unicode) -> None: ...

    def domainFileObjectClosed(self, file: ghidra.framework.model.DomainFile, object: ghidra.framework.model.DomainObject) -> None: ...

    def domainFileObjectOpenedForUpdate(self, file: ghidra.framework.model.DomainFile, object: ghidra.framework.model.DomainObject) -> None: ...

    def domainFileObjectReplaced(self, file: ghidra.framework.model.DomainFile, oldObject: ghidra.framework.model.DomainObject) -> None: ...

    def domainFileRemoved(self, parent: ghidra.framework.model.DomainFolder, name: unicode, fileID: unicode) -> None: ...

    def domainFileRenamed(self, file: ghidra.framework.model.DomainFile, oldName: unicode) -> None: ...

    def domainFileStatusChanged(self, file: ghidra.framework.model.DomainFile, fileIDset: bool) -> None: ...

    def domainFolderAdded(self, folder: ghidra.framework.model.DomainFolder) -> None: ...

    def domainFolderMoved(self, folder: ghidra.framework.model.DomainFolder, oldParent: ghidra.framework.model.DomainFolder) -> None: ...

    def domainFolderRemoved(self, parent: ghidra.framework.model.DomainFolder, name: unicode) -> None: ...

    def domainFolderRenamed(self, folder: ghidra.framework.model.DomainFolder, oldName: unicode) -> None: ...

    def domainFolderSetActive(self, folder: ghidra.framework.model.DomainFolder) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def stateChanged(self, affectedNewPath: unicode, affectedOldPath: unicode, isFolder: bool) -> None:
        """
        Provides a consolidated callback for those listener methods which have not been
         overridden.  This callback is NOT invoked for the following callbacks:
         <ul>
         <li>domainFolderSetActive</li>
         <li>domainFileObjectReplaced</li>
         <li>domainFileObjectOpenedForUpdate</li>
         <li>domainFileObjectClosed</li>
         </ul>
        @param affectedNewPath new path of affected folder/file, or null if item was
         removed (see affectedOldPath)
        @param affectedOldPath original path of affected folder/file, or null for new
         item (see affectedOldPath)
        @param isFolder true if affected item is/was a folder
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
