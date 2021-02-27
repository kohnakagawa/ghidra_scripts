from typing import Iterator
from typing import List
import db
import ghidra.program.database.code
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


class InstructionDB(ghidra.program.database.code.CodeUnitDB, ghidra.program.model.listing.Instruction, ghidra.program.model.lang.InstructionContext):
    """
    Database implementation for an Instruction.
    """





    def __init__(self, codeMgr: ghidra.program.database.code.CodeManager, cache: ghidra.program.database.DBObjectCache, address: ghidra.program.model.address.Address, addr: long, proto: ghidra.program.model.lang.InstructionPrototype, flags: int):
        """
        Construct a new InstructionDB.
        @param codeMgr code manager
        @param cache code unit cache
        @param address min address of this instruction
        @param addr database key
        @param proto instruction prototype
        @param flags flow override flags
        """
        ...



    def addMnemonicReference(self, refAddr: ghidra.program.model.address.Address, refType: ghidra.program.model.symbol.RefType, sourceType: ghidra.program.model.symbol.SourceType) -> None: ...

    def addOperandReference(self, opIndex: int, refAddr: ghidra.program.model.address.Address, type: ghidra.program.model.symbol.RefType, sourceType: ghidra.program.model.symbol.SourceType) -> None:
        """
        @see ghidra.program.model.listing.CodeUnit#addOperandReference(int,
              ghidra.program.model.address.Address,
              ghidra.program.model.symbol.RefType, SourceType)
        """
        ...

    def checkDeleted(self) -> None:
        """
        Checks if this object has been deleted, in which case any use of the object is not allowed.
        @throws ConcurrentModificationException if the object has been deleted from the database.
        """
        ...

    @overload
    def checkIsValid(self) -> bool:
        """
        Check whether this object is still valid. If the object is invalid, the object will attempt
         to refresh itself. If the refresh fails, the object will be marked as deleted.
        @return true if the object is valid.
        """
        ...

    @overload
    def checkIsValid(self, record: db.Record) -> bool:
        """
        Check whether this object is still valid. If the object is invalid, the object will attempt
         to refresh itself using the specified record. If the refresh fails, the object will be marked
         as deleted and removed from cache. If this object is already marked as deleted, the record
         can not be used to refresh the object.
        @param record optional record which may be used to refresh invalid object
        @return true if the object is valid.
        """
        ...

    def clearFallThroughOverride(self) -> None: ...

    def clearRegister(self, register: ghidra.program.model.lang.Register) -> None: ...

    def compareTo(self, a: ghidra.program.model.address.Address) -> int: ...

    def contains(self, testAddr: ghidra.program.model.address.Address) -> bool: ...

    @overload
    @staticmethod
    def dumpContextValue(__a0: ghidra.program.model.lang.RegisterValue, __a1: unicode) -> unicode: ...

    @overload
    @staticmethod
    def dumpContextValue(__a0: ghidra.program.model.lang.RegisterValue, __a1: unicode, __a2: java.lang.StringBuilder) -> None: ...

    def equals(self, obj: object) -> bool:
        """
        Return true if obj is equal to this.
        """
        ...

    @overload
    def getAddress(self) -> ghidra.program.model.address.Address: ...

    @overload
    def getAddress(self, opIndex: int) -> ghidra.program.model.address.Address: ...

    def getAddressString(self, showBlockName: bool, pad: bool) -> unicode: ...

    def getBaseContextRegister(self) -> ghidra.program.model.lang.Register: ...

    def getBigInteger(self, offset: int, size: int, signed: bool) -> long: ...

    def getByte(self, offset: int) -> int: ...

    @overload
    def getBytes(self) -> List[int]: ...

    @overload
    def getBytes(self, b: List[int], offset: int) -> int: ...

    def getBytesInCodeUnit(self, buffer: List[int], bufferOffset: int) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self, commentType: int) -> unicode: ...

    def getCommentAsArray(self, commentType: int) -> List[unicode]: ...

    def getDefaultFallThrough(self) -> ghidra.program.model.address.Address: ...

    def getDefaultFallThroughOffset(self) -> int: ...

    def getDefaultFlows(self) -> List[ghidra.program.model.address.Address]: ...

    def getDefaultOperandRepresentation(self, opIndex: int) -> unicode: ...

    def getDefaultOperandRepresentationList(self, opIndex: int) -> List[object]: ...

    def getDelaySlotDepth(self) -> int: ...

    def getExternalReference(self, opIndex: int) -> ghidra.program.model.symbol.ExternalReference: ...

    def getFallFrom(self) -> ghidra.program.model.address.Address: ...

    def getFallThrough(self) -> ghidra.program.model.address.Address: ...

    def getFlowOverride(self) -> ghidra.program.model.listing.FlowOverride: ...

    def getFlowType(self) -> ghidra.program.model.symbol.FlowType: ...

    def getFlows(self) -> List[ghidra.program.model.address.Address]: ...

    def getInputObjects(self) -> List[object]: ...

    def getInstructionContext(self) -> ghidra.program.model.lang.InstructionContext: ...

    def getInt(self, offset: int) -> int: ...

    def getIntProperty(self, name: unicode) -> int: ...

    def getKey(self) -> long:
        """
        Get the database key for this object.
        """
        ...

    def getLabel(self) -> unicode: ...

    def getLength(self) -> int: ...

    def getLong(self, offset: int) -> long: ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address: ...

    def getMemBuffer(self) -> ghidra.program.model.mem.MemBuffer: ...

    def getMemory(self) -> ghidra.program.model.mem.Memory: ...

    def getMinAddress(self) -> ghidra.program.model.address.Address: ...

    def getMnemonicReferences(self) -> List[ghidra.program.model.symbol.Reference]: ...

    def getMnemonicString(self) -> unicode: ...

    def getNext(self) -> ghidra.program.model.listing.Instruction: ...

    def getNumOperands(self) -> int: ...

    def getObjectProperty(self, name: unicode) -> ghidra.util.Saveable: ...

    def getOpObjects(self, opIndex: int) -> List[object]: ...

    def getOperandRefType(self, opIndex: int) -> ghidra.program.model.symbol.RefType: ...

    def getOperandReferences(self, opIndex: int) -> List[ghidra.program.model.symbol.Reference]: ...

    def getOperandType(self, opIndex: int) -> int: ...

    def getOriginalPrototypeContext(self, baseContextReg: ghidra.program.model.lang.Register) -> ghidra.program.model.lang.RegisterValue:
        """
        Get the original context used to establish the shared prototype
        @param baseContextReg
        @return prototype context value
        """
        ...

    @overload
    def getParserContext(self) -> ghidra.program.model.lang.ParserContext: ...

    @overload
    def getParserContext(self, instructionAddress: ghidra.program.model.address.Address) -> ghidra.program.model.lang.ParserContext: ...

    @overload
    def getPcode(self) -> List[ghidra.program.model.pcode.PcodeOp]: ...

    @overload
    def getPcode(self, opIndex: int) -> List[ghidra.program.model.pcode.PcodeOp]: ...

    @overload
    def getPcode(self, includeOverrides: bool) -> List[ghidra.program.model.pcode.PcodeOp]: ...

    def getPrevious(self) -> ghidra.program.model.listing.Instruction: ...

    def getPrimaryReference(self, index: int) -> ghidra.program.model.symbol.Reference: ...

    def getPrimarySymbol(self) -> ghidra.program.model.symbol.Symbol: ...

    def getProcessorContext(self) -> ghidra.program.model.lang.ProcessorContextView: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def getPrototype(self) -> ghidra.program.model.lang.InstructionPrototype: ...

    def getReferenceIteratorTo(self) -> ghidra.program.model.symbol.ReferenceIterator: ...

    def getReferencesFrom(self) -> List[ghidra.program.model.symbol.Reference]: ...

    @overload
    def getRegister(self, opIndex: int) -> ghidra.program.model.lang.Register: ...

    @overload
    def getRegister(self, name: unicode) -> ghidra.program.model.lang.Register: ...

    def getRegisterValue(self, register: ghidra.program.model.lang.Register) -> ghidra.program.model.lang.RegisterValue: ...

    def getRegisters(self) -> List[ghidra.program.model.lang.Register]: ...

    def getResultObjects(self) -> List[object]: ...

    def getScalar(self, opIndex: int) -> ghidra.program.model.scalar.Scalar: ...

    def getSeparator(self, opIndex: int) -> unicode: ...

    def getShort(self, offset: int) -> int: ...

    def getStringProperty(self, name: unicode) -> unicode: ...

    def getSymbols(self) -> List[ghidra.program.model.symbol.Symbol]: ...

    def getUnsignedByte(self, __a0: int) -> int: ...

    def getUnsignedInt(self, __a0: int) -> long: ...

    def getUnsignedShort(self, __a0: int) -> int: ...

    def getValue(self, register: ghidra.program.model.lang.Register, signed: bool) -> long: ...

    def getVarLengthInt(self, __a0: int, __a1: int) -> int: ...

    def getVarLengthUnsignedInt(self, __a0: int, __a1: int) -> long: ...

    def getVoidProperty(self, name: unicode) -> bool: ...

    def hasFallthrough(self) -> bool: ...

    def hasProperty(self, name: unicode) -> bool: ...

    def hasValue(self, register: ghidra.program.model.lang.Register) -> bool: ...

    def hashCode(self) -> int: ...

    def isBigEndian(self) -> bool: ...

    def isDeleted(self) -> bool:
        """
        Returns true if this object has been deleted. Note: once an object has been deleted, it will
         never be "refreshed". For example, if an object is ever deleted and is resurrected via an
         "undo", you will have get a fresh instance of the object.
        @return true if this object has been deleted.
        """
        ...

    def isFallThroughOverridden(self) -> bool: ...

    def isFallthrough(self) -> bool: ...

    def isInDelaySlot(self) -> bool: ...

    def isInitializedMemory(self) -> bool: ...

    def isInvalid(self) -> bool:
        """
        Returns true if object is currently invalid. Calling checkIsValid may successfully refresh
         object making it valid.
        @see #checkIsValid()
        """
        ...

    def isSuccessor(self, codeUnit: ghidra.program.model.listing.CodeUnit) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def propertyNames(self) -> Iterator[unicode]: ...

    def removeExternalReference(self, opIndex: int) -> None: ...

    def removeMnemonicReference(self, refAddr: ghidra.program.model.address.Address) -> None: ...

    def removeOperandReference(self, opIndex: int, refAddr: ghidra.program.model.address.Address) -> None: ...

    def removeProperty(self, name: unicode) -> None: ...

    def setComment(self, commentType: int, comment: unicode) -> None: ...

    def setCommentAsArray(self, commentType: int, comment: List[unicode]) -> None: ...

    def setFallThrough(self, fallThroughAddr: ghidra.program.model.address.Address) -> None: ...

    def setFlowOverride(self, flow: ghidra.program.model.listing.FlowOverride) -> None: ...

    def setInvalid(self) -> None:
        """
        Invalidate this object. This does not necessarily mean that this object can never be used
         again. If the object can refresh itself, it may still be useable.
        """
        ...

    def setPrimaryMemoryReference(self, ref: ghidra.program.model.symbol.Reference) -> None: ...

    @overload
    def setProperty(self, name: unicode) -> None: ...

    @overload
    def setProperty(self, name: unicode, value: int) -> None: ...

    @overload
    def setProperty(self, name: unicode, value: unicode) -> None: ...

    @overload
    def setProperty(self, name: unicode, value: ghidra.util.Saveable) -> None: ...

    def setRegisterReference(self, opIndex: int, reg: ghidra.program.model.lang.Register, sourceType: ghidra.program.model.symbol.SourceType, refType: ghidra.program.model.symbol.RefType) -> None: ...

    def setRegisterValue(self, value: ghidra.program.model.lang.RegisterValue) -> None: ...

    def setStackReference(self, opIndex: int, offset: int, sourceType: ghidra.program.model.symbol.SourceType, refType: ghidra.program.model.symbol.RefType) -> None: ...

    def setValue(self, register: ghidra.program.model.lang.Register, value: long) -> None: ...

    def toString(self) -> unicode: ...

    def validate(self, lock: ghidra.util.Lock) -> bool:
        """
        This method provides a cheap (lock free) way to test if an object is valid. If this object is
         invalid, then the lock will be used to refresh as needed.
        @param lock the lock that will be used if the object needs to be refreshed.
        @return true if object is valid, else false
        """
        ...

    def visitProperty(self, visitor: ghidra.util.prop.PropertyVisitor, propertyName: unicode) -> None: ...

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
    def memBuffer(self) -> ghidra.program.model.mem.MemBuffer: ...

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
    def parserContext(self) -> ghidra.program.model.lang.ParserContext: ...

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
    def processorContext(self) -> ghidra.program.model.lang.ProcessorContextView: ...

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
