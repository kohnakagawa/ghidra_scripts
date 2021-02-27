import ghidra.app.util.demangler
import ghidra.program.model.data
import java.lang


class DemangledDataType(ghidra.app.util.demangler.DemangledType):
    """
    A class to represent a demangled data type.
    """

    ARR_NOTATION: unicode = u'[]'
    BOOL: unicode = u'bool'
    CHAR: unicode = u'char'
    CLASS: unicode = u'class'
    COCLASS: unicode = u'coclass'
    COINTERFACE: unicode = u'cointerface'
    COMPLEX: unicode = u'complex'
    CONST: unicode = u'const'
    DOUBLE: unicode = u'double'
    ENUM: unicode = u'enum'
    FLOAT: unicode = u'float'
    FLOAT128: unicode = u'__float128'
    INT: unicode = u'int'
    INT0_T: unicode = u'int0_t'
    INT128: unicode = u'__int128'
    INT16: unicode = u'__int16'
    INT32: unicode = u'__int32'
    INT64: unicode = u'__int64'
    INT8: unicode = u'__int8'
    LONG: unicode = u'long'
    LONG_DOUBLE: unicode = u'long double'
    LONG_LONG: unicode = u'long long'
    PRIMITIVES: List[unicode] = array(java.lang.String, [u'void', u'bool', u'char', u'wchar_t', u'short', u'int', u'int0_t', u'long', u'long long', u'float', u'double', u'__int128', u'__float128', u'long double'])
    PTR64: unicode = u'__ptr64'
    PTR_NOTATION: unicode = u'*'
    REF_NOTATION: unicode = u'&'
    RESTRICT: unicode = u'__restrict'
    SHORT: unicode = u'short'
    SIGNED: unicode = u'signed'
    SPACE: int = ' '
    STRING: unicode = u'string'
    STRUCT: unicode = u'struct'
    UNALIGNED: unicode = u'__unaligned'
    UNDEFINED: unicode = u'undefined'
    UNION: unicode = u'union'
    UNSIGNED: unicode = u'unsigned'
    VARARGS: unicode = u'...'
    VOID: unicode = u'void'
    VOLATILE: unicode = u'volatile'
    WCHAR_T: unicode = u'wchar_t'



    def __init__(self, mangled: unicode, originaDemangled: unicode, name: unicode): ...



    def equals(self, __a0: object) -> bool: ...

    def getArrayDimensions(self) -> int: ...

    def getBasedName(self) -> unicode: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataType(self, dataTypeManager: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType:
        """
        Converts this demangled datatype into the corresponding Ghidra datatype
        @param dataTypeManager the manager to search and whose data organization should be used
        @return the Ghidra datatype corresponding to the demangled datatype
        """
        ...

    def getDemangledName(self) -> unicode: ...

    def getMangledString(self) -> unicode: ...

    def getMemberScope(self) -> unicode: ...

    def getName(self) -> unicode: ...

    def getNamespace(self) -> ghidra.app.util.demangler.Demangled: ...

    def getNamespaceName(self) -> unicode: ...

    def getNamespaceString(self) -> unicode: ...

    def getOriginalDemangled(self) -> unicode: ...

    def getPointerLevels(self) -> int: ...

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

    def isEnum(self) -> bool: ...

    def isPointer(self) -> bool: ...

    def isPointer64(self) -> bool: ...

    def isPrimitive(self) -> bool: ...

    def isReference(self) -> bool: ...

    def isRestrict(self) -> bool: ...

    def isSigned(self) -> bool: ...

    def isStruct(self) -> bool: ...

    def isTemplate(self) -> bool: ...

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

    def setClass(self) -> None: ...

    def setCoclass(self) -> None: ...

    def setCointerface(self) -> None: ...

    def setComplex(self) -> None: ...

    def setConst(self) -> None: ...

    def setEnum(self) -> None: ...

    @overload
    def setEnumType(self) -> unicode: ...

    @overload
    def setEnumType(self, enumType: unicode) -> None: ...

    def setMemberScope(self, memberScope: unicode) -> None: ...

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

    def setSigned(self) -> None: ...

    def setStruct(self) -> None: ...

    @overload
    def setTemplate(self) -> None: ...

    @overload
    def setTemplate(self, template: ghidra.app.util.demangler.DemangledTemplate) -> None: ...

    def setUnaligned(self) -> None: ...

    def setUnion(self) -> None: ...

    def setUnsigned(self) -> None: ...

    def setVarArgs(self) -> None: ...

    def setVolatile(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def array(self) -> bool: ...

    @property
    def arrayDimensions(self) -> int: ...

    @property
    def basedName(self) -> unicode: ...

    @basedName.setter
    def basedName(self, value: unicode) -> None: ...

    @property
    def class(self) -> bool: ...

    @property
    def coclass(self) -> bool: ...

    @property
    def cointerface(self) -> bool: ...

    @property
    def complex(self) -> bool: ...

    @property
    def enum(self) -> bool: ...

    @property
    def enumType(self) -> None: ...  # No getter available.

    @enumType.setter
    def enumType(self, value: unicode) -> None: ...

    @property
    def memberScope(self) -> unicode: ...

    @memberScope.setter
    def memberScope(self, value: unicode) -> None: ...

    @property
    def pointer(self) -> bool: ...

    @property
    def pointer64(self) -> bool: ...

    @property
    def pointerLevels(self) -> int: ...

    @property
    def primitive(self) -> bool: ...

    @property
    def reference(self) -> bool: ...

    @property
    def restrict(self) -> bool: ...

    @property
    def signature(self) -> unicode: ...

    @property
    def signed(self) -> bool: ...

    @property
    def struct(self) -> bool: ...

    @property
    def template(self) -> bool: ...

    @property
    def unaligned(self) -> bool: ...

    @property
    def union(self) -> bool: ...

    @property
    def unsigned(self) -> bool: ...

    @property
    def varArgs(self) -> bool: ...

    @property
    def void(self) -> bool: ...
