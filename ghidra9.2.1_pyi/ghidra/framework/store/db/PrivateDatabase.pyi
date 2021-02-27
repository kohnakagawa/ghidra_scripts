import db
import db.buffers
import ghidra.framework.store.db
import ghidra.util.task
import java.io
import java.lang


class PrivateDatabase(db.Database):
    """
    PrivateDatabase corresponds to a non-versioned database.
    """





    @overload
    def __init__(self, dbDir: java.io.File):
        """
        Constructor for an existing "Non-Versioned" Database.
        @param dbDir database directory
        @throws IOException
        """
        ...

    @overload
    def __init__(self, dbDir: java.io.File, packedFile: java.io.File, monitor: ghidra.util.task.TaskMonitor):
        """
        Constructs a new Database from an existing packed database file.
        @param dbDir private database directory
        @param packedFile packed database storage file
        @param monitor
        @throws IOException
        @throws CancelledException
        """
        ...

    @overload
    def __init__(self, dbDir: java.io.File, srcFile: db.buffers.BufferFile, resetDatabaseId: bool, monitor: ghidra.util.task.TaskMonitor):
        """
        Construct a new Database from an existing srcFile.
        @param dbDir
        @param srcFile
        @param resetDatabaseId if true database ID will be reset for new Database
        @param monitor
        @throws IOException
        @throws CancelledException
        """
        ...



    def canRecover(self) -> bool:
        """
        Returns true if recovery data exists which may enable recovery of unsaved changes
         resulting from a previous crash.
        """
        ...

    @staticmethod
    def createDatabase(dbDir: java.io.File, dbFileListener: db.DBFileListener, bufferSize: int) -> db.buffers.LocalManagedBufferFile:
        """
        Create a new database and provide the initial buffer file for writing.
        @param dbDir
        @param bufferSize
        @return initial buffer file
        @throws IOException
        """
        ...

    def dbMoved(self, dir: java.io.File) -> None:
        """
        Following a move of the database directory,
         this method should be invoked if this instance will
         continue to be used.
        @param dir new database directory
        @throws FileNotFoundException if the database directory cannot be found
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCurrentVersion(self) -> int:
        """
        Returns the version number associated with the latest buffer file version.
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

    def openBufferFile(self) -> db.buffers.LocalManagedBufferFile:
        """
        Open the current version of this database for non-update use.
        @return buffer file for non-update use
        @throws IOException
        """
        ...

    def openBufferFileForUpdate(self) -> db.buffers.LocalManagedBufferFile:
        """
        Open the current version of this database for update use.
        @return updateable buffer file
        @throws IOException if updating this database file is not allowed
        """
        ...

    def openForUpdate(self, monitor: ghidra.util.task.TaskMonitor) -> db.DBHandle:
        """
        Open the stored database for update use.
        @param monitor task monitor (may be null)
        @return buffer file
        @throws FileInUseException thrown if unable to obtain the required database lock(s).
        @throws IOException thrown if IO error occurs.
        @throws CancelledException if cancelled by monitor
        """
        ...

    def output(self, outputFile: java.io.File, name: unicode, filetype: int, contentType: unicode, monitor: ghidra.util.task.TaskMonitor) -> None:
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

    def setIsCheckoutCopy(self, state: bool) -> None:
        """
        If this is a checked-out copy and a cumulative change file
         should be maintained, this method must be invoked following
         construction.
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
    def updateCheckoutCopy(self) -> None:
        """
        If a cumulative change files exists, it will be deleted.
        @throws IOException
        """
        ...

    @overload
    def updateCheckoutCopy(self, srcFile: db.buffers.ManagedBufferFile, oldVersion: int, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        If this is a checked-out copy, replace the buffer file content with that
         provided by the specified srcFile.  This Database must be a checkout copy.
         If a cumulative change files exists, it will be deleted following the update.
        @param srcFile open source data buffer file or null if current version
         is already up-to-date.
        @param oldVersion older version of srcFile from which this database originated.
        @throws IOException
        @throws CancelledException
        """
        ...

    def updateCheckoutFrom(self, otherDb: ghidra.framework.store.db.PrivateDatabase) -> None:
        """
        Move the content of the otherDb into this database.
         The otherDb will no longer exist if this method is successful.
         If already open for update, a save should not be done or the database
         may become corrupted.  All existing handles should be closed and reopened
         when this method is complete.
        @param otherDb the other database.
        @throws IOException if an IO error occurs.  An attempt will be made to restore
         this database to its original state, however the otherDb will not be repaired
         and may become unusable.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def isCheckoutCopy(self) -> None: ...  # No getter available.

    @isCheckoutCopy.setter
    def isCheckoutCopy(self, value: bool) -> None: ...
