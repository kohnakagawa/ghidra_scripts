from typing import List
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.program.model.symbol
import java.lang


class StackFrameImpl(object, ghidra.program.model.listing.StackFrame):
    """
    Implements a simple stack frame for a function.  Each frame consists of a
     local sections, parameter section, and save information (return address,
     saved registers).

      When a frame is created, the parameter stack start offset must be set up.
     If the parameter start is = 0, then the stack grows in the negative
     direction. If the parameter start  0, then the stack grows in the positive
     direction. When a frame is created the parameter start offset must be
     specified. Later the parameter start offset can be changed, but it must
     remain positive/negative if the frame was created with a positive/negative
     value.

     WARNING! This implementation is deficient and is only used by the UndefinedFunction
     implementation
    """









    def clearVariable(self, offset: int) -> None: ...

    def createVariable(self, name: unicode, offset: int, dataType: ghidra.program.model.data.DataType, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.listing.Variable:
        """
        Create a new stack variable.

         Specified source is always ignored
         and the variable instance returned will never be a parameter.
        @see ghidra.program.model.listing.StackFrame#createVariable(String, int, DataType, SourceType)
        """
        ...

    def equals(self, obj: object) -> bool:
        """
        Returns whether some other stack frame is "equivalent to" this one.
         The stack frame is considered equal to another even if they are each
         part of a different function.
        @param obj the object to compare for equality.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFrameSize(self) -> int: ...

    def getFunction(self) -> ghidra.program.model.listing.Function: ...

    def getLocalSize(self) -> int: ...

    def getLocals(self) -> List[ghidra.program.model.listing.Variable]: ...

    def getParameterOffset(self) -> int: ...

    def getParameterSize(self) -> int: ...

    def getParameters(self) -> List[ghidra.program.model.listing.Variable]: ...

    def getReturnAddressOffset(self) -> int: ...

    def getStackVariables(self) -> List[ghidra.program.model.listing.Variable]: ...

    def getVariableContaining(self, offset: int) -> ghidra.program.model.listing.Variable: ...

    def growsNegative(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isParameterOffset(self, offset: int) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setLocalSize(self, size: int) -> None: ...

    def setReturnAddressOffset(self, offset: int) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
