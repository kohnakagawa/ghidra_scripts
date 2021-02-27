import ghidra.app.util.bin.format.pdb2.pdbreader
import ghidra.app.util.bin.format.pdb2.pdbreader.symbol
import java.lang


class DataHighLevelShaderLanguageSymbolInternals(ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractSymbolInternals):





    class DataHighLevelShaderLanguageSymbolInternals32(ghidra.app.util.bin.format.pdb2.pdbreader.symbol.DataHighLevelShaderLanguageSymbolInternals):




        def __init__(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb): ...



        def emit(self, __a0: java.lang.StringBuilder) -> None: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDataOffset(self) -> long: ...

        def getDataSlot(self) -> long: ...

        def getName(self) -> unicode: ...

        def getRegisterType(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType: ...

        def getSamplerSlotStart(self) -> long: ...

        def getTextureSlotStart(self) -> long: ...

        def getTypeRecordNumber(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber: ...

        def getUavSlotStart(self) -> long: ...

        def hashCode(self) -> int: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        @staticmethod
        def parse(__a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.DataHighLevelShaderLanguageSymbolInternals: ...

        @staticmethod
        def parse32(__a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.DataHighLevelShaderLanguageSymbolInternals: ...

        @staticmethod
        def parse32Ext(__a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.DataHighLevelShaderLanguageSymbolInternals: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...

        @property
        def dataSlot(self) -> long: ...

        @property
        def samplerSlotStart(self) -> long: ...

        @property
        def textureSlotStart(self) -> long: ...

        @property
        def uavSlotStart(self) -> long: ...




    class DataHighLevelShaderLanguageSymbolInternals32Extended(ghidra.app.util.bin.format.pdb2.pdbreader.symbol.DataHighLevelShaderLanguageSymbolInternals):




        def __init__(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb): ...



        def emit(self, __a0: java.lang.StringBuilder) -> None: ...

        def equals(self, __a0: object) -> bool: ...

        def getBindSlot(self) -> long: ...

        def getBindSpace(self) -> long: ...

        def getClass(self) -> java.lang.Class: ...

        def getDataOffset(self) -> long: ...

        def getName(self) -> unicode: ...

        def getRegisterIndex(self) -> long: ...

        def getRegisterType(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType: ...

        def getTypeRecordNumber(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber: ...

        def hashCode(self) -> int: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        @staticmethod
        def parse(__a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.DataHighLevelShaderLanguageSymbolInternals: ...

        @staticmethod
        def parse32(__a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.DataHighLevelShaderLanguageSymbolInternals: ...

        @staticmethod
        def parse32Ext(__a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.DataHighLevelShaderLanguageSymbolInternals: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...

        @property
        def bindSlot(self) -> long: ...

        @property
        def bindSpace(self) -> long: ...

        @property
        def registerIndex(self) -> long: ...

    def __init__(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb): ...



    def emit(self, __a0: java.lang.StringBuilder) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataOffset(self) -> long: ...

    def getName(self) -> unicode: ...

    def getRegisterType(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType: ...

    def getTypeRecordNumber(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def parse(__a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.DataHighLevelShaderLanguageSymbolInternals: ...

    @staticmethod
    def parse32(__a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.DataHighLevelShaderLanguageSymbolInternals: ...

    @staticmethod
    def parse32Ext(__a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.DataHighLevelShaderLanguageSymbolInternals: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def dataOffset(self) -> long: ...

    @property
    def name(self) -> unicode: ...

    @property
    def registerType(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.HLSLRegisterType: ...

    @property
    def typeRecordNumber(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.RecordNumber: ...
