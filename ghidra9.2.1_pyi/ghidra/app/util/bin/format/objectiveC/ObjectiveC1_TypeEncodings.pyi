import ghidra.app.util.bin.format.objectiveC
import ghidra.program.model.address
import ghidra.program.model.listing
import java.lang


class ObjectiveC1_TypeEncodings(object):
    _C_ARY_B: int = '['
    _C_ARY_E: int = ']'
    _C_ATOM: int = '%'
    _C_ATOMIC: int = 'A'
    _C_BFLD: int = 'b'
    _C_BOOL: int = 'B'
    _C_BYCOPY: int = 'O'
    _C_BYREF: int = 'R'
    _C_CHARPTR: int = '*'
    _C_CHR: int = 'c'
    _C_CLASS: int = '#'
    _C_CONST: int = 'r'
    _C_DBL: int = 'd'
    _C_FLT: int = 'f'
    _C_ID: int = '@'
    _C_IN: int = 'n'
    _C_INOUT: int = 'N'
    _C_INT: int = 'i'
    _C_LNG: int = 'l'
    _C_LNG_LNG: int = 'q'
    _C_ONEWAY: int = 'V'
    _C_OUT: int = 'o'
    _C_PTR: int = '^'
    _C_SEL: int = ':'
    _C_SHT: int = 's'
    _C_STRUCT_B: int = '{'
    _C_STRUCT_E: int = '}'
    _C_UCHR: int = 'C'
    _C_UINT: int = 'I'
    _C_ULNG: int = 'L'
    _C_ULNG_LNG: int = 'Q'
    _C_UNDEF: int = '?'
    _C_UNION_B: int = '('
    _C_UNION_E: int = ')'
    _C_USHT: int = 'S'
    _C_VECTOR: int = '!'
    _C_VOID: int = 'v'



    def __init__(self, pointerSize: int, categoryPath: ghidra.program.model.data.CategoryPath): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def processInstanceVariableSignature(self, name: unicode, mangledType: unicode) -> unicode: ...

    @overload
    def processInstanceVariableSignature(self, program: ghidra.program.model.listing.Program, instanceVariableAddress: ghidra.program.model.address.Address, mangledType: unicode, instanceVariableSize: int) -> None: ...

    def processMethodSignature(self, program: ghidra.program.model.listing.Program, methodAddress: ghidra.program.model.address.Address, mangledSignature: unicode, methodType: ghidra.app.util.bin.format.objectiveC.ObjectiveC_MethodType) -> None: ...

    def toFunctionSignature(self, methodName: unicode, mangledSignature: unicode) -> ghidra.program.model.listing.FunctionSignature: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
