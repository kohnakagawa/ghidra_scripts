from typing import List
import ghidra.formats.gfilesystem
import java.lang


class FileSystemIndexHelper(object):
    """
    A helper class used by GFilesystem implementors to track mappings between GFile
     instances and the underlying container filesystem's native file objects.

     Threadsafe after initial use of #storeFile(String, int, boolean, long, Object)
     by the owning filesystem.

     This class also provides filename 'unique-ifying' (per directory) where an auto-incrementing
     number will be added to a file's filename if it is not unique in the directory.

    """





    def __init__(self, fs: ghidra.formats.gfilesystem.GFileSystem, fsFSRL: ghidra.formats.gfilesystem.FSRLRoot):
        """
        Creates a new {@link FileSystemIndexHelper} for the specified {@link GFileSystem}.
         <p>
         A "root" directory GFile will be auto-created for the filesystem.
         <p>
        @param fs the {@link GFileSystem} that this index will be for.
        @param fsFSRL the {@link FSRLRoot fsrl} of the filesystem itself.
         (this parameter is explicitly passed here so there is no possibility of trying to call
         back to the fs's {@link GFileSystem#getFSRL()} on a half-constructed filesystem.)
        """
        ...



    def clear(self) -> None:
        """
        Removes all file info from this index.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFileCount(self) -> int:
        """
        Number of files in this index.
        @return number of file in this index.
        """
        ...

    def getListing(self, directory: ghidra.formats.gfilesystem.GFile) -> List[ghidra.formats.gfilesystem.GFile]:
        """
        Mirror's {@link GFileSystem#getListing(GFile)} interface.
        @param directory {@link GFile} directory to get the list of child files that have been
         added to this index, null means root directory.
        @return {@link List} of GFile files that are in the specified directory, never null.
        """
        ...

    def getMetadata(self, f: ghidra.formats.gfilesystem.GFile) -> METADATATYPE:
        """
        Gets the opaque filesystem specific blob that was associated with the specified file.
        @param f {@link GFile} to look for.
        @return Filesystem specific blob associated with the specified file, or null if not found.
        """
        ...

    def getRootDir(self) -> ghidra.formats.gfilesystem.GFile:
        """
        Gets the root {@link GFile} object for this filesystem index.
        @return root {@link GFile} object.
        """
        ...

    def hashCode(self) -> int: ...

    def lookup(self, path: unicode) -> ghidra.formats.gfilesystem.GFile:
        """
        Mirror's {@link GFileSystem#lookup(String)} interface.
        @param path path and filename of a file to find.
        @return {@link GFile} instance or null if no file was added to the index at that path.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def storeFile(self, __a0: unicode, __a1: int, __a2: bool, __a3: long, __a4: object) -> ghidra.formats.gfilesystem.GFileImpl: ...

    def storeFileWithParent(self, __a0: unicode, __a1: ghidra.formats.gfilesystem.GFile, __a2: int, __a3: bool, __a4: long, __a5: object) -> ghidra.formats.gfilesystem.GFile: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def fileCount(self) -> int: ...

    @property
    def rootDir(self) -> ghidra.formats.gfilesystem.GFile: ...
