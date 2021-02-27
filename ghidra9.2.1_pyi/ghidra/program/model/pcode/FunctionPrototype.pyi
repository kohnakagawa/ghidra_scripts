from typing import List
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.program.model.pcode
import ghidra.xml
import java.lang


class FunctionPrototype(object):
    """
    High-level prototype of a function based on Varnodes, describing the inputs and outputs
     of this function.
    """





    @overload
    def __init__(self, ls: ghidra.program.model.pcode.LocalSymbolMap, func: ghidra.program.model.listing.Function):
        """
        Construct a FunctionPrototype backed by a local symbolmap.
         This is only a partial initialization.  It is intended to be followed either by
         grabFromFunction() or readPrototypeXML()
        @param ls is the LocalSymbolMap backing the prototype
        @param func is the function using the symbolmap
        """
        ...

    @overload
    def __init__(self, proto: ghidra.program.model.listing.FunctionSignature, cspec: ghidra.program.model.lang.CompilerSpec, voidimpliesdotdotdot: bool):
        """
        Construct an internally backed prototype based on a FunctionSignature prototype
        @param proto is the FunctionSignature used to internally back input parameters
        @param cspec is the compiler spec used to pick prototype model
        @param voidimpliesdotdotdot set to true if a void prototype is interpreted as varargs
        """
        ...



    def buildPrototypeXML(self, res: java.lang.StringBuilder, dtmanage: ghidra.program.model.pcode.PcodeDataTypeManager) -> None:
        """
        append an XML string representing this function prototype
        @param res is where the string should be appended
        @param dtmanage is the DataTypeManager for building type reference tags
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getExtraPop(self) -> int:
        """
        @return the number of extra bytes popped off by this functions return
        """
        ...

    def getGenericCallingConvention(self) -> ghidra.program.model.data.GenericCallingConvention:
        """
        @return generic calling convention
        """
        ...

    def getModelName(self) -> unicode:
        """
        @return calling convention model name specific to the associated compiler spec
        """
        ...

    def getNumParams(self) -> int:
        """
        @return the number of defined parameters for this function prototype
        """
        ...

    def getParam(self, i: int) -> ghidra.program.model.pcode.HighSymbol:
        """
        @param i i'th parameter index
        @return the i'th HighParam to this function prototype or null
         if this prototype is not backed by a LocalSymbolMap
        """
        ...

    def getParameterDefinitions(self) -> List[ghidra.program.model.data.ParameterDefinition]:
        """
        @return parameter definitions if prototype was produced
         from a FunctionSignature or null if backed by a
         LocalSymbolMap
        """
        ...

    def getReturnStorage(self) -> ghidra.program.model.listing.VariableStorage:
        """
        @return the return storage for the function
        """
        ...

    def getReturnType(self) -> ghidra.program.model.data.DataType:
        """
        @return the return type for the function
        """
        ...

    def hasNoReturn(self) -> bool:
        """
        @return true if calls to this function do not return
        """
        ...

    def hasThisPointer(self) -> bool:
        """
        @return true if this function is a method taking a 'this' pointer as a parameter
        """
        ...

    def hashCode(self) -> int: ...

    def isBackedByLocalSymbolMap(self) -> bool:
        """
        @return true if this prototype is backed by a LocalSymbolMap, or
         false if generated from a FunctionSignature.
        """
        ...

    def isConstructor(self) -> bool:
        """
        @return true if this function is an (object-oriented) constructor
        """
        ...

    def isDestructor(self) -> bool:
        """
        @return true if this function is an (object-oriented) destructor
        """
        ...

    def isInline(self) -> bool:
        """
        @return true if this function should be inlined by the decompile
        """
        ...

    def isVarArg(self) -> bool:
        """
        @return true if this function has variable arguments
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def readPrototypeXML(self, parser: ghidra.xml.XmlPullParser, dtmanage: ghidra.program.model.pcode.PcodeDataTypeManager) -> None:
        """
        Parse the function prototype from {@code <prototype>} tag.
        @param parser is the XML document to parse
        @param dtmanage is the DataTypeManager used to parse data-type tags
        @throws PcodeXMLException for any problems parsing
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
    def backedByLocalSymbolMap(self) -> bool: ...

    @property
    def constructor(self) -> bool: ...

    @property
    def destructor(self) -> bool: ...

    @property
    def extraPop(self) -> int: ...

    @property
    def genericCallingConvention(self) -> ghidra.program.model.data.GenericCallingConvention: ...

    @property
    def inline(self) -> bool: ...

    @property
    def modelName(self) -> unicode: ...

    @property
    def numParams(self) -> int: ...

    @property
    def parameterDefinitions(self) -> List[ghidra.program.model.data.ParameterDefinition]: ...

    @property
    def returnStorage(self) -> ghidra.program.model.listing.VariableStorage: ...

    @property
    def returnType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def varArg(self) -> bool: ...
