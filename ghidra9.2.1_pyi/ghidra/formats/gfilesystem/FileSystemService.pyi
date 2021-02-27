from typing import List
import ghidra.app.util.bin
import ghidra.formats.gfilesystem
import ghidra.util.task
import java.io
import java.lang


class FileSystemService(object):
    """
    Provides methods for dealing with GFilesystem files and GFileSystem.

     Most methods take FSRL references to files as a way to decouple dependencies and
     reduce forced filesystem instantiation.

     (ie. a GFile instance is only valid if its GFileSystem is open, which
     means that its parent probably also has to be open, recursively, etc, whereas a FSRL
     is always valid and does not force the instantiation of parent objects)

     GFileSystem should be used via FileSystemRef
     handles that ensure the filesystem is pinned in memory and won't be closed while
     you are using it.

     If you are working with GFile instances, you should have a
     FileSystemRef that you are using to pin the filesystem.

     Thread-safe.



    """





    @overload
    def __init__(self):
        """
        Creates a FilesystemService instance, using the {@link Application}'s default value
         for {@link Application#getUserCacheDirectory() user cache directory} as the
         cache directory.
        """
        ...

    @overload
    def __init__(self, fscacheDir: java.io.File):
        """
        Creates a FilesystemService instance, using the supplied directory as its file caching
         root directory.
        @param fscacheDir {@link File Root dir} to use to store files placed into cache.
        """
        ...



    def addFileToCache(self, file: ghidra.formats.gfilesystem.GFile, is_: java.io.InputStream, monitor: ghidra.util.task.TaskMonitor) -> ghidra.formats.gfilesystem.FileCacheEntry:
        """
        Adds a {@link GFile file}'s stream's contents to the file cache, returning its MD5 hash.
        @param file {@link GFile} not really used currently
        @param is {@link InputStream} to add to the cache.
        @param monitor {@link TaskMonitor} to monitor and update.
        @return string with new file's md5.
        @throws IOException if IO error
        @throws CancelledException if user canceled.
        """
        ...

    def addStreamToCache(self, is_: java.io.InputStream, monitor: ghidra.util.task.TaskMonitor) -> ghidra.formats.gfilesystem.FileCacheEntry:
        """
        Stores a stream in the file cache.
         <p>
        @param is {@link InputStream} to store in the cache.
        @param monitor {@link TaskMonitor} to watch and update.
        @return {@link File} location of the new file.
        @throws IOException if IO error
        @throws CancelledException if the user cancels.
        """
        ...

    def clear(self) -> None:
        """
        Forcefully closes all open filesystems and clears caches.
        """
        ...

    def closeUnusedFileSystems(self) -> None:
        """
        Close unused filesystems.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAllFilesystemNames(self) -> List[unicode]:
        """
        Returns a list of all detected GFilesystem filesystem names.
         <p>
         See {@link FileSystemFactoryMgr#getAllFilesystemNames()}.
        @return {@link List} of strings.
        """
        ...

    def getByteProvider(self, fsrl: ghidra.formats.gfilesystem.FSRL, monitor: ghidra.util.task.TaskMonitor) -> ghidra.app.util.bin.ByteProvider:
        """
        Returns a {@link ByteProvider} with the contents of the requested {@link GFile file}
         (in the Global file cache directory).
         <p>
         Never returns null, throws IOException if there was a problem.
         <p>
         Caller is responsible for {@link ByteProvider#close() closing()} the ByteProvider
         when finished.
        @param fsrl {@link FSRL} file to wrap
        @param monitor {@link TaskMonitor} to watch and update.
        @return new {@link ByteProvider}
        @throws CancelledException if user cancels
        @throws IOException if IO problem.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDerivedFile(self, fsrl: ghidra.formats.gfilesystem.FSRL, derivedName: unicode, producer: ghidra.formats.gfilesystem.DerivedFileProducer, monitor: ghidra.util.task.TaskMonitor) -> ghidra.formats.gfilesystem.FileCacheEntry:
        """
        Returns a reference to a file in the FileCache that contains the
         derived (ie. decompressed or decrypted) contents of a source file, as well as
         its md5.
         <p>
         If the file was not present in the cache, the {@link DerivedFileProducer producer}
         lambda will be called and it will be responsible for returning an {@link InputStream}
         which has the derived contents, which will be added to the file cache for next time.
         <p>
        @param fsrl {@link FSRL} of the source (or container) file that this derived file is based on
        @param derivedName a unique string identifying the derived file inside the source (or container) file
        @param producer a {@link DerivedFileProducer callback or lambda} that returns an
         {@link InputStream} that will be streamed into a file and placed into the file cache.
         Example:{@code (file) -> { return new XYZDecryptorInputStream(file); }}
        @param monitor {@link TaskMonitor} that will be monitor for cancel requests and updated
         with file io progress
        @return {@link FileCacheEntry} with file and md5 fields
        @throws CancelledException if the user cancels
        @throws IOException if there was an io error
        """
        ...

    def getDerivedFilePush(self, fsrl: ghidra.formats.gfilesystem.FSRL, derivedName: unicode, pusher: ghidra.formats.gfilesystem.DerivedFilePushProducer, monitor: ghidra.util.task.TaskMonitor) -> ghidra.formats.gfilesystem.FileCacheEntry:
        """
        Returns a reference to a file in the FileCache that contains the
         derived (ie. decompressed or decrypted) contents of a source file, as well as
         its md5.
         <p>
         If the file was not present in the cache, the {@link DerivedFilePushProducer push producer}
         lambda will be called and it will be responsible for producing and writing the derived
         file's bytes to a {@link OutputStream}, which will be added to the file cache for next time.
         <p>
        @param fsrl {@link FSRL} of the source (or container) file that this derived file is based on
        @param derivedName a unique string identifying the derived file inside the source (or container) file
        @param pusher a {@link DerivedFilePushProducer callback or lambda} that recieves a {@link OutputStream}.
         Example:{@code (os) -> { ...write to outputstream os here...; }}
        @param monitor {@link TaskMonitor} that will be monitor for cancel requests and updated
         with file io progress
        @return {@link FileCacheEntry} with file and md5 fields
        @throws CancelledException if the user cancels
        @throws IOException if there was an io error
        """
        ...

    def getFile(self, fsrl: ghidra.formats.gfilesystem.FSRL, monitor: ghidra.util.task.TaskMonitor) -> java.io.File:
        """
        Returns a {@link File java.io.file} with the data from the requested FSRL.
         Simple local files will be returned directly, and files nested in containers
         will be located in the file cache directory and have a 'random' name.
         <p>
         Never returns nulls, throws IOException if not found or error.
        @param fsrl {@link FSRL} of the desired file.
        @param monitor {@link TaskMonitor} to watch and update.
        @return {@link File} of the desired file in the cache, never null.
        @throws CancelledException if user cancels.
        @throws IOException if IO problem.
        """
        ...

    def getFileHash(self, gfile: ghidra.formats.gfilesystem.GFile, monitor: ghidra.util.task.TaskMonitor) -> unicode: ...

    def getFilesystem(self, fsFSRL: ghidra.formats.gfilesystem.FSRLRoot, monitor: ghidra.util.task.TaskMonitor) -> ghidra.formats.gfilesystem.FileSystemRef:
        """
        Returns a filesystem instance for the requested {@link FSRLRoot}, either from an already
         loaded instance in the global fscache, or by instantiating the requested filesystem
         from its container file (in a possibly recursive manner, depending on the depth
         of the FSLR)
         <p>
         Never returns NULL, instead throws IOException if there is a problem.
         <p>
         The caller is responsible for releasing the {@link FileSystemRef}.
         <p>
        @param fsFSRL {@link FSRLRoot} of file system you want a reference to.
        @param monitor {@link TaskMonitor} to allow the user to cancel.
        @return a new {@link FileSystemRef} that the caller is responsible for closing when
         no longer needed, never {@code null}.
        @throws IOException if there was an io problem.
        @throws CancelledException if the user cancels.
        """
        ...

    def getFullyQualifiedFSRL(self, fsrl: ghidra.formats.gfilesystem.FSRL, monitor: ghidra.util.task.TaskMonitor) -> ghidra.formats.gfilesystem.FSRL:
        """
        Returns a cloned copy of the {@code FSRL} that should have MD5 values specified.
         (excluding GFile objects that don't have data streams)
         <p>
         Also implements a best-effort caching of non-root filesystem FSRL's MD5 values.
         (ie. the md5 values of files inside of containers are cached.  The md5 value of
         files on the real OS filesystem are not cached)
         <p>
        @param fsrl {@link FSRL} of the file that should be forced to have a MD5
        @param monitor {@link TaskMonitor} to watch and update with progress.
        @return possibly new {@link FSRL} instance with a MD5 value.
        @throws CancelledException if user cancels.
        @throws IOException if IO problem.
        """
        ...

    @staticmethod
    def getInstance() -> ghidra.formats.gfilesystem.FileSystemService: ...

    def getLocalFS(self) -> ghidra.formats.gfilesystem.GFileSystem:
        """
        Returns a direct reference to a filesystem that represents the local filesystem.
        @return {@link GFileSystem} that represents the local filesystem.
        """
        ...

    def getLocalFSRL(self, f: java.io.File) -> ghidra.formats.gfilesystem.FSRL:
        """
        Builds a {@link FSRL} of a {@link File file} located on the local filesystem.
        @param f {@link File} on the local filesystem
        @return {@link FSRL} pointing to the same file, never null
        """
        ...

    def getLocalGFile(self, f: java.io.File) -> ghidra.formats.gfilesystem.GFile:
        """
        Converts a java {@link File} instance into a GFilesystem {@link GFile} hosted on the
         {@link #getLocalFS() local filesystem}.
         <p>
        @param f {@link File} on the local filesystem
        @return {@link GFile} representing the same file or {@code null} if there was a problem
         with the file path.
        """
        ...

    def getMountedFilesystem(self, fsFSRL: ghidra.formats.gfilesystem.FSRLRoot) -> ghidra.formats.gfilesystem.FileSystemRef:
        """
        Returns a new FilesystemRef handle to an already mounted filesystem.
         <p>
         The caller is responsible for releasing the ref.
         <p>
         Returns null if there is no filesystem mounted at {@code fsFSRL}.
        @param fsFSRL {@link FSRLRoot} of file system to get a {@link FileSystemRef} to.
        @return new {@link FileSystemRef} or null if requested file system not mounted.
        """
        ...

    def getMountedFilesystems(self) -> List[ghidra.formats.gfilesystem.FSRLRoot]:
        """
        Returns a list of all currently mounted filesystems.
         <p>
         As a FSRL is returned, there is no guarantee that the filesystem will still be
         mounted when you later use values from the list.
         <p>
        @return {@link List} of {@link FSRLRoot} of currently mounted filesystems.
        """
        ...

    def getRefdFile(self, fsrl: ghidra.formats.gfilesystem.FSRL, monitor: ghidra.util.task.TaskMonitor) -> ghidra.formats.gfilesystem.RefdFile:
        """
        Returns the {@link GFile} pointed to by the FSRL, along with a {@link FileSystemRef}
         that the caller is responsible for releasing (either explicitly via
         {@code result.fsRef.close()} or via the {@link RefdFile#close()}).
        @param fsrl {@link FSRL} of the desired file
        @param monitor {@link TaskMonitor} so the user can cancel
        @return a {@link RefdFile} which contains the resultant {@link GFile} and a
         {@link FileSystemRef} that needs to be closed, or {@code null} if the filesystem
         does not have the requested file.
        @throws CancelledException if the user cancels
        @throws IOException if there was a file io problem
        """
        ...

    def hasDerivedFile(self, fsrl: ghidra.formats.gfilesystem.FSRL, derivedName: unicode, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Returns true if the specified derived file exists in the file cache.
        @param fsrl {@link FSRL} of the container
        @param derivedName name of the derived file inside of the container
        @param monitor {@link TaskMonitor}
        @return boolean true if file exists at time of query, false if file is not in cache
        @throws CancelledException if user cancels
        @throws IOException if other IO error
        """
        ...

    def hashCode(self) -> int: ...

    def isFileFilesystemContainer(self, containerFSRL: ghidra.formats.gfilesystem.FSRL, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Returns true if the container file probably holds one of the currently supported
         filesystem types.
         <p>
        @param containerFSRL {@link FSRL} of the file being queried.
        @param monitor {@link TaskMonitor} to watch and update progress.
        @return boolean true if the file probably is a container, false otherwise.
        @throws CancelledException if user cancels.
        @throws IOException if IO problem.
        """
        ...

    def isFilesystemMountedAt(self, fsrl: ghidra.formats.gfilesystem.FSRL) -> bool:
        """
        Returns true of there is a {@link GFileSystem filesystem} mounted at the requested
         {@link FSRL} location.
        @param fsrl {@link FSRL} container to query for mounted filesystem
        @return boolean true if filesystem mounted at location.
        """
        ...

    @staticmethod
    def isInitialized() -> bool:
        """
        Returns true if this service has been loaded
        @return true if this service has been loaded
        """
        ...

    @overload
    def isLocal(self, fsrl: ghidra.formats.gfilesystem.FSRL) -> bool:
        """
        Returns true if the specified location is a path on the local computer's
         filesystem.
        @param fsrl {@link FSRL} path to query
        @return true if local, false if the path points to an embedded file in a container.
        """
        ...

    @overload
    def isLocal(self, gfile: ghidra.formats.gfilesystem.GFile) -> bool:
        """
        Returns true if the specified file is on the local computer's
         filesystem.
        @param gfile file to query
        @return true if local, false if the path points to an embedded file in a container.
        """
        ...

    def mountSpecificFileSystem(self, containerFSRL: ghidra.formats.gfilesystem.FSRL, fsClass: java.lang.Class, monitor: ghidra.util.task.TaskMonitor) -> FSTYPE:
        """
        Mount a specific file system (by class) using a specified container file.
         <p>
         The newly constructed / mounted file system is not managed by this FileSystemService
         or controlled with {@link FileSystemRef}s.
         <p>
         The caller is responsible for closing the resultant file system instance when it is
         no longer needed.
         <p>
        @param containerFSRL a reference to the file that contains the file system image
        @param fsClass the GFileSystem derived class that implements the specific file system
        @param monitor {@link TaskMonitor} to allow the user to cancel
        @return new {@link GFileSystem} instance, caller is responsible for closing() when done.
        @throws CancelledException if user cancels
        @throws IOException if file io error or wrong file system type.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def openFileSystemContainer(self, containerFSRL: ghidra.formats.gfilesystem.FSRL, monitor: ghidra.util.task.TaskMonitor) -> ghidra.formats.gfilesystem.GFileSystem:
        """
        Open the file system contained at the specified location.
         <p>
         The newly constructed / mounted file system is not managed by this FileSystemService
         or controlled with {@link FileSystemRef}s.
         <p>
         The caller is responsible for closing the resultant file system instance when it is
         no longer needed.
         <p>
        @param containerFSRL a reference to the file that contains the file system image
        @param monitor {@link TaskMonitor} to allow the user to cancel
        @return new {@link GFileSystem} instance, caller is responsible for closing() when done.
        @throws CancelledException if user cancels
        @throws IOException if file io error or wrong file system type.
        """
        ...

    @overload
    def probeFileForFilesystem(self, containerFSRL: ghidra.formats.gfilesystem.FSRL, monitor: ghidra.util.task.TaskMonitor, conflictResolver: ghidra.formats.gfilesystem.FileSystemProbeConflictResolver) -> ghidra.formats.gfilesystem.FileSystemRef:
        """
        Auto-detects a filesystem in the container file pointed to by the FSRL.
         <p>
         Returns a filesystem instance for the requested container file, either from an already
         loaded instance in the Global fs cache, or by probing for a filesystem in the container
         file using the {@link FileSystemFactoryMgr}.
         <p>
         Returns null if no filesystem implementation was found that could handle the container
         file.
        @param containerFSRL {@link FSRL} of the file container
        @param monitor {@link TaskMonitor} to watch and update progress.
        @param conflictResolver {@link FileSystemProbeConflictResolver} to handle choosing
         the correct file system type among multiple results, or null if you want
         {@link FileSystemProbeConflictResolver#CHOOSEFIRST} .
        @return new {@link FileSystemRef} or null
        @throws CancelledException if user cancels.
        @throws IOException if IO problem.
        """
        ...

    @overload
    def probeFileForFilesystem(self, containerFSRL: ghidra.formats.gfilesystem.FSRL, monitor: ghidra.util.task.TaskMonitor, conflictResolver: ghidra.formats.gfilesystem.FileSystemProbeConflictResolver, priorityFilter: int) -> ghidra.formats.gfilesystem.FileSystemRef:
        """
        Auto-detects a filesystem in the container file pointed to by the FSRL.
         <p>
         Returns a filesystem instance for the requested container file, either from an already
         loaded instance in the Global fs cache, or by probing for a filesystem in the container
         file using a {@link FileSystemFactoryMgr}.
         <p>
         Returns null if no filesystem implementation was found that could handle the container
         file.
        @param containerFSRL {@link FSRL} of the file container
        @param monitor {@link TaskMonitor} to watch and update progress.
        @param conflictResolver {@link FileSystemProbeConflictResolver} to handle choosing
         the correct file system type among multiple results, or null if you want
         {@link FileSystemProbeConflictResolver#CHOOSEFIRST} .
        @param priorityFilter minimum filesystem {@link FileSystemInfo#priority()} to allow
         when using file system factories to probe the container.
        @return new {@link FileSystemRef} or null
        @throws CancelledException if user cancels.
        @throws IOException if IO problem.
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

    @property
    def localFS(self) -> ghidra.formats.gfilesystem.GFileSystem: ...

    @property
    def mountedFilesystems(self) -> List[object]: ...
