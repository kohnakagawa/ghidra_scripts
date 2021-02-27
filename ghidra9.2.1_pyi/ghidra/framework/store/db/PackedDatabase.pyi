import db
import db.buffers
import generic.jar
import ghidra.framework.store.db
import ghidra.util.task
import java.io
import java.lang


class PackedDatabase(db.Database):
    """
    PackedDatabase provides a packed form of Database
     which compresses a single version into a file.

     When opening a packed database, a PackedDBHandle is returned
     after first expanding the file into a temporary Database.
    """

    READ_ONLY_DIRECTORY_LOCK_FILE: unicode = u'.dbDirLock'







    @staticmethod
    def cleanupOldTempDatabases() -> None:
        """
        Attempt to remove all old temporary databases.
         Those still open by an existing process should
         not be removed by the operating system.
        """
        ...

    @overload
    def delete(self) -> None:
        """
        Deletes the storage file associated with this packed database.
         This method should not be called while the database is open, if
         it is an attempt will be made to close the handle.
        @throws IOException
        """
        ...

    @overload
    @staticmethod
    def delete(packedDbFile: java.io.File) -> None:
        """
        Deletes the storage file associated with this packed database.
        @throws IOException
        """
        ...

    def dispose(self) -> None:
        """
        Free resources consumed by this object.
         If there is an associated database handle it will be closed.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getContentType(self) -> unicode:
        """
        Returns the user defined content type associated with this database.
        """
        ...

    def getCurrentVersion(self) -> int:
        """
        Returns the version number associated with the latest buffer file version.
        """
        ...

    @overload
    @staticmethod
    def getPackedDatabase(packedDbFile: java.io.File, monitor: ghidra.util.task.TaskMonitor) -> ghidra.framework.store.db.PackedDatabase:
        """
        Get a packed database which whose unpacking will be cached if possible
        @param packedDbFile
        @param monitor
        @return packed database which corresponds to the specified packedDbFile
        @throws IOException
        @throws CancelledException
        """
        ...

    @overload
    @staticmethod
    def getPackedDatabase(packedDbFile: generic.jar.ResourceFile, neverCache: bool, monitor: ghidra.util.task.TaskMonitor) -> ghidra.framework.store.db.PackedDatabase:
        """
        Get a packed database whose unpacking may be cached if possible
         provided doNotCache is false.
        @param packedDbFile
        @param neverCache if true unpacking will never be cache.
        @param monitor
        @return packed database which corresponds to the specified packedDbFile
        @throws IOException
        @throws CancelledException
        """
        ...

    @overload
    @staticmethod
    def getPackedDatabase(packedDbFile: java.io.File, neverCache: bool, monitor: ghidra.util.task.TaskMonitor) -> ghidra.framework.store.db.PackedDatabase:
        """
        Get a packed database whose unpacking may be cached if possible
         provided doNotCache is false.
        @param packedDbFile
        @param neverCache if true unpacking will never be cache.
        @param monitor
        @return packed database which corresponds to the specified packedDbFile
        @throws IOException
        @throws CancelledException
        """
        ...

    def getPackedFile(self) -> generic.jar.ResourceFile:
        """
        Returns the storage file associated with this packed database.
        """
        ...

    def hashCode(self) -> int: ...

    def isReadOnly(self) -> bool: ...

    @staticmethod
    def isReadOnlyPDBDirectory(directory: generic.jar.ResourceFile) -> bool:
        """
        Check for the presence of directory read-only lock
        @param directory
        @return true if read-only lock exists+
        """
        ...

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

    def open(self, monitor: ghidra.util.task.TaskMonitor) -> db.DBHandle: ...

    def openForUpdate(self, monitor: ghidra.util.task.TaskMonitor) -> db.DBHandle: ...

    @staticmethod
    def packDatabase(dbh: db.DBHandle, itemName: unicode, contentType: unicode, outputFile: java.io.File, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Serialize (i.e., pack) an open database into the specified outputFile.
        @param dbh open database handle
        @param itemName item name to associate with packed content
        @param contentType supported content type
        @param outputFile packed output file to be created
        @param monitor progress monitor
        @throws IOException
        @throws CancelledException if monitor cancels operation
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

    @staticmethod
    def unpackDatabase(bfMgr: db.buffers.BufferFileManager, checkinId: long, packedFile: java.io.File, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Create a new Database with data provided by an ItemDeserializer.
        @param bfMgr the buffer manager for the database
        @param checkinId the check-in id
        @param packedFile the file to unpack
        @param monitor the task monitor
        @throws CancelledException
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def contentType(self) -> unicode: ...

    @property
    def packedFile(self) -> generic.jar.ResourceFile: ...

    @property
    def readOnly(self) -> bool: ...
