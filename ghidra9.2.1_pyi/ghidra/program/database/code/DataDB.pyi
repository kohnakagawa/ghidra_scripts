from typing import Iterator
from typing import List
import db
import ghidra.docking.settings
import ghidra.program.database.code
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


class DataDB(ghidra.program.database.code.CodeUnitDB, ghidra.program.model.listing.Data):
    """
    Database implementation for the Data interface.

     NOTE!! DataComponents only have a unique key within its parent Struct/Array.  This places a constraint on
     the use of the key field and getKey() method on the underlying classes CodeUnitDB and DataDB.
     The CodeUnit key should only be used for managing an object cache.  The addr field should be used within
     this class instead of the key field which represents an "index in parent" for data components which are
     cached separately.
    """





    def __init__(self, cache: ghidra.program.database.DBObjectCache, key: long):
        """
        Constructs a new DatabaseObject and adds it to the specified cache.
        @param cache to be used for this object or null if object will not be cached
        @param key database key to uniquely identify this object
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

    def addValueReference(self, refAddr: ghidra.program.model.address.Address, type: ghidra.program.model.symbol.RefType) -> None:
        """
        @see ghidra.program.model.listing.Data#addValueReference(ghidra.program.model.address.Address, ghidra.program.model.symbol.RefType)
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

    def clearAllSettings(self) -> None:
        """
        @see ghidra.docking.settings.Settings#clearAllSettings()
        """
        ...

    def clearRegister(self, register: ghidra.program.model.lang.Register) -> None: ...

    def clearSetting(self, name: unicode) -> None:
        """
        @see ghidra.docking.settings.Settings#clear(java.lang.String)
        """
        ...

    def compareTo(self, a: ghidra.program.model.address.Address) -> int: ...

    def contains(self, testAddr: ghidra.program.model.address.Address) -> bool: ...

    @overload
    @staticmethod
    def dumpContextValue(__a0: ghidra.program.model.lang.RegisterValue, __a1: unicode) -> unicode: ...

    @overload
    @staticmethod
    def dumpContextValue(__a0: ghidra.program.model.lang.RegisterValue, __a1: unicode, __a2: java.lang.StringBuilder) -> None: ...

    def equals(self, obj: object) -> bool: ...

    @overload
    def getAddress(self) -> ghidra.program.model.address.Address: ...

    @overload
    def getAddress(self, opIndex: int) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.listing.CodeUnit#getAddress(int)
        """
        ...

    def getAddressString(self, showBlockName: bool, pad: bool) -> unicode: ...

    def getBaseContextRegister(self) -> ghidra.program.model.lang.Register: ...

    def getBaseDataType(self) -> ghidra.program.model.data.DataType:
        """
        @see ghidra.program.model.listing.Data#getBaseDataType()
        """
        ...

    def getBigInteger(self, offset: int, size: int, signed: bool) -> long: ...

    def getByte(self, offset: int) -> int: ...

    def getByteArray(self, name: unicode) -> List[int]:
        """
        @see ghidra.docking.settings.Settings#getByteArray(java.lang.String)
        """
        ...

    @overload
    def getBytes(self) -> List[int]: ...

    @overload
    def getBytes(self, b: List[int], offset: int) -> int: ...

    def getBytesInCodeUnit(self, buffer: List[int], bufferOffset: int) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self, commentType: int) -> unicode: ...

    def getCommentAsArray(self, commentType: int) -> List[unicode]: ...

    @overload
    def getComponent(self, index: int) -> ghidra.program.model.listing.Data:
        """
        @see ghidra.program.model.listing.Data#getComponent(int)
        """
        ...

    @overload
    def getComponent(self, componentPath: List[int]) -> ghidra.program.model.listing.Data:
        """
        @see ghidra.program.model.listing.Data#getComponent(int[])
        """
        ...

    def getComponentAt(self, offset: int) -> ghidra.program.model.listing.Data: ...

    def getComponentIndex(self) -> int:
        """
        @see ghidra.program.model.listing.Data#getComponentIndex()
        """
        ...

    def getComponentLevel(self) -> int:
        """
        @see ghidra.program.model.listing.Data#getComponentLevel()
        """
        ...

    def getComponentPath(self) -> List[int]:
        """
        @see ghidra.program.model.listing.Data#getComponentPath()
        """
        ...

    def getComponentPathName(self) -> unicode:
        """
        @see ghidra.program.model.listing.Data#getComponentPathName()
        """
        ...

    def getComponentsContaining(self, offset: int) -> List[ghidra.program.model.listing.Data]: ...

    def getDataType(self) -> ghidra.program.model.data.DataType:
        """
        @see ghidra.program.model.listing.Data#getDataType()
        """
        ...

    def getDefaultLabelPrefix(self, options: ghidra.program.model.data.DataTypeDisplayOptions) -> unicode: ...

    def getDefaultSettings(self) -> ghidra.docking.settings.Settings:
        """
        @see ghidra.docking.settings.Settings#getDefaultSettings()
        """
        ...

    def getDefaultValueRepresentation(self) -> unicode:
        """
        @see ghidra.program.model.listing.Data#getDefaultValueRepresentation()
        """
        ...

    def getExternalReference(self, opIndex: int) -> ghidra.program.model.symbol.ExternalReference: ...

    def getFieldName(self) -> unicode:
        """
        @see ghidra.program.model.listing.Data#getFieldName()
        """
        ...

    def getInt(self, offset: int) -> int: ...

    def getIntProperty(self, name: unicode) -> int: ...

    def getKey(self) -> long:
        """
        Get the database key for this object.
        """
        ...

    def getLabel(self) -> unicode: ...

    def getLength(self) -> int: ...

    @overload
    def getLong(self, offset: int) -> long: ...

    @overload
    def getLong(self, name: unicode) -> long:
        """
        @see ghidra.docking.settings.Settings#getLong(java.lang.String)
        """
        ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address: ...

    def getMemory(self) -> ghidra.program.model.mem.Memory: ...

    def getMinAddress(self) -> ghidra.program.model.address.Address: ...

    def getMnemonicReferences(self) -> List[ghidra.program.model.symbol.Reference]: ...

    def getMnemonicString(self) -> unicode:
        """
        @see ghidra.program.model.listing.CodeUnit#getMnemonicString()
        """
        ...

    def getNames(self) -> List[unicode]:
        """
        @see ghidra.docking.settings.Settings#getNames()
        """
        ...

    def getNumComponents(self) -> int:
        """
        @see ghidra.program.model.listing.Data#getNumComponents()
        """
        ...

    def getNumOperands(self) -> int:
        """
        @see ghidra.program.model.listing.CodeUnit#getNumOperands()
        """
        ...

    def getObjectProperty(self, name: unicode) -> ghidra.util.Saveable: ...

    def getOperandReferences(self, opIndex: int) -> List[ghidra.program.model.symbol.Reference]: ...

    def getParent(self) -> ghidra.program.model.listing.Data:
        """
        @see ghidra.program.model.listing.Data#getParent()
        """
        ...

    def getParentOffset(self) -> int:
        """
        @see ghidra.program.model.listing.Data#getParentOffset()
        """
        ...

    def getPathName(self) -> unicode:
        """
        @see ghidra.program.model.listing.Data#getPathName()
        """
        ...

    def getPrimaryReference(self, index: int) -> ghidra.program.model.symbol.Reference: ...

    def getPrimarySymbol(self) -> ghidra.program.model.symbol.Symbol: ...

    def getPrimitiveAt(self, offset: int) -> ghidra.program.model.listing.Data:
        """
        @see ghidra.program.model.listing.Data#getPrimitiveAt(int)
        """
        ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def getReferenceIteratorTo(self) -> ghidra.program.model.symbol.ReferenceIterator: ...

    def getReferencesFrom(self) -> List[ghidra.program.model.symbol.Reference]:
        """
        @see ghidra.program.model.listing.CodeUnit#getReferencesFrom()
        """
        ...

    def getRegister(self, name: unicode) -> ghidra.program.model.lang.Register: ...

    def getRegisterValue(self, register: ghidra.program.model.lang.Register) -> ghidra.program.model.lang.RegisterValue: ...

    def getRegisters(self) -> List[ghidra.program.model.lang.Register]: ...

    def getRoot(self) -> ghidra.program.model.listing.Data:
        """
        @see ghidra.program.model.listing.Data#getRoot()
        """
        ...

    def getRootOffset(self) -> int:
        """
        @see ghidra.program.model.listing.Data#getRootOffset()
        """
        ...

    def getScalar(self, opIndex: int) -> ghidra.program.model.scalar.Scalar:
        """
        @see ghidra.program.model.listing.CodeUnit#getScalar(int)
        """
        ...

    def getShort(self, offset: int) -> int: ...

    def getString(self, name: unicode) -> unicode:
        """
        @see ghidra.docking.settings.Settings#getString(java.lang.String)
        """
        ...

    def getStringProperty(self, name: unicode) -> unicode: ...

    def getSymbols(self) -> List[ghidra.program.model.symbol.Symbol]: ...

    def getUnsignedByte(self, __a0: int) -> int: ...

    def getUnsignedInt(self, __a0: int) -> long: ...

    def getUnsignedShort(self, __a0: int) -> int: ...

    @overload
    def getValue(self) -> object:
        """
        @see ghidra.program.model.listing.Data#getValue()
        """
        ...

    @overload
    def getValue(self, name: unicode) -> object:
        """
        @see ghidra.docking.settings.Settings#getValue(java.lang.String)
        """
        ...

    @overload
    def getValue(self, register: ghidra.program.model.lang.Register, signed: bool) -> long: ...

    def getValueClass(self) -> java.lang.Class: ...

    def getValueReferences(self) -> List[ghidra.program.model.symbol.Reference]:
        """
        @see ghidra.program.model.listing.Data#getValueReferences()
        """
        ...

    def getVarLengthInt(self, __a0: int, __a1: int) -> int: ...

    def getVarLengthUnsignedInt(self, __a0: int, __a1: int) -> long: ...

    def getVoidProperty(self, name: unicode) -> bool: ...

    def hasProperty(self, name: unicode) -> bool: ...

    def hasStringValue(self) -> bool: ...

    def hasValue(self, register: ghidra.program.model.lang.Register) -> bool: ...

    def hashCode(self) -> int: ...

    def isArray(self) -> bool:
        """
        @see ghidra.program.model.listing.Data#isArray()
        """
        ...

    def isBigEndian(self) -> bool: ...

    def isConstant(self) -> bool:
        """
        @see ghidra.program.model.listing.Data#isConstant()
        """
        ...

    def isDefined(self) -> bool:
        """
        @see ghidra.program.model.listing.Data#isDefined()
        """
        ...

    def isDeleted(self) -> bool:
        """
        Returns true if this object has been deleted. Note: once an object has been deleted, it will
         never be "refreshed". For example, if an object is ever deleted and is resurrected via an
         "undo", you will have get a fresh instance of the object.
        @return true if this object has been deleted.
        """
        ...

    def isDynamic(self) -> bool:
        """
        @see ghidra.program.model.listing.Data#isDynamic()
        """
        ...

    def isEmpty(self) -> bool:
        """
        @see ghidra.docking.settings.Settings#isEmpty()
        """
        ...

    def isInitializedMemory(self) -> bool: ...

    def isInvalid(self) -> bool:
        """
        Returns true if object is currently invalid. Calling checkIsValid may successfully refresh
         object making it valid.
        @see #checkIsValid()
        """
        ...

    def isPointer(self) -> bool:
        """
        @see ghidra.program.model.listing.Data#isPointer()
        """
        ...

    def isStructure(self) -> bool:
        """
        @see ghidra.program.model.listing.Data#isStructure()
        """
        ...

    def isSuccessor(self, codeUnit: ghidra.program.model.listing.CodeUnit) -> bool: ...

    def isUnion(self) -> bool:
        """
        @see ghidra.program.model.listing.Data#isUnion()
        """
        ...

    def isVolatile(self) -> bool:
        """
        @see ghidra.program.model.listing.Data#isVolatile()
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def propertyNames(self) -> Iterator[unicode]: ...

    def removeExternalReference(self, opIndex: int) -> None: ...

    def removeMnemonicReference(self, refAddr: ghidra.program.model.address.Address) -> None: ...

    def removeOperandReference(self, opIndex: int, refAddr: ghidra.program.model.address.Address) -> None: ...

    def removeProperty(self, name: unicode) -> None: ...

    def removeValueReference(self, refAddr: ghidra.program.model.address.Address) -> None:
        """
        @see ghidra.program.model.listing.Data#removeValueReference(ghidra.program.model.address.Address)
        """
        ...

    def setByteArray(self, name: unicode, value: List[int]) -> None:
        """
        @see ghidra.docking.settings.Settings#setByteArray(java.lang.String, byte[])
        """
        ...

    def setComment(self, commentType: int, comment: unicode) -> None: ...

    def setCommentAsArray(self, commentType: int, comment: List[unicode]) -> None: ...

    def setInvalid(self) -> None:
        """
        Invalidate this object. This does not necessarily mean that this object can never be used
         again. If the object can refresh itself, it may still be useable.
        """
        ...

    def setLong(self, name: unicode, value: long) -> None:
        """
        @see ghidra.docking.settings.Settings#setLong(java.lang.String, long)
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

    def setString(self, name: unicode, value: unicode) -> None:
        """
        @see ghidra.docking.settings.Settings#setString(java.lang.String, java.lang.String)
        """
        ...

    @overload
    def setValue(self, register: ghidra.program.model.lang.Register, value: long) -> None: ...

    @overload
    def setValue(self, name: unicode, value: object) -> None:
        """
        @see ghidra.docking.settings.Settings#setValue(java.lang.String, java.lang.Object)
        """
        ...

    def toString(self) -> unicode:
        """
        Provide default formatted string representation of this instruction.
        @see java.lang.Object#toString()
        """
        ...

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
