import ghidra.framework.model
import ghidra.program.model.address
import java.lang


class CodeUnitUserDataChangeRecord(ghidra.framework.model.DomainObjectChangeRecord):




    def __init__(self, propertyName: unicode, codeUnitAddr: ghidra.program.model.address.Address, oldValue: object, newValue: object):
        """
        Constructor
        @param propertyName name of the property
        @param codeUnitAddr address of the code unit
        @param oldValue old value
        @param newValue new value
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address:
        """
        Get the address of the code unit for this property change.
        """
        ...

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
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def newValue(self) -> object: ...

    @property
    def oldValue(self) -> object: ...

    @property
    def propertyName(self) -> unicode: ...
