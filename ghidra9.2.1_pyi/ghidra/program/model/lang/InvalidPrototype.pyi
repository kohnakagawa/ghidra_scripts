from typing import List
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.mem
import ghidra.program.model.pcode
import ghidra.program.model.scalar
import ghidra.program.model.symbol
import java.lang


class InvalidPrototype(object, ghidra.program.model.lang.InstructionPrototype, ghidra.program.model.lang.ParserContext):
    """
    Class to represent an invalid instruction prototype.
    """

    INVALID_DEPTH_CHANGE: int = 16777216



    def __init__(self, lang: ghidra.program.model.lang.Language):
        """
        Construct a new invalid instruction prototype.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

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

    def getOpRepresentation(self, opIndex: int, buf: ghidra.program.model.mem.MemBuffer, context: ghidra.program.model.lang.ProcessorContextView, label: unicode) -> unicode: ...

    def getOpRepresentationList(self, opIndex: int, context: ghidra.program.model.lang.InstructionContext) -> List[object]: ...

    def getOpType(self, opIndex: int, context: ghidra.program.model.lang.InstructionContext) -> int: ...

    def getOperandRefType(self, opIndex: int, context: ghidra.program.model.lang.InstructionContext, override: ghidra.program.model.pcode.PcodeOverride, uniqueFactory: ghidra.program.model.address.UniqueAddressFactory) -> ghidra.program.model.symbol.RefType: ...

    def getOperandValueMask(self, operandIndex: int) -> ghidra.program.model.lang.Mask: ...

    def getParserContext(self, buf: ghidra.program.model.mem.MemBuffer, processorContext: ghidra.program.model.lang.ProcessorContextView) -> ghidra.program.model.lang.ParserContext: ...

    @overload
    def getPcode(self, context: ghidra.program.model.lang.InstructionContext, opIndex: int) -> List[ghidra.program.model.pcode.PcodeOp]: ...

    @overload
    def getPcode(self, context: ghidra.program.model.lang.InstructionContext, override: ghidra.program.model.pcode.PcodeOverride, uniqueFactory: ghidra.program.model.address.UniqueAddressFactory) -> List[ghidra.program.model.pcode.PcodeOp]: ...

    def getPcodePacked(self, context: ghidra.program.model.lang.InstructionContext, override: ghidra.program.model.pcode.PcodeOverride, uniqueFactory: ghidra.program.model.address.UniqueAddressFactory) -> ghidra.program.model.lang.PackedBytes: ...

    def getPrototype(self) -> ghidra.program.model.lang.InstructionPrototype: ...

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

    @property
    def prototype(self) -> ghidra.program.model.lang.InstructionPrototype: ...