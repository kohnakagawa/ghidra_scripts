from typing import List
import db
import db.util
import ghidra.framework.data
import ghidra.framework.model
import ghidra.framework.options
import ghidra.util
import ghidra.util.task
import java.io
import java.lang
import java.util


class DomainObjectAdapterDB(ghidra.framework.data.DomainObjectAdapter, ghidra.framework.model.UndoableDomainObject, db.util.ErrorHandler, db.DBConstants):
    """
    Database version of the DomainObjectAdapter; this version adds the
     concept of starting a transaction before a change is made to the
     domain object and ending the transaction. The transaction allows for
     undo/redo changes.

     The implementation class must also satisfy the following requirements:


     1. The following constructor signature must be implemented:

     		 **
    		 * Constructs new Domain Object
    		 * @param dbh a handle to an open domain object database.
    		 * @param openMode one of:
    		 * 		READ_ONLY: the original database will not be modified
    		 * 		UPDATE: the database can be written to.
    		 * 		UPGRADE: the database is upgraded to the latest schema as it is opened.
    		 * @param monitor TaskMonitor that allows the open to be cancelled.
    	     * @param consumer the object that keeping the program open.
    		 *
    		 * @throws IOException if an error accessing the database occurs.
    		 * @throws VersionException if database version does not match implementation. UPGRADE may be possible.
    		 **
    		 public DomainObjectAdapterDB(DBHandle dbh, int openMode, TaskMonitor monitor, Object consumer) throws IOException, VersionException

     2. The following static field must be provided:

     		 public static final String CONTENT_TYPE


    """









    def addCloseListener(self, listener: ghidra.framework.model.DomainObjectClosedListener) -> None: ...

    def addConsumer(self, consumer: object) -> bool:
        """
        @see ghidra.framework.model.DomainObject#addConsumer(java.lang.Object)
        """
        ...

    def addListener(self, l: ghidra.framework.model.DomainObjectListener) -> None:
        """
        @see ghidra.framework.model.DomainObject#addListener(ghidra.framework.model.DomainObjectListener)
        """
        ...

    def addSynchronizedDomainObject(self, domainObj: ghidra.framework.model.DomainObject) -> None:
        """
        Synchronize the specified domain object with this domain object
         using a shared transaction manager.  If either or both is already shared,
         a transition to a single shared transaction manager will be
         performed.
        @param domainObj
        @throws LockException if lock or open transaction is active on either
         this or the specified domain object
        """
        ...

    def addTransactionListener(self, listener: ghidra.framework.model.TransactionListener) -> None:
        """
        Adds the given transaction listener to this domain object
        @param listener the new transaction listener to add
        """
        ...

    def canLock(self) -> bool:
        """
        @see ghidra.framework.model.DomainObject#canLock()
        """
        ...

    def canRedo(self) -> bool:
        """
        @see ghidra.framework.model.Undoable#canRedo()
        """
        ...

    def canSave(self) -> bool:
        """
        @see ghidra.framework.model.DomainObject#canSave()
        """
        ...

    def canUndo(self) -> bool:
        """
        @see ghidra.framework.model.Undoable#canUndo()
        """
        ...

    def checkExclusiveAccess(self) -> None: ...

    def clearUndo(self) -> None:
        """
        @see ghidra.framework.model.Undoable#clearUndo()
        """
        ...

    def createPrivateEventQueue(self, listener: ghidra.framework.model.DomainObjectListener, maxDelay: int) -> ghidra.framework.model.EventQueueID: ...

    def dbError(self, e: java.io.IOException) -> None:
        """
        @see db.util.ErrorHandler#dbError(java.io.IOException)
        """
        ...

    def endTransaction(self, transactionID: int, commit: bool) -> None:
        """
        @see ghidra.framework.model.UndoableDomainObject#endTransaction(int, boolean)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def fireEvent(self, ev: ghidra.framework.model.DomainObjectChangeRecord) -> None:
        """
        Fires the specified event.
        @param ev event to fire
        """
        ...

    def flushEvents(self) -> None:
        """
        @see ghidra.framework.model.DomainObject#flushEvents()
        """
        ...

    def flushPrivateEventQueue(self, id: ghidra.framework.model.EventQueueID) -> None: ...

    def flushWriteCache(self) -> None:
        """
        Flush any pending database changes.
         This method will be invoked by the transaction manager
         prior to closing a transaction.
        """
        ...

    def forceLock(self, rollback: bool, reason: unicode) -> None:
        """
        @see ghidra.framework.model.DomainObject#forceLock(boolean, String)
        """
        ...

    def getChangeSet(self) -> ghidra.framework.data.DomainObjectDBChangeSet:
        """
        Returns the change set corresponding to all unsaved changes in this domain object.
        @return the change set corresponding to all unsaved changes in this domain object
        """
        ...

    def getChangeStatus(self) -> bool:
        """
        Return "changed" status
        @return true if this object has changed
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getConsumerList(self) -> List[object]: ...

    @staticmethod
    def getContentHandler(dobj: ghidra.framework.model.DomainObject) -> ghidra.framework.data.ContentHandler:
        """
        Get the ContentHandler associated with the specified domain object
        @param dobj domain object
        @return content handler
        """
        ...

    def getCurrentTransaction(self) -> ghidra.framework.model.Transaction:
        """
        @see ghidra.framework.model.UndoableDomainObject#getCurrentTransaction()
        """
        ...

    def getDBHandle(self) -> db.DBHandle:
        """
        Returns the open handle to the underlying database.
        """
        ...

    def getDescription(self) -> unicode:
        """
        @see ghidra.framework.model.DomainObject#getDescription()
        """
        ...

    def getDomainFile(self) -> ghidra.framework.model.DomainFile:
        """
        @see ghidra.framework.model.DomainObject#getDomainFile()
        """
        ...

    def getLock(self) -> ghidra.util.Lock: ...

    def getMetadata(self) -> java.util.Map: ...

    def getModificationNumber(self) -> long: ...

    def getName(self) -> unicode:
        """
        @see ghidra.framework.model.DomainObject#getName()
        """
        ...

    def getOptions(self, propertyListName: unicode) -> ghidra.framework.options.Options:
        """
        @see ghidra.framework.model.DomainObject#getOptions(java.lang.String)
        """
        ...

    def getOptionsNames(self) -> List[unicode]:
        """
        Returns all properties lists contained by this domain object.
        @return all property lists contained by this domain object.
        """
        ...

    def getRedoName(self) -> unicode:
        """
        @see ghidra.framework.model.Undoable#getRedoName()
        """
        ...

    def getSynchronizedDomainObjects(self) -> List[ghidra.framework.model.DomainObject]:
        """
        Return array of all domain objects synchronized with a
         shared transaction manager.
        @return returns array of synchronized domain objects or
         null if this domain object is not synchronized with others.
        """
        ...

    def getUndoName(self) -> unicode:
        """
        @see ghidra.framework.model.Undoable#getUndoName()
        """
        ...

    def getUndoStackDepth(self) -> int:
        """
        Returns the undo stack depth.
         (The number of items on the undo stack)
         This method is for JUnits.
        @return the undo stack depth
        """
        ...

    def hasExclusiveAccess(self) -> bool:
        """
        @see ghidra.framework.model.DomainObject#hasExclusiveAccess()
        """
        ...

    def hasTerminatedTransaction(self) -> bool:
        """
        @see ghidra.framework.model.UndoableDomainObject#hasTerminatedTransaction()
        """
        ...

    def hashCode(self) -> int: ...

    def invalidateWriteCache(self) -> None:
        """
        Invalidate (i.e., clear) any pending database changes not yet written.
         This method will be invoked by the transaction manager
         prior to aborting a transaction.
        """
        ...

    def isChangeable(self) -> bool: ...

    def isChanged(self) -> bool:
        """
        @see ghidra.framework.model.DomainObject#isChanged()
        """
        ...

    def isClosed(self) -> bool:
        """
        @see ghidra.framework.model.DomainObject#isClosed()
        """
        ...

    def isLocked(self) -> bool:
        """
        @see ghidra.framework.model.DomainObject#isLocked()
        """
        ...

    def isSendingEvents(self) -> bool: ...

    def isTemporary(self) -> bool:
        """
        @see ghidra.framework.model.DomainObject#isTemporary()
        """
        ...

    def isUsedBy(self, consumer: object) -> bool:
        """
        Returns true if the given tool is using this object.
        """
        ...

    def lock(self, reason: unicode) -> bool:
        """
        @see ghidra.framework.model.DomainObject#lock(String)
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def redo(self) -> None:
        """
        @see ghidra.framework.model.Undoable#redo()
        """
        ...

    def release(self, consumer: object) -> None:
        """
        @see ghidra.framework.model.DomainObject#release(java.lang.Object)
        """
        ...

    def releaseSynchronizedDomainObject(self) -> None:
        """
        Release this domain object from a shared transaction manager.  If
         this object has not been synchronized with others via a shared
         transaction manager, this method will have no affect.
        @throws LockException if lock or open transaction is active
        """
        ...

    def removeCloseListener(self, listener: ghidra.framework.model.DomainObjectClosedListener) -> None: ...

    def removeListener(self, l: ghidra.framework.model.DomainObjectListener) -> None:
        """
        @see ghidra.framework.model.DomainObject#removeListener(ghidra.framework.model.DomainObjectListener)
        """
        ...

    def removePrivateEventQueue(self, id: ghidra.framework.model.EventQueueID) -> bool: ...

    def removeTransactionListener(self, listener: ghidra.framework.model.TransactionListener) -> None:
        """
        Removes the given transaction listener from this domain object.
        @param listener the transaction listener to remove
        """
        ...

    def save(self, comment: unicode, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        @see ghidra.framework.model.DomainObject#save(java.lang.String, ghidra.util.task.TaskMonitor)
        """
        ...

    def saveToPackedFile(self, outputFile: java.io.File, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        @see ghidra.framework.model.DomainObject#saveToPackedFile(java.io.File, ghidra.util.task.TaskMonitor)
        """
        ...

    @staticmethod
    def setDefaultContentClass(doClass: java.lang.Class) -> None:
        """
        Set default content type
        @param doClass default domain object implementation
        """
        ...

    def setEventsEnabled(self, v: bool) -> None:
        """
        @see ghidra.framework.model.DomainObject#setEventsEnabled(boolean)
        """
        ...

    def setName(self, newName: unicode) -> None:
        """
        @see ghidra.framework.model.DomainObject#setName(java.lang.String)
        """
        ...

    def setTemporary(self, state: bool) -> None:
        """
        @see ghidra.framework.model.DomainObject#setTemporary(boolean)
        """
        ...

    @overload
    def startTransaction(self, description: unicode) -> int: ...

    @overload
    def startTransaction(self, description: unicode, listener: ghidra.framework.model.AbortedTransactionListener) -> int:
        """
        @see ghidra.framework.model.UndoableDomainObject#startTransaction(java.lang.String)
        """
        ...

    def toString(self) -> unicode:
        """
        @see java.lang.Object#toString()
        """
        ...

    def undo(self) -> None:
        """
        @see ghidra.framework.model.Undoable#undo()
        """
        ...

    def unlock(self) -> None:
        """
        @see ghidra.framework.model.DomainObject#unlock()
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def DBHandle(self) -> db.DBHandle: ...

    @property
    def changeSet(self) -> ghidra.framework.data.DomainObjectDBChangeSet: ...

    @property
    def changed(self) -> bool: ...

    @property
    def closed(self) -> bool: ...

    @property
    def currentTransaction(self) -> ghidra.framework.model.Transaction: ...

    @property
    def locked(self) -> bool: ...

    @property
    def optionsNames(self) -> List[object]: ...

    @property
    def redoName(self) -> unicode: ...

    @property
    def synchronizedDomainObjects(self) -> List[ghidra.framework.model.DomainObject]: ...

    @property
    def undoName(self) -> unicode: ...

    @property
    def undoStackDepth(self) -> int: ...
