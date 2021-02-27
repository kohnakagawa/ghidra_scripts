from typing import List
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.mem
import ghidra.program.model.pcode
import ghidra.program.model.scalar
import ghidra.program.model.symbol
import java.lang


class InstructionPrototype(object):
    """
    InstructionPrototype is designed to describe one machine level instruction.
     A language parser can return the same InstructionProtoype object for the
     same type node. Prototypes for instructions will normally be fixed for a node.
    """

    INVALID_DEPTH_CHANGE: int = 16777216







    def equals(self, __a0: object) -> bool: ...

    def getAddress(self, opIndex: int, context: ghidra.program.model.lang.InstructionContext) -> ghidra.program.model.address.Address:
        """
        If the indicated operand is an address, this gets the address value for
         that operand
        @param opIndex index of the operand.
        @param context the instruction context.
        @return the address indicated by the operand
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDelaySlotByteCount(self) -> int:
        """
        @return the number of delay-slot instruction bytes which correspond
         to this prototype.
        """
        ...

    def getDelaySlotDepth(self, context: ghidra.program.model.lang.InstructionContext) -> int:
        """
        Get the number of delay slot instructions for this
         argument. This should be 0 for instructions which don't have a
         delay slot.  This is used to support the delay slots found on
         some RISC processors such as SPARC and the PA-RISC. This
         returns an integer instead of a boolean in case some other
         processor executes more than one instruction from a delay slot.
        @param context the instruction context
        @return the number of delay slot instructions for this instruction.
        """
        ...

    def getFallThrough(self, context: ghidra.program.model.lang.InstructionContext) -> ghidra.program.model.address.Address:
        """
        Get the Address for default flow after instruction.
        @param context the instruction context
        @return Address of fall through flow or null if flow
         does not fall through this instruction.
        """
        ...

    def getFallThroughOffset(self, context: ghidra.program.model.lang.InstructionContext) -> int:
        """
        Get the byte offset to the default flow after instruction.
         If this instruction does not have a fall-through due to flow
         behavior, this method will still return an offset which accounts for
         the instruction length including delay slotted instructions if
         applicable.
        @param context the instruction context
        @return int how much to add to the current address to get
         the fall through address.
        """
        ...

    def getFlowType(self, context: ghidra.program.model.lang.InstructionContext) -> ghidra.program.model.symbol.FlowType:
        """
        Get the flow type of this instruction. Used
         for analysis purposes. i.e., how this
         instruction flows to the next instruction.
        @param context the instruction context
        @return flow type.
        """
        ...

    def getFlows(self, context: ghidra.program.model.lang.InstructionContext) -> List[ghidra.program.model.address.Address]:
        """
        Get an array of Address objects for all flows other than
         a fall-through, null if no flows.
        @param context the instruction context.
        @return an array of Address objects for all flows other than
          a fall-through, null if no flows.
        """
        ...

    def getInputObjects(self, context: ghidra.program.model.lang.InstructionContext) -> List[object]:
        """
        Get the Result objects produced/affected by this instruction
         These would probably only be Register or Address
        @param context the instruction context
        @return an array of objects that are used by this instruction
        """
        ...

    def getInstructionMask(self) -> ghidra.program.model.lang.Mask:
        """
        Get a Mask that describe which bits of this instruction determine
         the opcode.
        @return a Mask for the opcode bits or null if unknown.
        """
        ...

    def getLanguage(self) -> ghidra.program.model.lang.Language:
        """
        Get processor language module associated with this prototype.
        @return language module
        """
        ...

    def getLength(self) -> int:
        """
        Get the length of this CodeProtoype.
        @return the length of this CodeProtoype.
        """
        ...

    def getMnemonic(self, context: ghidra.program.model.lang.InstructionContext) -> unicode:
        """
        Get the mnemonic for this CodeProtype.  Examples: "MOV" and
         "CALL" for instructions and "DB" and "DA" for data.
        @param context the instruction context
        @return the mnemonic for this CodePrototype.
        """
        ...

    def getNumOperands(self) -> int:
        """
        Return the number of operands in this instruction.
        """
        ...

    def getOpObjects(self, opIndex: int, context: ghidra.program.model.lang.InstructionContext) -> List[object]:
        """
        Get objects used by this operand (Address, Scalar, Register ...)
        @param opIndex the index of the operand. (zero based)
        @param context the instruction context
        @return an array of objects found at this operand.
        """
        ...

    def getOpRepresentationList(self, opIndex: int, context: ghidra.program.model.lang.InstructionContext) -> List[object]:
        """
        Get a List of Objects that can be used to render an operands representation.
        @param opIndex operand to get the Representation List
        @param context the instruction context
        @return ArrayList of Register, Address, Scalar, VariableOffset and Character objects
                 of null if the operation isn't supported
        """
        ...

    def getOpType(self, opIndex: int, context: ghidra.program.model.lang.InstructionContext) -> int:
        """
        Get the type of a specific operand.
        @param opIndex the index of the operand. (zero based)
        @param context the instruction context.
        @return the type of the operand.
        """
        ...

    def getOperandRefType(self, opIndex: int, context: ghidra.program.model.lang.InstructionContext, override: ghidra.program.model.pcode.PcodeOverride, uniqueFactory: ghidra.program.model.address.UniqueAddressFactory) -> ghidra.program.model.symbol.RefType:
        """
        Get the suggested operand reference type.
        @param opIndex the index of the operand. (zero based)
        @param context the instruction context
        @param override if not null, steers local overrides of pcode generation
        @param uniqueFactory must be specified if flowOverride is not null
        @return reference type.
        """
        ...

    def getOperandValueMask(self, operandIndex: int) -> ghidra.program.model.lang.Mask:
        """
        Get a Mask that describe which bits of this instruction determine
         the operand value.
        @return a Mask for the operand bits or null if unknown.
        """
        ...

    def getParserContext(self, buf: ghidra.program.model.mem.MemBuffer, processorContext: ghidra.program.model.lang.ProcessorContextView) -> ghidra.program.model.lang.ParserContext:
        """
        Get a new instance of a ParserContext.
        @param buf
        @param processorContext
        @return instruction ParserContext
        @throws MemoryAccessException
        """
        ...

    @overload
    def getPcode(self, context: ghidra.program.model.lang.InstructionContext, opIndex: int) -> List[ghidra.program.model.pcode.PcodeOp]:
        """
        Get an array of PCode operations (micro code) that a particular operand
         performs to compute its value.
        @param context the instruction context
        @param opIndex the index of the operand for which to get PCode.
        @return array of PCODE,
                 zero length array if language doesn't support PCODE for this instruction
        """
        ...

    @overload
    def getPcode(self, context: ghidra.program.model.lang.InstructionContext, override: ghidra.program.model.pcode.PcodeOverride, uniqueFactory: ghidra.program.model.address.UniqueAddressFactory) -> List[ghidra.program.model.pcode.PcodeOp]:
        """
        Get an array of PCode operations (micro code) that this instruction
         performs.
        @param context the instruction context
        @param override if not null, may indicate that different elements of the pcode generation are overridden
        @param uniqueFactory must be specified if flowOverride is not null
        @return array of PCODE,
                 zero length array if language doesn't support PCODE for this instruction
        """
        ...

    def getPcodePacked(self, context: ghidra.program.model.lang.InstructionContext, override: ghidra.program.model.pcode.PcodeOverride, uniqueFactory: ghidra.program.model.address.UniqueAddressFactory) -> ghidra.program.model.lang.PackedBytes:
        """
        Same as getPcode but returns the operations in a packed format to optimize transfer to other processes
        @param context the instruction context
        @param override if not null, may indicate that different elements of the pcode generation are overridden
        @param uniqueFactory must be specified if flowOverride is not null
        @return
        """
        ...

    def getPseudoParserContext(self, addr: ghidra.program.model.address.Address, buffer: ghidra.program.model.mem.MemBuffer, processorContext: ghidra.program.model.lang.ProcessorContextView) -> ghidra.program.model.lang.ParserContext:
        """
        Get a ParserContext by parsing bytes outside of the normal disassembly process
        @param addr where the ParserContext is needed
        @param buffer of actual bytes
        @param processorContext
        @return
        @throws InsufficientBytesException
        @throws UnknownInstructionException
        @throws UnknownContextException
        @throws MemoryAccessException
        """
        ...

    def getRegister(self, opIndex: int, context: ghidra.program.model.lang.InstructionContext) -> ghidra.program.model.lang.Register:
        """
        If the indicated operand is a register, this gets the register value
         for that operand
        @param opIndex index of the operand.
        @param context the instruction context
        @return a register description for the indicated operand
        """
        ...

    def getResultObjects(self, context: ghidra.program.model.lang.InstructionContext) -> List[object]:
        """
        Get the Result objects produced/affected by this instruction
         These would probably only be Register or Address
        @param context the instruction context
        @return an array of objects that are affected by this instruction
        """
        ...

    def getScalar(self, opIndex: int, context: ghidra.program.model.lang.InstructionContext) -> ghidra.program.model.scalar.Scalar:
        """
        If the indicated operand is a scalar, this gets the scalar value for
         that operand
        @param opIndex index of the operand.
        @param context the instruction context
        @return the scalar for the indicated operand
        """
        ...

    def getSeparator(self, opIndex: int, context: ghidra.program.model.lang.InstructionContext) -> unicode:
        """
        Get the separator strings between an operand.

         The separator string for 0 are the characters before the first operand.
         The separator string for numOperands+1 are the characters after the last operand.
        @param opIndex valid values are 0 thru numOperands+1
        @param context the instruction context
        @return separator string, or null if there is no string
        """
        ...

    def hasCrossBuildDependency(self) -> bool:
        """
        @return true if instruction semantics have a CrossBuild instruction
         dependency which may require a robust InstructionContext with access
         to preceding instructions
        """
        ...

    def hasDelaySlots(self) -> bool:
        """
        @return true if instruction prototype expects one or more delay slotted
         instructions to exist.
        """
        ...

    def hasDelimeter(self, opIndex: int) -> bool:
        """
        Return true if the operand at opIndex should have a delimiter following it.
        @param opIndex the index of the operand to test for having a delimiter.
        """
        ...

    def hashCode(self) -> int: ...

    def isInDelaySlot(self) -> bool:
        """
        Return true if this prototype was disassembled in a delay slot.
        """
        ...

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
