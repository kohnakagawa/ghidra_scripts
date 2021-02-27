import ghidra.program.model.symbol
import java.lang


class DataRefType(ghidra.program.model.symbol.RefType):
    """
    Class to define reference types for data.
    """









    def equals(self, obj: object) -> bool:
        """
        @see java.lang.Object#equals(java.lang.Object)
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode:
        """
        Returns name of ref-type
        """
        ...

    def getValue(self) -> int:
        """
        Get the int value for this RefType object.
        """
        ...

    def hasFallthrough(self) -> bool:
        """
        Returns true if this flow type can fall through.
        """
        ...

    def hashCode(self) -> int:
        """
        @see java.lang.Object#hashCode()
        """
        ...

    def isCall(self) -> bool:
        """
        Returns true if the flow is call
        """
        ...

    def isComputed(self) -> bool:
        """
        Returns true if the flow is a computed call or compute jump.
        """
        ...

    def isConditional(self) -> bool:
        """
        Returns true if the flow is a conditional call or jump.
        """
        ...

    def isData(self) -> bool: ...

    def isFallthrough(self) -> bool:
        """
        Return true if this flow type is one that does not cause
         a break in control flow.
        """
        ...

    def isFlow(self) -> bool:
        """
        Returns true if the reference is an instruction flow reference.
        """
        ...

    def isIndirect(self) -> bool: ...

    def isJump(self) -> bool:
        """
        Returns true if the flow is jump
        """
        ...

    def isOverride(self) -> bool:
        """
        @return true precisely when the reference is an overriding reference
        """
        ...

    def isRead(self) -> bool: ...

    def isTerminal(self) -> bool:
        """
        returns true if this instruction terminates.
        """
        ...

    def isUnConditional(self) -> bool:
        """
        Returns true if the flow is an unconditional call or jump.
        """
        ...

    def isWrite(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode:
        """
        @see java.lang.Object#toString()
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def data(self) -> bool: ...

    @property
    def indirect(self) -> bool: ...

    @property
    def read(self) -> bool: ...

    @property
    def write(self) -> bool: ...
