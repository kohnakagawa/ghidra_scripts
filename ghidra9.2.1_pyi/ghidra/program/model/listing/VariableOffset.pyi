from typing import List
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.scalar
import java.lang


class VariableOffset(object):
    """
    VariableOffset can be used as an operand or sub-operand representation
     object.  The toString() method should be used to obtain the displayable representation
     string.  This object is intended to correspond to a explicit or implicit register/stack
     variable reference.  If an offset other than 0 is specified, the original Scalar should
     be specified.
    """





    @overload
    def __init__(self, ref: ghidra.program.model.symbol.Reference, var: ghidra.program.model.listing.Variable):
        """
        Constructor for an explicit variable reference.
        @param ref the reference
        @param var the variable being referenced
        """
        ...

    @overload
    def __init__(self, variable: ghidra.program.model.listing.Variable, offset: long, indirect: bool, dataAccess: bool):
        """
        Constructor for an implied variable reference.
        @param variable function variable
        @param offset offset into variable
        @param indirect if true and variable data-type is a pointer, the offset
         is relative to underlying data-type of the pointer-type.  This should generally be
         true for register use which would contain a structure pointer not a structure instance,
         whereas it would be false for stack-references.
        @param dataAccess true if content of variable is being read and/or written
        """
        ...



    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataTypeDisplayText(self) -> unicode:
        """
        Returns the data type access portion of this variable offset as a string
        @return the text
        """
        ...

    def getObjects(self) -> List[object]:
        """
        Get list of markup objects
        @return list of markup objects
        """
        ...

    def getOffset(self) -> long: ...

    def getReplacedElement(self) -> object:
        """
        Returns the Scalar or Register sub-operand replaced by this VariableOffset object.
        @return object or null
        """
        ...

    def getVariable(self) -> ghidra.program.model.listing.Variable: ...

    def hashCode(self) -> int: ...

    def isDataAccess(self) -> bool: ...

    def isIndirect(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def setReplacedElement(self, reg: ghidra.program.model.lang.Register) -> None:
        """
        Sets the original replaced sub-operand Register.
        """
        ...

    @overload
    def setReplacedElement(self, s: ghidra.program.model.scalar.Scalar, includeScalarAdjustment: bool) -> None:
        """
        Sets the original replaced sub-operand Scalar.
        @param s scalar
        @param includeScalarAdjustment if true scalar adjustment will be included
         with object list or string representation
        """
        ...

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
    def dataAccess(self) -> bool: ...

    @property
    def dataTypeDisplayText(self) -> unicode: ...

    @property
    def indirect(self) -> bool: ...

    @property
    def objects(self) -> List[object]: ...

    @property
    def offset(self) -> long: ...

    @property
    def replacedElement(self) -> object: ...

    @property
    def variable(self) -> ghidra.program.model.listing.Variable: ...
