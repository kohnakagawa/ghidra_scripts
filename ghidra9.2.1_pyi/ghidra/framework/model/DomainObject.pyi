from typing import List
import ghidra.framework.model
import ghidra.framework.options
import ghidra.util.task
import java.io
import java.lang
import java.util


class DomainObject(object):
    """
    DomainObject is the interface that must be supported by
     data objects that are persistent. DomainObjects maintain an
     association with a DomainFile. A DomainObject that
     has never been saved will have a null DomainFile.
    """

    DO_DOMAIN_FILE_CHANGED: int = 2
    DO_OBJECT_CLOSED: int = 6
    DO_OBJECT_ERROR: int = 8
    DO_OBJECT_RENAMED: int = 3
    DO_OBJECT_RESTORED: int = 4
    DO_OBJECT_SAVED: int = 1
    DO_PROPERTY_CHANGED: int = 5
    undoLock: object = java.lang.Object@471b5ac7







    def addCloseListener(self, listener: ghidra.framework.model.DomainObjectClosedListener) -> None:
        """
        Adds a listener that will be notified when this DomainObject is closed.  This is meant
         for clients to have a chance to cleanup, such as reference removal.
        @param listener the reference to add
        """
        ...

    def addConsumer(self, consumer: object) -> bool:
        """
        Adds the given object as a consumer.  The release method must be invoked
         with this same consumer instance when this domain object is no longer in-use.
        @param consumer domain object consumer
        @return false if this domain object has already been closed
        """
        ...

    def addListener(self, dol: ghidra.framework.model.DomainObjectListener) -> None:
        """
        Adds a listener for this object.
        @param dol listener notified when any change occurs to this domain object
        """
        ...

    def canLock(self) -> bool:
        """
        Returns true if a modification lock can be obtained on this
         domain object.  Care should be taken with using this method since
         this will not prevent another thread from modifying the domain object.
        """
        ...

    def canSave(self) -> bool:
        """
        Returns true if this object can be saved; a read-only file
         cannot be saved.
        """
        ...

    def createPrivateEventQueue(self, listener: ghidra.framework.model.DomainObjectListener, maxDelay: int) -> ghidra.framework.model.EventQueueID:
        """
        Creates a private event queue that can be flushed independently from the main event queue.
        @param listener the listener to be notified of domain object events.
        @param maxDelay the time interval (in milliseconds) used to buffer events.
        @return a unique identifier for this private queue.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def flushEvents(self) -> None:
        """
        Makes sure all pending domainEvents have been sent.
        """
        ...

    def flushPrivateEventQueue(self, id: ghidra.framework.model.EventQueueID) -> None:
        """
        Flush events from the specified event queue.
        @param id the id specifying the event queue to be flushed.
        """
        ...

    def forceLock(self, rollback: bool, reason: unicode) -> None:
        """
        Cancels any previous lock and aquires it.
        @param rollback if true, any changes in made with the previous lock should be discarded.
        @param reason very short reason for requesting lock
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getConsumerList(self) -> List[object]:
        """
        Returns the list of consumers on this domainObject
        @return the list of consumers.
        """
        ...

    def getDescription(self) -> unicode:
        """
        Returns a word or short phrase that best describes or categorizes
         the object in terms that a user will understand.
        """
        ...

    def getDomainFile(self) -> ghidra.framework.model.DomainFile:
        """
        Get the domain file for this domain object.
        @return the associated domain file
        """
        ...

    def getMetadata(self) -> java.util.Map:
        """
        Returns a map containing all the stored metadata associated with this domain object.  The map
         contains key,value pairs and are ordered by their insertion order.
        @return a map containing all the stored metadata associated with this domain object.
        """
        ...

    def getModificationNumber(self) -> long:
        """
        Returns a long value that gets incremented every time a change, undo, or redo takes place.
         Useful for implementing a lazy caching system.
        @return a long value that is incremented for every change to the program.
        """
        ...

    def getName(self) -> unicode:
        """
        Get the name of this domain object.
        """
        ...

    def getOptions(self, propertyListName: unicode) -> ghidra.framework.options.Options:
        """
        Get the property list for the given name.
        @param propertyListName name of property list
        """
        ...

    def getOptionsNames(self) -> List[unicode]:
        """
        Returns all properties lists contained by this domain object.
        @return all property lists contained by this domain object.
        """
        ...

    def hasExclusiveAccess(self) -> bool:
        """
        Returns true if the user has exclusive access to the domain object.  Exclusive access means
         either the object is not shared or the user has an exclusive checkout on the object.
        """
        ...

    def hashCode(self) -> int: ...

    def isChangeable(self) -> bool:
        """
        Returns true if changes are permitted.
        """
        ...

    def isChanged(self) -> bool:
        """
        Returns whether the object has changed.
        """
        ...

    def isClosed(self) -> bool:
        """
        Returns true if this domain object has been closed as a result of the last release
        """
        ...

    def isLocked(self) -> bool:
        """
        Returns true if the domain object currenly has a modification lock enabled.
        """
        ...

    def isSendingEvents(self) -> bool:
        """
        Returns true if this object is sending out events as it is changed.  The default is
         true.  You can change this value by calling {@link #setEventsEnabled(boolean)}.
        @see #setEventsEnabled(boolean)
        """
        ...

    def isTemporary(self) -> bool:
        """
        Returns true if this object has been marked as Temporary.
        """
        ...

    def isUsedBy(self, consumer: object) -> bool:
        """
        Returns true if the given consumer is using (has open) this domain object.
        @param consumer the object to test to see if it is a consumer of this domain object.
        @return true if the given consumer is using (has open) this domain object;
        """
        ...

    def lock(self, reason: unicode) -> bool:
        """
        Attempt to obtain a modification lock on the domain object.  Multiple locks
         may be granted on this domain object, although all lock owners must release their
         lock in a timely fashion.
        @param reason very short reason for requesting lock
        @return true if lock obtained successfully, else false which indicates that a
         modification is in process.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def release(self, consumer: object) -> None:
        """
        Notify the domain object that the specified consumer is no longer using it.
         When the last consumer invokes this method, the domain object will be closed
         and will become invalid.
        @param consumer the consumer (e.g., tool, plugin, etc) of the domain object
         previously established with the addConsumer method.
        """
        ...

    def removeCloseListener(self, listener: ghidra.framework.model.DomainObjectClosedListener) -> None:
        """
        Removes the given close listener.
        @param listener the listener to remove.
        """
        ...

    def removeListener(self, dol: ghidra.framework.model.DomainObjectListener) -> None:
        """
        Remove the listener for this object.
        @param dol listener
        """
        ...

    def removePrivateEventQueue(self, id: ghidra.framework.model.EventQueueID) -> bool:
        """
        Removes the specified private event queue
        @param id the id of the queue to remove.
        @return true if the id represents a valid queue that was removed.
        """
        ...

    def save(self, comment: unicode, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Saves changes to the DomainFile.
        @param comment comment used for new version
        @param monitor monitor that shows the progress of the save
        @throws IOException thrown if there was an error accessing this
         domain object
        @throws ReadOnlyException thrown if this DomainObject is read only
         and cannot be saved
        @throws CancelledException thrown if the user canceled the save
         operation
        """
        ...

    def saveToPackedFile(self, outputFile: java.io.File, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Saves (i.e., serializes) the current content to a packed file.
        @param outputFile packed output file
        @param monitor progress monitor
        @throws IOException
        @throws CancelledException
        @throws UnsupportedOperationException if not supported by object implementation
        """
        ...

    def setEventsEnabled(self, enabled: bool) -> None:
        """
        If true, domain object change events are sent. If false, no events are sent.
         <p>
         <b>
         NOTE: disabling events could cause plugins to be out of sync!
         </b>
         <p>
         NOTE: when re-enabling events, an event will be sent to the system to signal that
               every listener should update.
        @param enabled true means to enable events
        """
        ...

    def setName(self, name: unicode) -> None:
        """
        Set the name for this domain object.
        @param name object name
        """
        ...

    def setTemporary(self, state: bool) -> None:
        """
        Set the temporary state of this object.
         If this object is temporary, the isChanged() method will
         always return false.  The default temporary state is false.
        @param state if true object is marked as temporary
        """
        ...

    def toString(self) -> unicode: ...

    def unlock(self) -> None:
        """
        Release a modification lock previously granted with the lock method.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

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
