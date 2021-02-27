from typing import List
import ghidra.app.plugin.processors.sleigh
import ghidra.app.plugin.processors.sleigh.SleighInstructionPrototype
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.mem
import ghidra.program.model.pcode
import ghidra.program.model.scalar
import ghidra.program.model.symbol
import java.lang


class SleighInstructionPrototype(object, ghidra.program.model.lang.InstructionPrototype):
    """
    The InstructionPrototype for sleigh languages.
     The prototype is unique up to the tree of Constructors.
     Variations in the bit pattern that none of the Constructor
     mask/values care about get lumped under the same prototype
    """

    BRANCH_INDIRECT: int = 4
    BRANCH_TO_END: int = 64
    CALL: int = 8
    CALL_INDIRECT: int = 2
    CROSSBUILD: int = 128
    INVALID_DEPTH_CHANGE: int = 16777216
    JUMPOUT: int = 16
    LABEL: int = 256
    NO_FALLTHRU: int = 32
    RETURN: int = 1




    class FlowSummary(object):
        delay: int
        flowState: java.util.ArrayList
        hasCrossBuilds: bool
        lastop: ghidra.app.plugin.processors.sleigh.template.OpTpl



        def __init__(self): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class FlowRecord(object):
        addressnode: ghidra.app.plugin.processors.sleigh.ConstructState
        flowFlags: int
        op: ghidra.app.plugin.processors.sleigh.template.OpTpl



        def __init__(self): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self, lang: ghidra.app.plugin.processors.sleigh.SleighLanguage, buf: ghidra.program.model.mem.MemBuffer, context: ghidra.program.model.lang.ProcessorContextView, cache: ghidra.app.plugin.processors.sleigh.ContextCache, inDelaySlot: bool, debug: ghidra.app.plugin.processors.sleigh.SleighDebugLogger): ...



    def dumpConstructorTree(self) -> unicode:
        """
        Used for testing and diagnostics: list the constructor line numbers used to resolve this
         encoding

         This includes braces to describe the tree structure
        @see AssemblyResolvedConstructor#dumpConstructorTree()
        @return the constructor tree
        """
        ...

    def equals(self, obj: object) -> bool: ...

    @staticmethod
    def flowListToFlowType(__a0: List[object]) -> ghidra.program.model.symbol.FlowType: ...

    def getAddress(self, opIndex: int, context: ghidra.program.model.lang.InstructionContext) -> ghidra.program.model.address.Address: ...

    def getClass(self) -> java.lang.Class: ...

    def getDelaySlotByteCount(self) -> int: ...

    def getDelaySlotDepth(self, context: ghidra.program.model.lang.InstructionContext) -> int: ...

    def getFallThrough(self, context: ghidra.program.model.lang.InstructionContext) -> ghidra.program.model.address.Address: ...

    def getFallThroughOffset(self, context: ghidra.program.model.lang.InstructionContext) -> int: ...

    def getFlowType(self, context: ghidra.program.model.lang.InstructionContext) -> ghidra.program.model.symbol.FlowType: ...

    def getFlows(self, context: ghidra.program.model.lang.InstructionContext) -> List[ghidra.program.model.address.Address]: ...

    def getInputObjects(self, context: ghidra.program.model.lang.InstructionContext) -> List[object]: ...

    def getInstructionMask(self) -> ghidra.program.model.lang.Mask: ...

    def getLanguage(self) -> ghidra.program.model.lang.Language: ...

    def getLength(self) -> int: ...

    def getMnemonic(self, context: ghidra.program.model.lang.InstructionContext) -> unicode: ...

    def getNumOperands(self) -> int: ...

    def getOpObjects(self, opIndex: int, context: ghidra.program.model.lang.InstructionContext) -> List[object]: ...

    def getOpRepresentationList(self, opIndex: int, context: ghidra.program.model.lang.InstructionContext) -> List[object]: ...

    def getOpType(self, opIndex: int, context: ghidra.program.model.lang.InstructionContext) -> int: ...

    def getOperandRefType(self, opIndex: int, context: ghidra.program.model.lang.InstructionContext, override: ghidra.program.model.pcode.PcodeOverride, uniqueFactory: ghidra.program.model.address.UniqueAddressFactory) -> ghidra.program.model.symbol.RefType: ...

    def getOperandValueMask(self, operandIndex: int) -> ghidra.program.model.lang.Mask: ...

    def getParserContext(self, buf: ghidra.program.model.mem.MemBuffer, processorContext: ghidra.program.model.lang.ProcessorContextView) -> ghidra.app.plugin.processors.sleigh.SleighParserContext: ...

    @overload
    def getPcode(self, context: ghidra.program.model.lang.InstructionContext, opIndex: int) -> List[ghidra.program.model.pcode.PcodeOp]: ...

    @overload
    def getPcode(self, context: ghidra.program.model.lang.InstructionContext, override: ghidra.program.model.pcode.PcodeOverride, uniqueFactory: ghidra.program.model.address.UniqueAddressFactory) -> List[ghidra.program.model.pcode.PcodeOp]: ...

    def getPcodePacked(self, context: ghidra.program.model.lang.InstructionContext, override: ghidra.program.model.pcode.PcodeOverride, uniqueFactory: ghidra.program.model.address.UniqueAddressFactory) -> ghidra.program.model.lang.PackedBytes: ...

    def getPseudoParserContext(self, addr: ghidra.program.model.address.Address, buffer: ghidra.program.model.mem.MemBuffer, processorContext: ghidra.program.model.lang.ProcessorContextView) -> ghidra.program.model.lang.ParserContext: ...

    def getRegister(self, opIndex: int, context: ghidra.program.model.lang.InstructionContext) -> ghidra.program.model.lang.Register: ...

    def getResultObjects(self, context: ghidra.program.model.lang.InstructionContext) -> List[object]: ...

    def getScalar(self, opIndex: int, context: ghidra.program.model.lang.InstructionContext) -> ghidra.program.model.scalar.Scalar: ...

    def getSeparator(self, opIndex: int, context: ghidra.program.model.lang.InstructionContext) -> unicode: ...

    def hasCrossBuildDependency(self) -> bool: ...

    def hasDelaySlots(self) -> bool: ...

    def hasDelimeter(self, opIndex: int) -> bool: ...

    def hashCode(self) -> int: ...

    def isInDelaySlot(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @staticmethod
    def walkTemplates(walker: ghidra.app.plugin.processors.sleigh.OpTplWalker) -> ghidra.app.plugin.processors.sleigh.SleighInstructionPrototype.FlowSummary:
        """
        Walk the pcode templates in the order they would be emitted.
         Collect flowFlags FlowRecords
        @param walker the pcode template walker
        """
        ...

    @property
    def delaySlotByteCount(self) -> int: ...

    @property
    def inDelaySlot(self) -> bool: ...

    @property
    def instructionMask(self) -> ghidra.program.model.lang.Mask: ...

    @property
    def language(self) -> ghidra.program.model.lang.Language: ...

    @property
    def length(self) -> int: ...

    @property
    def numOperands(self) -> int: ...
