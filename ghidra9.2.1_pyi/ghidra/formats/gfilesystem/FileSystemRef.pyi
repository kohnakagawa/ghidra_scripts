import ghidra.formats.gfilesystem
import java.io
import java.lang


class FileSystemRef(object, java.io.Closeable):
    """
    A handle to a GFileSystem which allows tracking the current users of the filesystem.

     Instances must be #close() when not needed anymore, and should not be
     shared across threads.
    """









    def close(self) -> None:
        """
        Closes this reference, releasing it from the {@link FileSystemRefManager}.
        """
        ...

    def dup(self) -> ghidra.formats.gfilesystem.FileSystemRef:
        """
        Creates a duplicate ref.
        @return a new duplicate {@link FileSystemRef}
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def finalize(self) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getFilesystem(self) -> ghidra.formats.gfilesystem.GFileSystem:
        """
        {@link GFileSystem} this ref points to.
        @return {@link GFileSystem} this ref points to.
        """
        ...

    def hashCode(self) -> int: ...

    def isClosed(self) -> bool:
        """
        Returns true if this ref was {@link #close() closed}.
         <p>
        @return boolean true if this ref was closed.
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
    def filesystem(self) -> ghidra.formats.gfilesystem.GFileSystem: ...
