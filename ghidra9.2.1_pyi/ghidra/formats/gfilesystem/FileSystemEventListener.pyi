import ghidra.formats.gfilesystem
import java.lang


class FileSystemEventListener(object):
    """
    Events broadcast when a GFileSystem is closed or has a FileSystemRef change.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def onFilesystemClose(self, fs: ghidra.formats.gfilesystem.GFileSystem) -> None:
        """
        Called by GFilesystem's {@link GFileSystem#close()}, before any destructive changes
         are made to the filesystem instance.
        @param fs {@link GFileSystem} that is about to be closed.
        """
        ...

    def onFilesystemRefChange(self, fs: ghidra.formats.gfilesystem.GFileSystem, refManager: ghidra.formats.gfilesystem.FileSystemRefManager) -> None:
        """
        Called by {@link FileSystemRefManager} when a new {@link FileSystemRef} is created or
         released.
        @param fs {@link GFileSystem} that is being updated.
        @param refManager {@link FileSystemRefManager} that is tracking the modified GFileSystem.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
