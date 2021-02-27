from typing import List
import ghidra.formats.gfilesystem
import java.lang


class FileSystemCache(object, ghidra.formats.gfilesystem.FileSystemEventListener):
    """
    A threadsafe cache of GFileSystem instances (organized by their FSRLRoot)

     Any filesystems that are not referenced by outside users (via a FileSystemRef) will
     be closed and removed from the cache when the next #cacheMaint() is performed.
    """





    def __init__(self, rootFS: ghidra.formats.gfilesystem.GFileSystem):
        """
        Creates a new FileSystemCache object.
        @param rootFS reference to the global root file system, which is a special case
         file system that is not subject to eviction.
        """
        ...



    def add(self, fs: ghidra.formats.gfilesystem.GFileSystem) -> None:
        """
        Adds a new {@link GFileSystem} to the cache.
        @param fs {@link GFileSystem} to add to this cache.
        """
        ...

    def cacheMaint(self) -> None:
        """
        Performs maintainence on the filesystem cache, closing() any filesystems
         that are not used anymore.
        """
        ...

    def clear(self) -> None:
        """
        Forcefully closes any filesystems in the cache, then clears the list of
         cached filesystems.
        """
        ...

    def closeAllUnused(self) -> None:
        """
        Removes any unused filesystems in the cache.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFilesystemRefMountedAt(self, containerFSRL: ghidra.formats.gfilesystem.FSRL) -> ghidra.formats.gfilesystem.FileSystemRef:
        """
        Returns a new {@link FileSystemRef} to a already mounted {@link GFileSystem filesystem}
         (keeping the filesystem pinned in memory without the risk of it being closed during
         a race condition).
         <p>
         The caller is responsible for {@link FileSystemRef#close() closing} it when done.
         <p>
         Returns null if there is no filesystem mounted at the requested container fsrl.
        @param containerFSRL {@link FSRL} location where a filesystem is already mounted
        @return new {@link FileSystemRef} to the already mounted filesystem, or null
        """
        ...

    def getMountedFilesystems(self) -> List[ghidra.formats.gfilesystem.FSRLRoot]:
        """
        Returns a list of mounted file systems.
         <p>
        @return {@link List} of {@link FSRLRoot} of filesystems that are currently mounted.
        """
        ...

    def getRef(self, fsrl: ghidra.formats.gfilesystem.FSRLRoot) -> ghidra.formats.gfilesystem.FileSystemRef:
        """
        Returns a new {@link FileSystemRef} to an existing, already open {@link GFileSystem filesystem}.
         Caller is responsible for {@link FileSystemRef#close() closing} it.
         <p>
         Returns NULL if the requested filesystem isn't already open and mounted in the cache.
        @param fsrl {@link FSRLRoot} of the desired filesystem.
        @return a new {@link FileSystemRef} or null if the filesystem is not currently mounted.
        """
        ...

    def hashCode(self) -> int: ...

    def isFilesystemMountedAt(self, containerFSRL: ghidra.formats.gfilesystem.FSRL) -> bool:
        """
        Returns true if there is a filesystem in the cache that has a containerFSRL that
         is {@link FSRL#isEquivalent(FSRL) equiv} to the specified FSRL.
         <p>
        @param containerFSRL {@link FSRL} location to query for currently mounted filesystem.
        @return true if there is a filesystem mounted using that containerFSRL.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def onFilesystemClose(self, fs: ghidra.formats.gfilesystem.GFileSystem) -> None: ...

    def onFilesystemRefChange(self, fs: ghidra.formats.gfilesystem.GFileSystem, refManager: ghidra.formats.gfilesystem.FileSystemRefManager) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def mountedFilesystems(self) -> List[object]: ...
