from typing import List
import ghidra.formats.gfilesystem
import ghidra.util.task
import java.io
import java.lang


class LocalFileSystemSub(object, ghidra.formats.gfilesystem.GFileSystem):
    """
    A GFileSystem interface to a part of the user's local / native file system.

     This class is a sub-view of the LocalFileSystem, and returns hybrid GFile objects
     that have fully specified FSRL paths that are valid in the Root filesystem, but relative
     GFile paths.

     This class's name doesn't end with "FileSystem" to ensure it will not be auto-discovered
     by the FileSystemFactoryMgr.
    """





    def __init__(self, rootDir: java.io.File, rootFS: ghidra.formats.gfilesystem.GFileSystem): ...



    def close(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def getFSRL(self) -> ghidra.formats.gfilesystem.FSRLRoot: ...

    def getFileCount(self) -> int: ...

    def getInfo(self, file: ghidra.formats.gfilesystem.GFile, monitor: ghidra.util.task.TaskMonitor) -> unicode: ...

    def getInputStream(self, file: ghidra.formats.gfilesystem.GFile, monitor: ghidra.util.task.TaskMonitor) -> java.io.InputStream: ...

    def getListing(self, directory: ghidra.formats.gfilesystem.GFile) -> List[ghidra.formats.gfilesystem.GFile]: ...

    def getName(self) -> unicode: ...

    def getRefManager(self) -> ghidra.formats.gfilesystem.FileSystemRefManager: ...

    def getType(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def isClosed(self) -> bool: ...

    def isStatic(self) -> bool: ...

    def lookup(self, path: unicode) -> ghidra.formats.gfilesystem.GFile: ...

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
