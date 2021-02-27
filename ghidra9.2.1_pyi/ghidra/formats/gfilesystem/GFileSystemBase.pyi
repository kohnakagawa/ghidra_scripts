from typing import List
import ghidra.formats.gfilesystem
import ghidra.util.task
import java.io
import java.lang


class GFileSystemBase(object, ghidra.formats.gfilesystem.GFileSystem):
    """
    This is the original GFileSystem implementation abstract base class, with most of the
     initially implemented filesystem types extending this class.

     The new GFileSystem interface is being retro-fitted into this equation to support
     better probing and factory syntax, and new implementations should be based on
     the interface instead of extending this abstract class.

     NOTE:
     ALL GFileSystem sub-CLASSES MUST END IN "FileSystem".
     If not, the ClassSearcher will not find them.
     Yes, it is an implementation detail.

     GFileSystemBase instances are constructed when probing a container file and are queried
     with #isValid(TaskMonitor) to determine if the container file is handled
     by the GFileSystemBase subclass.
     The ByteProvider given to the constructor is not considered 'owned' by
     the GFileSystemBase instance until after it passes the #isValid(TaskMonitor)
     check and is #open(TaskMonitor).

    """









    def close(self) -> None:
        """
        Closes the file system.
         All resources should be released. (programs, temporary files, etc.)
        @throws IOException if an I/O error occurs
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def getFSRL(self) -> ghidra.formats.gfilesystem.FSRLRoot: ...

    def getFileCount(self) -> int: ...

    def getInfo(self, __a0: ghidra.formats.gfilesystem.GFile, __a1: ghidra.util.task.TaskMonitor) -> unicode: ...

    def getInputStream(self, file: ghidra.formats.gfilesystem.GFile, monitor: ghidra.util.task.TaskMonitor) -> java.io.InputStream: ...

    def getListing(self, directory: ghidra.formats.gfilesystem.GFile) -> List[ghidra.formats.gfilesystem.GFile]: ...

    def getName(self) -> unicode:
        """
        Returns the name of this file system.
        @return the name of this file system
        """
        ...

    def getRefManager(self) -> ghidra.formats.gfilesystem.FileSystemRefManager: ...

    def getType(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def isClosed(self) -> bool: ...

    def isStatic(self) -> bool: ...

    def isValid(self, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Returns true if this file system implementation
         can handle the bytes provided.
         This method should perform the minimal amount of
         checks required to determine validity.
         Keep it quick and tight!
        @param monitor a task monitor
        @return true if valid for the byte provider
        @throws IOException if an I/O error occurs
        """
        ...

    def lookup(self, path: unicode) -> ghidra.formats.gfilesystem.GFile: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def open(self, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Opens the file system.
        @throws IOException if an I/O error occurs
        @throws CryptoException if an encryption error occurs
        """
        ...

    def setFSRL(self, fsrl: ghidra.formats.gfilesystem.FSRLRoot) -> None: ...

    def setFilesystemService(self, fsService: ghidra.formats.gfilesystem.FileSystemService) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def FSRL(self) -> ghidra.formats.gfilesystem.FSRLRoot: ...

    @FSRL.setter
    def FSRL(self, value: ghidra.formats.gfilesystem.FSRLRoot) -> None: ...

    @property
    def closed(self) -> bool: ...

    @property
    def description(self) -> unicode: ...

    @property
    def fileCount(self) -> int: ...

    @property
    def filesystemService(self) -> None: ...  # No getter available.

    @filesystemService.setter
    def filesystemService(self, value: ghidra.formats.gfilesystem.FileSystemService) -> None: ...

    @property
    def name(self) -> unicode: ...

    @property
    def refManager(self) -> ghidra.formats.gfilesystem.FileSystemRefManager: ...

    @property
    def static(self) -> bool: ...

    @property
    def type(self) -> unicode: ...
