from typing import Iterator
from typing import List
import ghidra.app.util
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


class PseudoDataComponent(ghidra.app.util.PseudoData):
    """
    DataComponent provides Data and CodeUnit access to Struct and Array components.

     NOTE!! DataComponents only have a unique key within its parent Struct/Array.  This places a constraint on
     the use of the key field and getKey() method on the underlying classes CodeUnitDB and DataDB.
     The CodeUnit key should only be used for managing an object cache.
    """





    @overload
    def __init__(self, address: ghidra.program.model.address.Address, dataType: ghidra.program.model.data.DataType, memBuffer: ghidra.program.model.mem.MemBuffer): ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address, dataType: ghidra.program.model.data.DataType, memBuffer: ghidra.program.model.mem.MemBuffer): ...



    def addMnemonicReference(self, refAddr: ghidra.program.model.address.Address, refType: ghidra.program.model.symbol.RefType, sourceType: ghidra.program.model.symbol.SourceType) -> None:
        """
        Add a reference to the mnemonic for this code unit.
        @param refAddr address of reference to add
        @param refType type of reference being added
        """
        ...

    def addOperandReference(self, opIndex: int, refAddr: ghidra.program.model.address.Address, type: ghidra.program.model.symbol.RefType, sourceType: ghidra.program.model.symbol.SourceType) -> None:
        """
        Add a user defined reference to the operand at the given index.
        @see CodeUnit#addOperandReference(int, Address, RefType, SourceType)
        """
        ...

    def addValueReference(self, refAddr: ghidra.program.model.address.Address, type: ghidra.program.model.symbol.RefType) -> None: ...

    def clearAllSettings(self) -> None: ...

    def clearSetting(self, name: unicode) -> None: ...

    def compareTo(self, a: ghidra.program.model.address.Address) -> int:
        """
        Compares the given address to the address range of this node.
        @param a the address
        @return a negative integer if addr is greater than the maximum range
                 address zero if addr is in the range a positive integer if addr
                 is less than minimum range address
        @throws ConcurrentModificationException if this object is no longer valid.
        """
        ...

    def contains(self, testAddr: ghidra.program.model.address.Address) -> bool:
        """
        Determines if this code unit contains the indicated address.
        @param testAddr the address to test
        @return true if address is contained in the range.
        @throws ConcurrentModificationException if this object is no longer valid.
        """
        ...

    def equals(self, obj: object) -> bool:
        """
        Returns whether some other object is "equal to" this one.
        """
        ...

    @overload
    def getAddress(self) -> ghidra.program.model.address.Address:
        """
        Get the Address which corresponds to the offset 0.
        @return the current address of offset 0.
        """
        ...

    @overload
    def getAddress(self, opIndex: int) -> ghidra.program.model.address.Address: ...

    def getAddressString(self, showBlockName: bool, pad: bool) -> unicode: ...

    def getBaseDataType(self) -> ghidra.program.model.data.DataType: ...

    def getBigInteger(self, offset: int, size: int, signed: bool) -> long: ...

    def getByte(self, offset: int) -> int:
        """
        Get one byte from memory at the current position plus offset.
        @param offset the displacement from the current position.
        @return the data at offset from the current position.
        @throws AddressOutOfBoundsException if offset exceeds address space
        @throws IndexOutOfBoundsException if offset is negative
        @throws MemoryAccessException if memory cannot be read
        """
        ...

    def getByteArray(self, name: unicode) -> List[int]:
        """
        @see ghidra.docking.settings.Settings#getByteArray(java.lang.String)
        """
        ...

    def getByteCodeString(self) -> unicode: ...

    @overload
    def getBytes(self) -> List[int]:
        """
        Gets the bytes for this code unit.
        """
        ...

    @overload
    def getBytes(self, b: List[int], offset: int) -> int: ...

    def getBytesInCodeUnit(self, buffer: List[int], bufferOffset: int) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self, commentType: int) -> unicode:
        """
        @see ghidra.program.model.listing.CodeUnit#getComment(int)
        """
        ...

    def getCommentAsArray(self, commentType: int) -> List[unicode]:
        """
        Get the comment as an array where each element is a single line for the
         given type.
        @param commentType must be either EOL_COMMENT_TYPE, PRE_COMMENT_TYPE,
                    POST_COMMENT_TYPE, or PLATE_COMMENT_TYPE
        @throws IllegalArgumentException if type is not one of the three types of comments supported
        @throws ConcurrentModificationException if this object is no longer valid.
        """
        ...

    @overload
    def getComponent(self, index: int) -> ghidra.program.model.listing.Data: ...

    @overload
    def getComponent(self, componentPath: List[int]) -> ghidra.program.model.listing.Data: ...

    def getComponentAt(self, offset: int) -> ghidra.program.model.listing.Data: ...

    def getComponentIndex(self) -> int:
        """
        Get the index of this Data item within its parent
        @return the index of this component in its parent
                 returns -1 if this is not a component
        """
        ...

    def getComponentLevel(self) -> int: ...

    def getComponentPath(self) -> List[int]:
        """
        @see ghidra.program.model.listing.Data#getComponentPath()
        """
        ...

    def getComponentPathName(self) -> unicode:
        """
        @return the relative path name (dot notation) for this field
        """
        ...

    def getComponentsContaining(self, offset: int) -> List[ghidra.program.model.listing.Data]: ...

    def getDataType(self) -> ghidra.program.model.data.DataType: ...

    def getDefaultLabelPrefix(self, options: ghidra.program.model.data.DataTypeDisplayOptions) -> unicode: ...

    def getDefaultSettings(self) -> ghidra.docking.settings.Settings:
        """
        @see ghidra.docking.settings.Settings#getDefaultSettings()
        """
        ...

    def getDefaultValueRepresentation(self) -> unicode: ...

    def getExternalReference(self, opIndex: int) -> ghidra.program.model.symbol.ExternalReference: ...

    def getFieldName(self) -> unicode:
        """
        Get the name of this Data that is a component of another
         Data Item.
        @return the name as a component of another prototype,
                 and null if this is not a component of another prototype.
        """
        ...

    def getInt(self, offset: int) -> int: ...

    def getIntProperty(self, name: unicode) -> int:
        """
        Get the int property for name.
        @param name the name of the property.
        @throws NoValueException if there is not name property for this code unit
        @throws TypeMismatchException if the property manager for name does not support int types
        @throws ConcurrentModificationException if this object is no longer valid.
        """
        ...

    def getLabel(self) -> unicode:
        """
        Get the label for this code unit.
        @throws ConcurrentModificationException if this object is no longer valid.
        @deprecated
        """
        ...

    def getLength(self) -> int:
        """
        Get the length of the code unit.
        """
        ...

    @overload
    def getLong(self, offset: int) -> long: ...

    @overload
    def getLong(self, name: unicode) -> long:
        """
        @see ghidra.docking.settings.Settings#getLong(java.lang.String)
        """
        ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address:
        """
        Get the ending address for this code unit.
        @throws ConcurrentModificationException if this object is no longer valid.
        """
        ...

    def getMemory(self) -> ghidra.program.model.mem.Memory:
        """
        Get the Memory object actually used by the MemBuffer.

         return the Memory used by this MemBuffer.
        """
        ...

    def getMinAddress(self) -> ghidra.program.model.address.Address:
        """
        Get the starting address for this code unit.
        @throws ConcurrentModificationException if this object is no longer valid.
        """
        ...

    def getMnemonicReferences(self) -> List[ghidra.program.model.symbol.Reference]:
        """
        Get references for the mnemonic for this instruction.
        """
        ...

    def getMnemonicString(self) -> unicode: ...

    def getNames(self) -> List[unicode]: ...

    def getNextCodeUnit(self) -> ghidra.program.model.listing.CodeUnit:
        """
        Get the code unit after this code unit.
        @throws ConcurrentModificationException if this object is no longer valid.
        """
        ...

    def getNumComponents(self) -> int: ...

    def getNumOperands(self) -> int: ...

    def getObjectProperty(self, name: unicode) -> ghidra.util.Saveable:
        """
        Get the object property for name; returns null if there is no name
         property for this code unit.
        @param name the name of the property.
        @throws TypeMismatchException if the property manager for name does not support object
                     types
        @throws ConcurrentModificationException if this object is no longer valid.
        """
        ...

    def getOperandReferences(self, opIndex: int) -> List[ghidra.program.model.symbol.Reference]:
        """
        Get the references for the operand index. If the operand type is a
         register, then the user defined references are returned; otherwise an
         array with the address for the operand value is returned.
        """
        ...

    def getParent(self) -> ghidra.program.model.listing.Data:
        """
        Get the immediate parent Data Prototype of this component
        """
        ...

    def getParentOffset(self) -> int:
        """
        Get the offset of this Data item from the start of its immediate
         parent.
        """
        ...

    def getPathName(self) -> unicode:
        """
        Returns the path name (dot notation) for this field
        """
        ...

    def getPreviousCodeUnit(self) -> ghidra.program.model.listing.CodeUnit:
        """
        Get the code unit before this code unit.
        @throws ConcurrentModificationException if this object is no longer valid.
        """
        ...

    def getPrimaryReference(self, index: int) -> ghidra.program.model.symbol.Reference: ...

    def getPrimarySymbol(self) -> ghidra.program.model.symbol.Symbol:
        """
        Get the primary Symbol for this code unit.
        @throws ConcurrentModificationException if this object is no longer valid.
        """
        ...

    def getPrimitiveAt(self, offset: int) -> ghidra.program.model.listing.Data: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def getReferenceIteratorTo(self) -> ghidra.program.model.symbol.ReferenceIterator: ...

    def getReferencesFrom(self) -> List[ghidra.program.model.symbol.Reference]:
        """
        Get ALL reference FROM this code unit.
        """
        ...

    def getRoot(self) -> ghidra.program.model.listing.Data:
        """
        Get the highest level Data Prototype in a hierarchy of structures
         containing this component.
        """
        ...

    def getRootOffset(self) -> int:
        """
        Get the offset of this Data item from the start of
          some hierarchy of structures.
        """
        ...

    def getScalar(self, opIndex: int) -> ghidra.program.model.scalar.Scalar: ...

    def getShort(self, offset: int) -> int: ...

    def getStackReference(self, opIndex: int) -> ghidra.program.model.symbol.StackReference: ...

    def getString(self, name: unicode) -> unicode:
        """
        @see ghidra.docking.settings.Settings#getString(java.lang.String)
        """
        ...

    def getStringProperty(self, name: unicode) -> unicode:
        """
        Get the string property for name; returns null if there is no name
         property for this code unit.
        @param name the name of the property.
        @throws TypeMismatchException if the property manager for name does not support string
                     types
        @throws ConcurrentModificationException if this object is no longer valid.
        """
        ...

    def getSymbols(self) -> List[ghidra.program.model.symbol.Symbol]:
        """
        Get the symbols for this code unit.
        @throws ConcurrentModificationException if this object is no longer valid.
        """
        ...

    def getUnsignedByte(self, __a0: int) -> int: ...

    def getUnsignedInt(self, __a0: int) -> long: ...

    def getUnsignedShort(self, __a0: int) -> int: ...

    @overload
    def getValue(self) -> object: ...

    @overload
    def getValue(self, name: unicode) -> object:
        """
        @see ghidra.docking.settings.Settings#getValue(java.lang.String)
        """
        ...

    def getValueClass(self) -> java.lang.Class: ...

    def getValueReferences(self) -> List[ghidra.program.model.symbol.Reference]: ...

    def getVarLengthInt(self, __a0: int, __a1: int) -> int: ...

    def getVarLengthUnsignedInt(self, __a0: int, __a1: int) -> long: ...

    def getVoidProperty(self, name: unicode) -> bool:
        """
        Returns whether this code unit is marked as having the name property.
        @param name the name of the property.
        @throws TypeMismatchException if the property manager for name does not support void types
        @throws ConcurrentModificationException if this object is no longer valid.
        """
        ...

    def hasProperty(self, name: unicode) -> bool: ...

    def hasStringValue(self) -> bool: ...

    def hashCode(self) -> int: ...

    def invalidate(self) -> None:
        """
        Invalidate memory buffer
        """
        ...

    def isArray(self) -> bool: ...

    def isBigEndian(self) -> bool: ...

    def isConstant(self) -> bool: ...

    def isDefined(self) -> bool: ...

    def isDynamic(self) -> bool: ...

    def isEmpty(self) -> bool: ...

    def isInitializedMemory(self) -> bool: ...

    def isPointer(self) -> bool: ...

    def isStructure(self) -> bool: ...

    def isSuccessor(self, codeUnit: ghidra.program.model.listing.CodeUnit) -> bool:
        """
        Return true if the given CodeUnit follows directly after this code unit.
        @throws ConcurrentModificationException if this object is no longer valid.
        """
        ...

    def isUnion(self) -> bool: ...

    def isValid(self) -> bool: ...

    def isVolatile(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def propertyNames(self) -> Iterator[unicode]: ...

    def removeExternalReference(self, opIndex: int) -> None: ...

    def removeMnemonicReference(self, refAddr: ghidra.program.model.address.Address) -> None:
        """
        Remove a reference to the mnemonic for this instruction.
        """
        ...

    def removeOperandReference(self, opIndex: int, refAddr: ghidra.program.model.address.Address) -> None:
        """
        Remove a user defined reference to the operand at opIndex.
        """
        ...

    def removeProperty(self, name: unicode) -> None:
        """
        Remove the property value with the given name for this code unit.
        @param name the name of the property.
        """
        ...

    def removeStackReference(self, opIndex: int) -> None: ...

    def removeValueReference(self, refAddr: ghidra.program.model.address.Address) -> None: ...

    def setByteArray(self, name: unicode, value: List[int]) -> None: ...

    def setComment(self, commentType: int, comment: unicode) -> None:
        """
        Set the comment for the given type.
        @param commentType must be either EOL_COMMENT, PRE_COMMENT, POST_COMMENT, or
                    PLATE_COMMENT
        @param comment the comment
        @throws IllegalArgumentException if type is not one of the three types of comments supported
        @throws ConcurrentModificationException if this object is no longer valid.
        """
        ...

    def setCommentAsArray(self, commentType: int, comment: List[unicode]) -> None:
        """
        Set the comment for the given type.
        @param commentType must be either EOL_COMMENT, PRE_COMMENT, POST_COMMENT, or
                    PLATE_COMMENT
        @param comment the lines that make up the comment
        @throws IllegalArgumentException if type is not one of the three types of comments supported
        @throws ConcurrentModificationException if this object is no longer valid.
        """
        ...

    def setExternalReference(self, ref: ghidra.program.model.symbol.Reference) -> None: ...

    def setLong(self, name: unicode, value: long) -> None: ...

    def setMemoryReference(self, opIndex: int, refAddr: ghidra.program.model.address.Address, refType: ghidra.program.model.symbol.RefType) -> None: ...

    def setPrimaryMemoryReference(self, ref: ghidra.program.model.symbol.Reference) -> None: ...

    @overload
    def setProperty(self, name: unicode) -> None:
        """
        Mark the property name as having a value for this code unit.
        @param name the name of the property to save.
        @throws TypeMismatchException if the property manager for name does not support void types
        @throws ConcurrentModificationException if this object is no longer valid.
        """
        ...

    @overload
    def setProperty(self, name: unicode, value: int) -> None:
        """
        Set the property name with the given value for this code unit.
        @param name the name of the property to save.
        @param value the value of the property to save.
        @throws TypeMismatchException if the property manager for name does not support int types
        @throws ConcurrentModificationException if this object is no longer valid.
        """
        ...

    @overload
    def setProperty(self, name: unicode, value: unicode) -> None:
        """
        Set the property name with the given value for this code unit.
        @param name the name of the property to save.
        @param value the value of the property to save.
        @throws TypeMismatchException if the property manager for name does not support string
                     types
        @throws ConcurrentModificationException if this object is no longer valid.
        """
        ...

    @overload
    def setProperty(self, name: unicode, value: ghidra.util.Saveable) -> None:
        """
        Set the property name with the given value for this code unit.
        @param name the name of the property to save.
        @param value the value of the property to save.
        @throws TypeMismatchException if the property manager for name does not support object
                     types
        @throws ConcurrentModificationException if this object is no longer valid.
        """
        ...

    def setRegisterReference(self, opIndex: int, reg: ghidra.program.model.lang.Register, sourceType: ghidra.program.model.symbol.SourceType, refType: ghidra.program.model.symbol.RefType) -> None: ...

    def setStackReference(self, opIndex: int, offset: int, sourceType: ghidra.program.model.symbol.SourceType, refType: ghidra.program.model.symbol.RefType) -> None: ...

    def setString(self, name: unicode, value: unicode) -> None: ...

    def setValue(self, name: unicode, value: object) -> None: ...

    def toString(self) -> unicode: ...

    def visitProperty(self, visitor: ghidra.util.prop.PropertyVisitor, propertyName: unicode) -> None:
        """
        Invokes the visit() method of the specified PropertyVisitor if the named
         property exists for this code unit.
        @param visitor the class implementing the PropertyVisitor interface.
        @param propertyName the name of the property to be visited.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
