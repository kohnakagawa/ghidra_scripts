from typing import List
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.mem
import ghidra.program.model.pcode
import ghidra.program.model.scalar
import ghidra.program.model.symbol
import ghidra.util
import ghidra.util.prop
import java.lang
import java.util


class Instruction(ghidra.program.model.listing.CodeUnit, ghidra.program.model.lang.ProcessorContext, object):
    """
    Interface to define an instruction for a processor.
    """

    COMMENT_PROPERTY: unicode = u'COMMENT__GHIDRA_'
    DEFINED_DATA_PROPERTY: unicode = u'DEFINED_DATA__GHIDRA_'
    EOL_COMMENT: int = 0
    INSTRUCTION_PROPERTY: unicode = u'INSTRUCTION__GHIDRA_'
    INVALID_DEPTH_CHANGE: int = 16777216
    MNEMONIC: int = -1
    NO_COMMENT: int = -1
    PLATE_COMMENT: int = 3
    POST_COMMENT: int = 2
    PRE_COMMENT: int = 1
    REPEATABLE_COMMENT: int = 4
    SPACE_PROPERTY: unicode = u'Space'







    def addMnemonicReference(self, __a0: ghidra.program.model.address.Address, __a1: ghidra.program.model.symbol.RefType, __a2: ghidra.program.model.symbol.SourceType) -> None: ...

    def addOperandReference(self, __a0: int, __a1: ghidra.program.model.address.Address, __a2: ghidra.program.model.symbol.RefType, __a3: ghidra.program.model.symbol.SourceType) -> None: ...

    def clearFallThroughOverride(self) -> None:
        """
        Restores this instruction's fallthrough address back to the default fallthrough
         for this instruction.
        """
        ...

    def clearRegister(self, __a0: ghidra.program.model.lang.Register) -> None: ...

    def compareTo(self, __a0: ghidra.program.model.address.Address) -> int: ...

    def contains(self, __a0: ghidra.program.model.address.Address) -> bool: ...

    @overload
    @staticmethod
    def dumpContextValue(__a0: ghidra.program.model.lang.RegisterValue, __a1: unicode) -> unicode: ...

    @overload
    @staticmethod
    def dumpContextValue(__a0: ghidra.program.model.lang.RegisterValue, __a1: unicode, __a2: java.lang.StringBuilder) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    def getAddress(self) -> ghidra.program.model.address.Address: ...

    @overload
    def getAddress(self, __a0: int) -> ghidra.program.model.address.Address: ...

    def getAddressString(self, __a0: bool, __a1: bool) -> unicode: ...

    def getBaseContextRegister(self) -> ghidra.program.model.lang.Register: ...

    def getBigInteger(self, __a0: int, __a1: int, __a2: bool) -> long: ...

    def getByte(self, __a0: int) -> int: ...

    @overload
    def getBytes(self) -> List[int]: ...

    @overload
    def getBytes(self, __a0: List[int], __a1: int) -> int: ...

    def getBytesInCodeUnit(self, __a0: List[int], __a1: int) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self, __a0: int) -> unicode: ...

    def getCommentAsArray(self, __a0: int) -> List[unicode]: ...

    def getDefaultFallThrough(self) -> ghidra.program.model.address.Address:
        """
        Get the default fallthrough for this instruction.
         This accounts for any instructions contained with delay slots.
        @return fall-through address or null if instruction has no default fallthrough
        """
        ...

    def getDefaultFallThroughOffset(self) -> int:
        """
        Get default fall-through offset in bytes from start of instruction to the
         fallthrough instruction.  This accounts for any
         instructions contained with delay slots.
        @return default fall-through offset or zero (0) if instruction has no fallthrough
        """
        ...

    def getDefaultFlows(self) -> List[ghidra.program.model.address.Address]:
        """
        Get an array of Address objects for all default flows established
         by the underlying instruction prototype.  References are ignored.
        @return flow addresses or null if there are no flows
        """
        ...

    def getDefaultOperandRepresentation(self, opIndex: int) -> unicode:
        """
        Get the operand representation for the given operand index without markup.
        @param opIndex operand index
        @return operand represented as a string.
        """
        ...

    def getDefaultOperandRepresentationList(self, opIndex: int) -> List[object]:
        """
        Get the operand representation for the given operand index.
         A list of Register, Address, Scalar, Character and String objects is returned - without markup!
        @param opIndex operand index
        @return ArrayList of pieces of the operand representation.  Unsupported languages may return null.
        """
        ...

    def getDelaySlotDepth(self) -> int:
        """
        Get the number of delay slot instructions for this
         argument. This should be 0 for instructions which don't have a
         delay slot.  This is used to support the delay slots found on
         some RISC processors such as SPARC and the PA-RISC. This
         returns an integer instead of a boolean in case some other
         processor executes more than one instruction from a delay slot.
        """
        ...

    def getExternalReference(self, __a0: int) -> ghidra.program.model.symbol.ExternalReference: ...

    def getFallFrom(self) -> ghidra.program.model.address.Address:
        """
        Get the Address for the instruction that fell through to
         this instruction.
         This is useful for handling instructions that are found
         in a delay slot.
        """
        ...

    def getFallThrough(self) -> ghidra.program.model.address.Address:
        """
        Get the fallthrough for this instruction, factoring in
         any fallthrough override and delay slotted instructions.
        @return fall-through address or null if instruction has no fallthrough
        """
        ...

    def getFlowOverride(self) -> ghidra.program.model.listing.FlowOverride:
        """
        Returns the flow override which may have been set on this instruction.
        """
        ...

    def getFlowType(self) -> ghidra.program.model.symbol.FlowType:
        """
        Get the flow type of this instruction (how this
         instruction flows to the next instruction).
        """
        ...

    def getFlows(self) -> List[ghidra.program.model.address.Address]:
        """
        Get an array of Address objects for all flows other than
         a fall-through.  This will include any flow references which
         have been added to the instruction.
        @return flow addresses or null if there are no flows
        """
        ...

    def getInputObjects(self) -> List[object]:
        """
        Get the Input objects used by this instruction.
         These could be Scalars, Registers, Addresses
        @return an array of objects that are used by this instruction
        """
        ...

    def getInstructionContext(self) -> ghidra.program.model.lang.InstructionContext:
        """
        @return the instruction context for this instruction
        """
        ...

    def getInt(self, __a0: int) -> int: ...

    def getIntProperty(self, __a0: unicode) -> int: ...

    def getLabel(self) -> unicode: ...

    def getLength(self) -> int: ...

    def getLong(self, __a0: int) -> long: ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address: ...

    def getMemory(self) -> ghidra.program.model.mem.Memory: ...

    def getMinAddress(self) -> ghidra.program.model.address.Address: ...

    def getMnemonicReferences(self) -> List[ghidra.program.model.symbol.Reference]: ...

    def getMnemonicString(self) -> unicode: ...

    def getNext(self) -> ghidra.program.model.listing.Instruction:
        """
        Get the instruction following this one in address order.
        """
        ...

    def getNumOperands(self) -> int: ...

    def getObjectProperty(self, __a0: unicode) -> ghidra.util.Saveable: ...

    def getOpObjects(self, opIndex: int) -> List[object]:
        """
        Get objects used by this operand (Address, Scalar, Register ...)
        @param opIndex index of the operand.
        """
        ...

    def getOperandRefType(self, index: int) -> ghidra.program.model.symbol.RefType:
        """
        Get the operand reference type for the given operand index.
        @param index operand index
        """
        ...

    def getOperandReferences(self, __a0: int) -> List[ghidra.program.model.symbol.Reference]: ...

    def getOperandType(self, opIndex: int) -> int:
        """
        Get the type of a specific operand.
        @param opIndex the index of the operand. (zero based)
        @return the type of the operand.
        @see OperandType
        """
        ...

    @overload
    def getPcode(self) -> List[ghidra.program.model.pcode.PcodeOp]:
        """
        Get an array of PCode operations (micro code) that this instruction
         performs.  Flow overrides are not factored into pcode.
        @return an array of Pcode operations,
                 a zero length array if the language does not support PCode
        """
        ...

    @overload
    def getPcode(self, opIndex: int) -> List[ghidra.program.model.pcode.PcodeOp]:
        """
        Get an array of PCode operations (micro code) that a particular operand
         performs to compute its value.
        @param opIndex index of the operand to retrieve PCode
        @return an array of PCode operations,
                 a zero length array if the language does not support PCode
        """
        ...

    @overload
    def getPcode(self, includeOverrides: bool) -> List[ghidra.program.model.pcode.PcodeOp]:
        """
        Get an array of PCode operations (micro code) that this instruction
         performs.  NOTE: If includeOverrides is true, unique temporary varnodes
         may be produced which vary in size to those produced for other instructions.
         If your analysis is sensitive to this you should consider using
         {@link InstructionPrototype#getPcode(InstructionContext, PcodeOverride, UniqueAddressFactory)}
         instead with your own {@link UniqueAddressFactory} to prevent duplication within
         your scope of analysis.
         by this method may not be suitable for use with certain analysis
        @param includeOverrides if true any flow overrides will be factored
         into generated pcode.
        @return an array of Pcode operations,
                 a zero length array if the language does not support PCode
        """
        ...

    def getPrevious(self) -> ghidra.program.model.listing.Instruction:
        """
        Get the instruction before this one in address order.
        """
        ...

    def getPrimaryReference(self, __a0: int) -> ghidra.program.model.symbol.Reference: ...

    def getPrimarySymbol(self) -> ghidra.program.model.symbol.Symbol: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def getPrototype(self) -> ghidra.program.model.lang.InstructionPrototype:
        """
        Get the prototype for this instruction.
        """
        ...

    def getReferenceIteratorTo(self) -> ghidra.program.model.symbol.ReferenceIterator: ...

    def getReferencesFrom(self) -> List[ghidra.program.model.symbol.Reference]: ...

    @overload
    def getRegister(self, opIndex: int) -> ghidra.program.model.lang.Register:
        """
        If operand is a pure Register, return the register.
        @param opIndex index of the operand.
        @return A register if the operand represents a register.
        """
        ...

    @overload
    def getRegister(self, __a0: unicode) -> ghidra.program.model.lang.Register: ...

    def getRegisterValue(self, __a0: ghidra.program.model.lang.Register) -> ghidra.program.model.lang.RegisterValue: ...

    def getRegisters(self) -> List[object]: ...

    def getResultObjects(self) -> List[object]:
        """
        Get the Result objects produced/affected by this instruction
         These would probably only be Register or Address
        @return an array of objects that are affected by this instruction
        """
        ...

    def getScalar(self, __a0: int) -> ghidra.program.model.scalar.Scalar: ...

    def getSeparator(self, opIndex: int) -> unicode:
        """
        Get the separator strings between an operand.

         The separator string for 0 are the characters before the first operand.
         The separator string for numOperands+1 are the characters after the last operand.
        @param opIndex valid values are 0 thru numOperands+1
        @return separator string, or null if there is no string
        """
        ...

    def getShort(self, __a0: int) -> int: ...

    def getStringProperty(self, __a0: unicode) -> unicode: ...

    def getSymbols(self) -> List[ghidra.program.model.symbol.Symbol]: ...

    def getUnsignedByte(self, __a0: int) -> int: ...

    def getUnsignedInt(self, __a0: int) -> long: ...

    def getUnsignedShort(self, __a0: int) -> int: ...

    def getValue(self, __a0: ghidra.program.model.lang.Register, __a1: bool) -> long: ...

    def getVarLengthInt(self, __a0: int, __a1: int) -> int: ...

    def getVarLengthUnsignedInt(self, __a0: int, __a1: int) -> long: ...

    def getVoidProperty(self, __a0: unicode) -> bool: ...

    def hasFallthrough(self) -> bool:
        """
        Returns true if this instruction has a fall-through flow.
        """
        ...

    def hasProperty(self, __a0: unicode) -> bool: ...

    def hasValue(self, __a0: ghidra.program.model.lang.Register) -> bool: ...

    def hashCode(self) -> int: ...

    def isBigEndian(self) -> bool: ...

    def isFallThroughOverridden(self) -> bool:
        """
        Returns true if this instructions fallthrough has been overriden.
        """
        ...

    def isFallthrough(self) -> bool:
        """
        Returns true if this instruction has no execution flow other than fall-through.
        """
        ...

    def isInDelaySlot(self) -> bool:
        """
        Return true if this instruction was disassembled in a delay slot
        """
        ...

    def isInitializedMemory(self) -> bool: ...

    def isSuccessor(self, __a0: ghidra.program.model.listing.CodeUnit) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def propertyNames(self) -> java.util.Iterator: ...

    def removeExternalReference(self, __a0: int) -> None: ...

    def removeMnemonicReference(self, __a0: ghidra.program.model.address.Address) -> None: ...

    def removeOperandReference(self, __a0: int, __a1: ghidra.program.model.address.Address) -> None: ...

    def removeProperty(self, __a0: unicode) -> None: ...

    def setComment(self, __a0: int, __a1: unicode) -> None: ...

    def setCommentAsArray(self, __a0: int, __a1: List[unicode]) -> None: ...

    def setFallThrough(self, addr: ghidra.program.model.address.Address) -> None:
        """
        Overrides the instruction's default fallthrough address to the given address.
         The given address may be null to indicate that the instruction has no fallthrough.
        @param addr the address to be used as this instructions fallthrough address.  May be null.
        """
        ...

    def setFlowOverride(self, flowOverride: ghidra.program.model.listing.FlowOverride) -> None:
        """
        Set the flow override for this instruction.
        @param flowOverride
        """
        ...

    def setPrimaryMemoryReference(self, __a0: ghidra.program.model.symbol.Reference) -> None: ...

    @overload
    def setProperty(self, __a0: unicode) -> None: ...

    @overload
    def setProperty(self, __a0: unicode, __a1: int) -> None: ...

    @overload
    def setProperty(self, __a0: unicode, __a1: unicode) -> None: ...

    @overload
    def setProperty(self, __a0: unicode, __a1: ghidra.util.Saveable) -> None: ...

    def setRegisterReference(self, __a0: int, __a1: ghidra.program.model.lang.Register, __a2: ghidra.program.model.symbol.SourceType, __a3: ghidra.program.model.symbol.RefType) -> None: ...

    def setRegisterValue(self, __a0: ghidra.program.model.lang.RegisterValue) -> None: ...

    def setStackReference(self, __a0: int, __a1: int, __a2: ghidra.program.model.symbol.SourceType, __a3: ghidra.program.model.symbol.RefType) -> None: ...

    def setValue(self, __a0: ghidra.program.model.lang.Register, __a1: long) -> None: ...

    def toString(self) -> unicode: ...

    def visitProperty(self, __a0: ghidra.util.prop.PropertyVisitor, __a1: unicode) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def baseContextRegister(self) -> ghidra.program.model.lang.Register: ...

    @property
    def bigEndian(self) -> bool: ...

    @property
    def bytes(self) -> List[int]: ...

    @property
    def defaultFallThrough(self) -> ghidra.program.model.address.Address: ...

    @property
    def defaultFallThroughOffset(self) -> int: ...

    @property
    def defaultFlows(self) -> List[ghidra.program.model.address.Address]: ...

    @property
    def delaySlotDepth(self) -> int: ...

    @property
    def fallFrom(self) -> ghidra.program.model.address.Address: ...

    @property
    def fallThrough(self) -> ghidra.program.model.address.Address: ...

    @fallThrough.setter
    def fallThrough(self, value: ghidra.program.model.address.Address) -> None: ...

    @property
    def fallThroughOverridden(self) -> bool: ...

    @property
    def fallthrough(self) -> bool: ...

    @property
    def flowOverride(self) -> ghidra.program.model.listing.FlowOverride: ...

    @flowOverride.setter
    def flowOverride(self, value: ghidra.program.model.listing.FlowOverride) -> None: ...

    @property
    def flowType(self) -> ghidra.program.model.symbol.FlowType: ...

    @property
    def flows(self) -> List[ghidra.program.model.address.Address]: ...

    @property
    def inDelaySlot(self) -> bool: ...

    @property
    def initializedMemory(self) -> bool: ...

    @property
    def inputObjects(self) -> List[object]: ...

    @property
    def instructionContext(self) -> ghidra.program.model.lang.InstructionContext: ...

    @property
    def label(self) -> unicode: ...

    @property
    def length(self) -> int: ...

    @property
    def maxAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def memory(self) -> ghidra.program.model.mem.Memory: ...

    @property
    def minAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def mnemonicReferences(self) -> List[ghidra.program.model.symbol.Reference]: ...

    @property
    def mnemonicString(self) -> unicode: ...

    @property
    def next(self) -> ghidra.program.model.listing.Instruction: ...

    @property
    def numOperands(self) -> int: ...

    @property
    def pcode(self) -> List[ghidra.program.model.pcode.PcodeOp]: ...

    @property
    def previous(self) -> ghidra.program.model.listing.Instruction: ...

    @property
    def primaryMemoryReference(self) -> None: ...  # No getter available.

    @primaryMemoryReference.setter
    def primaryMemoryReference(self, value: ghidra.program.model.symbol.Reference) -> None: ...

    @property
    def primarySymbol(self) -> ghidra.program.model.symbol.Symbol: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...

    @property
    def property(self) -> None: ...  # No getter available.

    @property.setter
    def property(self, value: unicode) -> None: ...

    @property
    def prototype(self) -> ghidra.program.model.lang.InstructionPrototype: ...

    @property
    def referenceIteratorTo(self) -> ghidra.program.model.symbol.ReferenceIterator: ...

    @property
    def referencesFrom(self) -> List[ghidra.program.model.symbol.Reference]: ...

    @property
    def registerValue(self) -> None: ...  # No getter available.

    @registerValue.setter
    def registerValue(self, value: ghidra.program.model.lang.RegisterValue) -> None: ...

    @property
    def registers(self) -> List[object]: ...

    @property
    def resultObjects(self) -> List[object]: ...

    @property
    def symbols(self) -> List[ghidra.program.model.symbol.Symbol]: ...
