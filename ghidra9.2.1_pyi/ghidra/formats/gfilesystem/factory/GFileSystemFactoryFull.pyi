import ghidra.app.util.bin
import ghidra.formats.gfilesystem
import ghidra.formats.gfilesystem.factory
import ghidra.util.task
import java.io
import java.lang


class GFileSystemFactoryFull(ghidra.formats.gfilesystem.factory.GFileSystemFactory, object):
    """
    A GFileSystemFactory interface for filesystem implementations that need all available
     references to the source file, including a ByteProvider.

    """









    def create(self, containerFSRL: ghidra.formats.gfilesystem.FSRL, targetFSRL: ghidra.formats.gfilesystem.FSRLRoot, byteProvider: ghidra.app.util.bin.ByteProvider, containerFile: java.io.File, fsService: ghidra.formats.gfilesystem.FileSystemService, monitor: ghidra.util.task.TaskMonitor) -> FSTYPE:
        """
        Constructs a new {@link GFileSystem} instance that handles the specified file.
         <p>
        @param containerFSRL the {@link FSRL} of the file being opened.
        @param targetFSRL the {@link FSRLRoot} of the filesystem being created.
        @param byteProvider a {@link ByteProvider} containing the contents of the file being probed.
         This method is responsible for closing this byte provider instance.
        @param containerFile the {@link File} (probably in the filecache with non-useful filename)
         being opened.
        @param fsService a reference to the {@link FileSystemService} object
        @param monitor a {@link TaskMonitor} that should be polled to see if the user has
         requested to cancel the operation, and updated with progress information.
        @return a new {@link GFileSystem} derived instance.
        @throws IOException if there is an error reading files.
        @throws CancelledException if the user cancels
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
