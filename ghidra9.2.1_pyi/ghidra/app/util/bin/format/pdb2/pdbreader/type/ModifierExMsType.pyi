from typing import List
import ghidra.app.util.bin.format.pdb2.pdbreader
import ghidra.app.util.bin.format.pdb2.pdbreader.type
import java.lang


class ModifierExMsType(ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractMsType):
    PDB_ID: int = 5400




    class Modifier(java.lang.Enum):
        CONST: ghidra.app.util.bin.format.pdb2.pdbreader.type.ModifierExMsType.Modifier = const
        HLSL_CENTER: ghidra.app.util.bin.format.pdb2.pdbreader.type.ModifierExMsType.Modifier = __center__
        HLSL_CENTROID: ghidra.app.util.bin.format.pdb2.pdbreader.type.ModifierExMsType.Modifier = __centroid__
        HLSL_CONSTINTERP: ghidra.app.util.bin.format.pdb2.pdbreader.type.ModifierExMsType.Modifier = __constinterp__
        HLSL_LINE: ghidra.app.util.bin.format.pdb2.pdbreader.type.ModifierExMsType.Modifier = __line__
        HLSL_LINEADJ: ghidra.app.util.bin.format.pdb2.pdbreader.type.ModifierExMsType.Modifier = __lineadj__
        HLSL_LINEAR: ghidra.app.util.bin.format.pdb2.pdbreader.type.ModifierExMsType.Modifier = __linear__
        HLSL_NOPERSPECTIVE: ghidra.app.util.bin.format.pdb2.pdbreader.type.ModifierExMsType.Modifier = __noperspective__
        HLSL_PRECISE: ghidra.app.util.bin.format.pdb2.pdbreader.type.ModifierExMsType.Modifier = __precise__
        HLSL_SAMPLE: ghidra.app.util.bin.format.pdb2.pdbreader.type.ModifierExMsType.Modifier = __sample__
        HLSL_SNORM: ghidra.app.util.bin.format.pdb2.pdbreader.type.ModifierExMsType.Modifier = __snorm__
        HLSL_TRIANGLE: ghidra.app.util.bin.format.pdb2.pdbreader.type.ModifierExMsType.Modifier = __triangle__
        HLSL_TRIANGLEADJ: ghidra.app.util.bin.format.pdb2.pdbreader.type.ModifierExMsType.Modifier = __triangleadj__
        HLSL_UAV_GLOBALLY_COHERENT: ghidra.app.util.bin.format.pdb2.pdbreader.type.ModifierExMsType.Modifier = __uav_globally_coherent__
        HLSL_UNIFORM: ghidra.app.util.bin.format.pdb2.pdbreader.type.ModifierExMsType.Modifier = __uniform__
        HLSL_UNORM: ghidra.app.util.bin.format.pdb2.pdbreader.type.ModifierExMsType.Modifier = __unorm__
        INVALID: ghidra.app.util.bin.format.pdb2.pdbreader.type.ModifierExMsType.Modifier = INVALID
        UNALIGNED: ghidra.app.util.bin.format.pdb2.pdbreader.type.ModifierExMsType.Modifier = __unaligned
        VOLATILE: ghidra.app.util.bin.format.pdb2.pdbreader.type.ModifierExMsType.Modifier = volatile
        label: unicode
        value: int







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def emit(self, __a0: java.lang.StringBuilder) -> None: ...

        def equals(self, __a0: object) -> bool: ...

        @staticmethod
        def fromValue(__a0: int) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.ModifierExMsType.Modifier: ...

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
        def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.ModifierExMsType.Modifier: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.app.util.bin.format.pdb2.pdbreader.type.ModifierExMsType.Modifier]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader): ...



    @overload
    def emit(self, __a0: java.lang.StringBuilder) -> None: ...

    @overload
    def emit(self, __a0: java.lang.StringBuilder, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractMsType.Bind) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLength(self) -> long: ...

    def getName(self) -> unicode: ...

    def getPdbId(self) -> int: ...

    def getRecordNumber(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber: ...

    def getSize(self) -> long: ...

    def hasModifier(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.type.ModifierExMsType.Modifier) -> bool: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setRecordNumber(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def pdbId(self) -> int: ...
