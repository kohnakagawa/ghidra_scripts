from typing import List
import ghidra.app.util.demangler
import ghidra.program.model.data
import java.lang


class DemangledFunctionIndirect(ghidra.app.util.demangler.AbstractDemangledFunctionDefinitionDataType):
    """
    A class to represent a demangled function indirect.  A function indirect is
     similar to a function pointer or a function reference except that it does
     not have the start (*) for a pointer or ampersand () for a reference, but
     is still an indirect definition (not a regular function definition).  The
     function indirect is prevalent in the Microsoft model, if not other models.
    """





    def __init__(self, mangled: unicode, originalDemangled: unicode): ...



    def addParameter(self, parameter: ghidra.app.util.demangler.DemangledDataType) -> None:
        """
        Adds a parameters to the end of the parameter list for this demangled function
        @param parameter the new parameter to add
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getArrayDimensions(self) -> int: ...

    def getBasedName(self) -> unicode: ...

    def getCallingConvention(self) -> unicode:
        """
        Returns the calling convention or null, if unspecified
        @return the calling convention or null, if unspecified
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDataType(self, dataTypeManager: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType: ...

    def getDemangledName(self) -> unicode: ...

    def getMangledString(self) -> unicode: ...

    def getMemberScope(self) -> unicode: ...

    def getName(self) -> unicode: ...

    def getNamespace(self) -> ghidra.app.util.demangler.Demangled: ...

    def getNamespaceName(self) -> unicode: ...

    def getNamespaceString(self) -> unicode: ...

    def getOriginalDemangled(self) -> unicode: ...

    def getParameters(self) -> List[ghidra.app.util.demangler.DemangledDataType]:
        """
        Returns a list of the parameters for this demangled functions.
        @return a list of the parameters for this demangled functions
        """
        ...

    def getPointerLevels(self) -> int: ...

    def getReturnType(self) -> ghidra.app.util.demangler.DemangledDataType:
        """
        Returns the return type
        @return the return type
        """
        ...

    def getSignature(self) -> unicode: ...

    def getTemplate(self) -> ghidra.app.util.demangler.DemangledTemplate: ...

    def hashCode(self) -> int: ...

    def incrementPointerLevels(self) -> None: ...

    def isArray(self) -> bool: ...

    def isClass(self) -> bool: ...

    def isCoclass(self) -> bool: ...

    def isCointerface(self) -> bool: ...

    def isComplex(self) -> bool: ...

    def isConst(self) -> bool: ...

    def isConstPointer(self) -> bool: ...

    def isEnum(self) -> bool: ...

    def isPointer(self) -> bool: ...

    def isPointer64(self) -> bool: ...

    def isPrimitive(self) -> bool: ...

    def isReference(self) -> bool: ...

    def isRestrict(self) -> bool: ...

    def isSigned(self) -> bool: ...

    def isStruct(self) -> bool: ...

    def isTemplate(self) -> bool: ...

    def isTrailingPointer64(self) -> bool: ...

    def isTrailingRestrict(self) -> bool: ...

    def isTrailingUnaligned(self) -> bool: ...

    def isUnaligned(self) -> bool: ...

    def isUnion(self) -> bool: ...

    def isUnsigned(self) -> bool: ...

    def isVarArgs(self) -> bool: ...

    def isVoid(self) -> bool: ...

    def isVolatile(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setArray(self, dimensions: int) -> None: ...

    def setBasedName(self, basedName: unicode) -> None: ...

    def setCallingConvention(self, callingConvention: unicode) -> None:
        """
        Sets the function calling convention. For example, "__cdecl"
        @param callingConvention the function calling convention
        """
        ...

    def setClass(self) -> None: ...

    def setCoclass(self) -> None: ...

    def setCointerface(self) -> None: ...

    def setComplex(self) -> None: ...

    def setConst(self) -> None: ...

    def setConstPointer(self) -> None: ...

    def setDisplayFunctionPointerParens(self, b: bool) -> None: ...

    def setEnum(self) -> None: ...

    @overload
    def setEnumType(self) -> unicode: ...

    @overload
    def setEnumType(self, enumType: unicode) -> None: ...

    def setMemberScope(self, memberScope: unicode) -> None: ...

    def setModifier(self, modifier: unicode) -> None:
        """
        Sets the function __ modifier. For example, "namespace::".
        @param modifier the function modifier
        """
        ...

    def setName(self, name: unicode) -> None: ...

    def setNamespace(self, namespace: ghidra.app.util.demangler.Demangled) -> None: ...

    def setPointer64(self) -> None: ...

    def setRValueReference(self) -> None:
        """
        rvalue reference; C++11
        """
        ...

    def setReference(self) -> None: ...

    def setRestrict(self) -> None: ...

    def setReturnType(self, returnType: ghidra.app.util.demangler.DemangledDataType) -> None:
        """
        Sets the return type
        @param returnType the return type
        """
        ...

    def setSigned(self) -> None: ...

    def setStruct(self) -> None: ...

    @overload
    def setTemplate(self) -> None: ...

    @overload
    def setTemplate(self, template: ghidra.app.util.demangler.DemangledTemplate) -> None: ...

    def setTrailingPointer64(self) -> None: ...

    def setTrailingRestrict(self) -> None: ...

    def setTrailingUnaligned(self) -> None: ...

    def setUnaligned(self) -> None: ...

    def setUnion(self) -> None: ...

    def setUnsigned(self) -> None: ...

    def setVarArgs(self) -> None: ...

    def setVolatile(self) -> None: ...

    def toSignature(self, name: unicode) -> unicode: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...