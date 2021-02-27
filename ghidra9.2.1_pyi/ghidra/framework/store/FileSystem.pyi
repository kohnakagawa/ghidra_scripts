from typing import List
import db.buffers
import ghidra.framework.store
import ghidra.util.task
import java.io
import java.lang


class FileSystem(object):
    """
    FileSystem provides a hierarchical view and management of a
     set of files and folders.
    """

    SEPARATOR: unicode = u'/'
    SEPARATOR_CHAR: int = '/'







    def addFileSystemListener(self, listener: ghidra.framework.store.FileSystemListener) -> None:
        """
        Adds the given listener to be notified of file system changes.
        @param listener the listener to be added.
        """
        ...

    def createDataFile(self, parentPath: unicode, name: unicode, istream: java.io.InputStream, comment: unicode, contentType: unicode, monitor: ghidra.util.task.TaskMonitor) -> ghidra.framework.store.DataFileItem:
        """
        Creates a new empty data file within the specified parent folder.
        @param parentPath folder path of parent
        @param name new data file name
        @param istream source data
        @param comment version comment (used for versioned file system only)
        @param contentType application defined content type
        @param monitor progress monitor (used for cancel support,
         progress not used since length of input stream is unknown)
        @return new data file
        @throws DuplicateFileException Thrown if a folderItem with that name already exists.
        @throws InvalidNameException if the name has illegal characters.
         all alphanumerics
        @throws IOException if an IO error occurs.
        @throws CancelledException if cancelled by monitor
        """
        ...

    @overload
    def createDatabase(self, parentPath: unicode, name: unicode, fileID: unicode, contentType: unicode, bufferSize: int, user: unicode, projectPath: unicode) -> db.buffers.ManagedBufferFile:
        """
        Create a new empty database item within the specified parent folder.
         If this is a versioned file-system, the associated item is checked-out.
         The resulting checkoutId can be obtained from the returned buffer file.
        @param parentPath folder path of parent
        @param name new database name
        @param fileID file ID to be associated with new database or null
        @param contentType application defined content type
        @param bufferSize buffer size.  If copying an existing BufferFile, the buffer
         size must be the same as the source file.
        @param user name of user creating item (required for versioned item)
        @param projectPath path of project in which database is checked-out (required for versioned item)
        @return an empty BufferFile open for read-write.
        @throws FileNotFoundException thrown if parent folder does not exist.
        @throws DuplicateFileException if a folder item exists with this name
        @throws InvalidNameException if the name does not have
         all alphanumerics
        @throws IOException if an IO error occurs.
        """
        ...

    @overload
    def createDatabase(self, parentPath: unicode, name: unicode, fileID: unicode, bufferFile: db.buffers.BufferFile, comment: unicode, contentType: unicode, resetDatabaseId: bool, monitor: ghidra.util.task.TaskMonitor, user: unicode) -> ghidra.framework.store.DatabaseItem:
        """
        Create a new database item within the specified parent folder using the contents
         of the specified BufferFile.
        @param parentPath folder path of parent
        @param name new database name
        @param fileID file ID to be associated with new database or null
        @param bufferFile data source
        @param comment version comment (used for versioned file system only)
        @param contentType application defined content type
        @param resetDatabaseId if true database ID will be reset for new Database
        @param monitor allows the database copy to be monitored and cancelled.
        @param user name of user creating item (required for versioned item)
        @return new DatabaseItem
        @throws FileNotFoundException thrown if parent folder does not exist.
        @throws DuplicateFileException if a folder item exists with this name
        @throws InvalidNameException if the name does not have
         all alphanumerics
        @throws IOException if an IO error occurs.
        @throws CancelledException if cancelled by monitor
        """
        ...

    def createFile(self, parentPath: unicode, name: unicode, packedFile: java.io.File, monitor: ghidra.util.task.TaskMonitor, user: unicode) -> ghidra.framework.store.FolderItem:
        """
        Creates a new file item from a packed file.
         The content/item type must be determined from the input stream.
        @param parentPath folder path of parent
        @param name new data file name
        @param packedFile packed file data
        @param monitor progress monitor (used for cancel support,
         progress not used since length of input stream is unknown)
        @param user name of user creating item (required for versioned item)
        @return new item
        @throws InvalidNameException if the name has illegal characters.
         all alphanumerics
        @throws IOException if an IO error occurs.
        @throws CancelledException if cancelled by monitor
        """
        ...

    def createFolder(self, parentPath: unicode, folderName: unicode) -> None:
        """
        Creates a new subfolder within the specified parent folder.
        @param parentPath folder path of parent
        @param folderName name of new subfolder
        @throws DuplicateFileException if a folder exists with this name
        @throws InvalidNameException if the name does not have
         all alphanumerics
        @throws IOException thrown if an IO error occurs.
        """
        ...

    def deleteFolder(self, folderPath: unicode) -> None:
        """
        Delete the specified folder.
        @param folderPath path of folder to be deleted
        @throws FolderNotEmptyException Thrown if the folder is not empty.
        @throws FileNotFoundException if there is no folder with the given path name.
        @throws IOException if error occurred during delete.
        """
        ...

    def dispose(self) -> None:
        """
        Cleanup and release resources
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def fileExists(self, folderPath: unicode, name: unicode) -> bool:
        """
        Returns true if the file exists
        @param folderPath the folderPath of the folder that may contain the file.
        @param name the name of the file to check for existence.
        @throws IOException if an IO error occurs.
        """
        ...

    def folderExists(self, folderPath: unicode) -> bool:
        """
        Returns true if the folder specified by the path exists.
        @param folderPath the name of the folder to check for existence.
        @return true if the folder exists.
        @throws IOException if an IO error occurs.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFolderNames(self, folderPath: unicode) -> List[unicode]:
        """
        Return a list of subfolders (by name) that are stored within the specified folder path.
        @throws FileNotFoundException if folder path does not exist.
        @throws IOException if IO error occurs.
        """
        ...

    @overload
    def getItem(self, fileID: unicode) -> ghidra.framework.store.FolderItem:
        """
        Returns the FolderItem specified by its unique File-ID
        @param fileID the items unique file ID
        @return the FolderItem with the given folderPath and name, or null if it doesn't exist.
        @throws IOException if IO error occurs.
        @throws UnsupportedOperationException if file-system does not support this operation
        """
        ...

    @overload
    def getItem(self, folderPath: unicode, name: unicode) -> ghidra.framework.store.FolderItem:
        """
        Returns the FolderItem in the given folder with the given name
        @param folderPath the folder path containing the item.
        @param name the name of the item.
        @return the FolderItem with the given folderPath and name, or null if it doesn't exist.
        @throws IOException if IO error occurs.
        """
        ...

    def getItemCount(self) -> int:
        """
        Returns the number of folder items contained within this file-system.
        @throws IOException
        @throws UnsupportedOperationException if file-system does not support this operation
        """
        ...

    def getItemNames(self, folderPath: unicode) -> List[unicode]:
        """
        Returns a list of the folder item names contained in the given folder.
        @param folderPath the path of the folder.
        @return a list of folder item names.
        @throws IOException
        """
        ...

    def getUserName(self) -> unicode:
        """
        Get user name associated with this filesystem.  In the case of a remote filesystem
         this will correspond to the name used during login/authentication.  A null value may
         be returned if user name unknown.
        """
        ...

    def hashCode(self) -> int: ...

    def isOnline(self) -> bool:
        """
        Returns true if file-system is on-line.
        """
        ...

    def isReadOnly(self) -> bool:
        """
        Returns true if file-system is read-only.
        @throws IOException
        """
        ...

    def isShared(self) -> bool:
        """
        Returns true if this file system is shared
        """
        ...

    def isVersioned(self) -> bool:
        """
        Returns true if the file-system requires check-outs when
         modifying folder items.
        """
        ...

    def moveFolder(self, parentPath: unicode, folderName: unicode, newParentPath: unicode) -> None:
        """
        Move the specified folder to the path specified by newFolderPath.
         The moved folder must not be an ancestor of the new Parent.
        @param parentPath path of parent folder that the moving folder currently resides in.
        @param folderName name of the folder within the parentPath to be moved.
        @param newParentPath path to where the folder is to be moved.
        @throws FileNotFoundException if the moved folder does not exist.
        @throws DuplicateFileException if folder with the same name exists within the new parent folder
        @throws FileInUseException if any file within this folder or its decendents are in-use or checked-out
        @throws IOException if an IO error occurs.
        @throws InvalidNameException if the new FolderPath contains an illegal file name.
        @throws IllegalArgumentException if new Parent is invalid.
        """
        ...

    def moveItem(self, folderPath: unicode, name: unicode, newFolderPath: unicode, newName: unicode) -> None:
        """
        Moves the specified item to a new folder.
        @param folderPath path of folder containing the item.
        @param name name of the item to be moved.
        @param newFolderPath path of folder where item is to be moved.
        @throws FileNotFoundException if the item does not exist.
        @throws DuplicateFileException if item with the same name exists within the new parent folder.
        @throws FileInUseException if the item is in-use or checked-out
        @throws IOException if an IO error occurs.
        @throws InvalidNameException if the newName is invalid
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeFileSystemListener(self, listener: ghidra.framework.store.FileSystemListener) -> None:
        """
        Removes the listener from being notified of file system changes.
        @param listener
        """
        ...

    def renameFolder(self, parentPath: unicode, folderName: unicode, newFolderName: unicode) -> None:
        """
        Renames the specified folder to a new name.
        @param parentPath the parent folder of the folder to be renamed.
        @param folderName the current name of the folder to be renamed.
        @param newFolderName the name the folder to be renamed to.
        @throws FileNotFoundException if the folder to be renamed does not exist.
        @throws DuplicateFileException if folder with the new name already exists.
        @throws FileInUseException if any file within this folder or its decendents are in-use or checked-out
        @throws IOException if an IO error occurs.
        @throws InvalidNameException if the new FolderName contains an illegal file name.
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
    def itemCount(self) -> int: ...

    @property
    def online(self) -> bool: ...

    @property
    def readOnly(self) -> bool: ...

    @property
    def shared(self) -> bool: ...

    @property
    def userName(self) -> unicode: ...

    @property
    def versioned(self) -> bool: ...
