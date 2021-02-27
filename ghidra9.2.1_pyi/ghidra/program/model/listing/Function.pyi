from typing import List
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.listing.Function
import ghidra.program.model.symbol
import ghidra.util.task
import java.lang
import java.util


class Function(ghidra.program.model.symbol.Namespace, object):
    """
    Interface to define methods available on a function. Functions
     have a single entry point.
    """

    DEFAULT_CALLING_CONVENTION_STRING: unicode = u'default'
    DEFAULT_LOCAL_PREFIX: unicode = u'local_'
    DEFAULT_LOCAL_PREFIX_LEN: int = 6
    DEFAULT_LOCAL_RESERVED_PREFIX: unicode = u'local_res'
    DEFAULT_LOCAL_TEMP_PREFIX: unicode = u'temp_'
    DEFAULT_PARAM_PREFIX: unicode = u'param_'
    DEFAULT_PARAM_PREFIX_LEN: int = 6
    DELIMITER: unicode = u'::'
    GLOBAL_NAMESPACE_ID: long = 0x0L
    INLINE: unicode = u'inline'
    INVALID_STACK_DEPTH_CHANGE: int = 2147483646
    NAMESPACE_DELIMITER: unicode = u'::'
    NORETURN: unicode = u'noreturn'
    RETURN_PTR_PARAM_NAME: unicode = u'__return_storage_ptr__'
    THIS_PARAM_NAME: unicode = u'this'
    THUNK: unicode = u'thunk'
    UNKNOWN_CALLING_CONVENTION_STRING: unicode = u'unknown'
    UNKNOWN_STACK_DEPTH_CHANGE: int = 2147483647




    class FunctionUpdateType(java.lang.Enum):
        CUSTOM_STORAGE: ghidra.program.model.listing.Function.FunctionUpdateType = CUSTOM_STORAGE
        DYNAMIC_STORAGE_ALL_PARAMS: ghidra.program.model.listing.Function.FunctionUpdateType = DYNAMIC_STORAGE_ALL_PARAMS
        DYNAMIC_STORAGE_FORMAL_PARAMS: ghidra.program.model.listing.Function.FunctionUpdateType = DYNAMIC_STORAGE_FORMAL_PARAMS







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.program.model.listing.Function.FunctionUpdateType: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.program.model.listing.Function.FunctionUpdateType]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...







    def addLocalVariable(self, var: ghidra.program.model.listing.Variable, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.listing.Variable:
        """
        Adds a local variable to the function.
         The {@link VariableUtilities#checkVariableConflict(Function, Variable, VariableStorage, boolean)}
         method may be used to check and remove conflicting variables which already exist in the function.
        @param var the variable to add.
        @param source the source of this local variable
        @return the Variable added to the program.
        @throws DuplicateNameException if another local variable or parameter already
         has that name.
        """
        ...

    def addParameter(self, var: ghidra.program.model.listing.Variable, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.listing.Parameter:
        """
        Adds the given variable to the end of the parameters list.  The variable storage specified
         for the new parameter will be ignored if custom storage mode is not enabled.
         The {@link VariableUtilities#checkVariableConflict(Function, Variable, VariableStorage, boolean)}
         method may be used to check and remove conflicting variables which already exist in the function.
        @param var the variable to add as a new parameter.
        @param source the source of this parameter which will be applied to the parameter symbol and
         overall function signature source.  If parameter has a null or default name a SourceType of DEFAULT
         will be applied to the parameter symbol.
        @return the Parameter object created.
        @throws DuplicateNameException if another variable(parameter or local) already
         exists in the function with that name.
        @throws InvalidInputException if data type is not a fixed length or variable name is invalid.
        @throws VariableSizeException if data type size is too large based upon storage constraints.
        @deprecated The use of this method is discouraged due to the potential injection of auto-parameters
         which are easily overlooked when considering parameter ordinal.  The function signature should generally be
         adjusted with a single call to {@link #updateFunction(String, Variable, List, FunctionUpdateType, boolean, SourceType)}
        """
        ...

    def addTag(self, name: unicode) -> bool:
        """
        Adds the tag with the given name to this function; if one does
         not exist, one is created.
        @param name the tag name to add
        @return true if the tag was successfully added
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAllVariables(self) -> List[ghidra.program.model.listing.Variable]:
        """
        Returns an array of all local and parameter variables
        @return
        """
        ...

    def getAutoParameterCount(self) -> int:
        """
        Gets the number of auto-parameters for this function also included in the total
         count provided by {@link #getParameterCount()}.  This number will always be 0 when
         custom parameter storage is used.
        @return the number of auto-parameters
        """
        ...

    def getBody(self) -> ghidra.program.model.address.AddressSetView: ...

    def getCallFixup(self) -> unicode:
        """
        Returns the current call-fixup name set on this instruction or null
         if one has not been set.
        """
        ...

    def getCalledFunctions(self, monitor: ghidra.util.task.TaskMonitor) -> java.util.Set:
        """
        Returns a set of functions that this function calls.
        @param monitor The monitor that is used to report progress and allow for canceling of
                        the search.  May be null.
        @return a set of functions that this function calls.
        """
        ...

    def getCallingConvention(self) -> ghidra.program.model.lang.PrototypeModel:
        """
        Gets the calling convention prototype model for this function.
        @return the prototype model of the function's current calling convention or null.
        """
        ...

    def getCallingConventionName(self) -> unicode:
        """
        Gets the calling convention's name for this function.
        @return the name of the calling convention
         or Function.DEFAULT_CALLING_CONVENTION_STRING
         (i.e. "default", if the calling convention has been set to the default for this function)
         or Function.UNKNOWN_CALLING_CONVENTION_STRING
         (i.e. "unknown", if no calling convention is specified for this function).
        """
        ...

    def getCallingFunctions(self, monitor: ghidra.util.task.TaskMonitor) -> java.util.Set:
        """
        Returns a set of functions that call this function.
        @param monitor The monitor that is used to report progress and allow for canceling of
                        the search.  May be null.
        @return a set of functions that call this function.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self) -> unicode:
        """
        Get the comment for this function.
        @return the comment for this function
        """
        ...

    def getCommentAsArray(self) -> List[unicode]:
        """
        Returns the function (same as plate) comment as an array of strings where
         each item in the array is a line of text in the comment.
        """
        ...

    def getDefaultCallingConventionName(self) -> unicode:
        """
        Gets the name of the default calling convention.
         <br>Note: The name in the PrototypeModel of the default calling convention may be null.
        @return the name of the default calling convention.
        """
        ...

    def getEntryPoint(self) -> ghidra.program.model.address.Address:
        """
        Get the entry point for this function.
         Functions may only have ONE entry point.
        @return the entry point
        """
        ...

    def getExternalLocation(self) -> ghidra.program.model.symbol.ExternalLocation:
        """
        @return if this is an external function return the associated external location object.
        """
        ...

    def getFunctionThunkAddresses(self) -> List[ghidra.program.model.address.Address]:
        """
        If this function is "Thunked", an array of Thunk Function entry points is returned
        @return associated thunk function entry points or null if this is not a "Thunked" function.
        """
        ...

    def getID(self) -> long: ...

    @overload
    def getLocalVariables(self) -> List[ghidra.program.model.listing.Variable]:
        """
        Get all local function variables
        @return all local function variables
        """
        ...

    @overload
    def getLocalVariables(self, filter: ghidra.program.model.listing.VariableFilter) -> List[ghidra.program.model.listing.Variable]:
        """
        Get all local function variables which satisfy the specified filter
        @param filter variable filter or null for all local variables to be returned
        @return all function variables which satisfy the specified filter
        """
        ...

    @overload
    def getName(self) -> unicode:
        """
        Get the name of this function.
        @return the functions name
        """
        ...

    @overload
    def getName(self, __a0: bool) -> unicode: ...

    def getParameter(self, ordinal: int) -> ghidra.program.model.listing.Parameter:
        """
        Returns the specified parameter including an auto-param at the specified ordinal.
        @param ordinal the index of the parameter to return.
        @return parameter or null if ordinal is out of range
        """
        ...

    def getParameterCount(self) -> int:
        """
        Gets the total number of parameters for this function.  This number also includes any
         auto-parameters which may have been injected when dynamic parameter storage is used.
        @return the total number of parameters
        """
        ...

    @overload
    def getParameters(self) -> List[ghidra.program.model.listing.Parameter]:
        """
        Get all function parameters
        @return all function parameters
        """
        ...

    @overload
    def getParameters(self, filter: ghidra.program.model.listing.VariableFilter) -> List[ghidra.program.model.listing.Parameter]:
        """
        Get all function parameters which satisfy the specified filter
        @param filter variable filter or null for all parameters to be returned
        @return all function parameters which satisfy the specified filter
        """
        ...

    def getParentNamespace(self) -> ghidra.program.model.symbol.Namespace: ...

    def getProgram(self) -> ghidra.program.model.listing.Program:
        """
        Get the program containing this function.
        @return the program
        """
        ...

    def getPrototypeString(self, formalSignature: bool, includeCallingConvention: bool) -> unicode:
        """
        Return a string representation of the function signature
        @param formalSignature if true only original raw return/parameter types will be retained and
         auto-params discarded (e.g., this, __return_storage_ptr__, etc.) within the returned
         signature.  If false, the effective signature will be returned where forced indirect
         and auto-params are reflected in the signature.  This option has no affect if the specified
         function has custom storage enabled.
        @param includeCallingConvention if true prototype will include call convention
         declaration if known.
        """
        ...

    def getRepeatableComment(self) -> unicode:
        """
        Returns the repeatable comment for this function.
         A repeatable comment is a comment that will appear
         at locations that 'call' this function.
        @return the repeatable comment for this function
        """
        ...

    def getRepeatableCommentAsArray(self) -> List[unicode]:
        """
        Returns the repeatable comment as an array of strings.
        @return the repeatable comment as an array of strings
        """
        ...

    def getReturn(self) -> ghidra.program.model.listing.Parameter:
        """
        Get the Function's return type/storage represented by a Parameter
         object.  The parameter's ordinal value will be equal to
         Parameter.RETURN_ORIDINAL.
        @return return data-type/storage
        """
        ...

    def getReturnType(self) -> ghidra.program.model.data.DataType:
        """
        Get the Function's return type.
         A null return value indicates the functions return type has never been set.
        @return the DataType that this function returns.
        """
        ...

    @overload
    def getSignature(self) -> ghidra.program.model.listing.FunctionSignature:
        """
        Get the function's effective signature.
         This is equivalent to invoking <code>getSignature(false)</code> where auto-params and
         forced-indirect types will be reflected in the signature if present.
         <br><br>WARNING! It is important to note that the calling convention may not be properly retained
         by the returned signature object if a non-generic calling convention is used by this function as
         defined by the program's compiler specification.
        @return the function's signature
        """
        ...

    @overload
    def getSignature(self, formalSignature: bool) -> ghidra.program.model.listing.FunctionSignature:
        """
        Get the function's signature.
         <br><br>WARNING! It is important to note that the calling convention may not be properly retained
         by the returned signature object if a non-generic calling convention is used by this function as
         defined by the program's compiler specification.
        @param formalSignature if true only original raw types will be retained and
         auto-params discarded (e.g., this, __return_storage_ptr__, etc.) within the returned
         signature.  If false, the effective signature will be returned where forced indirect
         and auto-params are reflected in the signature.  This option has no affect if the specified
         function has custom storage enabled.
        @return the function's signature
        """
        ...

    def getSignatureSource(self) -> ghidra.program.model.symbol.SourceType:
        """
        Returns the source type for the overall signature excluding function name and parameter names
         whose source is carried by the corresponding symbol.
        @return the overall SourceType of the function signature;
        """
        ...

    def getStackFrame(self) -> ghidra.program.model.listing.StackFrame:
        """
        Get the stack frame for this function.
         NOTE: Use of the stack frame must be avoided during upgrade activity since
         the compiler spec may not be known (i.e., due to language upgrade process).
        @return this functions stack frame
        """
        ...

    def getStackPurgeSize(self) -> int:
        """
        Get the change in the stack pointer resulting from calling
          this function.
        @return int the change in bytes to the stack pointer
        """
        ...

    def getSymbol(self) -> ghidra.program.model.symbol.Symbol: ...

    def getTags(self) -> java.util.Set:
        """
        Return all {@link FunctionTag} objects associated with this function.
        @return set of tag names
        """
        ...

    def getThunkedFunction(self, recursive: bool) -> ghidra.program.model.listing.Function:
        """
        If this function is a Thunk, this method returns the referenced function.
        @param recursive if true and the thunked-function is a thunk itself, the returned
         thunked-function will be the final thunked-function which will never be a thunk.
        @return function referenced by this Thunk Function or null if this is not a Thunk
         function
        """
        ...

    def getVariables(self, filter: ghidra.program.model.listing.VariableFilter) -> List[ghidra.program.model.listing.Variable]:
        """
        Get all function variables which satisfy the specified filter
        @param filter variable filter or null for all variables to be returned
        @return all function variables which satisfy the specified filter
        """
        ...

    def hasCustomVariableStorage(self) -> bool:
        """
        @return true if function parameters utilize custom variable storage.
        """
        ...

    def hasNoReturn(self) -> bool:
        """
        @return true if this function does not return.
        """
        ...

    def hasVarArgs(self) -> bool:
        """
        Returns true if this function has a variable argument list (VarArgs).
        """
        ...

    def hashCode(self) -> int: ...

    def insertParameter(self, ordinal: int, var: ghidra.program.model.listing.Variable, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.listing.Parameter:
        """
        Inserts the given variable into the parameters list.  The variable storage specified
         for the new parameter will be ignored if custom storage mode is not enabled.
         The {@link VariableUtilities#checkVariableConflict(Function, Variable, VariableStorage, boolean)}
         method may be used to check and remove conflicting variables which already exist in the function.
        @param ordinal the position with the parameters to insert to.  This ordinal must factor in the
         presence of auto-parameters which may be injected dynamically based upon calling convention and
         return data type.  Parameters may not be inserted befor an auto-parameter.
        @param var the variable to add as a new parameter.
        @param source the source of this parameter which will be applied to the parameter symbol and
         overall function signature source.  If parameter has a null or default name a SourceType of DEFAULT
         will be applied to the parameter symbol.
        @return the Parameter object created.
        @throws DuplicateNameException if another variable(parameter or local) already
         exists in the function with that name.
        @throws InvalidInputException if data type is not a fixed length or variable name is invalid.
        @throws VariableSizeException if data type size is too large based upon storage constraints.
        @deprecated The use of this method is discouraged due to the potential injection of auto-parameters
         which are easily overlooked when considering parameter ordinal.  The function signature should generally be
         adjusted with a single call to {@link #updateFunction(String, Variable, List, FunctionUpdateType, boolean, SourceType)}
        """
        ...

    def isExternal(self) -> bool:
        """
        @return true if this function is external (i.e., entry point is in EXTERNAL address space)
        """
        ...

    def isGlobal(self) -> bool: ...

    def isInline(self) -> bool:
        """
        @return true if this is an inline function.
        """
        ...

    def isStackPurgeSizeValid(self) -> bool:
        """
        check if stack purge size is valid.
        @return true if the stack depth is valid
        """
        ...

    def isThunk(self) -> bool:
        """
        @return true if this function is a Thunk and has a referenced Thunked Function.
        @see #getThunkedFunction(boolean)
        """
        ...

    def moveParameter(self, fromOrdinal: int, toOrdinal: int) -> ghidra.program.model.listing.Parameter:
        """
        Move the parameter which occupies the fromOrdinal position to the toOrdinal position.
         Parameters will be renumbered to reflect the new ordering.  Auto-parameters may not be
         moved but must be accounted for in the specified ordinals.
        @param fromOrdinal from ordinal position using the current numbering
        @param toOrdinal the final position of the specified parameter
        @return parameter which was moved
        @deprecated The use of this method is discouraged.  The function signature should generally be
         adjusted with a single call to {@link #updateFunction(String, Variable, List, FunctionUpdateType, boolean, SourceType)}
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def promoteLocalUserLabelsToGlobal(self) -> None:
        """
        Changes all local user-defined labels for this function to global symbols. If a
         global code symbol already exists with the same name at the symbols address the
         symbol will be removed.
        """
        ...

    def removeParameter(self, ordinal: int) -> None:
        """
        Remove the specified parameter.  Auto-parameters may not be removed but must be accounted
         for in the specified ordinal.
        @param ordinal the index of the parameter to be removed.
        @deprecated The use of this method is discouraged.  The function signature should generally be
         adjusted with a single call to {@link #updateFunction(String, Variable, List, FunctionUpdateType, boolean, SourceType)}
        """
        ...

    def removeTag(self, name: unicode) -> None:
        """
        Removes the given tag from this function.
        @param name the tag name to be removed.
        """
        ...

    def removeVariable(self, var: ghidra.program.model.listing.Variable) -> None:
        """
        Removes the given variable from the function.
        @param var the variable to remove.
        """
        ...

    @overload
    def replaceParameters(self, __a0: List[object], __a1: ghidra.program.model.listing.Function.FunctionUpdateType, __a2: bool, __a3: ghidra.program.model.symbol.SourceType) -> None: ...

    @overload
    def replaceParameters(self, updateType: ghidra.program.model.listing.Function.FunctionUpdateType, force: bool, source: ghidra.program.model.symbol.SourceType, params: List[ghidra.program.model.listing.Variable]) -> None:
        """
        Replace all current parameters with the given list of parameters.
         The {@link VariableUtilities#checkVariableConflict(Function, Variable, VariableStorage, boolean)}
         method may be used to check and remove conflicting variables which already exist in the function.
        @param updateType function update type
        @param force if true any conflicting local parameters will be removed
        @param source the source of these parameters which will be applied to the parameter symbols and
         overall function signature source.  If parameter names are null or a default name a SourceType of DEFAULT
         will be applied to the corresponding parameter symbol.
        @param params the new parameters for the function.
        @throws DuplicateNameException if another variable(parameter or local) already
         exists in the function with that name.
        @throws InvalidInputException if a parameter data type is not a fixed length or variable name is invalid.
        @throws VariableSizeException if a parameter data type size is too large based upon storage constraints
         or conflicts with another variable.
        """
        ...

    def setBody(self, newBody: ghidra.program.model.address.AddressSetView) -> None:
        """
        Set the new body for this function. The entry point must be contained
         in the new body.
        @param newBody address set to use as the body of this function
        @throws OverlappingFunctionException if the address set overlaps that
         of another function
        """
        ...

    def setCallFixup(self, name: unicode) -> None:
        """
        Set the named call-fixup for this function.
        @param name name of call-fixup specified by compiler spec.  A null
         value will clear the current setting.
        """
        ...

    def setCallingConvention(self, name: unicode) -> None:
        """
        Sets the calling convention for this function to the named calling convention.
        @param name the name of the calling convention. "unknown" and "default" are reserved names
         that can also be used here.
         <br>Null or Function.UNKNOWN_CALLING_CONVENTION_STRING sets this function to not have a
         calling convention (i.e. unknown).
         <br>Function.DEFAULT_CALLING_CONVENTION_STRING sets this function to use the default calling
         convention. (i.e. default)
        @throws InvalidInputException if the specified name is not a recognized calling convention name.
        """
        ...

    def setComment(self, comment: unicode) -> None:
        """
        Set the comment for this function.
        @param comment the string to set as the comment.
        """
        ...

    def setCustomVariableStorage(self, hasCustomVariableStorage: bool) -> None:
        """
        Set whether or not this function uses custom variable storage
        @param hasCustomVariableStorage
        """
        ...

    def setInline(self, isInline: bool) -> None:
        """
        Sets whether or not this function is inline.
        @param isInline true if this is an inline function.
        """
        ...

    def setName(self, name: unicode, source: ghidra.program.model.symbol.SourceType) -> None:
        """
        Set the name of this function.
        @param name the new name of the function
        @param source the source of this function name
        @throws DuplicateNameException if the name is used by some other symbol
        @throws InvalidInputException if the name is not a valid function name.
        """
        ...

    def setNoReturn(self, hasNoReturn: bool) -> None:
        """
        Set whether or not this function has a return.
        @param hasNoReturn true if this function does not return.
        """
        ...

    def setParentNamespace(self, __a0: ghidra.program.model.symbol.Namespace) -> None: ...

    def setRepeatableComment(self, comment: unicode) -> None:
        """
        Set the repeatable comment for this function.
        @param comment the string to set as the repeatable comment.
        """
        ...

    def setReturn(self, type: ghidra.program.model.data.DataType, storage: ghidra.program.model.listing.VariableStorage, source: ghidra.program.model.symbol.SourceType) -> None:
        """
        Set the return data-type and storage.
         <p>NOTE: The storage and source are ignored if the function does not have custom storage enabled.
        @param type
        @param storage
        @param source source to be combined with the overall signature source.
        @throws InvalidInputException if data type is not a fixed length or storage is improperly sized
        """
        ...

    def setReturnType(self, type: ghidra.program.model.data.DataType, source: ghidra.program.model.symbol.SourceType) -> None:
        """
        Set the function's return type.
        @param type the dataType that will define this functions return type.
        @param source TODO
        @throws InvalidInputException if data type is not a fixed length.
        """
        ...

    def setSignatureSource(self, signatureSource: ghidra.program.model.symbol.SourceType) -> None:
        """
        Set the source type for the overall signature excluding function name and parameter names
         whose source is carried by the corresponding symbol.
        @param signatureSource function signature source type
        """
        ...

    def setStackPurgeSize(self, purgeSize: int) -> None:
        """
        Set the change in the stack pointer resulting from calling
         this function.
        @param purgeSize the change in bytes to the stack pointer
        """
        ...

    def setThunkedFunction(self, thunkedFunction: ghidra.program.model.listing.Function) -> None:
        """
        Set the currently Thunked Function or null to convert to a normal function
        @param thunkedFunction the thunked function or null to convert this thunked function to a
         normal function.
        @throws IllegalArgumentException if an attempt is made to thunk a function or another
         thunk which would result in a loop back to this function or if this function is an external
         function, or specified function is from a different program instance.
        """
        ...

    def setVarArgs(self, hasVarArgs: bool) -> None:
        """
        Set whether parameters can be passed as a VarArg (variable argument list).
        @param hasVarArgs true if this function has a variable argument list (ie printf(fmt, ...)).
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def updateFunction(self, __a0: unicode, __a1: ghidra.program.model.listing.Variable, __a2: List[object], __a3: ghidra.program.model.listing.Function.FunctionUpdateType, __a4: bool, __a5: ghidra.program.model.symbol.SourceType) -> None: ...

    @overload
    def updateFunction(self, callingConvention: unicode, returnValue: ghidra.program.model.listing.Variable, updateType: ghidra.program.model.listing.Function.FunctionUpdateType, force: bool, source: ghidra.program.model.symbol.SourceType, newParams: List[ghidra.program.model.listing.Variable]) -> None:
        """
        Replace all current parameters with the given list of parameters and optionally change the calling convention
         and function return.
         The {@link VariableUtilities#checkVariableConflict(Function, Variable, VariableStorage, boolean)}
         method may be used to check and remove conflicting variables which already exist in the function.
        @param callingConvention updated calling convention name or null if no change is required
        @param returnValue return variable or null if no change required
        @param updateType function update type
        @param force if true any conflicting local parameters will be removed
        @param source the source of these parameters which will be applied to the parameter symbols and
         overall function signature source.  If parameter names are null or a default name a SourceType of DEFAULT
         will be applied to the corresponding parameter symbol.
        @param newParams a variable number of parameters for the function.
        @throws DuplicateNameException if another variable(parameter or local) already
         exists in the function with that name.
        @throws InvalidInputException if a parameter data type is not a fixed length or variable name is invalid.
        @throws VariableSizeException if a parameter data type size is too large based upon storage constraints
         or conflicts with another variable.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def ID(self) -> long: ...

    @property
    def allVariables(self) -> List[ghidra.program.model.listing.Variable]: ...

    @property
    def autoParameterCount(self) -> int: ...

    @property
    def body(self) -> ghidra.program.model.address.AddressSetView: ...

    @body.setter
    def body(self, value: ghidra.program.model.address.AddressSetView) -> None: ...

    @property
    def callFixup(self) -> unicode: ...

    @callFixup.setter
    def callFixup(self, value: unicode) -> None: ...

    @property
    def callingConvention(self) -> ghidra.program.model.lang.PrototypeModel: ...

    @property
    def callingConventionName(self) -> unicode: ...

    @property
    def comment(self) -> unicode: ...

    @comment.setter
    def comment(self, value: unicode) -> None: ...

    @property
    def commentAsArray(self) -> List[unicode]: ...

    @property
    def customVariableStorage(self) -> None: ...  # No getter available.

    @customVariableStorage.setter
    def customVariableStorage(self, value: bool) -> None: ...

    @property
    def defaultCallingConventionName(self) -> unicode: ...

    @property
    def entryPoint(self) -> ghidra.program.model.address.Address: ...

    @property
    def external(self) -> bool: ...

    @property
    def externalLocation(self) -> ghidra.program.model.symbol.ExternalLocation: ...

    @property
    def functionThunkAddresses(self) -> List[ghidra.program.model.address.Address]: ...

    @property
    def global(self) -> bool: ...

    @property
    def inline(self) -> bool: ...

    @inline.setter
    def inline(self, value: bool) -> None: ...

    @property
    def localVariables(self) -> List[ghidra.program.model.listing.Variable]: ...

    @property
    def name(self) -> unicode: ...

    @property
    def noReturn(self) -> None: ...  # No getter available.

    @noReturn.setter
    def noReturn(self, value: bool) -> None: ...

    @property
    def parameterCount(self) -> int: ...

    @property
    def parameters(self) -> List[ghidra.program.model.listing.Parameter]: ...

    @property
    def parentNamespace(self) -> ghidra.program.model.symbol.Namespace: ...

    @parentNamespace.setter
    def parentNamespace(self, value: ghidra.program.model.symbol.Namespace) -> None: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...

    @property
    def repeatableComment(self) -> unicode: ...

    @repeatableComment.setter
    def repeatableComment(self, value: unicode) -> None: ...

    @property
    def repeatableCommentAsArray(self) -> List[unicode]: ...

    @property
    def return(self) -> ghidra.program.model.listing.Parameter: ...

    @property
    def returnType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def signature(self) -> ghidra.program.model.listing.FunctionSignature: ...

    @property
    def signatureSource(self) -> ghidra.program.model.symbol.SourceType: ...

    @signatureSource.setter
    def signatureSource(self, value: ghidra.program.model.symbol.SourceType) -> None: ...

    @property
    def stackFrame(self) -> ghidra.program.model.listing.StackFrame: ...

    @property
    def stackPurgeSize(self) -> int: ...

    @stackPurgeSize.setter
    def stackPurgeSize(self, value: int) -> None: ...

    @property
    def stackPurgeSizeValid(self) -> bool: ...

    @property
    def symbol(self) -> ghidra.program.model.symbol.Symbol: ...

    @property
    def tags(self) -> java.util.Set: ...

    @property
    def thunk(self) -> bool: ...

    @property
    def thunkedFunction(self) -> None: ...  # No getter available.

    @thunkedFunction.setter
    def thunkedFunction(self, value: ghidra.program.model.listing.Function) -> None: ...

    @property
    def varArgs(self) -> None: ...  # No getter available.

    @varArgs.setter
    def varArgs(self, value: bool) -> None: ...
