import ghidra.app.util.bin.format.pdb2.pdbreader
import ghidra.app.util.bin.format.pdb2.pdbreader.symbol
import java.lang


class Compile3MsSymbol(ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractMsSymbol):
    PDB_ID: int = 4412



    def __init__(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader): ...



    def emit(self, __a0: java.lang.StringBuilder) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getBackEndBuildVersionNumber(self) -> int: ...

    def getBackEndMajorVersionNumber(self) -> int: ...

    def getBackEndMinorVersionNumber(self) -> int: ...

    def getBackEndQuickFixEngineeringVersionNumber(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getCompilerVersionString(self) -> unicode: ...

    def getFrontEndBuildVersionNumber(self) -> int: ...

    def getFrontEndMajorVersionNumber(self) -> int: ...

    def getFrontEndMinorVersionNumber(self) -> int: ...

    def getFrontEndQuickFixEngineeringVersionNumber(self) -> int: ...

    def getLanguage(self) -> unicode: ...

    def getPdbId(self) -> int: ...

    def getProcessor(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.Processor: ...

    def hashCode(self) -> int: ...

    def isCompiledForEditAndContinue(self) -> bool: ...

    def isCompiledWithBzalignNoDataAlign(self) -> bool: ...

    def isCompiledWithGsBufferSecurityChecks(self) -> bool: ...

    def isCompiledWithHotPatch(self) -> bool: ...

    def isCompiledWithLinkTimeCodeGeneration(self) -> bool: ...

    def isCompiledWithLtcgPgoOrPgu(self) -> bool: ...

    def isCompiledWithSdl(self) -> bool: ...

    def isDotExpModule(self) -> bool: ...

    def isManagedCodeDataPresent(self) -> bool: ...

    def isMicrosoftIntermediateLanguageNetModule(self) -> bool: ...

    def isNotCompiledWithDebugInfo(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def wasConvertedWithCvtcil(self) -> bool: ...

    @property
    def backEndBuildVersionNumber(self) -> int: ...

    @property
    def backEndMajorVersionNumber(self) -> int: ...

    @property
    def backEndMinorVersionNumber(self) -> int: ...

    @property
    def backEndQuickFixEngineeringVersionNumber(self) -> int: ...

    @property
    def compiledForEditAndContinue(self) -> bool: ...

    @property
    def compiledWithBzalignNoDataAlign(self) -> bool: ...

    @property
    def compiledWithGsBufferSecurityChecks(self) -> bool: ...

    @property
    def compiledWithHotPatch(self) -> bool: ...

    @property
    def compiledWithLinkTimeCodeGeneration(self) -> bool: ...

    @property
    def compiledWithLtcgPgoOrPgu(self) -> bool: ...

    @property
    def compiledWithSdl(self) -> bool: ...

    @property
    def compilerVersionString(self) -> unicode: ...

    @property
    def dotExpModule(self) -> bool: ...

    @property
    def frontEndBuildVersionNumber(self) -> int: ...

    @property
    def frontEndMajorVersionNumber(self) -> int: ...

    @property
    def frontEndMinorVersionNumber(self) -> int: ...

    @property
    def frontEndQuickFixEngineeringVersionNumber(self) -> int: ...

    @property
    def language(self) -> unicode: ...

    @property
    def managedCodeDataPresent(self) -> bool: ...

    @property
    def microsoftIntermediateLanguageNetModule(self) -> bool: ...

    @property
    def notCompiledWithDebugInfo(self) -> bool: ...

    @property
    def pdbId(self) -> int: ...

    @property
    def processor(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.Processor: ...
