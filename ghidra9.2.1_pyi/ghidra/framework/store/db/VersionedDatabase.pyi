import db
import db.buffers
import ghidra.framework.store.db
import ghidra.util.task
import java.io
import java.lang


class VersionedDatabase(db.Database):
    """
    VersionedDatabase corresponds to a versioned database.
    """

    DEFAULT_CHECKOUT_ID: long = -0x1L
    LATEST_VERSION: int



    @overload
    def __init__(self, dbDir: java.io.File, verDBListener: ghidra.framework.store.db.VersionedDBListener):
        """
        Constructor for an existing "Versioned" Database.
        @param dbDir database directory
        @param verDBListener
        @throws IOException
        """
        ...

    @overload
    def __init__(self, dbDir: java.io.File, srcFile: db.buffers.BufferFile, verDBListener: ghidra.framework.store.db.VersionedDBListener, checkoutId: long, comment: unicode, monitor: ghidra.util.task.TaskMonitor):
        """
        Construct a new "Versioned" Database from an existing srcFile.
        @param dbDir
        @param srcFile
        @param monitor
        @throws IOException
        @throws CancelledException
        """
        ...

    @overload
    def __init__(self, dbDir: java.io.File, packedFile: java.io.File, verDBListener: ghidra.framework.store.db.VersionedDBListener, checkoutId: long, comment: unicode, monitor: ghidra.util.task.TaskMonitor):
        """
        Construct a new "Versioned" Database from a packed database file
        @param dbDir
        @param packedFile
        @param verDBListener
        @param checkoutId
        @param comment
        @param monitor
        @throws IOException
        @throws CancelledException
        """
        ...



    @staticmethod
    def createVersionedDatabase(dbDir: java.io.File, bufferSize: int, verDBListener: ghidra.framework.store.db.VersionedDBListener, checkoutId: long) -> db.buffers.LocalManagedBufferFile:
        """
        Create a new database and provide the initial buffer file for writing.
        @param dbDir
        @param bufferSize
        @return initial buffer file
        @throws IOException
        """
        ...

    def dbMoved(self, dbDir: java.io.File) -> None:
        """
        Following a move of the database directory,
         this method should be invoked if this instance will
         continue to be used.
        @param dbDir new database directory
        """
        ...

    def deleteCurrentVersion(self) -> None:
        """
        Delete latest version.
        @throws IOException if an error occurs or this is the only version.
        """
        ...

    def deleteMinimumVersion(self) -> None:
        """
        Delete oldest version.
        @throws IOException if an error occurs or this is the only version.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCurrentVersion(self) -> int:
        """
        Returns the version number associated with the latest buffer file version.
        """
        ...

    def getMinimumVersion(self) -> int:
        """
        Returns the version number associated with the oldest buffer file version.
        """
        ...

    def hashCode(self) -> int: ...

    def lastModified(self) -> long:
        """
        Returns the time at which this database was last saved.
        """
        ...

    def length(self) -> long:
        """
        Returns the length of this domain file.  This size is the minimum disk space
         used for storing this file, but does not account for additional storage space
         used to tracks changes, etc.
        @return file length
        @throws IOException thrown if IO or access error occurs
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def open(self, monitor: ghidra.util.task.TaskMonitor) -> db.DBHandle:
        """
        Open the stored database for non-update use.
         The returned handle does not support the Save operation.
        @param monitor task monitor (may be null)
        @return database handle
        @throws FileInUseException thrown if unable to obtain the required database lock(s).
        @throws IOException thrown if IO error occurs.
        @throws CancelledException if cancelled by monitor
        """
        ...

    @overload
    def open(self, version: int, minChangeDataVer: int, monitor: ghidra.util.task.TaskMonitor) -> db.DBHandle:
        """
        Open a specific version of the stored database for non-update use.
         The returned handle does not support the Save operation.
        @param version database version
        @param monitor task monitor (may be null)
        @return database handle
        @throws FileInUseException thrown if unable to obtain the required database lock(s).
        @throws IOException thrown if IO error occurs.
        """
        ...

    def openBufferFile(self, version: int, minChangeDataVer: int) -> db.buffers.LocalManagedBufferFile:
        """
        Open a specific version of this database for non-update use.
        @param version database version or LATEST_VERSION for current version
        @param minChangeDataVer the minimum database version whoose change data
         should be associated with the returned buffer file.  A value of -1 indicates that
         change data is not required.
        @return buffer file for non-update use.
        @throws IOException
        """
        ...

    def openBufferFileForUpdate(self, checkoutId: long) -> db.buffers.LocalManagedBufferFile:
        """
        Open the current version of this database for update use.
        @param checkoutId checkout ID
        @return updateable buffer file
        @throws IOException if update not permitted or other error occurs
        """
        ...

    def openForUpdate(self, monitor: ghidra.util.task.TaskMonitor) -> db.DBHandle: ...

    def output(self, version: int, outputFile: java.io.File, name: unicode, filetype: int, contentType: unicode, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Output the current version of this database to a packed storage file.
        @param outputFile packed storage file to be written
        @param name database name
        @param filetype application file type
        @param contentType user content type
        @param monitor
        @throws IOException
        @throws CancelledException
        """
        ...

    def refresh(self) -> None:
        """
        Scan files and update state.
        """
        ...

    def setSynchronizationObject(self, syncObject: object) -> None:
        """
        Set the object to be used for synchronization.
        @param syncObject
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
    def currentVersion(self) -> int: ...

    @property
    def minimumVersion(self) -> int: ...
