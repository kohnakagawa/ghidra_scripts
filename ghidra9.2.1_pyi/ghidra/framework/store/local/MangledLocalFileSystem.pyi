from typing import List
import db.buffers
import ghidra.framework.store
import ghidra.framework.store.local
import ghidra.util.task
import java.io
import java.lang


class MangledLocalFileSystem(ghidra.framework.store.local.LocalFileSystem):
    """
    MangledLocalFileSystem implements the legacy project data storage
     scheme which utilizes a simplified name mangling which provides case-sensitive
     file-naming with support for spaces.  Project folder hierarchy maps directly to
     the actual storage hierarchy.
    """

    MAX_NAME_LENGTH: int = 60







    def addFileSystemListener(self, listener: ghidra.framework.store.FileSystemListener) -> None: ...

    def convertToIndexedLocalFileSystem(self) -> None:
        """
        Convert this mangled filesystem to an indexed filesystem.  This instance should be discarded
         and not used once the conversion has completed.
        @throws IOException
        """
        ...

    def createDataFile(self, parentPath: unicode, name: unicode, istream: java.io.InputStream, comment: unicode, contentType: unicode, monitor: ghidra.util.task.TaskMonitor) -> ghidra.framework.store.local.LocalDataFile: ...

    @overload
    def createDatabase(self, parentPath: unicode, name: unicode, fileID: unicode, contentType: unicode, bufferSize: int, user: unicode, projectPath: unicode) -> db.buffers.LocalManagedBufferFile: ...

    @overload
    def createDatabase(self, parentPath: unicode, name: unicode, fileID: unicode, bufferFile: db.buffers.BufferFile, comment: unicode, contentType: unicode, resetDatabaseId: bool, monitor: ghidra.util.task.TaskMonitor, user: unicode) -> ghidra.framework.store.local.LocalDatabaseItem: ...

    def createFile(self, parentPath: unicode, name: unicode, packedFile: java.io.File, monitor: ghidra.util.task.TaskMonitor, user: unicode) -> ghidra.framework.store.local.LocalDatabaseItem: ...

    def createFolder(self, parentPath: unicode, folderName: unicode) -> None: ...

    def createTemporaryDatabase(self, parentPath: unicode, name: unicode, fileID: unicode, bufferFile: db.buffers.BufferFile, contentType: unicode, resetDatabaseId: bool, monitor: ghidra.util.task.TaskMonitor) -> ghidra.framework.store.local.LocalDatabaseItem: ...

    def deleteFolder(self, folderPath: unicode) -> None: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def escapeHiddenDirPrefixChars(name: unicode) -> unicode:
        """
        Escape hidden prefix chars in name
        @param name
        @return escaped name
        """
        ...

    def fileExists(self, folderPath: unicode, name: unicode) -> bool: ...

    def folderExists(self, folderPath: unicode) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFolderNames(self, folderPath: unicode) -> List[unicode]: ...

    @overload
    def getItem(self, fileID: unicode) -> ghidra.framework.store.FolderItem: ...

    @overload
    def getItem(self, folderPath: unicode, name: unicode) -> ghidra.framework.store.local.LocalFolderItem: ...

    def getItemCount(self) -> int: ...

    def getItemNames(self, folderPath: unicode) -> List[unicode]:
        """
        @see ghidra.framework.store.FileSystem#getItemNames(java.lang.String)
        """
        ...

    @staticmethod
    def getLocalFileSystem(rootPath: unicode, create: bool, isVersioned: bool, readOnly: bool, enableAsyncronousDispatching: bool) -> ghidra.framework.store.local.LocalFileSystem:
        """
        Construct a local filesystem for existing data
        @param rootPath
        @param create
        @param isVersioned
        @param readOnly
        @param enableAsyncronousDispatching
        @return local filesystem
        @throws FileNotFoundException if specified rootPath does not exist
        @throws IOException if error occurs while reading/writing index files
        """
        ...

    def getMaxNameLength(self) -> int: ...

    def getUserName(self) -> unicode: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isHiddenDirName(name: unicode) -> bool:
        """
        Determines if the specified storage directory name corresponds to a
         hidden directory (includes both system and application hidden directories).
        @param name directory name as it appears on storage file system.
        @return true if name is a hidden name, else false
        """
        ...

    def isOnline(self) -> bool: ...

    def isReadOnly(self) -> bool: ...

    @staticmethod
    def isRefreshRequired() -> bool:
        """
        @return true if folder item resources must be refreshed.
        @see #setValidationRequired()
        """
        ...

    def isShared(self) -> bool: ...

    @staticmethod
    def isValidNameCharacter(c: int) -> bool:
        """
        @return true if c is a valid character within the FileSystem.
        """
        ...

    def isVersioned(self) -> bool: ...

    def migrationInProgress(self) -> bool: ...

    def moveFolder(self, parentPath: unicode, folderName: unicode, newParentPath: unicode) -> None: ...

    def moveItem(self, folderPath: unicode, name: unicode, newFolderPath: unicode, newName: unicode) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeFileSystemListener(self, listener: ghidra.framework.store.FileSystemListener) -> None: ...

    def renameFolder(self, parentPath: unicode, folderName: unicode, newFolderName: unicode) -> None: ...

    def setAssociatedRepositoryLogger(self, repositoryLogger: ghidra.framework.store.local.RepositoryLogger) -> None:
        """
        Associate file system with a specific repository logger
        @param repositoryLogger
        """
        ...

    @staticmethod
    def setValidationRequired() -> None:
        """
        If set, the state of folder item resources will be continually refreshed.
         This is required if multiple instances exist for a single item.  The default is
         disabled.   This feature should be enabled for testing only since it may have a
         significant performance impact.  This does not provide locking which may be
         required for a shared environment (e.g., checkin locking is only managed by a
         single instance).
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

    @staticmethod
    def unescapeHiddenDirPrefixChars(name: unicode) -> unicode:
        """
        Unescape a non-hidden directory name
        @param name
        @return unescaped name or null if name is a hidden name
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def itemCount(self) -> int: ...

    @property
    def maxNameLength(self) -> int: ...
