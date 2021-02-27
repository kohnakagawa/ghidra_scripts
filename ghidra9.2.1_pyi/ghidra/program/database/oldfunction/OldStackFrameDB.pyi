from typing import List
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.program.model.symbol
import java.lang


class OldStackFrameDB(object, ghidra.program.model.listing.StackFrame):








    def clearVariable(self, offset: int) -> None:
        """
        Clear the stack variable defined at offset
        @param offset Offset onto the stack to be cleared.
        """
        ...

    def createVariable(self, name: unicode, offset: int, dataType: ghidra.program.model.data.DataType, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.listing.Variable:
        """
        @see ghidra.program.model.listing.StackFrame#createVariable(java.lang.String, int, ghidra.program.model.data.DataType, ghidra.program.model.symbol.SourceType)
        """
        ...

    def equals(self, obj: object) -> bool:
        """
        Returns whether some other stack frame is "equivalent to" this one.
         The stack frame is considered equal to another even if they are each
         part of a different function.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFrameSize(self) -> int:
        """
        Get the size of this stack frame in bytes.
        @return stack frame size
        """
        ...

    def getFunction(self) -> ghidra.program.model.listing.Function:
        """
        Get the function that this stack belongs to.
        @return the function
        """
        ...

    def getLocalSize(self) -> int:
        """
        Get the local portion of the stack frame in bytes.
        @return local frame size
        """
        ...

    def getLocals(self) -> List[ghidra.program.model.listing.Variable]:
        """
        Get all defined local variables.
        @return an array of all local variables
        """
        ...

    def getParameterOffset(self) -> int:
        """
        Get the offset to the start of the parameters.
        @return offset
        """
        ...

    def getParameterSize(self) -> int:
        """
        Get the parameter portion of the stack frame in bytes.
        @return parameter frame size
        """
        ...

    def getParameters(self) -> List[ghidra.program.model.listing.Variable]:
        """
        Get all defined parameters.
        @return an array of parameters.
        """
        ...

    def getReturnAddressOffset(self) -> int:
        """
        Get the stack variable containing offset.  This may fall in
         the middle of a defined variable.
        @param offset offset of on stack to get variable.
        """
        ...

    def getStackVariables(self) -> List[ghidra.program.model.listing.Variable]:
        """
        @see ghidra.program.model.listing.StackFrame#getStackVariables()
        """
        ...

    def getVariableContaining(self, offset: int) -> ghidra.program.model.listing.Variable:
        """
        Get the stack variable containing offset.  This may fall in
         the middle of a defined variable.
        @param offset offset of on stack to get variable.
        """
        ...

    def growsNegative(self) -> bool:
        """
        A stack that grows negative has local references negative and
         parameter references positive.  A positive growing stack has
         positive locals and negative parameters.
        @return true if the stack grows in a negative direction.
        """
        ...

    def hashCode(self) -> int: ...

    def isParameterOffset(self, offset: int) -> bool:
        """
        @param offset
        @return boolean
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setLocalSize(self, size: int) -> None:
        """
        Set the size of the local stack in bytes.
        @param size size of local stack
        """
        ...

    def setReturnAddressOffset(self, offset: int) -> None:
        """
        Set the return address stack size.
        @param offset offset of return address.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
