from typing import List
import ghidra.app.util.bin.format.pdb2.pdbreader
import ghidra.app.util.bin.format.pdb2.pdbreader.symbol
import java.lang


class AbstractCompile2MsSymbol(ghidra.app.util.bin.format.pdb2.pdbreader.symbol.AbstractMsSymbol):




    def __init__(self, __a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractPdb, __a1: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader, __a2: ghidra.app.util.bin.format.pdb2.pdbreader.StringParseType): ...



    def emit(self, __a0: java.lang.StringBuilder) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getBackEndBuildVersionNumber(self) -> int: ...

    def getBackEndMajorVersionNumber(self) -> int: ...

    def getBackEndMinorVersionNumber(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getCompilerVersionString(self) -> unicode: ...

    def getFrontEndBuildVersionNumber(self) -> int: ...

    def getFrontEndMajorVersionNumber(self) -> int: ...

    def getFrontEndMinorVersionNumber(self) -> int: ...

    def getLanguage(self) -> unicode: ...

    def getPdbId(self) -> int: ...

    def getProcessor(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.Processor: ...

    def getStringList(self) -> List[object]: ...

    def hashCode(self) -> int: ...

    def isCompiledForEditAndContinue(self) -> bool: ...

    def isCompiledWithBzalignNoDataAlign(self) -> bool: ...

    def isCompiledWithGsBufferSecurityChecks(self) -> bool: ...

    def isCompiledWithHotPatch(self) -> bool: ...

    def isCompiledWithLinkTimeCodeGeneration(self) -> bool: ...

    def isConvertedWithCvtcil(self) -> bool: ...

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

    @property
    def backEndBuildVersionNumber(self) -> int: ...

    @property
    def backEndMajorVersionNumber(self) -> int: ...

    @property
    def backEndMinorVersionNumber(self) -> int: ...

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
    def compilerVersionString(self) -> unicode: ...

    @property
    def convertedWithCvtcil(self) -> bool: ...

    @property
    def frontEndBuildVersionNumber(self) -> int: ...

    @property
    def frontEndMajorVersionNumber(self) -> int: ...

    @property
    def frontEndMinorVersionNumber(self) -> int: ...

    @property
    def language(self) -> unicode: ...

    @property
    def managedCodeDataPresent(self) -> bool: ...

    @property
    def microsoftIntermediateLanguageNetModule(self) -> bool: ...

    @property
    def notCompiledWithDebugInfo(self) -> bool: ...

    @property
    def processor(self) -> ghidra.app.util.bin.format.pdb2.pdbreader.Processor: ...

    @property
    def stringList(self) -> List[object]: ...
