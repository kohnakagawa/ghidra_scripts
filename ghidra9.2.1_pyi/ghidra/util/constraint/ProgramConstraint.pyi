import generic.constraint
import ghidra.util.classfinder
import java.lang


class ProgramConstraint(generic.constraint.Constraint, ghidra.util.classfinder.ExtensionPoint):




    def __init__(self, name: unicode): ...



    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode:
        """
        Returns a description of this constraint (with its configuration data) to be used
         to journal the decision path that was taken.
        @return a description of this constraint with its configuration data.
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of the constraint.  Note: this name is also the XML tag used in the
         constraints specification files.
        @return the name of the constraint
        """
        ...

    def hashCode(self) -> int: ...

    def isSatisfied(self, t: object) -> bool:
        """
        Returns true if the given object satisfies this constraint.
        @param t the object to test this constraint on.
        @return true if the given object satisfies this constraint.
        """
        ...

    def loadConstraintData(self, data: generic.constraint.ConstraintData) -> None:
        """
        Initialized this constraint state.  Attributes in the xml element with this constaints
         tag name will be extracted into the ConstraintData object for easy retrieval.
        @param data the ConstraintData object used to initialize this constraint.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
