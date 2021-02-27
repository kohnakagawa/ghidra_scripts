from typing import List
import ghidra.app.util.bin.format.pdb2.pdbreader.symbol
import java.lang


class HLSLRegisterType(java.lang.Enum):
    CONSTANT_BUFFER: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = CONSTANT_BUFFER
    CYCLE_COUNTER: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = CYCLE_COUNTER
    FUNCTION_BODY: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = FUNCTION_BODY
    FUNCTION_INPUT: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = FUNCTION_INPUT
    FUNCTION_OUTPUT: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = FUNCTION_OUTPUT
    FUNCTION_TABLE: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = FUNCTION_TABLE
    IMMEDIATE32: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = IMMEDIATE32
    IMMEDIATE64: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = IMMEDIATE64
    IMMEDIATE_CONSTANT_BUFFER: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = IMMEDIATE_CONSTANT_BUFFER
    INDEXABLE_TEMP: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = INDEXABLE_TEMP
    INPUT: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = INPUT
    INPUT_CONTROL_POINT: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = INPUT_CONTROL_POINT
    INPUT_COVERAGE_MASK: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = INPUT_COVERAGE_MASK
    INPUT_DOMAIN_POINT: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = INPUT_DOMAIN_POINT
    INPUT_FORK_INSTANCE_ID: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = INPUT_FORK_INSTANCE_ID
    INPUT_GS_INSTANCE_ID: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = INPUT_GS_INSTANCE_ID
    INPUT_JOIN_INSTANCE_ID: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = INPUT_JOIN_INSTANCE_ID
    INPUT_PATCH_CONSTANT: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = INPUT_PATCH_CONSTANT
    INPUT_PRIMITIVEID: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = INPUT_PRIMITIVEID
    INPUT_THREAD_GROUP_ID: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = INPUT_THREAD_GROUP_ID
    INPUT_THREAD_ID: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = INPUT_THREAD_ID
    INPUT_THREAD_ID_IN_GROUP: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = INPUT_THREAD_ID_IN_GROUP
    INPUT_THREAD_ID_IN_GROUP_FLATTENED: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = INPUT_THREAD_ID_IN_GROUP_FLATTENED
    INTERFACE: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = INTERFACE
    INVALID: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = INVALID_REG
    LABEL: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = LABEL
    NULL: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = NULL
    OUTPUT: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = OUTPUT
    OUTPUT_CONTROL_POINT: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = OUTPUT_CONTROL_POINT
    OUTPUT_CONTROL_POINT_ID: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = OUTPUT_CONTROL_POINT_ID
    OUTPUT_COVERAGE_MASK: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = OUTPUT_COVERAGE_MASK
    OUTPUT_DEPTH: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = OUTPUT_DEPTH
    OUTPUT_DEPTH_GREATER_EQUA: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = OUTPUT_DEPTH_GREATER_EQUA
    OUTPUT_DEPTH_LESS_EQUAL: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = OUTPUT_DEPTH_LESS_EQUAL
    RASTERIZER: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = RASTERIZER
    RESOURCE: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = RESOURCE
    SAMPLER: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = SAMPLER
    STREAM: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = STREAM
    TEMP: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = TEMP
    THIS_POINTER: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = THIS_POINTER
    THREAD_GROUP_SHARED_MEMORY: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = THREAD_GROUP_SHARED_MEMORY
    UNORDERED_ACCESS_VIEW: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType = UNORDERED_ACCESS_VIEW
    label: unicode
    value: int







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def fromValue(__a0: int) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType: ...

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
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
