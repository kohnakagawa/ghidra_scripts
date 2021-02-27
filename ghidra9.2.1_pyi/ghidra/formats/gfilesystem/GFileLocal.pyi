from typing import List
import ghidra.formats.gfilesystem
import java.io
import java.lang


class GFileLocal(object, ghidra.formats.gfilesystem.GFile):
    """
    GFile implementation that refers to a real java.io.File on the local
     file system.

     This implementation keeps track of the FSRL and GFile path separately so that
     they can be different, as is the case with LocalFileSystemSub files that
     have real FSRLs but fake relative paths.
    """





    def __init__(self, f: java.io.File, path: unicode, fsrl: ghidra.formats.gfilesystem.FSRL, fs: ghidra.formats.gfilesystem.GFileSystem, parent: ghidra.formats.gfilesystem.GFile):
        """
        Create new GFileLocal instance.
        @param f {@link File} on the local filesystem
        @param path String path (including filename) of this instance
        @param fsrl {@link FSRL} of this instance
        @param fs {@link GFileSystem} that created this file.
        @param parent Parent directory that contains this file, or null if parent is root.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFSRL(self) -> ghidra.formats.gfilesystem.FSRL: ...

    def getFilesystem(self) -> ghidra.formats.gfilesystem.GFileSystem: ...

    def getLastModified(self) -> long: ...

    def getLength(self) -> long: ...

    def getListing(self) -> List[object]: ...

    def getLocalFile(self) -> java.io.File: ...

    def getName(self) -> unicode: ...

    def getParentFile(self) -> ghidra.formats.gfilesystem.GFile: ...

    def getPath(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def isDirectory(self) -> bool: ...

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
    def FSRL(self) -> ghidra.formats.gfilesystem.FSRL: ...

    @property
    def directory(self) -> bool: ...

    @property
    def filesystem(self) -> ghidra.formats.gfilesystem.GFileSystem: ...

    @property
    def lastModified(self) -> long: ...

    @property
    def length(self) -> long: ...

    @property
    def listing(self) -> List[object]: ...

    @property
    def localFile(self) -> java.io.File: ...

    @property
    def name(self) -> unicode: ...

    @property
    def parentFile(self) -> ghidra.formats.gfilesystem.GFile: ...

    @property
    def path(self) -> unicode: ...
