from typing import List
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.pcode
import ghidra.program.model.symbol
import java.lang


class Variable(java.lang.Comparable, object):
    """
    Defines an object that stores a value of some specific data type. The
     variable has a name, type, size, and a comment.
    """









    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self) -> unicode:
        """
        Get the Comment for this variable
        @return the comment
        """
        ...

    def getDataType(self) -> ghidra.program.model.data.DataType:
        """
        Get the Data Type of this variable
        @return the data type of the variable
        """
        ...

    def getFirstStorageVarnode(self) -> ghidra.program.model.pcode.Varnode:
        """
        Get the first storage varnode for this variable
        @return the first storage varnode associated with this variable
        @see #getVariableStorage()
        """
        ...

    def getFirstUseOffset(self) -> int:
        """
        @return the first use offset relative to the function entry point.
        """
        ...

    def getFunction(self) -> ghidra.program.model.listing.Function:
        """
        Returns the function that contains this Variable.  May be null if the variable is not in
         a function.
        """
        ...

    def getLastStorageVarnode(self) -> ghidra.program.model.pcode.Varnode:
        """
        Get the last storage varnode for this variable
        @return the last storage varnode associated with this variable
        @see #getVariableStorage()
        """
        ...

    def getLength(self) -> int:
        """
        Get the length of this variable
        @return the length of the variable
        """
        ...

    def getMinAddress(self) -> ghidra.program.model.address.Address:
        """
        @return the minimum address corresponding to the first varnode of this storage
         or null if this is a special empty storage: {@link VariableStorage#BAD_STORAGE},
         {@link VariableStorage#UNASSIGNED_STORAGE}, {@link VariableStorage#VOID_STORAGE}
        """
        ...

    def getName(self) -> unicode:
        """
        Get the Name of this variable or null if not assigned or not-applicable
        @return the name of the variable
        """
        ...

    def getProgram(self) -> ghidra.program.model.listing.Program:
        """
        Returns the program that contains this variable or is the intended target
        @return the program.
        """
        ...

    def getRegister(self) -> ghidra.program.model.lang.Register:
        """
        @return first storage register associated with this variable, else null is returned.
         A variable with compound storage may have more than one register or other storage
         in addition to the register returned by this method.
        @see #isRegisterVariable()
        """
        ...

    def getRegisters(self) -> List[ghidra.program.model.lang.Register]:
        """
        @return all storage register(s) associated with this variable, else null is returned if
         no registers are used.  A variable with compound storage may have more than one register
         or other storage in addition to the register(s) returned by this method.
        @see #isRegisterVariable()
        @see #isCompoundVariable()
        """
        ...

    def getSource(self) -> ghidra.program.model.symbol.SourceType:
        """
        Get the source of this variable
        @return the source of this variable
        """
        ...

    def getStackOffset(self) -> int:
        """
        @return the stack offset associated with simple stack variable (i.e., {@link #isStackVariable()}
         returns true).
        @throws UnsupportedOperationException if storage is not a simple stack variable
        """
        ...

    def getSymbol(self) -> ghidra.program.model.symbol.Symbol:
        """
        @return the symbol associated with this variable or null if no symbol
         associated.  Certain dynamic variables such as auto-parameters do not
         have a symbol.
        """
        ...

    def getVariableStorage(self) -> ghidra.program.model.listing.VariableStorage:
        """
        Get the variable storage associated with this variable.
        @return the variable storage for this variable
        """
        ...

    def hasAssignedStorage(self) -> bool:
        """
        @return true if this variable has been assigned storage.  This is equivalent to
         {@link #getVariableStorage()} != null
        """
        ...

    def hasStackStorage(self) -> bool:
        """
        @return true if this variable uses simple or compound storage which contains a stack element.
         If true, the last storage varnode will always be the stack element.
        @see #getLastStorageVarnode()
        """
        ...

    def hashCode(self) -> int: ...

    def isCompoundVariable(self) -> bool:
        """
        @return true if this variable uses compound storage consisting of two or more storage elements
         which will be returned by the {@link #getVariableStorage()} method.  Compound variables will
         always use a register(s) optionally followed by other storage (i.e., stack).
        """
        ...

    def isEquivalent(self, variable: ghidra.program.model.listing.Variable) -> bool:
        """
        @return true if the specified variable is equivalent to this variable
        """
        ...

    def isMemoryVariable(self) -> bool:
        """
        @return true if this is a simple variable consisting of a single storage memory element
         which will be returned by either the {@link #getFirstStorageVarnode()} or
         {@link #getVariableStorage()} methods.
        """
        ...

    def isRegisterVariable(self) -> bool:
        """
        @return true if this is a simple variable consisting of a single register varnode
         which will be returned by either the {@link #getFirstStorageVarnode()} or
         {@link getLastStorageVarnode()} methods.  The register can be obtained using the
         {@link #getRegister()} method.
        """
        ...

    def isStackVariable(self) -> bool:
        """
        @return true if this is a simple variable consisting of a single stack varnode
         which will be returned by either the {@link #getFirstStorageVarnode()} or
         {@link #getLastStorageVarnode()} methods. The stack offset can be obtained using:
         <pre>
         		getFirstStorageVarnode().getOffset()
          </pre>
        """
        ...

    def isUniqueVariable(self) -> bool:
        """
        @return true if this is a simple variable consisting of a single storage unique/hash element
         which will be returned by either the {@link #getFirstStorageVarnode()} or
         {@link #getVariableStorage()} methods.  The unique hash can be obtained from the
         storage address offset corresponding to the single storage element.
        """
        ...

    def isValid(self) -> bool:
        """
        Verify that the variable is valid
         (i.e., storage is valid and size matches variable data type size)
        @return true if variable is valid
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setComment(self, comment: unicode) -> None:
        """
        Set the comment for this variable
        @param comment the comment
        """
        ...

    @overload
    def setDataType(self, type: ghidra.program.model.data.DataType, source: ghidra.program.model.symbol.SourceType) -> None:
        """
        Set the Data Type of this variable using the default alignment behavior (implementation specific).
         The given dataType must have a fixed length.  If contained within a stack-frame, data-type size
         will be constrained by existing variables (e.g., equivalent to force=false)
         Note: stack offset will be maintained for stack variables.
        @param type the data type
        @param source signature source
        @throws InvalidInputException if data type is not a fixed length or violates storage constraints.
        @throws VariableSizeException if data type size causes a conflict with other variables
        @see #setDataType(DataType, boolean, boolean, SourceType)
        """
        ...

    @overload
    def setDataType(self, type: ghidra.program.model.data.DataType, alignStack: bool, force: bool, source: ghidra.program.model.symbol.SourceType) -> None:
        """
        Set the Data Type of this variable. The given dataType must have a fixed length.
        @param type the data type
        @param alignStack maintain proper stack alignment/justification if supported by implementation.
         			If false and this is a stack variable, the current stack address/offset will not change.
         			If true, the affect is implementation dependent since alignment can
         			not be performed without access to a compiler specification.
        @param force overwrite conflicting variables
        @param source signature source
        @throws InvalidInputException if data type is not a fixed length or violates storage constraints.
        @throws VariableSizeException if force is false and data type size causes a conflict
         with other variables
        """
        ...

    @overload
    def setDataType(self, type: ghidra.program.model.data.DataType, storage: ghidra.program.model.listing.VariableStorage, force: bool, source: ghidra.program.model.symbol.SourceType) -> None:
        """
        Set the Data Type of this variable and the associated storage whose size matches the
         data type length.
         <p>NOTE: The storage and source are ignored if the function does not have custom storage enabled.
        @param type the data type
        @param storage properly sized storage for the new data type
        @param force overwrite conflicting variables
        @param source variable storage source (used only for function parameters and return)
        @throws InvalidInputException if data type is not a fixed length or violates storage constraints.
        @throws VariableSizeException if force is false and data type size causes a conflict
         with other variables
        """
        ...

    def setName(self, name: unicode, source: ghidra.program.model.symbol.SourceType) -> None:
        """
        Set the name of this variable.
        @param name the name
        @param source the source of this variable name
        @throws DuplicateNameException if the name collides with the name of another variable.
        @throws InvalidInputException if name contains blank characters, is zero length, or is null
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
    def comment(self) -> unicode: ...

    @comment.setter
    def comment(self, value: unicode) -> None: ...

    @property
    def compoundVariable(self) -> bool: ...

    @property
    def dataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def firstStorageVarnode(self) -> ghidra.program.model.pcode.Varnode: ...

    @property
    def firstUseOffset(self) -> int: ...

    @property
    def function(self) -> ghidra.program.model.listing.Function: ...

    @property
    def lastStorageVarnode(self) -> ghidra.program.model.pcode.Varnode: ...

    @property
    def length(self) -> int: ...

    @property
    def memoryVariable(self) -> bool: ...

    @property
    def minAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def name(self) -> unicode: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...

    @property
    def register(self) -> ghidra.program.model.lang.Register: ...

    @property
    def registerVariable(self) -> bool: ...

    @property
    def registers(self) -> List[object]: ...

    @property
    def source(self) -> ghidra.program.model.symbol.SourceType: ...

    @property
    def stackOffset(self) -> int: ...

    @property
    def stackVariable(self) -> bool: ...

    @property
    def symbol(self) -> ghidra.program.model.symbol.Symbol: ...

    @property
    def uniqueVariable(self) -> bool: ...

    @property
    def valid(self) -> bool: ...

    @property
    def variableStorage(self) -> ghidra.program.model.listing.VariableStorage: ...
