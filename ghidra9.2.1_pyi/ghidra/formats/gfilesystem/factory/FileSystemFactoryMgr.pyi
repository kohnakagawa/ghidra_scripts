from typing import List
import ghidra.formats.gfilesystem
import ghidra.formats.gfilesystem.factory
import ghidra.util.task
import java.io
import java.lang


class FileSystemFactoryMgr(object):
    """
    Statically scoped mugger that handles the dirty work of probing for and creating
     GFileSystem instances.

     Auto-discovers all GFileSystem instances in the classpath that have a
     FileSystemInfo annotation.

    """









    def equals(self, __a0: object) -> bool: ...

    def getAllFilesystemNames(self) -> List[unicode]:
        """
        Returns a list of all registered filesystem implementation descriptions.
        @return list of strings
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFileSystemType(self, fsClass: java.lang.Class) -> unicode:
        """
        Returns the file system type of the specified {@link GFileSystem} class.
        @param fsClass Class to inspect
        @return String file system type, from the {@link FileSystemInfo#type()} annotation.
        """
        ...

    @staticmethod
    def getInstance() -> ghidra.formats.gfilesystem.factory.FileSystemFactoryMgr:
        """
        <p>
        @return The single global {@link FileSystemFactoryMgr} instance.
        """
        ...

    def hashCode(self) -> int: ...

    def mountFileSystem(self, fsType: unicode, containerFSRL: ghidra.formats.gfilesystem.FSRL, containerFile: java.io.File, fsService: ghidra.formats.gfilesystem.FileSystemService, monitor: ghidra.util.task.TaskMonitor) -> ghidra.formats.gfilesystem.GFileSystem:
        """
        Creates a new {@link GFileSystem} instance when the filesystem type is already
         known.
         <p>
        @param fsType filesystem type string, ie. "file", "zip".
        @param containerFSRL {@link FSRL} of the containing file.
        @param containerFile {@link File} the containing file.
        @param fsService reference to the {@link FileSystemService} instance.
        @param monitor {@link TaskMonitor} to use for canceling and updating progress.
        @return new {@link GFileSystem} instance.
        @throws IOException if error when opening the filesystem or unknown fsType.
        @throws CancelledException if the user canceled the operation.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def probe(self, containerFSRL: ghidra.formats.gfilesystem.FSRL, containerFile: java.io.File, fsService: ghidra.formats.gfilesystem.FileSystemService, conflictResolver: ghidra.formats.gfilesystem.FileSystemProbeConflictResolver, monitor: ghidra.util.task.TaskMonitor) -> ghidra.formats.gfilesystem.GFileSystem:
        """
        Probes the specified file for a supported {@link GFileSystem} implementation, and
         if found, creates a new filesystem instance.
         <p>
        @param containerFSRL {@link FSRL} of the containing file.
        @param containerFile {@link File} the containing file.
        @param fsService reference to the {@link FileSystemService} instance.
        @param conflictResolver {@link FileSystemProbeConflictResolver conflict resolver} to
         use when more than one {@link GFileSystem} implementation can handle the specified
         file.
        @param monitor {@link TaskMonitor} to use for canceling and updating progress.
        @return new {@link GFileSystem} instance or null not supported.
        @throws IOException if error accessing the containing file
        @throws CancelledException if the user cancels the operation
        """
        ...

    @overload
    def probe(self, containerFSRL: ghidra.formats.gfilesystem.FSRL, containerFile: java.io.File, fsService: ghidra.formats.gfilesystem.FileSystemService, conflictResolver: ghidra.formats.gfilesystem.FileSystemProbeConflictResolver, priorityFilter: int, monitor: ghidra.util.task.TaskMonitor) -> ghidra.formats.gfilesystem.GFileSystem:
        """
        Probes the specified file for a supported {@link GFileSystem} implementation, and
         if found, creates a new filesystem instance.
         <p>
        @param containerFSRL {@link FSRL} of the containing file.
        @param containerFile {@link File} the containing file.
        @param fsService reference to the {@link FileSystemService} instance.
        @param conflictResolver {@link FileSystemProbeConflictResolver conflict resolver} to
         use when more than one {@link GFileSystem} implementation can handle the specified
         file.
        @param priorityFilter limits the probe to filesystems that have a {@link FileSystemInfo#priority()}
         greater than or equal to this value.  Use {@link FileSystemInfo#PRIORITY_LOWEST} to
         include all filesystem implementations.
        @param monitor {@link TaskMonitor} to use for canceling and updating progress.
        @return new {@link GFileSystem} instance or null not supported.
        @throws IOException if error accessing the containing file
        @throws CancelledException if the user cancels the operation
        """
        ...

    def test(self, containerFSRL: ghidra.formats.gfilesystem.FSRL, containerFile: java.io.File, fsService: ghidra.formats.gfilesystem.FileSystemService, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Returns true if the specified file contains a supported {@link GFileSystem}.
         <p>
        @param containerFSRL {@link FSRL} of the containing file.
        @param containerFile {@link File} the containing file.
        @param fsService reference to the {@link FileSystemService} instance.
        @param monitor {@link TaskMonitor} to use for canceling and updating progress.
        @return {@code true} if the file seems to contain a filesystem, {@code false} if it does not.
        @throws IOException if error when accessing the containing file
        @throws CancelledException if the user canceled the operation
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
    def allFilesystemNames(self) -> List[object]: ...
