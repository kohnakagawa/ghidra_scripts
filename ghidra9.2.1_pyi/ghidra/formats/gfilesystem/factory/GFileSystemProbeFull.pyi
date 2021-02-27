import ghidra.app.util.bin
import ghidra.formats.gfilesystem
import ghidra.formats.gfilesystem.factory
import ghidra.util.task
import java.io
import java.lang


class GFileSystemProbeFull(ghidra.formats.gfilesystem.factory.GFileSystemProbe, object):
    """
    A GFileSystemProbe interface for filesystems that need all available
     references to the source file, including a ByteProvider.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def probe(self, containerFSRL: ghidra.formats.gfilesystem.FSRL, byteProvider: ghidra.app.util.bin.ByteProvider, containerFile: java.io.File, fsService: ghidra.formats.gfilesystem.FileSystemService, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Probes the specified {@code containerFile} to determine if this filesystem implementation
         can handle the file.
        @param containerFSRL the {@link FSRL} of the file being probed
        @param byteProvider a {@link ByteProvider} containing the contents of the file being probed.
         Implementors of this method should <b>NOT</b> {@link ByteProvider#close() close()} this
         object.
        @param containerFile the {@link File} (probably in the filecache with non-useful filename)
         being probed.
        @param fsService a reference to the {@link FileSystemService} object
        @param monitor a {@link TaskMonitor} that should be polled to see if the user has
         requested to cancel the operation, and updated with progress information.
        @return {@code true} if the specified file is handled by this filesystem implementation,
         {@code false} if not.
        @throws IOException if there is an error reading files.
        @throws CancelledException if the user cancels
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
