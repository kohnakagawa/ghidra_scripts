from typing import List
import generic.stl
import ghidra.pcodeCPort.opcodes
import ghidra.pcodeCPort.semantics
import ghidra.pcodeCPort.slgh_compile
import ghidra.pcodeCPort.slghsymbol
import ghidra.pcodeCPort.space
import ghidra.sleigh.grammar
import java.lang


class PcodeParser(ghidra.pcodeCPort.slgh_compile.PcodeCompile):
    log: org.apache.logging.log4j.Logger = ghidra.pcodeCPort.slgh_compile.PcodeParser:DEBUG in 75412c2f
    noplist: generic.stl.VectorSTL



    def __init__(self, __a0: unicode): ...



    def addOperand(self, __a0: ghidra.sleigh.grammar.Location, __a1: unicode, __a2: int) -> None: ...

    def addSymbol(self, __a0: ghidra.pcodeCPort.slghsymbol.SleighSymbol) -> None: ...

    def addressOf(self, __a0: ghidra.pcodeCPort.semantics.VarnodeTpl, __a1: int) -> ghidra.pcodeCPort.semantics.VarnodeTpl: ...

    def allocateTemp(self) -> long: ...

    def appendOp(self, __a0: ghidra.sleigh.grammar.Location, __a1: ghidra.pcodeCPort.opcodes.OpCode, __a2: ghidra.pcodeCPort.slgh_compile.ExprTree, __a3: long, __a4: int) -> None: ...

    def assignBitRange(self, __a0: ghidra.sleigh.grammar.Location, __a1: ghidra.pcodeCPort.semantics.VarnodeTpl, __a2: int, __a3: int, __a4: ghidra.pcodeCPort.slgh_compile.ExprTree) -> generic.stl.VectorSTL: ...

    def buildTemporary(self, __a0: ghidra.sleigh.grammar.Location) -> ghidra.pcodeCPort.semantics.VarnodeTpl: ...

    def buildTruncatedVarnode(self, __a0: ghidra.sleigh.grammar.Location, __a1: ghidra.pcodeCPort.semantics.VarnodeTpl, __a2: int, __a3: int) -> ghidra.pcodeCPort.semantics.VarnodeTpl: ...

    def clearSymbols(self) -> None: ...

    def compilePcode(self, __a0: unicode, __a1: unicode, __a2: int) -> ghidra.pcodeCPort.semantics.ConstructTpl: ...

    def createBitRange(self, __a0: ghidra.sleigh.grammar.Location, __a1: ghidra.pcodeCPort.slghsymbol.SpecificSymbol, __a2: int, __a3: int) -> ghidra.pcodeCPort.slgh_compile.ExprTree: ...

    def createCrossBuild(self, __a0: ghidra.sleigh.grammar.Location, __a1: ghidra.pcodeCPort.semantics.VarnodeTpl, __a2: ghidra.pcodeCPort.slghsymbol.SectionSymbol) -> generic.stl.VectorSTL: ...

    def createLoad(self, __a0: ghidra.sleigh.grammar.Location, __a1: ghidra.pcodeCPort.slgh_compile.StarQuality, __a2: ghidra.pcodeCPort.slgh_compile.ExprTree) -> ghidra.pcodeCPort.slgh_compile.ExprTree: ...

    def createMacroUse(self, __a0: ghidra.sleigh.grammar.Location, __a1: ghidra.pcodeCPort.slghsymbol.MacroSymbol, __a2: generic.stl.VectorSTL) -> generic.stl.VectorSTL: ...

    @overload
    def createOp(self, __a0: ghidra.sleigh.grammar.Location, __a1: ghidra.pcodeCPort.opcodes.OpCode, __a2: ghidra.pcodeCPort.slgh_compile.ExprTree) -> ghidra.pcodeCPort.slgh_compile.ExprTree: ...

    @overload
    def createOp(self, __a0: ghidra.sleigh.grammar.Location, __a1: ghidra.pcodeCPort.opcodes.OpCode, __a2: ghidra.pcodeCPort.slgh_compile.ExprTree, __a3: ghidra.pcodeCPort.slgh_compile.ExprTree) -> ghidra.pcodeCPort.slgh_compile.ExprTree: ...

    def createOpConst(self, __a0: ghidra.sleigh.grammar.Location, __a1: ghidra.pcodeCPort.opcodes.OpCode, __a2: long) -> generic.stl.VectorSTL: ...

    @overload
    def createOpNoOut(self, __a0: ghidra.sleigh.grammar.Location, __a1: ghidra.pcodeCPort.opcodes.OpCode, __a2: ghidra.pcodeCPort.slgh_compile.ExprTree) -> generic.stl.VectorSTL: ...

    @overload
    def createOpNoOut(self, __a0: ghidra.sleigh.grammar.Location, __a1: ghidra.pcodeCPort.opcodes.OpCode, __a2: ghidra.pcodeCPort.slgh_compile.ExprTree, __a3: ghidra.pcodeCPort.slgh_compile.ExprTree) -> generic.stl.VectorSTL: ...

    def createOpOut(self, __a0: ghidra.sleigh.grammar.Location, __a1: ghidra.pcodeCPort.semantics.VarnodeTpl, __a2: ghidra.pcodeCPort.opcodes.OpCode, __a3: ghidra.pcodeCPort.slgh_compile.ExprTree, __a4: ghidra.pcodeCPort.slgh_compile.ExprTree) -> ghidra.pcodeCPort.slgh_compile.ExprTree: ...

    def createOpOutUnary(self, __a0: ghidra.sleigh.grammar.Location, __a1: ghidra.pcodeCPort.semantics.VarnodeTpl, __a2: ghidra.pcodeCPort.opcodes.OpCode, __a3: ghidra.pcodeCPort.slgh_compile.ExprTree) -> ghidra.pcodeCPort.slgh_compile.ExprTree: ...

    def createStore(self, __a0: ghidra.sleigh.grammar.Location, __a1: ghidra.pcodeCPort.slgh_compile.StarQuality, __a2: ghidra.pcodeCPort.slgh_compile.ExprTree, __a3: ghidra.pcodeCPort.slgh_compile.ExprTree) -> generic.stl.VectorSTL: ...

    def createUserOp(self, __a0: ghidra.pcodeCPort.slghsymbol.UserOpSymbol, __a1: generic.stl.VectorSTL) -> ghidra.pcodeCPort.slgh_compile.ExprTree: ...

    def createUserOpNoOut(self, __a0: ghidra.sleigh.grammar.Location, __a1: ghidra.pcodeCPort.slghsymbol.UserOpSymbol, __a2: generic.stl.VectorSTL) -> generic.stl.VectorSTL: ...

    def createVariadic(self, __a0: ghidra.sleigh.grammar.Location, __a1: ghidra.pcodeCPort.opcodes.OpCode, __a2: generic.stl.VectorSTL) -> ghidra.pcodeCPort.slgh_compile.ExprTree: ...

    def defineLabel(self, __a0: ghidra.sleigh.grammar.Location, __a1: unicode) -> ghidra.pcodeCPort.slghsymbol.LabelSymbol: ...

    @staticmethod
    def entry(__a0: unicode, __a1: List[object]) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def fillinZero(self, __a0: ghidra.pcodeCPort.semantics.OpTpl, __a1: generic.stl.VectorSTL) -> None: ...

    def finalNamedSection(self, __a0: ghidra.pcodeCPort.slgh_compile.SectionVector, __a1: ghidra.pcodeCPort.semantics.ConstructTpl) -> ghidra.pcodeCPort.slgh_compile.SectionVector: ...

    def findInternalFunction(self, __a0: ghidra.sleigh.grammar.Location, __a1: unicode, __a2: generic.stl.VectorSTL) -> object: ...

    def findSymbol(self, __a0: unicode) -> ghidra.pcodeCPort.slghsymbol.SleighSymbol: ...

    def firstNamedSection(self, __a0: ghidra.pcodeCPort.semantics.ConstructTpl, __a1: ghidra.pcodeCPort.slghsymbol.SectionSymbol) -> ghidra.pcodeCPort.slgh_compile.SectionVector: ...

    def getClass(self) -> java.lang.Class: ...

    def getConstantSpace(self) -> ghidra.pcodeCPort.space.AddrSpace: ...

    def getDefaultSpace(self) -> ghidra.pcodeCPort.space.AddrSpace: ...

    def getErrors(self) -> int: ...

    def getUniqueSpace(self) -> ghidra.pcodeCPort.space.AddrSpace: ...

    def getWarnings(self) -> int: ...

    def hashCode(self) -> int: ...

    def isInternalFunction(self, __a0: unicode) -> bool: ...

    def matchSize(self, __a0: int, __a1: ghidra.pcodeCPort.semantics.OpTpl, __a2: bool, __a3: generic.stl.VectorSTL) -> None: ...

    @overload
    def newLocalDefinition(self, __a0: ghidra.sleigh.grammar.Location, __a1: unicode) -> None: ...

    @overload
    def newLocalDefinition(self, __a0: ghidra.sleigh.grammar.Location, __a1: unicode, __a2: int) -> None: ...

    @overload
    def newOutput(self, __a0: ghidra.sleigh.grammar.Location, __a1: bool, __a2: ghidra.pcodeCPort.slgh_compile.ExprTree, __a3: unicode) -> generic.stl.VectorSTL: ...

    @overload
    def newOutput(self, __a0: ghidra.sleigh.grammar.Location, __a1: bool, __a2: ghidra.pcodeCPort.slgh_compile.ExprTree, __a3: unicode, __a4: int) -> generic.stl.VectorSTL: ...

    def newSectionSymbol(self, __a0: ghidra.sleigh.grammar.Location, __a1: unicode) -> ghidra.pcodeCPort.slghsymbol.SectionSymbol: ...

    def nextNamedSection(self, __a0: ghidra.pcodeCPort.slgh_compile.SectionVector, __a1: ghidra.pcodeCPort.semantics.ConstructTpl, __a2: ghidra.pcodeCPort.slghsymbol.SectionSymbol) -> ghidra.pcodeCPort.slgh_compile.SectionVector: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def placeLabel(self, __a0: ghidra.sleigh.grammar.Location, __a1: ghidra.pcodeCPort.slghsymbol.LabelSymbol) -> generic.stl.VectorSTL: ...

    def propagateSize(self, __a0: ghidra.pcodeCPort.semantics.ConstructTpl) -> bool: ...

    def recordNop(self, __a0: ghidra.sleigh.grammar.Location) -> None: ...

    def reportError(self, __a0: ghidra.sleigh.grammar.Location, __a1: unicode) -> None: ...

    def reportWarning(self, __a0: ghidra.sleigh.grammar.Location, __a1: unicode) -> None: ...

    def resetLabelCount(self) -> None: ...

    def setEnforceLocalKey(self, __a0: bool) -> None: ...

    def setResultStarVarnode(self, __a0: ghidra.pcodeCPort.semantics.ConstructTpl, __a1: ghidra.pcodeCPort.slgh_compile.StarQuality, __a2: ghidra.pcodeCPort.semantics.VarnodeTpl) -> ghidra.pcodeCPort.semantics.ConstructTpl: ...

    def setResultVarnode(self, __a0: ghidra.pcodeCPort.semantics.ConstructTpl, __a1: ghidra.pcodeCPort.semantics.VarnodeTpl) -> ghidra.pcodeCPort.semantics.ConstructTpl: ...

    def standaloneSection(self, __a0: ghidra.pcodeCPort.semantics.ConstructTpl) -> ghidra.pcodeCPort.slgh_compile.SectionVector: ...

    @staticmethod
    def stringifyTemplate(__a0: ghidra.pcodeCPort.semantics.ConstructTpl) -> unicode: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def constantSpace(self) -> ghidra.pcodeCPort.space.AddrSpace: ...

    @property
    def defaultSpace(self) -> ghidra.pcodeCPort.space.AddrSpace: ...

    @property
    def uniqueSpace(self) -> ghidra.pcodeCPort.space.AddrSpace: ...
