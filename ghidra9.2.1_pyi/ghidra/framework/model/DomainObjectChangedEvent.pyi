from typing import Iterator
import ghidra.framework.model
import java.lang
import java.util
import java.util.function


class DomainObjectChangedEvent(java.util.EventObject, java.lang.Iterable):
    """
    An event indicating a DomainObject has changed.  This event is actually
     a list of DomainObjectChangeRecords.

     NOTE: This object is TRANSIENT - it is only valid during the life of calls
     to all the DomainObjectChangeListeners.  Listeners who need to retain
     any of this event information past the listener call should save the
     DomainObjectChangeRecords, which will remain valid always.
    """





    def __init__(self, __a0: ghidra.framework.model.DomainObject, __a1: List[object]): ...

    def __iter__(self): ...

    def containsEvent(self, eventType: int) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def getChangeRecord(self, i: int) -> ghidra.framework.model.DomainObjectChangeRecord:
        """
        Get the specified change record within this event.
        @param i change record number
        @return change record
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getSource(self) -> object: ...

    def hashCode(self) -> int: ...

    def iterator(self) -> Iterator[ghidra.framework.model.DomainObjectChangeRecord]:
        """
        Returns iterator over all sub-events
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def numRecords(self) -> int:
        """
        Return the number of change records contained within this event.
        """
        ...

    def spliterator(self) -> java.util.Spliterator: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
