from typing import List
import ghidra.formats.gfilesystem
import ghidra.util.task
import java.io
import java.lang


class LocalFileSystem(object, ghidra.formats.gfilesystem.GFileSystem):
    """
    A GFileSystem implementation giving access to the user's operating system's
     local file system.

     This implementation does not have a GFileSystemFactory as
     this class will be used as the single root filesystem.

     Closing() this filesystem does nothing.
    """

    FSTYPE: unicode = u'file'







    def close(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def getFSRL(self) -> ghidra.formats.gfilesystem.FSRLRoot: ...

    def getFileCount(self) -> int: ...

    def getInfo(self, file: ghidra.formats.gfilesystem.GFile, monitor: ghidra.util.task.TaskMonitor) -> unicode: ...

    def getInputStream(self, file: ghidra.formats.gfilesystem.GFile, monitor: ghidra.util.task.TaskMonitor) -> java.io.InputStream: ...

    def getListing(self, directory: ghidra.formats.gfilesystem.GFile) -> List[ghidra.formats.gfilesystem.GFile]: ...

    def getLocalFile(self, fsrl: ghidra.formats.gfilesystem.FSRL) -> java.io.File: ...

    def getName(self) -> unicode: ...

    def getRefManager(self) -> ghidra.formats.gfilesystem.FileSystemRefManager: ...

    def getType(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def isClosed(self) -> bool: ...

    def isLocalSubdir(self, fsrl: ghidra.formats.gfilesystem.FSRL) -> bool:
        """
        Returns true if the {@link FSRL} is a local filesystem subdirectory.
        @param fsrl {@link FSRL} to test.
        @return boolean true if local filesystem directory.
        """
        ...

    def isStatic(self) -> bool: ...

    def lookup(self, path: unicode) -> ghidra.formats.gfilesystem.GFileImpl: ...

    @staticmethod
    def makeGlobalRootFS() -> ghidra.formats.gfilesystem.LocalFileSystem:
        """
        Create a new instance
        @return new {@link LocalFileSystem} instance using {@link #FSTYPE} as its FSRL type.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def FSRL(self) -> ghidra.formats.gfilesystem.FSRLRoot: ...

    @property
    def closed(self) -> bool: ...

    @property
    def description(self) -> unicode: ...

    @property
    def fileCount(self) -> int: ...

    @property
    def name(self) -> unicode: ...

    @property
    def refManager(self) -> ghidra.formats.gfilesystem.FileSystemRefManager: ...

    @property
    def static(self) -> bool: ...

    @property
    def type(self) -> unicode: ...
