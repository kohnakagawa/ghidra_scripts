from typing import List
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.lang
import ghidra.program.model.listing
import java.lang
import java.util


class BasicCompilerSpec(object, ghidra.program.model.lang.CompilerSpec):
    CALLING_CONVENTION_cdecl: unicode = u'__cdecl'
    CALLING_CONVENTION_fastcall: unicode = u'__fastcall'
    CALLING_CONVENTION_pascal: unicode = u'__pascal'
    CALLING_CONVENTION_stdcall: unicode = u'__stdcall'
    CALLING_CONVENTION_thiscall: unicode = u'__thiscall'
    CALLING_CONVENTION_vectorcall: unicode = u'__vectorcall'
    CONSTANT_SPACE_INDEX: int = 0
    DECOMPILER_OUTPUT_DEF: ghidra.program.model.lang.DecompilerLanguage = c-language
    DECOMPILER_OUTPUT_DESC: unicode = u'Select the source language output by the decompiler.'
    DECOMPILER_OUTPUT_LANGUAGE: unicode = u'Output Language'
    DECOMPILER_PROPERTY_LIST_NAME: unicode = u'Decompiler'
    JOIN_SPACE_NAME: unicode = u'join'
    OTHER_SPACE_INDEX: int = 1
    OTHER_SPACE_NAME: unicode = u'OTHER'
    STACK_SPACE_NAME: unicode = u'stack'



    def __init__(self, description: ghidra.program.model.lang.CompilerSpecDescription, language: ghidra.app.plugin.processors.sleigh.SleighLanguage, cspecFile: generic.jar.ResourceFile): ...



    def applyContextSettings(self, programContext: ghidra.program.model.listing.DefaultProgramContext) -> None: ...

    def doesCDataTypeConversions(self) -> bool: ...

    @staticmethod
    def enableJavaLanguageDecompilation(program: ghidra.program.model.listing.Program) -> None:
        """
        Adds and enables an option to have the decompiler display java.
        @param program to be enabled
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def findBestCallingConvention(self, params: List[ghidra.program.model.listing.Parameter]) -> ghidra.program.model.lang.PrototypeModel: ...

    def getAddressSpace(self, spaceName: unicode) -> ghidra.program.model.address.AddressSpace: ...

    def getCallingConvention(self, name: unicode) -> ghidra.program.model.lang.PrototypeModel: ...

    def getCallingConventions(self) -> List[ghidra.program.model.lang.PrototypeModel]: ...

    def getClass(self) -> java.lang.Class: ...

    def getCompilerSpecDescription(self) -> ghidra.program.model.lang.CompilerSpecDescription: ...

    def getCompilerSpecID(self) -> ghidra.program.model.lang.CompilerSpecID: ...

    def getCompilerSpecString(self) -> unicode: ...

    def getDataOrganization(self) -> ghidra.program.model.data.DataOrganization: ...

    def getDecompilerOutputLanguage(self, program: ghidra.program.model.listing.Program) -> ghidra.program.model.lang.DecompilerLanguage: ...

    def getDefaultCallingConvention(self) -> ghidra.program.model.lang.PrototypeModel: ...

    def getLanguage(self) -> ghidra.program.model.lang.Language: ...

    def getNamedCallingConventions(self) -> List[ghidra.program.model.lang.PrototypeModel]: ...

    def getPcodeInjectLibrary(self) -> ghidra.program.model.lang.PcodeInjectLibrary: ...

    @overload
    def getProperty(self, key: unicode) -> unicode: ...

    @overload
    def getProperty(self, key: unicode, defaultString: unicode) -> unicode: ...

    def getPropertyAsBoolean(self, key: unicode, defaultBoolean: bool) -> bool: ...

    def getPropertyAsInt(self, key: unicode, defaultInt: int) -> int: ...

    def getPropertyKeys(self) -> java.util.Set: ...

    def getPrototypeEvaluationModel(self, program: ghidra.program.model.listing.Program) -> object: ...

    def getStackBaseSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    def getStackPointer(self) -> ghidra.program.model.lang.Register: ...

    def getStackSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    def hasProperty(self, key: unicode) -> bool: ...

    def hashCode(self) -> int: ...

    def isGlobal(self, addr: ghidra.program.model.address.Address) -> bool: ...

    def isStackRightJustified(self) -> bool: ...

    def matchConvention(self, genericCallingConvention: ghidra.program.model.data.GenericCallingConvention) -> ghidra.program.model.lang.PrototypeModel: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def registerProgramOptions(self, program: ghidra.program.model.listing.Program) -> None: ...

    def stackGrowsNegative(self) -> bool: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def callingConventions(self) -> List[ghidra.program.model.lang.PrototypeModel]: ...

    @property
    def compilerSpecDescription(self) -> ghidra.program.model.lang.CompilerSpecDescription: ...

    @property
    def compilerSpecID(self) -> ghidra.program.model.lang.CompilerSpecID: ...

    @property
    def compilerSpecString(self) -> unicode: ...

    @property
    def dataOrganization(self) -> ghidra.program.model.data.DataOrganization: ...

    @property
    def defaultCallingConvention(self) -> ghidra.program.model.lang.PrototypeModel: ...

    @property
    def language(self) -> ghidra.program.model.lang.Language: ...

    @property
    def namedCallingConventions(self) -> List[ghidra.program.model.lang.PrototypeModel]: ...

    @property
    def pcodeInjectLibrary(self) -> ghidra.program.model.lang.PcodeInjectLibrary: ...

    @property
    def propertyKeys(self) -> java.util.Set: ...

    @property
    def stackBaseSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    @property
    def stackPointer(self) -> ghidra.program.model.lang.Register: ...

    @property
    def stackRightJustified(self) -> bool: ...

    @property
    def stackSpace(self) -> ghidra.program.model.address.AddressSpace: ...