from typing import List
import ghidra.framework.data
import ghidra.framework.model
import ghidra.framework.options
import ghidra.util
import ghidra.util.task
import java.io
import java.lang
import java.util


class DomainObjectAdapter(object, ghidra.framework.model.DomainObject):
    """
    An abstract class that provides default behavior for
     DomainObject(s), specifically it handles listeners and
     change status; the derived class must provide the
     getDescription() method.
    """

    DO_DOMAIN_FILE_CHANGED: int = 2
    DO_OBJECT_CLOSED: int = 6
    DO_OBJECT_ERROR: int = 8
    DO_OBJECT_RENAMED: int = 3
    DO_OBJECT_RESTORED: int = 4
    DO_OBJECT_SAVED: int = 1
    DO_PROPERTY_CHANGED: int = 5
    undoLock: object = java.lang.Object@471b5ac7







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

    def canLock(self) -> bool: ...

    def canSave(self) -> bool: ...

    def checkExclusiveAccess(self) -> None: ...

    def createPrivateEventQueue(self, listener: ghidra.framework.model.DomainObjectListener, maxDelay: int) -> ghidra.framework.model.EventQueueID: ...

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

    def forceLock(self, __a0: bool, __a1: unicode) -> None: ...

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

    def getOptions(self, __a0: unicode) -> ghidra.framework.options.Options: ...

    def getOptionsNames(self) -> List[object]: ...

    def hasExclusiveAccess(self) -> bool:
        """
        @see ghidra.framework.model.DomainObject#hasExclusiveAccess()
        """
        ...

    def hashCode(self) -> int: ...

    def isChangeable(self) -> bool: ...

    def isChanged(self) -> bool:
        """
        @see ghidra.framework.model.DomainObject#isChanged()
        """
        ...

    def isClosed(self) -> bool: ...

    def isLocked(self) -> bool: ...

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

    def lock(self, __a0: unicode) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def release(self, consumer: object) -> None:
        """
        @see ghidra.framework.model.DomainObject#release(java.lang.Object)
        """
        ...

    def removeCloseListener(self, listener: ghidra.framework.model.DomainObjectClosedListener) -> None: ...

    def removeListener(self, l: ghidra.framework.model.DomainObjectListener) -> None:
        """
        @see ghidra.framework.model.DomainObject#removeListener(ghidra.framework.model.DomainObjectListener)
        """
        ...

    def removePrivateEventQueue(self, id: ghidra.framework.model.EventQueueID) -> bool: ...

    def save(self, __a0: unicode, __a1: ghidra.util.task.TaskMonitor) -> None: ...

    def saveToPackedFile(self, __a0: java.io.File, __a1: ghidra.util.task.TaskMonitor) -> None: ...

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

    def toString(self) -> unicode:
        """
        @see java.lang.Object#toString()
        """
        ...

    def unlock(self) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def changeStatus(self) -> bool: ...

    @property
    def changeable(self) -> bool: ...

    @property
    def changed(self) -> bool: ...

    @property
    def closed(self) -> bool: ...

    @property
    def consumerList(self) -> java.util.ArrayList: ...

    @property
    def description(self) -> unicode: ...

    @property
    def domainFile(self) -> ghidra.framework.model.DomainFile: ...

    @property
    def eventsEnabled(self) -> None: ...  # No getter available.

    @eventsEnabled.setter
    def eventsEnabled(self, value: bool) -> None: ...

    @property
    def locked(self) -> bool: ...

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
    def sendingEvents(self) -> bool: ...

    @property
    def temporary(self) -> bool: ...

    @temporary.setter
    def temporary(self, value: bool) -> None: ...
