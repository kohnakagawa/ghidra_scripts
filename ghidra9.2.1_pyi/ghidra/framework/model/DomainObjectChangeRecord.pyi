import java.io
import java.lang


class DomainObjectChangeRecord(object, java.io.Serializable):
    """
    Information about a change that was made to a domain object. The
     record is delivered as part of the change notification. The event
     types correspond to the constants in
     ghidra.program.util.ChangeManager.
    """





    @overload
    def __init__(self):
        """
        Construct a new DomainObjectChangeRecord.
        """
        ...

    @overload
    def __init__(self, type: int):
        """
        Construct a new DomainObjectChangeRecord.
        @param type event type
        """
        ...

    @overload
    def __init__(self, type: int, oldValue: object, newValue: object):
        """
        Construct a new DomainObjectChangeRecord.
        @param type event type
        @param oldValue old value
        @param newValue new value
        """
        ...

    @overload
    def __init__(self, type: int, subType: int, oldValue: object, newValue: object):
        """
        Construct a new DomainObjectChangeRecord.
        @param type event type
        @param subType sub-event type (use 0 if unspecified)
        @param oldValue old value
        @param newValue new value
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEventType(self) -> int:
        """
        Return the event type for this change record.
        """
        ...

    def getNewValue(self) -> object:
        """
        Return the new value.
        """
        ...

    def getOldValue(self) -> object:
        """
        Return the old value.
        """
        ...

    def getSubEventType(self) -> int:
        """
        Return the sub-event type for this change record.
         A value of 0 is the default if unspecified.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def eventType(self) -> int: ...

    @property
    def newValue(self) -> object: ...

    @property
    def oldValue(self) -> object: ...

    @property
    def subEventType(self) -> int: ...
