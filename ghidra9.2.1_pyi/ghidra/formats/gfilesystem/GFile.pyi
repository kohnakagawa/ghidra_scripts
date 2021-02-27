from typing import List
import ghidra.formats.gfilesystem
import java.lang


class GFile(object):
    """
    Represents a file in a GFileSystem.

     Only valid while the #getFilesystem() object is still open and not
     GFileSystem#close().

    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFSRL(self) -> ghidra.formats.gfilesystem.FSRL:
        """
        The {@link FSRL} of this file.
        @return {@link FSRL} of this file.
        """
        ...

    def getFilesystem(self) -> ghidra.formats.gfilesystem.GFileSystem:
        """
        The {@link GFileSystem} that owns this file.
        @return {@link GFileSystem} that owns this file.
        """
        ...

    def getLastModified(self) -> long: ...

    def getLength(self) -> long:
        """
        Returns the length of this file, or -1 if not known.
        @return number of bytes in this file.
        """
        ...

    def getListing(self) -> List[ghidra.formats.gfilesystem.GFile]:
        """
        Returns a listing of files in this sub-directory.
         <p>
        @return {@link List} of {@link GFile} instances.
        @throws IOException if not a directory or error when accessing files.
        """
        ...

    def getName(self) -> unicode:
        """
        The name of this file.
        @return name of this file.
        """
        ...

    def getParentFile(self) -> ghidra.formats.gfilesystem.GFile:
        """
        The parent directory of this file.
        @return parent {@link GFile} directory of this file.
        """
        ...

    def getPath(self) -> unicode:
        """
        The path and filename of this file, relative to its owning filesystem.
        @return path and filename of this file, relative to its owning filesystem.
        """
        ...

    def hashCode(self) -> int: ...

    def isDirectory(self) -> bool:
        """
        Returns true if this is a directory.
         <p>
        @return boolean true if this file is a directory, false otherwise.
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
    def name(self) -> unicode: ...

    @property
    def parentFile(self) -> ghidra.formats.gfilesystem.GFile: ...

    @property
    def path(self) -> unicode: ...
