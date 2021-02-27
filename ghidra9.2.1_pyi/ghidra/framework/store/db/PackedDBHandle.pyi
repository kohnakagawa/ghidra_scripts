from typing import List
import db
import db.buffers
import ghidra.framework.store.db
import ghidra.util.task
import java.io
import java.lang


class PackedDBHandle(db.DBHandle):
    """
    DBHandle provides access to a PackedDatabase.
    """





    def __init__(self, contentType: unicode):
        """
        Constructs a temporary packed database handle.
        @param contentType user defined content type.
        @throws IOException
        """
        ...



    def addListener(self, listener: db.DBListener) -> None:
        """
        Add Database listener
        @param listener database listener
        """
        ...

    def canRedo(self) -> bool:
        """
        Determine if there are any changes which can be redone
        @return true if a redo can be performed.
        """
        ...

    def canUndo(self) -> bool:
        """
        Determine if there are any changes which can be undone.
        @return true if an undo can be performed.
        """
        ...

    def canUpdate(self) -> bool:
        """
        Determine if this database can be updated.
        @return true if this database handle is intended for update
        """
        ...

    def checkTransaction(self) -> None:
        """
        Verify that a valid transaction has been started.
        @throws NoTransactionException if transaction has not been started
        @throws TerminatedTransactionException transaction was prematurely terminated
        """
        ...

    @overload
    def close(self) -> None: ...

    @overload
    def close(self, keepRecoveryData: bool) -> None:
        """
        Close the database and dispose of the underlying buffer manager.
        @param keepRecoveryData true if existing recovery data should be retained or false to remove
         any recovery data
        """
        ...

    def closeScratchPad(self) -> None:
        """
        Close the scratch-pad database handle if it open.
        """
        ...

    @overload
    def createBuffer(self, length: int) -> db.DBBuffer:
        """
        Create a new buffer with the specified length.
         This method may only be invoked while a database transaction
         is in progress. A database transaction must also be in progress
         when invoking the various put, delete and setSize methods on the returned buffer.
        @param length the size of the buffer to create
        @return Buffer the newly created buffer
        @throws IOException if an I/O error occurs while creating the buffer.
        """
        ...

    @overload
    def createBuffer(self, shadowBuffer: db.DBBuffer) -> db.DBBuffer:
        """
        Create a new buffer that layers on top of another buffer.  This buffer
         will return values from the shadowBuffer unless they have been changed in this buffer.
         This method may only be invoked while a database transaction
         is in progress. A database transaction must also be in progress
         when invoking the various put, delete and setSize methods on the returned buffer.
        @param shadowBuffer the source of the byte values to use unless they have been changed.
        @return Buffer the newly created buffer
        @throws IOException if an I/O error occurs while creating the buffer.
        """
        ...

    @overload
    def createTable(self, name: unicode, schema: db.Schema) -> db.Table:
        """
        Creates a new non-indexed table with the given name, version and type.
        @param name name of new table
        @param schema table schema to be applied
        @return new table instance
        @throws IOException if IO error occurs
        """
        ...

    @overload
    def createTable(self, name: unicode, schema: db.Schema, indexedColumns: List[int]) -> db.Table:
        """
        Creates a new table with the given name, version and type.
         Create secondary indexes as specified by the array of column indexes.
        @param name name of new table
        @param schema table schema to be applied
        @param indexedColumns array of column indices which should have an index associated with them
        @return new table instance
        @throws IOException if IO error occurs
        """
        ...

    def deleteTable(self, name: unicode) -> None:
        """
        Delete the specified table from the database.
        @param name table name
        @throws IOException if there is an I/O error or the table does not exist
        """
        ...

    def enablePreCache(self) -> None:
        """
        Enable and start source file pre-cache if appropriate.
         WARNING! EXPERIMENTAL !!!
        """
        ...

    def endTransaction(self, id: long, commit: bool) -> bool:
        """
        Terminate transaction.  If commit is false, Table instances may be added
         or removed/invalidated.
        @param id transaction ID
        @param commit if true a new checkpoint will be established, if
         false all changes since the previous checkpoint will be discarded.
        @return true if new checkpoint established.
        @throws IOException if IO error occurs
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAvailableRedoCount(self) -> int:
        """
        @return the number of redo-able transactions
        """
        ...

    def getAvailableUndoCount(self) -> int:
        """
        @return number of undo-able transactions
        """
        ...

    @overload
    def getBuffer(self, id: int) -> db.DBBuffer:
        """
        Get an existing buffer.  This method should be used with care to avoid
         providing an improper id.  A database transaction must be in progress
         when invoking the various put, delete and setSize methods on the returned buffer.
        @param id the buffer id.
        @return Buffer the buffer associated with the given id.
        @throws IOException if an I/O error occurs while getting the buffer.
        """
        ...

    @overload
    def getBuffer(self, id: int, shadowBuffer: db.DBBuffer) -> db.DBBuffer:
        """
        Get an existing buffer that uses a shadowBuffer for byte values if they haven't been
         explicitly changed in this buffer.  This method should be used with care to avoid
         providing an improper id.  A database transaction must be in progress
         when invoking the various put, delete and setSize methods on the returned buffer.
        @param id the buffer id.
        @param shadowBuffer the buffer to use for byte values if they haven't been changed in
         this buffer.
        @return Buffer the buffer associated with the given id.
        @throws IOException if an I/O error occurs while getting the buffer.
        """
        ...

    def getBufferSize(self) -> int:
        """
        Returns size of buffers utilized within the underlying
         buffer file.  This may be larger than than the requested
         buffer size.  This value may be used to instatiate a
         new BufferFile which is compatible with this database
         when using the saveAs method.
        @return buffer size utilized by this database
        """
        ...

    def getCacheHits(self) -> long:
        """
        @return number of buffer cache hits
        """
        ...

    def getCacheMisses(self) -> long:
        """
        @return number of buffer cache misses
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getContentType(self) -> unicode:
        """
        Returns user defined content type associated with this handle.
        """
        ...

    def getDatabaseId(self) -> long:
        """
        @return unique database ID or 0 if this is an older read-only database.
        """
        ...

    def getLowBufferCount(self) -> int:
        """
        @return low water mark (minimum buffer pool size)
        """
        ...

    def getPackedDatabase(self) -> ghidra.framework.store.db.PackedDatabase:
        """
        Returns PackedDatabase associated with this handle, or null if
         this is a temporary handle which has not yet been saved to a
         PackedDatabase using saveAs.
        """
        ...

    def getRecoveryChangeSetFile(self) -> db.buffers.LocalBufferFile:
        """
        Returns the recovery changeSet data file for reading or null if one is not available.
         The caller must dispose of the returned file before peforming generating any new
         recovery snapshots.
        @return recovery changeSet data file for reading or null if one is not available.
        @throws IOException if IO error occurs
        """
        ...

    def getScratchPad(self) -> db.DBHandle:
        """
        Returns a shared temporary database handle.
         This temporary handle will remain open unitl either this
         handle is closed or closeScratchPad is invoked.
        @return shared temporary database handle.
        @throws IOException if IO error occurs
        """
        ...

    def getTable(self, name: unicode) -> db.Table:
        """
        Returns the Table that was created with the given name or null if
         no such table exists.
        @param name of requested table
        @return table instance or null if not found
        """
        ...

    def getTableCount(self) -> int:
        """
        Return the number of tables defined within the master table.
        @return int number of tables.
        """
        ...

    def getTables(self) -> List[db.Table]:
        """
        Get all tables defined within the database.
        @return Table[] tables
        """
        ...

    def hasUncommittedChanges(self) -> bool:
        """
        Returns true if there are uncommitted changes to the database.
        @return true if there are uncommitted changes to the database.
        """
        ...

    def hashCode(self) -> int: ...

    def isChanged(self) -> bool:
        """
        @return true if unsaved changes have been made.
        """
        ...

    def isClosed(self) -> bool:
        """
        @return true if this database handle has been closed.
        """
        ...

    def isConsistent(self, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Check the consistency of this database.
        @param monitor task monitor
        @return true if consistency check passed, else false
        @throws CancelledException if consistency check is cancelled
        """
        ...

    def isTransactionActive(self) -> bool:
        """
        @return true if transaction is currently active
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def rebuild(self, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Rebuild database tables to resolve certain consistency problems.  Use of this
         method does not recover lost data which may have occurred during original
         database corruption.
        @param monitor task monitor
        @return true if rebuild succeeded, else false
        @throws CancelledException if rebuild is cancelled
        """
        ...

    def redo(self) -> bool:
        """
        Redo previously undone transaction checkpoint.
         Moves forward by one checkpoint only.
         All upper-levels must clear table-based cached data prior to
         invoking this method.
        @return boolean
        @throws IOException if IO error occurs
        """
        ...

    @staticmethod
    def resetDatabaseId(file: java.io.File) -> None:
        """
        Reset the database ID contained within the specified database file.
         This method is intended to be used when unpacking a packed database
         to ensure that a duplicate database ID does not exist within the project.
         WARNING! Use with extreme caution since this modifies
         the original file and could destroy data if used
         improperly.
        @param file database buffer file to be updated
        @throws IOException if IO error occurs
        """
        ...

    @overload
    def save(self, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Saves the open database to the corresponding PackedDatabase file.
        @param monitor
        @throws IOException
        @throws CancelledException
        """
        ...

    @overload
    def save(self, comment: unicode, changeSet: db.DBChangeSet, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    @overload
    def saveAs(self, outFile: db.buffers.BufferFile, associateWithNewFile: bool, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    @overload
    def saveAs(self, file: java.io.File, associateWithNewFile: bool, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Save the database to the specified buffer file.
        @param file buffer file to be created
        @param associateWithNewFile if true the outFile will be associated with this DBHandle as the
         current source file, if false no change will be made to this DBHandle's state and the outFile
         will be written and set as read-only.  The caller is responsbile for disposing the outFile if
         this parameter is false.
        @param monitor progress monitor
        @throws DuplicateFileException if file already exists.
        @throws IOException if IO error occurs
        @throws CancelledException if monitor cancels operation
        """
        ...

    @overload
    def saveAs(self, itemName: unicode, dir: java.io.File, packedFileName: unicode, monitor: ghidra.util.task.TaskMonitor) -> ghidra.framework.store.db.PackedDatabase:
        """
        Save open database to a new packed database.
         If another PackedDatabase was associated with this handle prior to this invocation
         it should be disposed to that the underlying database resources can be cleaned-up.
        @param itemName
        @param dir
        @param packedFileName
        @param monitor
        @return new packed Database object now associated with this handle.
        @throws CancelledException if task monitor cancelled operation.
        @throws IOException
        @throws DuplicateFileException
        """
        ...

    @overload
    def saveAs(self, itemName: unicode, dir: java.io.File, packedFileName: unicode, newDatabaseId: long, monitor: ghidra.util.task.TaskMonitor) -> ghidra.framework.store.db.PackedDatabase:
        """
        Save open database to a new packed database with a specified newDatabaseId.
         If another PackedDatabase was associated with this handle prior to this invocation
         it should be disposed to that the underlying database resources can be cleaned-up.
         NOTE: This method is intended for use in transforming one database to
         match another existing database.
        @param itemName
        @param dir
        @param packedFileName
        @param newDatabaseId database ID to be forced for new database or null to generate
         new database ID
        @param monitor
        @return new packed Database object now associated with this handle.
        @throws CancelledException if task monitor cancelled operation.
        @throws IOException
        @throws DuplicateFileException
        """
        ...

    def setMaxUndos(self, maxUndos: int) -> None:
        """
        Set the maximum number of undo transaction checkpoints maintained by the
         underlying buffer manager.
        @param maxUndos maximum number of undo checkpoints.  An illegal
         value restores the default value.
        """
        ...

    def setTableName(self, oldName: unicode, newName: unicode) -> bool:
        """
        Changes the name of an existing table.
        @param oldName the old name of the table
        @param newName the new name of the table
        @throws DuplicateNameException if a table with the new name already exists
        @return true if the name was changed successfully
        """
        ...

    def startTransaction(self) -> long:
        """
        Start a new transaction
        @return transaction ID
        """
        ...

    def takeRecoverySnapshot(self, changeSet: db.DBChangeSet, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Request a recovery snapshot be taken of any unsaved changes;
        @param changeSet an optional database-backed change set which reflects changes
         made since the last version.
        @param monitor task monitor
        @return true if snapshot successful or not needed, false if an active transaction prevented snapshot
        @throws CancelledException if cancelled by monitor
        @throws IOException if IO error occurs
        """
        ...

    def terminateTransaction(self, id: long, commit: bool) -> None: ...

    def toString(self) -> unicode: ...

    def undo(self) -> bool:
        """
        Undo changes made during the previous transaction checkpoint.
         All upper-levels must clear table-based cached data prior to
         invoking this method.
        @return true if an undo was successful
        @throws IOException if IO error occurs
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
    def packedDatabase(self) -> ghidra.framework.store.db.PackedDatabase: ...
