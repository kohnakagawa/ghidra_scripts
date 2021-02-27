from typing import Iterator
from typing import List
import ghidra.docking.settings
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.mem
import ghidra.program.model.scalar
import ghidra.program.model.symbol
import ghidra.util
import ghidra.util.prop
import java.lang


class DataStub(object, ghidra.program.model.listing.Data):
    """
    DataStub can be extended for use by tests. It throws an UnsupportedOperationException
     for all methods in the Data interface. Any method that is needed for your test can then
     be overridden so it can provide its own test implementation and return value.
    """

    COMMENT_PROPERTY: unicode = u'COMMENT__GHIDRA_'
    DEFINED_DATA_PROPERTY: unicode = u'DEFINED_DATA__GHIDRA_'
    EOL_COMMENT: int = 0
    INSTRUCTION_PROPERTY: unicode = u'INSTRUCTION__GHIDRA_'
    MNEMONIC: int = -1
    NO_COMMENT: int = -1
    PLATE_COMMENT: int = 3
    POST_COMMENT: int = 2
    PRE_COMMENT: int = 1
    REPEATABLE_COMMENT: int = 4
    SPACE_PROPERTY: unicode = u'Space'



    def __init__(self): ...



    def addMnemonicReference(self, refAddr: ghidra.program.model.address.Address, refType: ghidra.program.model.symbol.RefType, sourceType: ghidra.program.model.symbol.SourceType) -> None: ...

    def addOperandReference(self, index: int, refAddr: ghidra.program.model.address.Address, type: ghidra.program.model.symbol.RefType, sourceType: ghidra.program.model.symbol.SourceType) -> None: ...

    def addValueReference(self, refAddr: ghidra.program.model.address.Address, type: ghidra.program.model.symbol.RefType) -> None: ...

    def clearAllSettings(self) -> None: ...

    def clearSetting(self, name: unicode) -> None: ...

    def compareTo(self, addr: ghidra.program.model.address.Address) -> int: ...

    def contains(self, testAddr: ghidra.program.model.address.Address) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    def getAddress(self) -> ghidra.program.model.address.Address: ...

    @overload
    def getAddress(self, opIndex: int) -> ghidra.program.model.address.Address: ...

    def getAddressString(self, showBlockName: bool, pad: bool) -> unicode: ...

    def getBaseDataType(self) -> ghidra.program.model.data.DataType: ...

    def getBigInteger(self, offset: int, size: int, signed: bool) -> long: ...

    def getByte(self, offset: int) -> int: ...

    def getByteArray(self, name: unicode) -> List[int]: ...

    @overload
    def getBytes(self) -> List[int]: ...

    @overload
    def getBytes(self, b: List[int], memoryBufferOffset: int) -> int: ...

    def getBytesInCodeUnit(self, buffer: List[int], bufferOffset: int) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self, commentType: int) -> unicode: ...

    def getCommentAsArray(self, commentType: int) -> List[unicode]: ...

    @overload
    def getComponent(self, index: int) -> ghidra.program.model.listing.Data: ...

    @overload
    def getComponent(self, componentPath: List[int]) -> ghidra.program.model.listing.Data: ...

    def getComponentAt(self, offset: int) -> ghidra.program.model.listing.Data: ...

    def getComponentIndex(self) -> int: ...

    def getComponentLevel(self) -> int: ...

    def getComponentPath(self) -> List[int]: ...

    def getComponentPathName(self) -> unicode: ...

    def getComponentsContaining(self, offset: int) -> List[ghidra.program.model.listing.Data]: ...

    def getDataType(self) -> ghidra.program.model.data.DataType: ...

    def getDefaultLabelPrefix(self, options: ghidra.program.model.data.DataTypeDisplayOptions) -> unicode: ...

    def getDefaultSettings(self) -> ghidra.docking.settings.Settings: ...

    def getDefaultValueRepresentation(self) -> unicode: ...

    def getExternalReference(self, opIndex: int) -> ghidra.program.model.symbol.ExternalReference: ...

    def getFieldName(self) -> unicode: ...

    def getInt(self, offset: int) -> int: ...

    def getIntProperty(self, name: unicode) -> int: ...

    def getLabel(self) -> unicode: ...

    def getLength(self) -> int: ...

    @overload
    def getLong(self, offset: int) -> long: ...

    @overload
    def getLong(self, name: unicode) -> long: ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address: ...

    def getMemory(self) -> ghidra.program.model.mem.Memory: ...

    def getMinAddress(self) -> ghidra.program.model.address.Address: ...

    def getMnemonicReferences(self) -> List[ghidra.program.model.symbol.Reference]: ...

    def getMnemonicString(self) -> unicode: ...

    def getNames(self) -> List[unicode]: ...

    def getNumComponents(self) -> int: ...

    def getNumOperands(self) -> int: ...

    def getObjectProperty(self, name: unicode) -> ghidra.util.Saveable: ...

    def getOperandReferences(self, index: int) -> List[ghidra.program.model.symbol.Reference]: ...

    def getParent(self) -> ghidra.program.model.listing.Data: ...

    def getParentOffset(self) -> int: ...

    def getPathName(self) -> unicode: ...

    def getPrimaryReference(self, index: int) -> ghidra.program.model.symbol.Reference: ...

    def getPrimarySymbol(self) -> ghidra.program.model.symbol.Symbol: ...

    def getPrimitiveAt(self, offset: int) -> ghidra.program.model.listing.Data: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def getReferenceIteratorTo(self) -> ghidra.program.model.symbol.ReferenceIterator: ...

    def getReferencesFrom(self) -> List[ghidra.program.model.symbol.Reference]: ...

    def getRoot(self) -> ghidra.program.model.listing.Data: ...

    def getRootOffset(self) -> int: ...

    def getScalar(self, opIndex: int) -> ghidra.program.model.scalar.Scalar: ...

    def getShort(self, offset: int) -> int: ...

    def getString(self, name: unicode) -> unicode: ...

    def getStringProperty(self, name: unicode) -> unicode: ...

    def getSymbols(self) -> List[ghidra.program.model.symbol.Symbol]: ...

    def getUnsignedByte(self, __a0: int) -> int: ...

    def getUnsignedInt(self, __a0: int) -> long: ...

    def getUnsignedShort(self, __a0: int) -> int: ...

    @overload
    def getValue(self) -> object: ...

    @overload
    def getValue(self, name: unicode) -> object: ...

    def getValueClass(self) -> java.lang.Class: ...

    def getValueReferences(self) -> List[ghidra.program.model.symbol.Reference]: ...

    def getVarLengthInt(self, __a0: int, __a1: int) -> int: ...

    def getVarLengthUnsignedInt(self, __a0: int, __a1: int) -> long: ...

    def getVoidProperty(self, name: unicode) -> bool: ...

    def hasProperty(self, name: unicode) -> bool: ...

    def hasStringValue(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isArray(self) -> bool: ...

    def isBigEndian(self) -> bool: ...

    def isConstant(self) -> bool: ...

    def isDefined(self) -> bool: ...

    def isDynamic(self) -> bool: ...

    def isEmpty(self) -> bool: ...

    def isInitializedMemory(self) -> bool: ...

    def isPointer(self) -> bool: ...

    def isStructure(self) -> bool: ...

    def isSuccessor(self, codeUnit: ghidra.program.model.listing.CodeUnit) -> bool: ...

    def isUnion(self) -> bool: ...

    def isVolatile(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def propertyNames(self) -> Iterator[unicode]: ...

    def removeExternalReference(self, opIndex: int) -> None: ...

    def removeMnemonicReference(self, refAddr: ghidra.program.model.address.Address) -> None: ...

    def removeOperandReference(self, index: int, refAddr: ghidra.program.model.address.Address) -> None: ...

    def removeProperty(self, name: unicode) -> None: ...

    def removeValueReference(self, refAddr: ghidra.program.model.address.Address) -> None: ...

    def setByteArray(self, name: unicode, value: List[int]) -> None: ...

    def setComment(self, commentType: int, comment: unicode) -> None: ...

    def setCommentAsArray(self, commentType: int, comment: List[unicode]) -> None: ...

    def setLong(self, name: unicode, value: long) -> None: ...

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

    def setStackReference(self, opIndex: int, offset: int, sourceType: ghidra.program.model.symbol.SourceType, refType: ghidra.program.model.symbol.RefType) -> None: ...

    def setString(self, name: unicode, value: unicode) -> None: ...

    def setValue(self, name: unicode, value: object) -> None: ...

    def toString(self) -> unicode: ...

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
    def array(self) -> bool: ...

    @property
    def baseDataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def bigEndian(self) -> bool: ...

    @property
    def bytes(self) -> List[int]: ...

    @property
    def componentIndex(self) -> int: ...

    @property
    def componentLevel(self) -> int: ...

    @property
    def componentPath(self) -> List[int]: ...

    @property
    def componentPathName(self) -> unicode: ...

    @property
    def constant(self) -> bool: ...

    @property
    def dataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def defaultSettings(self) -> ghidra.docking.settings.Settings: ...

    @property
    def defaultValueRepresentation(self) -> unicode: ...

    @property
    def defined(self) -> bool: ...

    @property
    def dynamic(self) -> bool: ...

    @property
    def empty(self) -> bool: ...

    @property
    def fieldName(self) -> unicode: ...

    @property
    def initializedMemory(self) -> bool: ...

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
    def names(self) -> List[unicode]: ...

    @property
    def numComponents(self) -> int: ...

    @property
    def numOperands(self) -> int: ...

    @property
    def parent(self) -> ghidra.program.model.listing.Data: ...

    @property
    def parentOffset(self) -> int: ...

    @property
    def pathName(self) -> unicode: ...

    @property
    def pointer(self) -> bool: ...

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
    def referenceIteratorTo(self) -> ghidra.program.model.symbol.ReferenceIterator: ...

    @property
    def referencesFrom(self) -> List[ghidra.program.model.symbol.Reference]: ...

    @property
    def root(self) -> ghidra.program.model.listing.Data: ...

    @property
    def rootOffset(self) -> int: ...

    @property
    def structure(self) -> bool: ...

    @property
    def symbols(self) -> List[ghidra.program.model.symbol.Symbol]: ...

    @property
    def union(self) -> bool: ...

    @property
    def value(self) -> object: ...

    @property
    def valueClass(self) -> java.lang.Class: ...

    @property
    def valueReferences(self) -> List[ghidra.program.model.symbol.Reference]: ...

    @property
    def volatile(self) -> bool: ...
