from typing import List
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.program.model.symbol
import java.lang


class StackFrame(object):
    """
    Definition of a stack frame.
     All offsets into a stack are from a zero base.  Usually
     negative offsets are parameters and positive offsets are
     locals.  That does not have to be the case, it depends on whether
     the stack grows positively or negatively.  On an a 80x86 architecture,
     the stack grows negatively.  When a value is pushed onto the stack,
     the stack pointer is decremented by some size.

     Each frame consists of a local sections, parameter section, and save
     information (return address, saved registers, etc...).  A frame is said to
     grow negative if the parameters are referenced with negative offsets from 0,
     or positive if the parameters are referenced with negative offsets from 0.



      Negative Growth
                        -5      local2 (2 bytes)
                        -3      local1 (4 bytes)
       frame base        0      stuff (4 bytes)
       return offset     4      return addr (4 bytes)
       param offset      8      param2 (4 bytes)
                        12      param1


      Positive Growth
                       -15     param offset 1
                       -11     param offset 2
       param offset     -8
       return offset    -7     return address
                        -3     stuff
       frame base        0     local 1
                         4     local 2
                         8

    """

    GROWS_NEGATIVE: int = -1
    GROWS_POSITIVE: int = 1
    UNKNOWN_PARAM_OFFSET: int = 131072







    def clearVariable(self, offset: int) -> None:
        """
        Clear the stack variable defined at offset
        @param offset Offset onto the stack to be cleared.
        """
        ...

    def createVariable(self, name: unicode, offset: int, dataType: ghidra.program.model.data.DataType, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.listing.Variable:
        """
        Create a stack variable.  It could be a parameter or a local depending
         on the direction of the stack.
         <p><B>WARNING!</B> Use of this method to add parameters may force the function
         to use custom variable storage.  In addition, parameters may be appended even if the
         current calling convention does not support them.
        @throws DuplicateNameException if another variable(parameter or local) already
         exists in the function with that name.
        @throws InvalidInputException if data type is not a fixed length or variable name is invalid.
        @throws VariableSizeException if data type size is too large based upon storage constraints.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

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
         This could return null if the stack frame isn't part of a function.
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
        Get all defined parameters as stack variables.
        @return an array of parameters.
        """
        ...

    def getReturnAddressOffset(self) -> int:
        """
        Get the return address stack offset.
        @return return address offset.
        """
        ...

    def getStackVariables(self) -> List[ghidra.program.model.listing.Variable]:
        """
        Get all defined stack variables.
         Variables are returned from least offset (-) to greatest offset (+)
        @return an array of parameters.
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
        Returns true if specified offset could correspond to a parameter
        @param offset
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
        Set the return address stack offset.
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

    @property
    def frameSize(self) -> int: ...

    @property
    def function(self) -> ghidra.program.model.listing.Function: ...

    @property
    def localSize(self) -> int: ...

    @localSize.setter
    def localSize(self, value: int) -> None: ...

    @property
    def locals(self) -> List[ghidra.program.model.listing.Variable]: ...

    @property
    def parameterOffset(self) -> int: ...

    @property
    def parameterSize(self) -> int: ...

    @property
    def parameters(self) -> List[ghidra.program.model.listing.Variable]: ...

    @property
    def returnAddressOffset(self) -> int: ...

    @returnAddressOffset.setter
    def returnAddressOffset(self, value: int) -> None: ...

    @property
    def stackVariables(self) -> List[ghidra.program.model.listing.Variable]: ...
