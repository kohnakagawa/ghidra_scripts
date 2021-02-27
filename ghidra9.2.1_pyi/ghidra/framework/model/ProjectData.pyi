from typing import List
import ghidra.framework.client
import ghidra.framework.model
import ghidra.framework.remote
import ghidra.util.task
import java.lang
import java.net


class ProjectData(object):
    """
    The ProjectData interface provides access to all the data files and folders
     in a project.
    """









    def addDomainFolderChangeListener(self, listener: ghidra.framework.model.DomainFolderChangeListener) -> None:
        """
        Adds a listener that will be notified when any folder or file
         changes in the project.
        @param listener the listener to be notified of folder and file changes.
        """
        ...

    def close(self) -> None:
        """
        Close the project storage associated with this project data object.
         NOTE: This should not be invoked if this object is utilized by a Project instance.
        """
        ...

    def convertProjectToShared(self, repository: ghidra.framework.client.RepositoryAdapter, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Convert a local project to a shared project. NOTE: The project should be closed and
         then reopened after this method is called.
        @param repository the repository that the project will be associated with.
        @param monitor task monitor
        @throws IOException thrown if files under version control are still checked out, or
         if there was a problem accessing the filesystem
        @throws CancelledException if the conversion was cancelled while versioned files were being
         converted to private files.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def findOpenFiles(self, __a0: List[object]) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getFile(self, path: unicode) -> ghidra.framework.model.DomainFile:
        """
        Get domain file specified by an absolute data path.
        @param path the absolute path of domain file relative to the root folder.
        @return domain file or null if file not found
        """
        ...

    def getFileByID(self, fileID: unicode) -> ghidra.framework.model.DomainFile:
        """
        Get domain file specified by its unique fileID.
        @param fileID domain file ID
        @return domain file or null if file not found
        """
        ...

    def getFileCount(self) -> int:
        """
        Get the approximate number of files contained within the project.  The number
         may be reduced if not connected to the shared repository.  Only the newer
         indexed file-system supports this capability, a value of -1 will be
         returned for older projects utilizing the mangled file-system or if an
         IO Error occurs.
         An approximate number is provided since the two underlying file systems
         are consulted separately and the local private file-system does not
         distinguish between checked-out files and private files.  This number
         is currently intended as a rough sizing number to disable certain features
         when very large projects are in use.  Generally the larger of the two
         file counts will be returned.
        @return number of project files or -1 if unknown.
        """
        ...

    def getFolder(self, path: unicode) -> ghidra.framework.model.DomainFolder:
        """
        Get domain folder specified by an absolute data path.
        @param path the absolute path of domain folder relative to the data folder.
        @return domain folder or null if folder not found
        """
        ...

    def getLocalStorageClass(self) -> java.lang.Class:
        """
        @return local storage implementation class
        """
        ...

    def getMaxNameLength(self) -> int:
        """
        @return the maximum name length permitted for folders or items.
        """
        ...

    def getProjectLocator(self) -> ghidra.framework.model.ProjectLocator:
        """
        Returns the projectLocator for the this ProjectData.
        """
        ...

    def getRepository(self) -> ghidra.framework.client.RepositoryAdapter:
        """
        Return the repository for this project data.
        @return null if the project is not associated with a repository
        """
        ...

    def getRootFolder(self) -> ghidra.framework.model.DomainFolder:
        """
        Returns the root folder of the project.
        """
        ...

    def getSharedFileURL(self, path: unicode) -> java.net.URL:
        """
        Get a URL for a shared domain file which is available
         within a remote repository.
        @param path the absolute path of domain file relative to the root folder.
        @return URL object for accessing shared file from outside of a project, or
         null if file does not exist or is not shared.
        """
        ...

    def getUser(self) -> ghidra.framework.remote.User:
        """
        Returns User object associated with remote repository or null if a remote repository
         is not used.
        """
        ...

    def hashCode(self) -> int: ...

    def makeValidName(self, name: unicode) -> unicode:
        """
        Transform the specified name into an acceptable folder or file item name.  Only an individual folder
         or file name should be specified, since any separators will be stripped-out.
         NOTE: Uniqueness of name within the intended target folder is not considered.
        @param name
        @return valid name or "unknown" if no valid characters exist within name provided
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def refresh(self, force: bool) -> None:
        """
        Sync the Domain folder/file structure with the underlying file structure.
        @param force if true all folders will be be visited and refreshed, if false
         only those folders previously visited will be refreshed.
        """
        ...

    def removeDomainFolderChangeListener(self, listener: ghidra.framework.model.DomainFolderChangeListener) -> None:
        """
        Removes the listener to be notified of folder and file changes.
        @param listener the listener to be removed.
        """
        ...

    def testValidName(self, name: unicode, isPath: bool) -> None:
        """
        Validate a folder/item name or path.
        @param name folder or item name
        @param isPath if true name represents full path
        @throws InvalidNameException if name is invalid
        """
        ...

    def toString(self) -> unicode: ...

    def updateRepositoryInfo(self, repository: ghidra.framework.client.RepositoryAdapter, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Update the repository for this project; the server may have changed or a different
         repository is being used.  NOTE: The project should be closed and then reopened after this
         method is called.
        @param repository new repository to use
        @param monitor task monitor
        @throws IOException thrown if files are still checked out, or if there was a problem accessing
         the filesystem
        @throws CancelledException if the user canceled the update
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def fileCount(self) -> int: ...

    @property
    def localStorageClass(self) -> java.lang.Class: ...

    @property
    def maxNameLength(self) -> int: ...

    @property
    def projectLocator(self) -> ghidra.framework.model.ProjectLocator: ...

    @property
    def repository(self) -> ghidra.framework.client.RepositoryAdapter: ...

    @property
    def rootFolder(self) -> ghidra.framework.model.DomainFolder: ...

    @property
    def user(self) -> ghidra.framework.remote.User: ...
