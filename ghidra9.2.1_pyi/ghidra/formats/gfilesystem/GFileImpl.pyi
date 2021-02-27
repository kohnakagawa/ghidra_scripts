from typing import List
import ghidra.formats.gfilesystem
import java.lang


class GFileImpl(object, ghidra.formats.gfilesystem.GFile):
    """
    Base implementation of file in a GFileSystem.

     Only valid while the owning filesystem object is still open and not
     GFileSystem#close().

     See GFile.
    """









    def equals(self, obj: object) -> bool: ...

    @staticmethod
    def fromFSRL(fileSystem: ghidra.formats.gfilesystem.GFileSystem, parent: ghidra.formats.gfilesystem.GFile, fsrl: ghidra.formats.gfilesystem.FSRL, isDirectory: bool, length: long) -> ghidra.formats.gfilesystem.GFileImpl:
        """
        Creates a GFile for a filesystem using the information in a FSRL as the file's name
         and as a child of the specified parent.
         <p>
        @param fileSystem the {@link GFileSystem} that owns this file
        @param parent the parent of the new GFile or null if child-of-root.
        @param fsrl {@link FSRL} to assign to the file.
        @param isDirectory boolean flag to indicate that this is a directory
        @param length length of the file (use -1 if not know or specified).
        @return a new {@link GFileImpl}
        """
        ...

    @staticmethod
    def fromFilename(fileSystem: ghidra.formats.gfilesystem.GFileSystem, parent: ghidra.formats.gfilesystem.GFile, filename: unicode, isDirectory: bool, length: long, fsrl: ghidra.formats.gfilesystem.FSRL) -> ghidra.formats.gfilesystem.GFileImpl:
        """
        Creates a GFile for a filesystem using a simple name (not a path)
         and as a child of the specified parent.
         <p>
         The filename is accepted without checking or validation.
         <p>
        @param fileSystem the {@link GFileSystem} that owns this file
        @param parent the parent of the new GFile or null if child-of-root.
        @param filename the file's name, not used if FSRL param specified.
        @param isDirectory boolean flag to indicate that this is a directory
        @param length length of the file (use -1 if not know or specified).
        @param fsrl {@link FSRL} to assign to the file, NULL if an auto-created FSRL is ok.
        @return a new {@link GFileImpl}
        """
        ...

    @overload
    @staticmethod
    def fromPathString(fileSystem: ghidra.formats.gfilesystem.GFileSystem, path: unicode, fsrl: ghidra.formats.gfilesystem.FSRL, isDirectory: bool, length: long) -> ghidra.formats.gfilesystem.GFileImpl:
        """
        Creates a GFile for a filesystem using a string
         path (ie. "dir/subdir/filename"), with the path starting at the root of the
         filesystem.
         <p>
         The parents of this GFile are created fresh from any directory names
         in the path string.  It is better to use the
         {@link #fromFilename(GFileSystem, GFile, String, boolean, long, FSRL)} method
         to create GFile instances if you can supply the parent value as that will
         allow reuse of the parent objects instead of duplicates of them being created
         for each file with the same parent path.
         <p>
        @param fileSystem the {@link GFileSystem} that owns this file
        @param path forward slash '/' separated path and filename string.
        @param fsrl {@link FSRL} to assign to the file, NULL if an auto-created FSRL is ok.
        @param isDirectory boolean flag to indicate that this is a directory
        @param length length of the file (use -1 if not know or specified).
        @return a new {@link GFileImpl}
        """
        ...

    @overload
    @staticmethod
    def fromPathString(fileSystem: ghidra.formats.gfilesystem.GFileSystem, parent: ghidra.formats.gfilesystem.GFile, path: unicode, fsrl: ghidra.formats.gfilesystem.FSRL, isDirectory: bool, length: long) -> ghidra.formats.gfilesystem.GFileImpl:
        """
        Creates a GFile for a specific owning filesystem using a string
         path (ie. "dir/subdir/filename"), with the path starting at the supplied
         {@code parent} directory.
         <p>
         The parents of this GFile are created fresh from any directory names
         in the path string.  It is better to use the
         {@link #fromFilename(GFileSystem, GFile, String, boolean, long, FSRL)} method
         to create GFile instances if you can supply the parent value as that will
         allow reuse of the parent objects instead of duplicates of them being created
         for each file with the same parent path.
         <p>
        @param fileSystem the {@link GFileSystem} that owns this file
        @param parent the parent of the new GFile or null if child-of-root.
        @param path forward slash '/' separated path and filename string.
        @param fsrl {@link FSRL} to assign to the file, NULL if an auto-created FSRL is ok.
        @param isDirectory boolean flag to indicate that this is a directory
        @param length length of the file (use -1 if not know or specified).
        @return a new {@link GFileImpl}
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFSRL(self) -> ghidra.formats.gfilesystem.FSRL: ...

    def getFilesystem(self) -> ghidra.formats.gfilesystem.GFileSystem: ...

    def getLastModified(self) -> long: ...

    def getLength(self) -> long: ...

    def getListing(self) -> List[object]: ...

    def getName(self) -> unicode: ...

    def getParentFile(self) -> ghidra.formats.gfilesystem.GFile: ...

    def getPath(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def isDirectory(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setFSRL(self, fsrl: ghidra.formats.gfilesystem.FSRL) -> None: ...

    def setLength(self, length: long) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def FSRL(self) -> ghidra.formats.gfilesystem.FSRL: ...

    @FSRL.setter
    def FSRL(self, value: ghidra.formats.gfilesystem.FSRL) -> None: ...

    @property
    def directory(self) -> bool: ...

    @property
    def filesystem(self) -> ghidra.formats.gfilesystem.GFileSystem: ...

    @property
    def lastModified(self) -> long: ...

    @property
    def length(self) -> long: ...

    @length.setter
    def length(self, value: long) -> None: ...

    @property
    def listing(self) -> List[object]: ...

    @property
    def name(self) -> unicode: ...

    @property
    def parentFile(self) -> ghidra.formats.gfilesystem.GFile: ...

    @property
    def path(self) -> unicode: ...
