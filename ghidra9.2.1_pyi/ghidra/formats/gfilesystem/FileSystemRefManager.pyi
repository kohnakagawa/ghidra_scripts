import ghidra.formats.gfilesystem
import java.lang


class FileSystemRefManager(object):
    """
    A threadsafe helper class that manages creating and releasing FileSystemRef instances
     and broadcasting events to FileSystemEventListener listeners.

    """





    def __init__(self, fs: ghidra.formats.gfilesystem.GFileSystem):
        """
        Creates a new {@link FileSystemRefManager} pointing at the specified {@link GFileSystem}.
        @param fs {@link GFileSystem} to manage.
        """
        ...



    def addListener(self, listener: ghidra.formats.gfilesystem.FileSystemEventListener) -> None:
        """
        Adds a {@link FileSystemEventListener listener} that will be called when
         this filesystem is {@link FileSystemEventListener#onFilesystemClose(GFileSystem) closed}
         or when {@link FileSystemEventListener#onFilesystemRefChange(GFileSystem, FileSystemRefManager) refs change}.
        @param listener {@link FileSystemEventListener} to receive callbacks, weakly refd and
         automagically removed if a reference isn't held to the listener somewhere else.
        """
        ...

    def canClose(self, callersRef: ghidra.formats.gfilesystem.FileSystemRef) -> bool:
        """
        Returns true if the only {@link FileSystemRef} pinning this filesystem is the
         caller's ref.
        @param callersRef {@link FileSystemRef} to test
        @return boolean true if the tested {@link FileSystemRef} is the only ref pinning
         the filesystem.
        """
        ...

    def create(self) -> ghidra.formats.gfilesystem.FileSystemRef:
        """
        Creates a new {@link FileSystemRef} that points at the owning {@link GFileSystem filesystem}.
         <p>
        @return new {@link FileSystemRef} pointing at the filesystem, never null.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def finalize(self) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getLastUsedTimestamp(self) -> long: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def onClose(self) -> None:
        """
        Called from the {@link GFileSystem#close()} before any destructive changes have
         been made to gracefully shutdown the ref manager.
         <p>
         Broadcasts {@link FileSystemEventListener#onFilesystemClose(GFileSystem)}.
        """
        ...

    def release(self, ref: ghidra.formats.gfilesystem.FileSystemRef) -> None:
        """
        Releases an existing {@link FileSystemRef} and broadcasts
         {@link FileSystemEventListener#onFilesystemRefChange(GFileSystem, FileSystemRefManager)}
         to listeners.
         <p>
        @param ref the {@link FileSystemRef} to release.
        """
        ...

    def removeListener(self, listener: ghidra.formats.gfilesystem.FileSystemEventListener) -> None:
        """
        Removes a previously added {@link FileSystemEventListener listener}.
        @param listener {@link FileSystemEventListener} to remove.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def lastUsedTimestamp(self) -> long: ...
