from typing import List
import ghidra.framework.model
import ghidra.util.task
import java.io
import java.lang


class DomainFolder(java.lang.Comparable, object):
    """
    DomainFolder provides a storage interface for project
     folders.  A DomainFolder is an immutable reference to
     a folder contained within a project.  The state of a DomainFolder
     object does not track name/parent changes made to the referenced project folder.
    """

    COPY_SUFFIX: unicode = u'.copy'
    SEPARATOR: unicode = u'/'







    def compareTo(self, __a0: object) -> int: ...

    def copyTo(self, newParent: ghidra.framework.model.DomainFolder, monitor: ghidra.util.task.TaskMonitor) -> ghidra.framework.model.DomainFolder:
        """
        Copy this folder into the newParent folder.
        @param newParent new parent folder
        @param monitor the task monitor
        @throws DuplicateFileException if a folder or file by
         this name already exists in the newParent folder
        @throws IOException thrown if an IO or access error occurs.
        @throws CancelledException if task monitor cancelled operation.
        """
        ...

    @overload
    def createFile(self, name: unicode, obj: ghidra.framework.model.DomainObject, monitor: ghidra.util.task.TaskMonitor) -> ghidra.framework.model.DomainFile:
        """
        Add a domain object to this folder.
        @param name domain file name
        @param obj domain object to be stored
        @param monitor progress monitor
        @return domain file created as a result of adding
         the domain object to this folder
        @throws DuplicateFileException thrown if the file name already exists
        @throws InvalidNameException if name is an empty string
         or if it contains characters other than alphanumerics.
        @throws IOException if IO or access error occurs
        @throws CancelledException if the user cancels the create.
        """
        ...

    @overload
    def createFile(self, name: unicode, packFile: java.io.File, monitor: ghidra.util.task.TaskMonitor) -> ghidra.framework.model.DomainFile:
        """
        Add a new domain file to this folder.
        @param name domain file name
        @param packFile packed file containing domain file data
        @param monitor progress monitor
        @return domain file created as a result of adding
         the domain object to this folder
        @throws DuplicateFileException thrown if the file name already exists
        @throws InvalidNameException if name is an empty string
         or if it contains characters other than alphanumerics.
        @throws IOException if IO or access error occurs
        @throws CancelledException if the user cancels the create.
        """
        ...

    def createFolder(self, folderName: unicode) -> ghidra.framework.model.DomainFolder:
        """
        Create a subfolder of this folder.
        @param folderName sub-folder name
        @throws DuplicateFileException if a folder by
         this name already exists
        @throws InvalidNameException if name is an empty string
         of if it contains characters other than alphanumerics.
        @throws IOException if IO or access error occurs
        """
        ...

    def delete(self) -> None:
        """
        Deletes this folder and all of its contents
        @throws IOException if IO or access error occurs
        @throws FolderNotEmptyException Thrown if the subfolder is not empty.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFile(self, name: unicode) -> ghidra.framework.model.DomainFile:
        """
        Get the domain file in this folder with the given name.
        @param name name of file in this folder to retrieve
        @return domain file or null if there is no domain file in this folder with the given name.
        """
        ...

    def getFiles(self) -> List[ghidra.framework.model.DomainFile]:
        """
        Get all domain files in this folder.
         This returns cached information and does not force a full refresh.
        @return list of domain files
        """
        ...

    def getFolder(self, name: unicode) -> ghidra.framework.model.DomainFolder:
        """
        Return the folder for the given name.
        @param name of folder to retrieve
        @return folder or null if there is no folder by the given name.
        """
        ...

    def getFolders(self) -> List[ghidra.framework.model.DomainFolder]:
        """
        Get DomainFolders in this folder.
         This returns cached information and does not force a full refresh.
        @return list of sub-folders
        """
        ...

    def getName(self) -> unicode:
        """
        Return this folder's name.
        """
        ...

    def getParent(self) -> ghidra.framework.model.DomainFolder:
        """
        Return parent folder or null if this DomainFolder is the root folder.
        """
        ...

    def getPathname(self) -> unicode:
        """
        Returns the path name to the domain object.
        """
        ...

    def getProjectData(self) -> ghidra.framework.model.ProjectData: ...

    def getProjectLocator(self) -> ghidra.framework.model.ProjectLocator:
        """
        Returns the local storage location for the project that this DomainFolder belongs to.
        """
        ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool:
        """
        Determine if this folder contains any sub-folders or domain files.
        @return true if this folder is empty.
        """
        ...

    def isInWritableProject(self) -> bool:
        """
        Returns true if this file is in a writable project.
        """
        ...

    def moveTo(self, newParent: ghidra.framework.model.DomainFolder) -> ghidra.framework.model.DomainFolder:
        """
        Move this folder into the newParent folder.  If connected to an archive
         this affects both private and repository folders and files.  If not
         connected, only private folders and files are affected.
        @param newParent new parent folder within the same project
        @return the newly relocated folder (the original DomainFolder object becomes invalid since it is immutable)
        @throws DuplicateFileException if a folder with the same name
         already exists in newParent folder.
        @throws FileInUseException if this folder or one of its decendents
         contains a file which is in-use / checked-out.
        @throws IOException thrown if an IO or access error occurs.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setActive(self) -> None:
        """
        Allows the framework to react to a request to make this folder the
         "active" one.
        """
        ...

    def setName(self, newName: unicode) -> ghidra.framework.model.DomainFolder:
        """
        Set the name on this domain folder.
        @param newName domain folder name
        @return renamed domain file (the original DomainFolder object becomes invalid since it is immutable)
        @throws InvalidNameException if newName contains illegal characters
        @throws DuplicateFileException if a folder named newName
         already exists in this files domain folder.
        @throws FileInUseException if any file within this folder or its
         decendents is in-use / checked-out.
        @throws IOException thrown if an IO or access error occurs.
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
    def empty(self) -> bool: ...

    @property
    def files(self) -> List[ghidra.framework.model.DomainFile]: ...

    @property
    def folders(self) -> List[ghidra.framework.model.DomainFolder]: ...

    @property
    def inWritableProject(self) -> bool: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def parent(self) -> ghidra.framework.model.DomainFolder: ...

    @property
    def pathname(self) -> unicode: ...

    @property
    def projectData(self) -> ghidra.framework.model.ProjectData: ...

    @property
    def projectLocator(self) -> ghidra.framework.model.ProjectLocator: ...
