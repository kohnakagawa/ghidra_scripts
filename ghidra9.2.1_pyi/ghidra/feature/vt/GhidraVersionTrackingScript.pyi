from typing import List
import generic.jar
import ghidra.app.script
import ghidra.app.tablechooser
import ghidra.feature.vt.api.main
import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.mem
import ghidra.program.model.symbol
import ghidra.util.task
import java.awt
import java.io
import java.lang
import java.util


class GhidraVersionTrackingScript(ghidra.app.script.GhidraScript):




    def __init__(self): ...



    def addEntryPoint(self, __a0: ghidra.program.model.address.Address) -> None: ...

    def addInstructionXref(self, __a0: ghidra.program.model.address.Address, __a1: ghidra.program.model.address.Address, __a2: int, __a3: ghidra.program.model.symbol.FlowType) -> ghidra.program.model.symbol.Reference: ...

    def analyze(self, __a0: ghidra.program.model.listing.Program) -> None: ...

    def analyzeAll(self, __a0: ghidra.program.model.listing.Program) -> None: ...

    def analyzeChanges(self, __a0: ghidra.program.model.listing.Program) -> None: ...

    def askAddress(self, __a0: unicode, __a1: unicode) -> ghidra.program.model.address.Address: ...

    def askBytes(self, __a0: unicode, __a1: unicode) -> List[int]: ...

    def askChoice(self, __a0: unicode, __a1: unicode, __a2: List[object], __a3: object) -> object: ...

    @overload
    def askChoices(self, __a0: unicode, __a1: unicode, __a2: List[object]) -> List[object]: ...

    @overload
    def askChoices(self, __a0: unicode, __a1: unicode, __a2: List[object], __a3: List[object]) -> List[object]: ...

    def askDirectory(self, __a0: unicode, __a1: unicode) -> java.io.File: ...

    def askDomainFile(self, __a0: unicode) -> ghidra.framework.model.DomainFile: ...

    def askDouble(self, __a0: unicode, __a1: unicode) -> float: ...

    def askFile(self, __a0: unicode, __a1: unicode) -> java.io.File: ...

    def askInt(self, __a0: unicode, __a1: unicode) -> int: ...

    def askLanguage(self, __a0: unicode, __a1: unicode) -> ghidra.program.model.lang.LanguageCompilerSpecPair: ...

    def askLong(self, __a0: unicode, __a1: unicode) -> long: ...

    def askProgram(self, __a0: unicode) -> ghidra.program.model.listing.Program: ...

    def askProjectFolder(self, __a0: unicode) -> ghidra.framework.model.DomainFolder: ...

    @overload
    def askString(self, __a0: unicode, __a1: unicode) -> unicode: ...

    @overload
    def askString(self, __a0: unicode, __a1: unicode, __a2: unicode) -> unicode: ...

    def askYesNo(self, __a0: unicode, __a1: unicode) -> bool: ...

    def cleanup(self, __a0: bool) -> None: ...

    @overload
    def clearBackgroundColor(self, __a0: ghidra.program.model.address.Address) -> None: ...

    @overload
    def clearBackgroundColor(self, __a0: ghidra.program.model.address.AddressSetView) -> None: ...

    @overload
    def clearListing(self, __a0: ghidra.program.model.address.Address) -> None: ...

    @overload
    def clearListing(self, __a0: ghidra.program.model.address.AddressSetView) -> None: ...

    @overload
    def clearListing(self, __a0: ghidra.program.model.address.Address, __a1: ghidra.program.model.address.Address) -> None: ...

    @overload
    def clearListing(self, __a0: ghidra.program.model.address.AddressSetView, __a1: bool, __a2: bool, __a3: bool, __a4: bool, __a5: bool, __a6: bool, __a7: bool, __a8: bool, __a9: bool, __a10: bool, __a11: bool, __a12: bool) -> bool: ...

    def closeProgram(self, __a0: ghidra.program.model.listing.Program) -> None: ...

    def closeVersionTrackingSession(self) -> None: ...

    def createAddressSet(self) -> ghidra.program.model.address.AddressSet: ...

    @overload
    def createAsciiString(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data: ...

    @overload
    def createAsciiString(self, __a0: ghidra.program.model.address.Address, __a1: int) -> ghidra.program.model.listing.Data: ...

    def createBookmark(self, __a0: ghidra.program.model.address.Address, __a1: unicode, __a2: unicode) -> ghidra.program.model.listing.Bookmark: ...

    def createByte(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data: ...

    def createChar(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data: ...

    def createDWord(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data: ...

    def createData(self, __a0: ghidra.program.model.address.Address, __a1: ghidra.program.model.data.DataType) -> ghidra.program.model.listing.Data: ...

    def createDouble(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data: ...

    def createDwords(self, __a0: ghidra.program.model.address.Address, __a1: int) -> None: ...

    @overload
    def createEquate(self, __a0: ghidra.program.model.listing.Data, __a1: unicode) -> ghidra.program.model.symbol.Equate: ...

    @overload
    def createEquate(self, __a0: ghidra.program.model.listing.Instruction, __a1: int, __a2: unicode) -> ghidra.program.model.symbol.Equate: ...

    @overload
    def createExternalReference(self, __a0: ghidra.program.model.listing.Data, __a1: unicode, __a2: unicode, __a3: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Reference: ...

    @overload
    def createExternalReference(self, __a0: ghidra.program.model.listing.Instruction, __a1: int, __a2: unicode, __a3: unicode, __a4: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Reference: ...

    @overload
    def createExternalReference(self, __a0: ghidra.program.model.listing.Instruction, __a1: int, __a2: unicode, __a3: unicode, __a4: ghidra.program.model.address.Address, __a5: ghidra.program.model.symbol.RefType) -> ghidra.program.model.symbol.Reference: ...

    def createFloat(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data: ...

    @overload
    def createFragment(self, __a0: unicode, __a1: ghidra.program.model.address.Address, __a2: long) -> ghidra.program.model.listing.ProgramFragment: ...

    @overload
    def createFragment(self, __a0: unicode, __a1: ghidra.program.model.address.Address, __a2: ghidra.program.model.address.Address) -> ghidra.program.model.listing.ProgramFragment: ...

    @overload
    def createFragment(self, __a0: ghidra.program.model.listing.ProgramModule, __a1: unicode, __a2: ghidra.program.model.address.Address, __a3: long) -> ghidra.program.model.listing.ProgramFragment: ...

    @overload
    def createFragment(self, __a0: ghidra.program.model.listing.ProgramModule, __a1: unicode, __a2: ghidra.program.model.address.Address, __a3: ghidra.program.model.address.Address) -> ghidra.program.model.listing.ProgramFragment: ...

    def createFunction(self, __a0: ghidra.program.model.address.Address, __a1: unicode) -> ghidra.program.model.listing.Function: ...

    def createHighlight(self, __a0: ghidra.program.model.address.AddressSetView) -> None: ...

    @overload
    def createLabel(self, __a0: ghidra.program.model.address.Address, __a1: unicode, __a2: bool) -> ghidra.program.model.symbol.Symbol: ...

    @overload
    def createLabel(self, __a0: ghidra.program.model.address.Address, __a1: unicode, __a2: bool, __a3: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.Symbol: ...

    @overload
    def createLabel(self, __a0: ghidra.program.model.address.Address, __a1: unicode, __a2: ghidra.program.model.symbol.Namespace, __a3: bool, __a4: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.Symbol: ...

    @overload
    def createMemoryBlock(self, __a0: unicode, __a1: ghidra.program.model.address.Address, __a2: List[int], __a3: bool) -> ghidra.program.model.mem.MemoryBlock: ...

    @overload
    def createMemoryBlock(self, __a0: unicode, __a1: ghidra.program.model.address.Address, __a2: java.io.InputStream, __a3: long, __a4: bool) -> ghidra.program.model.mem.MemoryBlock: ...

    @overload
    def createMemoryReference(self, __a0: ghidra.program.model.listing.Data, __a1: ghidra.program.model.address.Address, __a2: ghidra.program.model.symbol.RefType) -> ghidra.program.model.symbol.Reference: ...

    @overload
    def createMemoryReference(self, __a0: ghidra.program.model.listing.Instruction, __a1: int, __a2: ghidra.program.model.address.Address, __a3: ghidra.program.model.symbol.RefType) -> ghidra.program.model.symbol.Reference: ...

    @overload
    def createProgram(self, __a0: unicode, __a1: ghidra.program.model.lang.LanguageID) -> ghidra.program.model.listing.Program: ...

    @overload
    def createProgram(self, __a0: unicode, __a1: ghidra.program.model.lang.Language, __a2: ghidra.program.model.lang.CompilerSpec) -> ghidra.program.model.listing.Program: ...

    @overload
    def createProgram(self, __a0: unicode, __a1: ghidra.program.model.lang.LanguageID, __a2: ghidra.program.model.lang.CompilerSpecID) -> ghidra.program.model.listing.Program: ...

    def createQWord(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data: ...

    def createSelection(self, __a0: ghidra.program.model.address.AddressSetView) -> None: ...

    def createStackReference(self, __a0: ghidra.program.model.listing.Instruction, __a1: int, __a2: int, __a3: bool) -> ghidra.program.model.symbol.Reference: ...

    @overload
    def createSymbol(self, __a0: ghidra.program.model.address.Address, __a1: unicode, __a2: bool) -> ghidra.program.model.symbol.Symbol: ...

    @overload
    def createSymbol(self, __a0: ghidra.program.model.address.Address, __a1: unicode, __a2: bool, __a3: bool, __a4: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.Symbol: ...

    @overload
    def createTableChooserDialog(self, __a0: unicode, __a1: ghidra.app.tablechooser.TableChooserExecutor) -> ghidra.app.tablechooser.TableChooserDialog: ...

    @overload
    def createTableChooserDialog(self, __a0: unicode, __a1: ghidra.app.tablechooser.TableChooserExecutor, __a2: bool) -> ghidra.app.tablechooser.TableChooserDialog: ...

    def createUnicodeString(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data: ...

    @overload
    def createVersionTrackingSession(self, __a0: unicode, __a1: unicode) -> None: ...

    @overload
    def createVersionTrackingSession(self, __a0: unicode, __a1: ghidra.program.model.listing.Program, __a2: ghidra.program.model.listing.Program) -> None: ...

    def createWord(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data: ...

    def disassemble(self, __a0: ghidra.program.model.address.Address) -> bool: ...

    def end(self, __a0: bool) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def execute(self, __a0: ghidra.app.script.GhidraState, __a1: ghidra.util.task.TaskMonitor, __a2: java.io.PrintWriter) -> None: ...

    @overload
    def find(self, __a0: unicode) -> ghidra.program.model.address.Address: ...

    @overload
    def find(self, __a0: ghidra.program.model.address.Address, __a1: int) -> ghidra.program.model.address.Address: ...

    @overload
    def find(self, __a0: ghidra.program.model.address.Address, __a1: List[int]) -> ghidra.program.model.address.Address: ...

    @overload
    def findBytes(self, __a0: ghidra.program.model.address.Address, __a1: unicode) -> ghidra.program.model.address.Address: ...

    @overload
    def findBytes(self, __a0: ghidra.program.model.address.Address, __a1: unicode, __a2: int) -> List[ghidra.program.model.address.Address]: ...

    @overload
    def findBytes(self, __a0: ghidra.program.model.address.Address, __a1: unicode, __a2: int, __a3: int) -> List[ghidra.program.model.address.Address]: ...

    @overload
    def findBytes(self, __a0: ghidra.program.model.address.AddressSetView, __a1: unicode, __a2: int, __a3: int) -> List[ghidra.program.model.address.Address]: ...

    @overload
    def findBytes(self, __a0: ghidra.program.model.address.AddressSetView, __a1: unicode, __a2: int, __a3: int, __a4: bool) -> List[ghidra.program.model.address.Address]: ...

    def findPascalStrings(self, __a0: ghidra.program.model.address.AddressSetView, __a1: int, __a2: int, __a3: bool) -> List[object]: ...

    def findStrings(self, __a0: ghidra.program.model.address.AddressSetView, __a1: int, __a2: int, __a3: bool, __a4: bool) -> List[object]: ...

    def getAddressFactory(self) -> ghidra.program.model.address.AddressFactory: ...

    def getAnalysisOptionDefaultValue(self, __a0: ghidra.program.model.listing.Program, __a1: unicode) -> unicode: ...

    def getAnalysisOptionDefaultValues(self, __a0: ghidra.program.model.listing.Program, __a1: List[object]) -> java.util.Map: ...

    def getAnalysisOptionDescription(self, __a0: ghidra.program.model.listing.Program, __a1: unicode) -> unicode: ...

    def getAnalysisOptionDescriptions(self, __a0: ghidra.program.model.listing.Program, __a1: List[object]) -> java.util.Map: ...

    def getBookmarks(self, __a0: ghidra.program.model.address.Address) -> List[ghidra.program.model.listing.Bookmark]: ...

    def getByte(self, __a0: ghidra.program.model.address.Address) -> int: ...

    def getBytes(self, __a0: ghidra.program.model.address.Address, __a1: int) -> List[int]: ...

    def getCategory(self) -> unicode: ...

    def getClass(self) -> java.lang.Class: ...

    def getCodeUnitFormat(self) -> ghidra.program.model.listing.CodeUnitFormat: ...

    def getCurrentAnalysisOptionsAndValues(self, __a0: ghidra.program.model.listing.Program) -> java.util.Map: ...

    def getCurrentProgram(self) -> ghidra.program.model.listing.Program: ...

    @overload
    def getDataAfter(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data: ...

    @overload
    def getDataAfter(self, __a0: ghidra.program.model.listing.Data) -> ghidra.program.model.listing.Data: ...

    def getDataAt(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data: ...

    @overload
    def getDataBefore(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data: ...

    @overload
    def getDataBefore(self, __a0: ghidra.program.model.listing.Data) -> ghidra.program.model.listing.Data: ...

    def getDataContaining(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data: ...

    def getDataTypes(self, __a0: unicode) -> List[ghidra.program.model.data.DataType]: ...

    def getDefaultLanguage(self, __a0: ghidra.program.model.lang.Processor) -> ghidra.program.model.lang.Language: ...

    def getDemangled(self, __a0: unicode) -> unicode: ...

    def getDestinationFunction(self, __a0: ghidra.feature.vt.api.main.VTMatch) -> ghidra.program.model.listing.Function: ...

    def getDestinationFunctions(self) -> java.util.Set: ...

    def getDouble(self, __a0: ghidra.program.model.address.Address) -> float: ...

    def getEOLComment(self, __a0: ghidra.program.model.address.Address) -> unicode: ...

    def getEOLCommentAsRendered(self, __a0: ghidra.program.model.address.Address) -> unicode: ...

    @overload
    def getEquate(self, __a0: ghidra.program.model.listing.Data) -> ghidra.program.model.symbol.Equate: ...

    @overload
    def getEquate(self, __a0: ghidra.program.model.listing.Instruction, __a1: int) -> ghidra.program.model.symbol.Equate: ...

    @overload
    def getEquate(self, __a0: ghidra.program.model.listing.Instruction, __a1: int, __a2: long) -> ghidra.program.model.symbol.Equate: ...

    def getEquates(self, __a0: ghidra.program.model.listing.Instruction, __a1: int) -> List[object]: ...

    def getFirstData(self) -> ghidra.program.model.listing.Data: ...

    def getFirstFunction(self) -> ghidra.program.model.listing.Function: ...

    @overload
    def getFirstInstruction(self) -> ghidra.program.model.listing.Instruction: ...

    @overload
    def getFirstInstruction(self, __a0: ghidra.program.model.listing.Function) -> ghidra.program.model.listing.Instruction: ...

    def getFloat(self, __a0: ghidra.program.model.address.Address) -> float: ...

    def getFragment(self, __a0: ghidra.program.model.listing.ProgramModule, __a1: unicode) -> ghidra.program.model.listing.ProgramFragment: ...

    def getFunction(self, __a0: unicode) -> ghidra.program.model.listing.Function: ...

    @overload
    def getFunctionAfter(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Function: ...

    @overload
    def getFunctionAfter(self, __a0: ghidra.program.model.listing.Function) -> ghidra.program.model.listing.Function: ...

    def getFunctionAt(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Function: ...

    @overload
    def getFunctionBefore(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Function: ...

    @overload
    def getFunctionBefore(self, __a0: ghidra.program.model.listing.Function) -> ghidra.program.model.listing.Function: ...

    def getFunctionContaining(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Function: ...

    def getGhidraVersion(self) -> unicode: ...

    def getGlobalFunctions(self, __a0: unicode) -> List[object]: ...

    @overload
    def getInstructionAfter(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Instruction: ...

    @overload
    def getInstructionAfter(self, __a0: ghidra.program.model.listing.Instruction) -> ghidra.program.model.listing.Instruction: ...

    def getInstructionAt(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Instruction: ...

    @overload
    def getInstructionBefore(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Instruction: ...

    @overload
    def getInstructionBefore(self, __a0: ghidra.program.model.listing.Instruction) -> ghidra.program.model.listing.Instruction: ...

    def getInstructionContaining(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Instruction: ...

    def getInt(self, __a0: ghidra.program.model.address.Address) -> int: ...

    def getLanguage(self, __a0: ghidra.program.model.lang.LanguageID) -> ghidra.program.model.lang.Language: ...

    def getLastData(self) -> ghidra.program.model.listing.Data: ...

    def getLastFunction(self) -> ghidra.program.model.listing.Function: ...

    def getLastInstruction(self) -> ghidra.program.model.listing.Instruction: ...

    def getLong(self, __a0: ghidra.program.model.address.Address) -> long: ...

    def getMatchesFromLastRunCorrelator(self) -> java.util.Collection: ...

    @overload
    def getMemoryBlock(self, __a0: unicode) -> ghidra.program.model.mem.MemoryBlock: ...

    @overload
    def getMemoryBlock(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.mem.MemoryBlock: ...

    def getMemoryBlocks(self) -> List[ghidra.program.model.mem.MemoryBlock]: ...

    def getMonitor(self) -> ghidra.util.task.TaskMonitor: ...

    def getNamespace(self, __a0: ghidra.program.model.symbol.Namespace, __a1: unicode) -> ghidra.program.model.symbol.Namespace: ...

    def getPlateComment(self, __a0: ghidra.program.model.address.Address) -> unicode: ...

    def getPlateCommentAsRendered(self, __a0: ghidra.program.model.address.Address) -> unicode: ...

    def getPostComment(self, __a0: ghidra.program.model.address.Address) -> unicode: ...

    def getPostCommentAsRendered(self, __a0: ghidra.program.model.address.Address) -> unicode: ...

    def getPreComment(self, __a0: ghidra.program.model.address.Address) -> unicode: ...

    def getPreCommentAsRendered(self, __a0: ghidra.program.model.address.Address) -> unicode: ...

    def getProgramCorrelators(self) -> List[object]: ...

    def getProgramFile(self) -> java.io.File: ...

    def getProjectRootFolder(self) -> ghidra.framework.model.DomainFolder: ...

    @overload
    def getReference(self, __a0: ghidra.program.model.listing.Data, __a1: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Reference: ...

    @overload
    def getReference(self, __a0: ghidra.program.model.listing.Instruction, __a1: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Reference: ...

    def getReferencesFrom(self, __a0: ghidra.program.model.address.Address) -> List[ghidra.program.model.symbol.Reference]: ...

    def getReferencesTo(self, __a0: ghidra.program.model.address.Address) -> List[ghidra.program.model.symbol.Reference]: ...

    def getRepeatableComment(self, __a0: ghidra.program.model.address.Address) -> unicode: ...

    def getRepeatableCommentAsRendered(self, __a0: ghidra.program.model.address.Address) -> unicode: ...

    def getScriptAnalysisMode(self) -> ghidra.app.script.GhidraScript.AnalysisMode: ...

    def getScriptArgs(self) -> List[unicode]: ...

    def getScriptName(self) -> unicode: ...

    def getShort(self, __a0: ghidra.program.model.address.Address) -> int: ...

    def getSourceFile(self) -> generic.jar.ResourceFile: ...

    def getSourceFunction(self, __a0: ghidra.feature.vt.api.main.VTMatch) -> ghidra.program.model.listing.Function: ...

    def getSourceFunctions(self) -> java.util.Set: ...

    def getState(self) -> ghidra.app.script.GhidraState: ...

    def getSymbol(self, __a0: unicode, __a1: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.symbol.Symbol: ...

    @overload
    def getSymbolAfter(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Symbol: ...

    @overload
    def getSymbolAfter(self, __a0: ghidra.program.model.symbol.Symbol) -> ghidra.program.model.symbol.Symbol: ...

    @overload
    def getSymbolAt(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Symbol: ...

    @overload
    def getSymbolAt(self, __a0: ghidra.program.model.address.Address, __a1: unicode) -> ghidra.program.model.symbol.Symbol: ...

    @overload
    def getSymbolAt(self, __a0: ghidra.program.model.address.Address, __a1: unicode, __a2: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.symbol.Symbol: ...

    @overload
    def getSymbolBefore(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Symbol: ...

    @overload
    def getSymbolBefore(self, __a0: ghidra.program.model.symbol.Symbol) -> ghidra.program.model.symbol.Symbol: ...

    def getSymbols(self, __a0: unicode, __a1: ghidra.program.model.symbol.Namespace) -> List[object]: ...

    def getUndefinedDataAfter(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data: ...

    def getUndefinedDataAt(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data: ...

    def getUndefinedDataBefore(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data: ...

    def getUserName(self) -> unicode: ...

    @overload
    def goTo(self, __a0: ghidra.program.model.address.Address) -> bool: ...

    @overload
    def goTo(self, __a0: ghidra.program.model.listing.Function) -> bool: ...

    @overload
    def goTo(self, __a0: ghidra.program.model.symbol.Symbol) -> bool: ...

    def hashCode(self) -> int: ...

    def importFile(self, __a0: java.io.File) -> ghidra.program.model.listing.Program: ...

    def importFileAsBinary(self, __a0: java.io.File, __a1: ghidra.program.model.lang.Language, __a2: ghidra.program.model.lang.CompilerSpec) -> ghidra.program.model.listing.Program: ...

    def isAnalysisOptionDefaultValue(self, __a0: ghidra.program.model.listing.Program, __a1: unicode, __a2: unicode) -> bool: ...

    def isRunningHeadless(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def openDataTypeArchive(self, __a0: java.io.File, __a1: bool) -> ghidra.program.model.data.FileDataTypeManager: ...

    @overload
    def openProgram(self, __a0: unicode) -> ghidra.program.model.listing.Program: ...

    @overload
    def openProgram(self, __a0: ghidra.program.model.listing.Program) -> None: ...

    def openVersionTrackingSession(self, __a0: unicode) -> None: ...

    def parseAddress(self, __a0: unicode) -> ghidra.program.model.address.Address: ...

    def parseBoolean(self, __a0: unicode) -> bool: ...

    def parseBytes(self, __a0: unicode) -> List[int]: ...

    def parseChoice(self, __a0: unicode, __a1: List[object]) -> object: ...

    @overload
    def parseChoices(self, __a0: unicode, __a1: List[object]) -> List[object]: ...

    @overload
    def parseChoices(self, __a0: unicode, __a1: List[object], __a2: List[object]) -> List[object]: ...

    def parseDirectory(self, __a0: unicode) -> java.io.File: ...

    def parseDomainFile(self, __a0: unicode) -> ghidra.framework.model.DomainFile: ...

    def parseDouble(self, __a0: unicode) -> float: ...

    def parseFile(self, __a0: unicode) -> java.io.File: ...

    def parseInt(self, __a0: unicode) -> int: ...

    def parseLanguageCompileSpecPair(self, __a0: unicode) -> ghidra.program.model.lang.LanguageCompilerSpecPair: ...

    def parseLong(self, __a0: unicode) -> long: ...

    def parseProjectFolder(self, __a0: unicode) -> ghidra.framework.model.DomainFolder: ...

    def popup(self, __a0: unicode) -> None: ...

    def print(self, __a0: unicode) -> None: ...

    def printerr(self, __a0: unicode) -> None: ...

    def printf(self, __a0: unicode, __a1: List[object]) -> None: ...

    @overload
    def println(self) -> None: ...

    @overload
    def println(self, __a0: unicode) -> None: ...

    def removeBookmark(self, __a0: ghidra.program.model.listing.Bookmark) -> None: ...

    def removeData(self, __a0: ghidra.program.model.listing.Data) -> None: ...

    def removeDataAt(self, __a0: ghidra.program.model.address.Address) -> None: ...

    def removeEntryPoint(self, __a0: ghidra.program.model.address.Address) -> None: ...

    @overload
    def removeEquate(self, __a0: ghidra.program.model.listing.Data) -> None: ...

    @overload
    def removeEquate(self, __a0: ghidra.program.model.listing.Instruction, __a1: int) -> None: ...

    @overload
    def removeEquate(self, __a0: ghidra.program.model.listing.Instruction, __a1: int, __a2: long) -> None: ...

    def removeEquates(self, __a0: ghidra.program.model.listing.Instruction, __a1: int) -> None: ...

    def removeFunction(self, __a0: ghidra.program.model.listing.Function) -> None: ...

    def removeFunctionAt(self, __a0: ghidra.program.model.address.Address) -> None: ...

    def removeHighlight(self) -> None: ...

    def removeInstruction(self, __a0: ghidra.program.model.listing.Instruction) -> None: ...

    def removeInstructionAt(self, __a0: ghidra.program.model.address.Address) -> None: ...

    def removeMemoryBlock(self, __a0: ghidra.program.model.mem.MemoryBlock) -> None: ...

    def removeReference(self, __a0: ghidra.program.model.symbol.Reference) -> None: ...

    def removeSelection(self) -> None: ...

    def removeSymbol(self, __a0: ghidra.program.model.address.Address, __a1: unicode) -> bool: ...

    def resetAllAnalysisOptions(self, __a0: ghidra.program.model.listing.Program) -> None: ...

    def resetAnalysisOption(self, __a0: ghidra.program.model.listing.Program, __a1: unicode) -> None: ...

    def resetAnalysisOptions(self, __a0: ghidra.program.model.listing.Program, __a1: List[object]) -> None: ...

    @overload
    def runCommand(self, __a0: ghidra.framework.cmd.BackgroundCommand) -> bool: ...

    @overload
    def runCommand(self, __a0: ghidra.framework.cmd.Command) -> bool: ...

    def runCorrelator(self, __a0: unicode) -> None: ...

    @overload
    def runScript(self, __a0: unicode) -> None: ...

    @overload
    def runScript(self, __a0: unicode, __a1: List[unicode]) -> None: ...

    @overload
    def runScript(self, __a0: unicode, __a1: ghidra.app.script.GhidraState) -> None: ...

    @overload
    def runScript(self, __a0: unicode, __a1: List[unicode], __a2: ghidra.app.script.GhidraState) -> None: ...

    def runScriptPreserveMyState(self, __a0: unicode) -> ghidra.app.script.GhidraState: ...

    @overload
    def saveProgram(self, __a0: ghidra.program.model.listing.Program) -> None: ...

    @overload
    def saveProgram(self, __a0: ghidra.program.model.listing.Program, __a1: List[object]) -> None: ...

    def saveSessionAs(self, __a0: unicode, __a1: unicode) -> None: ...

    def saveVersionTrackingSession(self) -> None: ...

    def set(self, __a0: ghidra.app.script.GhidraState, __a1: ghidra.util.task.TaskMonitor, __a2: java.io.PrintWriter) -> None: ...

    def setAnalysisOption(self, __a0: ghidra.program.model.listing.Program, __a1: unicode, __a2: unicode) -> None: ...

    def setAnalysisOptions(self, __a0: ghidra.program.model.listing.Program, __a1: java.util.Map) -> None: ...

    def setAnonymousServerCredentials(self) -> bool: ...

    @overload
    def setBackgroundColor(self, __a0: ghidra.program.model.address.Address, __a1: java.awt.Color) -> None: ...

    @overload
    def setBackgroundColor(self, __a0: ghidra.program.model.address.AddressSetView, __a1: java.awt.Color) -> None: ...

    def setByte(self, __a0: ghidra.program.model.address.Address, __a1: int) -> None: ...

    def setBytes(self, __a0: ghidra.program.model.address.Address, __a1: List[int]) -> None: ...

    def setCurrentHighlight(self, __a0: ghidra.program.model.address.AddressSetView) -> None: ...

    def setCurrentLocation(self, __a0: ghidra.program.model.address.Address) -> None: ...

    def setCurrentSelection(self, __a0: ghidra.program.model.address.AddressSetView) -> None: ...

    def setDouble(self, __a0: ghidra.program.model.address.Address, __a1: float) -> None: ...

    def setEOLComment(self, __a0: ghidra.program.model.address.Address, __a1: unicode) -> bool: ...

    def setFloat(self, __a0: ghidra.program.model.address.Address, __a1: float) -> None: ...

    def setInt(self, __a0: ghidra.program.model.address.Address, __a1: int) -> None: ...

    def setLong(self, __a0: ghidra.program.model.address.Address, __a1: long) -> None: ...

    def setPlateComment(self, __a0: ghidra.program.model.address.Address, __a1: unicode) -> bool: ...

    def setPostComment(self, __a0: ghidra.program.model.address.Address, __a1: unicode) -> bool: ...

    def setPotentialPropertiesFileLocations(self, __a0: List[object]) -> None: ...

    def setPreComment(self, __a0: ghidra.program.model.address.Address, __a1: unicode) -> bool: ...

    def setPropertiesFile(self, __a0: java.io.File) -> None: ...

    def setPropertiesFileLocation(self, __a0: unicode, __a1: unicode) -> None: ...

    @overload
    def setReferencePrimary(self, __a0: ghidra.program.model.symbol.Reference) -> None: ...

    @overload
    def setReferencePrimary(self, __a0: ghidra.program.model.symbol.Reference, __a1: bool) -> None: ...

    def setRepeatableComment(self, __a0: ghidra.program.model.address.Address, __a1: unicode) -> bool: ...

    def setScriptArgs(self, __a0: List[unicode]) -> None: ...

    def setServerCredentials(self, __a0: unicode, __a1: unicode) -> bool: ...

    def setShort(self, __a0: ghidra.program.model.address.Address, __a1: int) -> None: ...

    def setSourceFile(self, __a0: generic.jar.ResourceFile) -> None: ...

    def setToolStatusMessage(self, __a0: unicode, __a1: bool) -> None: ...

    @overload
    def show(self, __a0: List[ghidra.program.model.address.Address]) -> None: ...

    @overload
    def show(self, __a0: unicode, __a1: ghidra.program.model.address.AddressSetView) -> None: ...

    def start(self) -> None: ...

    @overload
    def toAddr(self, __a0: long) -> ghidra.program.model.address.Address: ...

    @overload
    def toAddr(self, __a0: int) -> ghidra.program.model.address.Address: ...

    @overload
    def toAddr(self, __a0: unicode) -> ghidra.program.model.address.Address: ...

    @overload
    def toHexString(self, __a0: long, __a1: bool, __a2: bool) -> unicode: ...

    @overload
    def toHexString(self, __a0: int, __a1: bool, __a2: bool) -> unicode: ...

    @overload
    def toHexString(self, __a0: int, __a1: bool, __a2: bool) -> unicode: ...

    @overload
    def toHexString(self, __a0: int, __a1: bool, __a2: bool) -> unicode: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def destinationFunctions(self) -> java.util.Set: ...

    @property
    def matchesFromLastRunCorrelator(self) -> java.util.Collection: ...

    @property
    def programCorrelators(self) -> List[object]: ...

    @property
    def sourceFunctions(self) -> java.util.Set: ...
