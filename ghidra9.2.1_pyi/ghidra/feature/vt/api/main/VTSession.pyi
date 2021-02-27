from typing import List
import db.util
import ghidra.feature.vt.api.main
import ghidra.framework.model
import ghidra.framework.options
import ghidra.program.model.listing
import ghidra.util.task
import java.io
import java.lang
import java.util


class VTSession(db.util.ErrorHandler, ghidra.framework.model.UndoableDomainObject, object):
    DO_DOMAIN_FILE_CHANGED: int = 2
    DO_OBJECT_CLOSED: int = 6
    DO_OBJECT_ERROR: int = 8
    DO_OBJECT_RENAMED: int = 3
    DO_OBJECT_RESTORED: int = 4
    DO_OBJECT_SAVED: int = 1
    DO_PROPERTY_CHANGED: int = 5
    undoLock: object = java.lang.Object@471b5ac7







    def addAssociationHook(self, __a0: ghidra.feature.vt.api.main.AssociationHook) -> None: ...

    def addCloseListener(self, __a0: ghidra.framework.model.DomainObjectClosedListener) -> None: ...

    def addConsumer(self, __a0: object) -> bool: ...

    def addListener(self, __a0: ghidra.framework.model.DomainObjectListener) -> None: ...

    def addSynchronizedDomainObject(self, __a0: ghidra.framework.model.DomainObject) -> None: ...

    def addTransactionListener(self, __a0: ghidra.framework.model.TransactionListener) -> None: ...

    def canLock(self) -> bool: ...

    def canRedo(self) -> bool: ...

    def canSave(self) -> bool: ...

    def canUndo(self) -> bool: ...

    def clearUndo(self) -> None: ...

    def createMatchSet(self, __a0: ghidra.feature.vt.api.main.VTProgramCorrelator) -> ghidra.feature.vt.api.main.VTMatchSet: ...

    def createMatchTag(self, __a0: unicode) -> ghidra.feature.vt.api.main.VTMatchTag: ...

    def createPrivateEventQueue(self, __a0: ghidra.framework.model.DomainObjectListener, __a1: int) -> ghidra.framework.model.EventQueueID: ...

    def dbError(self, __a0: java.io.IOException) -> None: ...

    def deleteMatchTag(self, __a0: ghidra.feature.vt.api.main.VTMatchTag) -> None: ...

    def endTransaction(self, __a0: int, __a1: bool) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def flushEvents(self) -> None: ...

    def flushPrivateEventQueue(self, __a0: ghidra.framework.model.EventQueueID) -> None: ...

    def forceLock(self, __a0: bool, __a1: unicode) -> None: ...

    def getAssociationManager(self) -> ghidra.feature.vt.api.main.VTAssociationManager: ...

    def getClass(self) -> java.lang.Class: ...

    def getConsumerList(self) -> java.util.ArrayList: ...

    def getCurrentTransaction(self) -> ghidra.framework.model.Transaction: ...

    def getDescription(self) -> unicode: ...

    def getDestinationProgram(self) -> ghidra.program.model.listing.Program: ...

    def getDomainFile(self) -> ghidra.framework.model.DomainFile: ...

    def getImpliedMatchSet(self) -> ghidra.feature.vt.api.main.VTMatchSet: ...

    def getManualMatchSet(self) -> ghidra.feature.vt.api.main.VTMatchSet: ...

    def getMatchSets(self) -> List[object]: ...

    def getMatchTags(self) -> java.util.Set: ...

    def getMatches(self, __a0: ghidra.feature.vt.api.main.VTAssociation) -> List[object]: ...

    def getMetadata(self) -> java.util.Map: ...

    def getModificationNumber(self) -> long: ...

    def getName(self) -> unicode: ...

    def getOptions(self, __a0: unicode) -> ghidra.framework.options.Options: ...

    def getOptionsNames(self) -> List[object]: ...

    def getRedoName(self) -> unicode: ...

    def getSourceProgram(self) -> ghidra.program.model.listing.Program: ...

    def getSynchronizedDomainObjects(self) -> List[ghidra.framework.model.DomainObject]: ...

    def getUndoName(self) -> unicode: ...

    def hasExclusiveAccess(self) -> bool: ...

    def hasTerminatedTransaction(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isChangeable(self) -> bool: ...

    def isChanged(self) -> bool: ...

    def isClosed(self) -> bool: ...

    def isLocked(self) -> bool: ...

    def isSendingEvents(self) -> bool: ...

    def isTemporary(self) -> bool: ...

    def isUsedBy(self, __a0: object) -> bool: ...

    def lock(self, __a0: unicode) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def redo(self) -> None: ...

    def release(self, __a0: object) -> None: ...

    def releaseSynchronizedDomainObject(self) -> None: ...

    def removeAssociationHook(self, __a0: ghidra.feature.vt.api.main.AssociationHook) -> None: ...

    def removeCloseListener(self, __a0: ghidra.framework.model.DomainObjectClosedListener) -> None: ...

    def removeListener(self, __a0: ghidra.framework.model.DomainObjectListener) -> None: ...

    def removePrivateEventQueue(self, __a0: ghidra.framework.model.EventQueueID) -> bool: ...

    def removeTransactionListener(self, __a0: ghidra.framework.model.TransactionListener) -> None: ...

    @overload
    def save(self) -> None: ...

    @overload
    def save(self, __a0: unicode, __a1: ghidra.util.task.TaskMonitor) -> None: ...

    def saveToPackedFile(self, __a0: java.io.File, __a1: ghidra.util.task.TaskMonitor) -> None: ...

    def setEventsEnabled(self, __a0: bool) -> None: ...

    def setName(self, __a0: unicode) -> None: ...

    def setTemporary(self, __a0: bool) -> None: ...

    @overload
    def startTransaction(self, __a0: unicode) -> int: ...

    @overload
    def startTransaction(self, __a0: unicode, __a1: ghidra.framework.model.AbortedTransactionListener) -> int: ...

    def toString(self) -> unicode: ...

    def undo(self) -> None: ...

    def unlock(self) -> None: ...

    def updateDestinationProgram(self, __a0: ghidra.program.model.listing.Program) -> None: ...

    def updateSourceProgram(self, __a0: ghidra.program.model.listing.Program) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def associationManager(self) -> ghidra.feature.vt.api.main.VTAssociationManager: ...

    @property
    def changeable(self) -> bool: ...

    @property
    def changed(self) -> bool: ...

    @property
    def closed(self) -> bool: ...

    @property
    def consumerList(self) -> java.util.ArrayList: ...

    @property
    def currentTransaction(self) -> ghidra.framework.model.Transaction: ...

    @property
    def description(self) -> unicode: ...

    @property
    def destinationProgram(self) -> ghidra.program.model.listing.Program: ...

    @property
    def domainFile(self) -> ghidra.framework.model.DomainFile: ...

    @property
    def eventsEnabled(self) -> None: ...  # No getter available.

    @eventsEnabled.setter
    def eventsEnabled(self, value: bool) -> None: ...

    @property
    def impliedMatchSet(self) -> ghidra.feature.vt.api.main.VTMatchSet: ...

    @property
    def locked(self) -> bool: ...

    @property
    def manualMatchSet(self) -> ghidra.feature.vt.api.main.VTMatchSet: ...

    @property
    def matchSets(self) -> List[object]: ...

    @property
    def matchTags(self) -> java.util.Set: ...

    @property
    def metadata(self) -> java.util.Map: ...

    @property
    def modificationNumber(self) -> long: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def optionsNames(self) -> List[object]: ...

    @property
    def redoName(self) -> unicode: ...

    @property
    def sendingEvents(self) -> bool: ...

    @property
    def sourceProgram(self) -> ghidra.program.model.listing.Program: ...

    @property
    def synchronizedDomainObjects(self) -> List[ghidra.framework.model.DomainObject]: ...

    @property
    def temporary(self) -> bool: ...

    @temporary.setter
    def temporary(self, value: bool) -> None: ...

    @property
    def undoName(self) -> unicode: ...
