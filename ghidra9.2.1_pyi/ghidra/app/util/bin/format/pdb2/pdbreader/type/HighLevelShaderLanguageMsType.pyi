from typing import List
import ghidra.app.util.bin.format.pdb2.pdbreader
import ghidra.app.util.bin.format.pdb2.pdbreader.type
import java.lang


class HighLevelShaderLanguageMsType(ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractMsType):
    PDB_ID: int = 5399




    class Kind(java.lang.Enum):
        APPEND_STRUCTURED_BUFFER: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = AppendStructuredBuffer
        BUFFER: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = Buffer
        BYTE_ADDRESS_BUFFER: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = ByteAddressBuffer
        CONSUME_STRUCTURED_BUFFER: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = ConsumeStructuredBuffer
        INPUT_PATCH: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = InputPatch
        INTERFACE_POINTER: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = InterfacePointer
        INVALID: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = invalid
        LINE_STREAM: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = LineStream
        MIN_10FLOAT: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = Min10Float
        MIN_12INT: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = Min12Int
        MIN_16FLOAT: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = Min16Float
        MIN_16INT: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = Min16Int
        MIN_16UINT: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = Min16UInt
        MIN_8FLOAT: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = Min8Float
        OUTPUT_PATCH: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = OutputPatch
        POINT_STREAM: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = PointStream
        RW_BUFFER: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = RwBuffer
        RW_BYTE_ADDRESS_BUFFER: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = RwByteAddressBuffer
        RW_STRUCTURED_BUFFER: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = RwStructuredBuffer
        RW_TEXTURE_1D: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = RwTexture1D
        RW_TEXTURE_1D_ARRAY: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = RwTexture1DArray
        RW_TEXTURE_2D: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = RwTexture2D
        RW_TEXTURE_2D_ARRAY: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = RwTexture2DArray
        RW_TEXTURE_3D: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = RwTexture3D
        SAMPLER: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = Sampler
        SAMPLER_COMPARISON: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = SamplerComparison
        STRUCTURED_BUFFER: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = StructuredBuffer
        TEXTURE_1D: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = Texture1D
        TEXTURE_1D_ARRAY: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = Texture1DArray
        TEXTURE_2D: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = Texture2D
        TEXTURE_2D_ARRAY: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = Texture2DArray
        TEXTURE_2D_MS: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = Texture2DMs
        TEXTURE_2D_MS_ARRAY: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = Texture2DMsArray
        TEXTURE_3D: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = Texture3D
        TEXTURE_CUBE: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = TextureCube
        TEXTURE_CUBE_ARRAY: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = TextureCubeArray
        TRIANGLE_STREAM: ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind = TriangleStream
        label: unicode
        value: int







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        @staticmethod
        def fromValue(__a0: int) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind: ...

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
        def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind]: ...

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

    def getData(self) -> List[int]: ...

    def getKind(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind: ...

    def getLength(self) -> long: ...

    def getName(self) -> unicode: ...

    def getPdbId(self) -> int: ...

    def getRecordNumber(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber: ...

    def getSize(self) -> long: ...

    def getSubtypeRecordNumber(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber: ...

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
    def data(self) -> List[int]: ...

    @property
    def kind(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.type.HighLevelShaderLanguageMsType.Kind: ...

    @property
    def pdbId(self) -> int: ...

    @property
    def subtypeRecordNumber(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber: ...
