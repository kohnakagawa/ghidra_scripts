import ghidra.formats.gfilesystem
import ghidra.util.task
import java.io
import java.lang


class FileCache(object):
    """
    File caching implementation.

     Caches files based on a hash of the contents of the file.
     Files are retrieved using the hash string.
     Cached files are stored in a file with a name that is the hex encoded value of the hash.
     Cached files are organized into a nested directory structure to prevent
     overwhelming a single directory with thousands of files.

     Nested directory structure is based on the file's name:
       File: AABBCCDDEEFF...
       Directory (2 level nesting): AA/BB/AABBCCDDEEFF...

     Cache size is not bounded.

     Cache maint is done during startup if interval since last maint has been exceeded

     No file data is maintained in memory.

     No file is moved or removed from the cache after being added (except during startup)
     as there is no use count or reference tracking of the files.
    """

    MD5_HEXSTR_LEN: int = 32



    def __init__(self, cacheDir: java.io.File):
        """
        Creates a new {@link FileCache} instance where files are stored under the specified
         {@code cacheDir}
         <p>
        @param cacheDir where to store the files
        @throws IOException if there was a problem creating subdirectories under cacheDir or
         when pruning expired files.
        """
        ...



    def addFile(self, f: java.io.File, monitor: ghidra.util.task.TaskMonitor) -> ghidra.formats.gfilesystem.FileCacheEntry:
        """
        Adds a {@link File} to the cache, returning a {@link FileCacheEntry}.
        @param f {@link File} to add to cache.
        @param monitor {@link TaskMonitor} to monitor for cancel and to update progress.
        @return {@link FileCacheEntry} with new File and md5.
        @throws IOException if error
        @throws CancelledException if canceled
        """
        ...

    def addStream(self, is_: java.io.InputStream, monitor: ghidra.util.task.TaskMonitor) -> ghidra.formats.gfilesystem.FileCacheEntry:
        """
        Adds a contents of a stream to the cache, returning the md5 identifier of the stream.
         <p>
         The stream is copied into a temp file in the cacheDir/new directory while its md5
         is calculated.  The temp file is then moved into its final location
         based on the md5 of the stream: AA/BB/AABBCCDDEEFF....
         <p>
         The monitor progress is updated with the number of bytes that are being copied.  No
         message or maximum is set.
         <p>
        @param is {@link InputStream} to add to the cache.  Not closed when done.
        @param monitor {@link TaskMonitor} that will be checked for canceling and updating progress.
        @return {@link FileCacheEntry} with file info and md5, never null.
        @throws IOException if error
        @throws CancelledException if canceled
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFile(self, md5: unicode) -> ghidra.formats.gfilesystem.FileCacheEntry:
        """
        Returns a {@link FileCacheEntry} for the matching file, based on its MD5, or
         NULL if there is no matching file.
         <p>
         Tweaks the file's last modified time to implement a LRU.
        @param md5 md5 string.
        @return {@link FileCacheEntry} with a File and it's md5 string or {@code null} if no
         matching file exists in cache.
        """
        ...

    def getFileAddCount(self) -> int:
        """
        Number of files added to this cache.
        @return Number of files added to this cache
        """
        ...

    def getFileReUseCount(self) -> int:
        """
        Number of times a file-add was a no-op and the contents were already present
         in the cache.
        @return Number of times a file-add was a no-op and the contents were already present
         in the cache.
        """
        ...

    def getMaxFileAgeMS(self) -> long:
        """
        How old (in milliseconds) files must be before being aged-off during cache maintenance.
        @return Max cache file age in milliseconds.
        """
        ...

    def getStorageEstimateBytes(self) -> long:
        """
        Estimate of the number of bytes in the cache.
        @return estimate of the number of bytes in the cache - could be very wrong
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def purge(self) -> None:
        """
        Deletes all stored files from this file cache that are under a "NN" two hex digit
         nesting dir.
         <p>
         Will cause other processes which are accessing or updating the cache to error.
        """
        ...

    def pushStream(self, pusher: ghidra.formats.gfilesystem.DerivedFilePushProducer, monitor: ghidra.util.task.TaskMonitor) -> ghidra.formats.gfilesystem.FileCacheEntry:
        """
        Adds a file to the cache, using a 'pusher' strategy where the producer is given a
         {@link OutputStream} to write to.
         <p>
         Unbeknownst to the producer, but knownst to us, the outputstream is really a
         {@link HashingOutputStream} that will allow us to get the MD5 hash when the producer
         is finished pushing.
        @param pusher functional callback that will accept an {@link OutputStream} and write
         to it.
         <pre> (os) -&gt; { os.write(.....); }</pre>
        @param monitor {@link TaskMonitor} that will be checked for cancel and updated with
         file io progress.
        @return a new {@link FileCacheEntry} with the newly added cache file's File and MD5,
         never null.
        @throws IOException if an IO error
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

    @property
    def fileAddCount(self) -> int: ...

    @property
    def fileReUseCount(self) -> int: ...

    @property
    def maxFileAgeMS(self) -> long: ...

    @property
    def storageEstimateBytes(self) -> long: ...
