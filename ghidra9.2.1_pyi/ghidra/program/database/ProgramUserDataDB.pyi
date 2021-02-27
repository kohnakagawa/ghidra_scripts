from typing import List
import db
import ghidra.framework.data
import ghidra.framework.model
import ghidra.framework.options
import ghidra.program.model.listing
import ghidra.program.model.util
import ghidra.util
import ghidra.util.task
import java.io
import java.lang
import java.util


class ProgramUserDataDB(ghidra.framework.data.DomainObjectAdapterDB, ghidra.program.model.listing.ProgramUserData):
    """
    ProgramUserDataDB stores user data associated with a specific program.
     A ContentHandler should not be created for this class since it must never be stored
     within a DomainFolder.
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

    def canSave(self) -> bool: ...

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

    @overload
    def endTransaction(self, transactionID: int) -> None: ...

    @overload
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

    def getBooleanProperty(self, owner: unicode, propertyName: unicode, create: bool) -> ghidra.program.model.util.VoidPropertyMap: ...

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

    def getDescription(self) -> unicode: ...

    def getDomainFile(self) -> ghidra.framework.model.DomainFile:
        """
        @see ghidra.framework.model.DomainObject#getDomainFile()
        """
        ...

    def getIntProperty(self, owner: unicode, propertyName: unicode, create: bool) -> ghidra.program.model.util.IntPropertyMap: ...

    def getLock(self) -> ghidra.util.Lock: ...

    def getLongProperty(self, owner: unicode, propertyName: unicode, create: bool) -> ghidra.program.model.util.LongPropertyMap: ...

    def getMetadata(self) -> java.util.Map: ...

    def getModificationNumber(self) -> long: ...

    def getName(self) -> unicode:
        """
        @see ghidra.framework.model.DomainObject#getName()
        """
        ...

    def getObjectProperty(self, owner: unicode, propertyName: unicode, saveableObjectClass: java.lang.Class, create: bool) -> ghidra.program.model.util.ObjectPropertyMap: ...

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

    def getProperties(self, owner: unicode) -> List[ghidra.program.model.util.PropertyMap]: ...

    def getPropertyOwners(self) -> List[unicode]: ...

    def getRedoName(self) -> unicode:
        """
        @see ghidra.framework.model.Undoable#getRedoName()
        """
        ...

    def getStringProperty(self, owner: unicode, propertyName: unicode, create: bool) -> ghidra.program.model.util.StringPropertyMap: ...

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

    def save(self, comment: unicode, monitor: ghidra.util.task.TaskMonitor) -> None: ...

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
    def startTransaction(self) -> int: ...

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
