from typing import List
import ghidra.formats.gfilesystem
import java.lang


class SingleFileSystemIndexHelper(object):
    """
    A helper class used by GFilesystem implementors that have a single file to handle lookups
     and requests for that file.

     This class is patterned on FileSystemIndexHelper and has pretty much the same api.
    """





    def __init__(self, fs: ghidra.formats.gfilesystem.GFileSystem, fsFSRL: ghidra.formats.gfilesystem.FSRLRoot, payloadFilename: unicode, length: long, payloadMD5: unicode):
        """
        Creates a new instance.

         A "root" directory GFile will be auto-created for the filesystem.
         <p>
        @param fs the {@link GFileSystem} that this index will be for.
        @param fsFSRL the {@link FSRLRoot fsrl} of the filesystem itself.
         (this parameter is explicitly passed here so there is no possibility of trying to call
         back to the fs's {@link GFileSystem#getFSRL()} on a half-constructed filesystem.)
        @param payloadFilename name of the single file that this filesystem holds.
        @param length length of the payload file.
        @param payloadMD5 md5 of the payload file.
        """
        ...



    def clear(self) -> None:
        """
        Clears the data held by this object.
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
        @throws IOException if already closed.
        """
        ...

    def getPayloadFile(self) -> ghidra.formats.gfilesystem.GFile:
        """
        Gets the 'payload' file, ie. the main file of this filesystem.
        @return {@link GFile} payload file.
        """
        ...

    def getRootDir(self) -> ghidra.formats.gfilesystem.GFile:
        """
        Gets the root {@link GFile} object for this filesystem index.
        @return root {@link GFile} object.
        """
        ...

    def getRootDirFSRL(self) -> ghidra.formats.gfilesystem.FSRL:
        """
        Gets the root dir's FSRL.
        @return {@link FSRL} of the root dir.
        """
        ...

    def hashCode(self) -> int: ...

    def isClosed(self) -> bool:
        """
        Returns true if this object has been {@link #clear()}'ed.
        @return boolean true if data has been cleared.
        """
        ...

    def lookup(self, path: unicode) -> ghidra.formats.gfilesystem.GFile:
        """
        Mirror's {@link GFileSystem#lookup(String)} interface.
        @param path path and filename of a file to find (either "/" for root or the payload file's
         path).
        @return {@link GFile} instance or null if requested path is not the same as
         the payload file.
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
    def closed(self) -> bool: ...

    @property
    def fileCount(self) -> int: ...

    @property
    def payloadFile(self) -> ghidra.formats.gfilesystem.GFile: ...

    @property
    def rootDir(self) -> ghidra.formats.gfilesystem.GFile: ...

    @property
    def rootDirFSRL(self) -> ghidra.formats.gfilesystem.FSRL: ...
