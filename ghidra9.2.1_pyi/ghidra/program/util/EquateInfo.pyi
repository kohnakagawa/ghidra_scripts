import ghidra.program.model.address
import java.lang


class EquateInfo(object):
    """
    Class to hold information about an Equate; it is used
     in a ProgramChangeRecord when an equate is created and
     when references to the Equate are updated.
    """





    def __init__(self, name: unicode, value: long, refAddr: ghidra.program.model.address.Address, opIndex: int, dynamicHash: long):
        """
        Constructor.
        @param name Equate name
        @param value Equate value
        @param refAddr Reference address (may be null for some event types)
        @param opIndex operand index for the reference; useful only if
         refAddr is not null. May be -1 if only dynamicHash applies.
        @param dynamicHash dynamic hash. May be 0 if only opIndex applies.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDynamicHash(self) -> long:
        """
        Get the varnode dynamic hash of where the equate was placed;
         This value is meaningful only if the reference address is not null, and
         may be 0 if only the operand index applies.
        """
        ...

    def getName(self) -> unicode:
        """
        Get the equate name.
        """
        ...

    def getOperandIndex(self) -> int:
        """
        Get the operand index of where the equate was placed;
         This value is meaningful only if the reference address is not null, and
         may be -1 if only the dynamicHash applies.
        """
        ...

    def getReferenceAddress(self) -> ghidra.program.model.address.Address:
        """
        Get the reference address.
        """
        ...

    def getValue(self) -> long:
        """
        Get the equate value.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode:
        """
        Return a meaningful string for debugging purposes.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def dynamicHash(self) -> long: ...

    @property
    def name(self) -> unicode: ...

    @property
    def operandIndex(self) -> int: ...

    @property
    def referenceAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def value(self) -> long: ...
