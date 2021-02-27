from typing import List
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.listing.Function
import ghidra.program.model.symbol
import ghidra.util
import ghidra.util.task
import java.lang
import java.util


class UndefinedFunction(object, ghidra.program.model.listing.Function):
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



    def __init__(self, p: ghidra.program.model.listing.Program, entry: ghidra.program.model.address.Address):
        """
        Undefined Function constructor.
         Function will adopt the default calling convention prototype
         defined by the program's compiler specification.  The
         associated stack frame will also follow this default
         convention.
        @param p program containing the function
        @param entry function entry point
        """
        ...



    def addLocalVariable(self, var: ghidra.program.model.listing.Variable, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.listing.Variable: ...

    def addParameter(self, var: ghidra.program.model.listing.Variable, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.listing.Parameter: ...

    def addTag(self, tagName: unicode) -> bool: ...

    def equals(self, obj: object) -> bool: ...

    @staticmethod
    def findFunction(program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> ghidra.util.UndefinedFunction:
        """
        locates the function based on the location given at construction time.
        """
        ...

    @staticmethod
    def findFunctionUsingIsolatedBlockModel(program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> ghidra.util.UndefinedFunction: ...

    @staticmethod
    def findFunctionUsingSimpleBlockModel(program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> ghidra.util.UndefinedFunction: ...

    def getAllVariables(self) -> List[ghidra.program.model.listing.Variable]: ...

    def getAutoParameterCount(self) -> int: ...

    def getBody(self) -> ghidra.program.model.address.AddressSetView: ...

    def getCallFixup(self) -> unicode: ...

    def getCalledFunctions(self, monitor: ghidra.util.task.TaskMonitor) -> java.util.Set: ...

    def getCallingConvention(self) -> ghidra.program.model.lang.PrototypeModel: ...

    def getCallingConventionName(self) -> unicode: ...

    def getCallingFunctions(self, monitor: ghidra.util.task.TaskMonitor) -> java.util.Set: ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self) -> unicode: ...

    def getCommentAsArray(self) -> List[unicode]: ...

    def getDefaultCallingConventionName(self) -> unicode: ...

    def getEntryPoint(self) -> ghidra.program.model.address.Address: ...

    def getExternalLocation(self) -> ghidra.program.model.symbol.ExternalLocation: ...

    def getFunctionThunkAddresses(self) -> List[ghidra.program.model.address.Address]: ...

    def getID(self) -> long: ...

    @overload
    def getLocalVariables(self) -> List[ghidra.program.model.listing.Variable]: ...

    @overload
    def getLocalVariables(self, filter: ghidra.program.model.listing.VariableFilter) -> List[ghidra.program.model.listing.Variable]: ...

    @overload
    def getName(self) -> unicode: ...

    @overload
    def getName(self, includeNamespacePath: bool) -> unicode: ...

    def getParameter(self, ordinal: int) -> ghidra.program.model.listing.Parameter: ...

    def getParameterCount(self) -> int: ...

    @overload
    def getParameters(self) -> List[ghidra.program.model.listing.Parameter]: ...

    @overload
    def getParameters(self, filter: ghidra.program.model.listing.VariableFilter) -> List[ghidra.program.model.listing.Parameter]: ...

    def getParentNamespace(self) -> ghidra.program.model.symbol.Namespace: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def getPrototypeString(self, formalSignature: bool, includeCallingConvention: bool) -> unicode: ...

    def getRepeatableComment(self) -> unicode: ...

    def getRepeatableCommentAsArray(self) -> List[unicode]: ...

    def getReturn(self) -> ghidra.program.model.listing.Parameter: ...

    def getReturnType(self) -> ghidra.program.model.data.DataType: ...

    @overload
    def getSignature(self) -> ghidra.program.model.listing.FunctionSignature: ...

    @overload
    def getSignature(self, formalSignature: bool) -> ghidra.program.model.listing.FunctionSignature: ...

    def getSignatureSource(self) -> ghidra.program.model.symbol.SourceType: ...

    def getStackFrame(self) -> ghidra.program.model.listing.StackFrame: ...

    def getStackPurgeSize(self) -> int: ...

    def getSymbol(self) -> ghidra.program.model.symbol.Symbol: ...

    def getTags(self) -> java.util.Set: ...

    def getThunkedFunction(self, recursive: bool) -> ghidra.program.model.listing.Function: ...

    def getVariables(self, filter: ghidra.program.model.listing.VariableFilter) -> List[ghidra.program.model.listing.Variable]: ...

    def hasCustomVariableStorage(self) -> bool: ...

    def hasNoReturn(self) -> bool: ...

    def hasVarArgs(self) -> bool: ...

    def hashCode(self) -> int: ...

    def insertParameter(self, ordinal: int, var: ghidra.program.model.listing.Variable, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.listing.Parameter: ...

    def isExternal(self) -> bool: ...

    def isGlobal(self) -> bool: ...

    def isInline(self) -> bool: ...

    def isStackPurgeSizeValid(self) -> bool: ...

    def isThunk(self) -> bool: ...

    def moveParameter(self, fromOrdinal: int, toOrdinal: int) -> ghidra.program.model.listing.Parameter: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def promoteLocalUserLabelsToGlobal(self) -> None: ...

    def removeParameter(self, ordinal: int) -> None: ...

    def removeTag(self, tagName: unicode) -> None: ...

    def removeVariable(self, var: ghidra.program.model.listing.Variable) -> None: ...

    @overload
    def replaceParameters(self, __a0: List[object], __a1: ghidra.program.model.listing.Function.FunctionUpdateType, __a2: bool, __a3: ghidra.program.model.symbol.SourceType) -> None: ...

    @overload
    def replaceParameters(self, updateType: ghidra.program.model.listing.Function.FunctionUpdateType, force: bool, source: ghidra.program.model.symbol.SourceType, params: List[ghidra.program.model.listing.Variable]) -> None: ...

    def setBody(self, newBody: ghidra.program.model.address.AddressSetView) -> None: ...

    def setCallFixup(self, name: unicode) -> None: ...

    def setCallingConvention(self, name: unicode) -> None: ...

    def setComment(self, comment: unicode) -> None: ...

    def setCustomVariableStorage(self, hasCustomVariableStorage: bool) -> None: ...

    def setInline(self, isInline: bool) -> None: ...

    def setName(self, name: unicode, source: ghidra.program.model.symbol.SourceType) -> None: ...

    def setNoReturn(self, hasNoReturn: bool) -> None: ...

    def setParentNamespace(self, parentNamespace: ghidra.program.model.symbol.Namespace) -> None: ...

    def setRepeatableComment(self, comment: unicode) -> None: ...

    def setReturn(self, type: ghidra.program.model.data.DataType, storage: ghidra.program.model.listing.VariableStorage, source: ghidra.program.model.symbol.SourceType) -> None: ...

    def setReturnType(self, type: ghidra.program.model.data.DataType, source: ghidra.program.model.symbol.SourceType) -> None: ...

    def setSignatureSource(self, signatureSource: ghidra.program.model.symbol.SourceType) -> None: ...

    def setStackPurgeSize(self, purgeSize: int) -> None: ...

    def setThunkedFunction(self, thunkedFunction: ghidra.program.model.listing.Function) -> None: ...

    def setVarArgs(self, hasVarArgs: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def updateFunction(self, __a0: unicode, __a1: ghidra.program.model.listing.Variable, __a2: List[object], __a3: ghidra.program.model.listing.Function.FunctionUpdateType, __a4: bool, __a5: ghidra.program.model.symbol.SourceType) -> None: ...

    @overload
    def updateFunction(self, callingConvention: unicode, returnValue: ghidra.program.model.listing.Variable, updateType: ghidra.program.model.listing.Function.FunctionUpdateType, force: bool, source: ghidra.program.model.symbol.SourceType, newParams: List[ghidra.program.model.listing.Variable]) -> None: ...

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
