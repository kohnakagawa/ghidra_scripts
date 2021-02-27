import generic.constraint
import ghidra.program.model.listing
import ghidra.util.constraint
import java.lang


class PropertyConstraint(ghidra.util.constraint.ProgramConstraint):




    def __init__(self): ...



    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode: ...

    def getName(self) -> unicode:
        """
        Returns the name of the constraint.  Note: this name is also the XML tag used in the
         constraints specification files.
        @return the name of the constraint
        """
        ...

    def hashCode(self) -> int: ...

    @overload
    def isSatisfied(self, program: ghidra.program.model.listing.Program) -> bool: ...

    @overload
    def isSatisfied(self, t: object) -> bool:
        """
        Returns true if the given object satisfies this constraint.
        @param t the object to test this constraint on.
        @return true if the given object satisfies this constraint.
        """
        ...

    def loadConstraintData(self, data: generic.constraint.ConstraintData) -> None: ...

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
    def description(self) -> unicode: ...
