import ghidra.framework.model
import java.lang


class UserDataChangeRecord(ghidra.framework.model.DomainObjectChangeRecord):




    @overload
    def __init__(self, propertyName: unicode):
        """
        Constructor for change record for removing a range of properties.
        @param propertyName name of the property
        """
        ...

    @overload
    def __init__(self, propertyName: unicode, oldValue: object, newValue: object):
        """
        Constructor
        @param propertyName name of the property
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
        Get the new value.
        """
        ...

    def getOldValue(self) -> object:
        """
        Get the original value.
        """
        ...

    def getPropertyName(self) -> unicode:
        """
        Get the name of the property being changed.
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
    def newValue(self) -> object: ...

    @property
    def oldValue(self) -> object: ...

    @property
    def propertyName(self) -> unicode: ...
