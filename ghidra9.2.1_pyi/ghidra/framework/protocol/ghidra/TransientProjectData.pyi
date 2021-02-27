from typing import List
import ghidra.framework.client
import ghidra.framework.data
import ghidra.framework.model
import ghidra.framework.remote
import ghidra.framework.store
import ghidra.util.task
import java.io
import java.lang
import java.net


class TransientProjectData(ghidra.framework.data.ProjectFileManager):








    def addDomainFolderChangeListener(self, l: ghidra.framework.model.DomainFolderChangeListener) -> None:
        """
        @see ghidra.framework.model.ProjectData#addDomainFolderChangeListener(
         											ghidra.framework.model.DomainFolderChangeListener)
        """
        ...

    def close(self) -> None: ...

    def convertProjectToShared(self, newRepository: ghidra.framework.client.RepositoryAdapter, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def findOpenFiles(self, __a0: List[object]) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getFile(self, path: unicode) -> ghidra.framework.model.DomainFile:
        """
        @see ghidra.framework.model.ProjectData#getFile(java.lang.String)
        """
        ...

    def getFileByID(self, fileID: unicode) -> ghidra.framework.model.DomainFile:
        """
        @see ghidra.framework.model.ProjectData#getFileByID(java.lang.String)
        """
        ...

    def getFileCount(self) -> int: ...

    def getFolder(self, path: unicode) -> ghidra.framework.model.DomainFolder:
        """
        @see ghidra.framework.model.ProjectData#getFolder(java.lang.String)
        """
        ...

    def getLocalStorageClass(self) -> java.lang.Class: ...

    def getMaxNameLength(self) -> int: ...

    def getOwner(self) -> unicode:
        """
        Returns the owner of the project that is associated with this
         ProjectFileManager.  A value of null indicates an old multiuser
         project.
        @return the owner of the project
        """
        ...

    def getPrivateFileSystem(self) -> ghidra.framework.store.FileSystem:
        """
        Returns the private files system associated with this project file manager.
        @return the private files system associated with this project file manager
        """
        ...

    def getProjectDir(self) -> java.io.File:
        """
        Return the project directory.
        """
        ...

    def getProjectDisposalMonitor(self) -> ghidra.util.task.TaskMonitor:
        """
        Get monitor which will be cancelled if project is closed
        @return cancel monitor
        """
        ...

    def getProjectLocator(self) -> ghidra.framework.model.ProjectLocator:
        """
        @see ghidra.framework.model.ProjectData#getProjectLocator()
        """
        ...

    def getRepository(self) -> ghidra.framework.client.RepositoryAdapter:
        """
        Returns the repository associated with this project file manager.
        @return the repository associated with this project file manager
        """
        ...

    def getRootFolder(self) -> ghidra.framework.data.GhidraFolder:
        """
        @see ghidra.framework.model.ProjectData#getRootFolder()
        """
        ...

    def getSharedFileURL(self, path: unicode) -> java.net.URL:
        """
        @see ghidra.framework.model.ProjectData#getSharedFileURL(java.lang.String)
        """
        ...

    def getUser(self) -> ghidra.framework.remote.User:
        """
        @see ghidra.framework.model.ProjectData#getUser()
        """
        ...

    @staticmethod
    def getUserDataFilename(associatedFileID: unicode) -> unicode:
        """
        Returns the standard user data filename associated with the specified file ID.
        @param associatedFileID the file id
        @return user data filename
        """
        ...

    def hashCode(self) -> int: ...

    def incrementInstanceUseCount(self) -> None: ...

    def makeValidName(self, name: unicode) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def refresh(self, force: bool) -> None:
        """
        @see ghidra.framework.model.ProjectData#refresh(boolean)
        """
        ...

    def releaseDomainFiles(self, consumer: object) -> None:
        """
        Releases all domain files for the specified consumer.
        @param consumer the domain object consumer
        """
        ...

    def removeDomainFolderChangeListener(self, l: ghidra.framework.model.DomainFolderChangeListener) -> None:
        """
        @see ghidra.framework.model.ProjectData#removeDomainFolderChangeListener(
         											ghidra.framework.model.DomainFolderChangeListener)
        """
        ...

    def removeFromIndex(self, fileID: unicode) -> None:
        """
        Remove specified fileID from index.
        @param fileID
        """
        ...

    def testValidName(self, name: unicode, isPath: bool) -> None: ...

    def toString(self) -> unicode: ...

    def updateFileIndex(self, fileData: ghidra.framework.data.GhidraFileData) -> None:
        """
        Update the file index for the specified file data
        @param fileData file data
        """
        ...

    def updateRepositoryInfo(self, newRepository: ghidra.framework.client.RepositoryAdapter, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
