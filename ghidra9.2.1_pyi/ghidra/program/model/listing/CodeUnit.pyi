from typing import Iterator
from typing import List
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.mem
import ghidra.program.model.scalar
import ghidra.program.model.symbol
import ghidra.util
import ghidra.util.prop
import java.lang


class CodeUnit(ghidra.program.model.mem.MemBuffer, object):
    """
    Interface common to both instructions and data.
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







    def addMnemonicReference(self, refAddr: ghidra.program.model.address.Address, refType: ghidra.program.model.symbol.RefType, sourceType: ghidra.program.model.symbol.SourceType) -> None:
        """
        Add a reference to the mnemonic for this code unit.
        @param refAddr address to add as a reference.
        @param refType the type of reference to add.
        @param sourceType the source of this reference
        """
        ...

    def addOperandReference(self, index: int, refAddr: ghidra.program.model.address.Address, type: ghidra.program.model.symbol.RefType, sourceType: ghidra.program.model.symbol.SourceType) -> None:
        """
        Add a memory reference to the operand at the given index.
        @param index operand index
        @param refAddr reference address
        @param type the reference type to be added.
        @param sourceType the source of this reference
        """
        ...

    def compareTo(self, addr: ghidra.program.model.address.Address) -> int:
        """
        Compares the given address to the address range of this node.
        @param addr address to compare.
        @return a negative integer if this addr is greater than the maximum range address
                 zero if addr is in the range
                 a positive integer if addr is less than minimum range address
        """
        ...

    def contains(self, testAddr: ghidra.program.model.address.Address) -> bool:
        """
        Returns true if address is contained in the range of this codeUnit
        @param testAddr the address to test.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    def getAddress(self) -> ghidra.program.model.address.Address: ...

    @overload
    def getAddress(self, opIndex: int) -> ghidra.program.model.address.Address:
        """
        Get the Address for the given operand index if one exists.  Data
         objects have one operand (the value).
        @param opIndex index of the operand.
        @return An addres if the operand represents a fully qualified
         address (given the context), or if the operand is a Scalar treated
         as an address. Null is returned if no address or scalar exists on that
         operand.
        """
        ...

    def getAddressString(self, showBlockName: bool, pad: bool) -> unicode:
        """
        Get the string representation of the starting address for
         this code unit.
        @param showBlockName true if the string should include the memory block name
        @param pad if true, the address will be padded with leading zeros.  Even if pad is
         false, the string will be padded to make the address string contain at least 4 digits.
        @return string representation of address
        """
        ...

    def getBigInteger(self, __a0: int, __a1: int, __a2: bool) -> long: ...

    def getByte(self, __a0: int) -> int: ...

    @overload
    def getBytes(self) -> List[int]:
        """
        Get the bytes that make up this code unit.
        @return an array of bytes that are in memory at the codeunits address.  The
         array length is the same as the codeUnits length
        @throws MemoryAccessException if the full number of bytes could not be read.
        """
        ...

    @overload
    def getBytes(self, __a0: List[int], __a1: int) -> int: ...

    def getBytesInCodeUnit(self, buffer: List[int], bufferOffset: int) -> None:
        """
        Copies max(buffer.length, code unit length) bytes into buffer starting at location offset in buffer.
        @param buffer byte array to copy into
        @param bufferOffset offset in byte array the copy will start
        @throws MemoryAccessException if the full number of bytes could not be read.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self, commentType: int) -> unicode:
        """
        Get the comment for the given type
        @param commentType either EOL_COMMENT, PRE_COMMENT,
         POST_COMMENT, or REPEATABLE_COMMENT
        @return the comment string of the appropriate type or null if no comment of
         that type exists for this codeunit
        @throws IllegalArgumentException if type is not one of the
         three types of comments supported
        """
        ...

    def getCommentAsArray(self, commentType: int) -> List[unicode]:
        """
        Get the comment for the given type and parse it into an array of strings
         such that each line is its own string.
        @param commentType either EOL_COMMENT, PRE_COMMENT,
         POST_COMMENT, or REPEATABLE_COMMENT
        @return an array of strings where each item in the array is a line of text
         in the comment.  If there is no comment of the requested type, an empty array
         is returned.
        @throws IllegalArgumentException if type is not one of the
         three types of comments supported
        """
        ...

    def getExternalReference(self, opIndex: int) -> ghidra.program.model.symbol.ExternalReference:
        """
        Gets the external reference (if any) at the opIndex
        @param opIndex the operand index to look for external references
        @return the external reference at the operand or null if none exists.
        """
        ...

    def getInt(self, __a0: int) -> int: ...

    def getIntProperty(self, name: unicode) -> int:
        """
        Get the int property for name.
        @param name the name of the property
        @throws NoValueException if there is not name property
         for this code unit
        """
        ...

    def getLabel(self) -> unicode:
        """
        Get the label for this code unit.
        """
        ...

    def getLength(self) -> int:
        """
        Get length of this code unit.
        """
        ...

    def getLong(self, __a0: int) -> long: ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address:
        """
        Get the ending address for this code unit.
        """
        ...

    def getMemory(self) -> ghidra.program.model.mem.Memory: ...

    def getMinAddress(self) -> ghidra.program.model.address.Address:
        """
        Get the starting address for this code unit.
        """
        ...

    def getMnemonicReferences(self) -> List[ghidra.program.model.symbol.Reference]:
        """
        Get references for the mnemonic for this code unit.
        @return an array of memory references. A zero length array will be
         returned if there are no references for the mnemonic.
        """
        ...

    def getMnemonicString(self) -> unicode:
        """
        Get the mnemonic for this code unit, e.g., MOV, JMP
        """
        ...

    def getNumOperands(self) -> int:
        """
        Get the number of operands for this code unit.
        """
        ...

    def getObjectProperty(self, name: unicode) -> ghidra.util.Saveable:
        """
        Get the object property for name; returns null if
         there is no name property for this code unit.
        @param name the name of the property
        """
        ...

    def getOperandReferences(self, index: int) -> List[ghidra.program.model.symbol.Reference]:
        """
        Get the references for the operand index.
        @param index operand index (0 is the first operand)
        """
        ...

    def getPrimaryReference(self, index: int) -> ghidra.program.model.symbol.Reference:
        """
        Get the primary reference for the operand index.
        @param index operand index (0 is the first operand)
        """
        ...

    def getPrimarySymbol(self) -> ghidra.program.model.symbol.Symbol:
        """
        Get the Primary Symbol for this code unit.
        @throws ConcurrentModificationException if this object is no
         longer valid.
        """
        ...

    def getProgram(self) -> ghidra.program.model.listing.Program:
        """
        Returns the program that generated this CodeUnit.
        """
        ...

    def getReferenceIteratorTo(self) -> ghidra.program.model.symbol.ReferenceIterator:
        """
        Get an iterator over all references TO this code unit.
        """
        ...

    def getReferencesFrom(self) -> List[ghidra.program.model.symbol.Reference]:
        """
        Get ALL memory references FROM this code unit.
        @return an array of memory references from this codeUnit or an empty array
         if there are no references.
        """
        ...

    def getScalar(self, opIndex: int) -> ghidra.program.model.scalar.Scalar:
        """
        Returns the scalar at the given operand index.  Data objects have
         one operand (the value).
        @param opIndex index of the operand.
        @return the scalar at the given operand index or null if no
         scalar exists at that index.
        """
        ...

    def getShort(self, __a0: int) -> int: ...

    def getStringProperty(self, name: unicode) -> unicode:
        """
        Get the string property for name; returns null if
         there is no name property for this code unit.
        @param name the name of the property
        """
        ...

    def getSymbols(self) -> List[ghidra.program.model.symbol.Symbol]:
        """
        Get the Symbols for this code unit.
        @throws ConcurrentModificationException if this object is no
         longer valid.
        """
        ...

    def getUnsignedByte(self, __a0: int) -> int: ...

    def getUnsignedInt(self, __a0: int) -> long: ...

    def getUnsignedShort(self, __a0: int) -> int: ...

    def getVarLengthInt(self, __a0: int, __a1: int) -> int: ...

    def getVarLengthUnsignedInt(self, __a0: int, __a1: int) -> long: ...

    def getVoidProperty(self, name: unicode) -> bool:
        """
        Returns whether this code unit is marked as having the
         name property.
        @param name the name of the property
        """
        ...

    def hasProperty(self, name: unicode) -> bool:
        """
        Returns true if the codeunit has the given property defined.
        @param name the name of the property
        """
        ...

    def hashCode(self) -> int: ...

    def isBigEndian(self) -> bool: ...

    def isInitializedMemory(self) -> bool: ...

    def isSuccessor(self, codeUnit: ghidra.program.model.listing.CodeUnit) -> bool:
        """
        Return true if the given CodeUnit follows
         directly after this code unit.
        @param codeUnit the codeUnit being tested to see if it follows this codeUnit.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def propertyNames(self) -> Iterator[unicode]:
        """
        Get an iterator over the property names.
        """
        ...

    def removeExternalReference(self, opIndex: int) -> None:
        """
        Remove external reference (if any) at the given opIndex
         opIndex the index of the operand from which to remove any external reference.
        """
        ...

    def removeMnemonicReference(self, refAddr: ghidra.program.model.address.Address) -> None:
        """
        Remove a reference to the mnemonic for this code unit.
        @param refAddr the address to remove as a reference.
        """
        ...

    def removeOperandReference(self, index: int, refAddr: ghidra.program.model.address.Address) -> None:
        """
        Remove a reference to the operand.
        @param index operand index
        @param refAddr address referencing the operand
        """
        ...

    def removeProperty(self, name: unicode) -> None:
        """
        Remove the property with the given name from this code unit.
        @param name the name of the property
        """
        ...

    def setComment(self, commentType: int, comment: unicode) -> None:
        """
        Set the comment for the given comment type.  Passing <code>null</code> clears the comment
        @param commentType either EOL_COMMENT, PRE_COMMENT,
         POST_COMMENT, or REPEATABLE_COMMENT
        @param comment comment for code unit; null clears the comment
        @throws IllegalArgumentException if type is not one of the
         three types of comments supported
        """
        ...

    def setCommentAsArray(self, commentType: int, comment: List[unicode]) -> None:
        """
        Set the comment (with each line in its own string) for the given comment type
        @param commentType either EOL_COMMENT, PRE_COMMENT,
         POST_COMMENT, or REPEATABLE_COMMENT
        @param comment an array of strings where each string is a single line of the comment.
        @throws IllegalArgumentException if type is not one of the
         three types of comments supported
        """
        ...

    def setPrimaryMemoryReference(self, ref: ghidra.program.model.symbol.Reference) -> None:
        """
        Sets a memory reference to be the primary reference at its
         address/opIndex location. The primary reference is the one that
         is used in the getOperandRepresentation() method.
        @param ref the reference to be set as primary.
        """
        ...

    @overload
    def setProperty(self, name: unicode) -> None:
        """
        Set the named property.  This method is used for "void" properites. The
         property is either set or not set - there is no value
        @param name the name of the property.
        """
        ...

    @overload
    def setProperty(self, name: unicode, value: int) -> None:
        """
        Set the named property with the given value at the address of this codeunit.
        @param name the name of the property.
        @param value value to be stored.
        """
        ...

    @overload
    def setProperty(self, name: unicode, value: unicode) -> None:
        """
        Set the named property with the given value at the address of this codeunit.
        @param name the name of the property.
        @param value value to be stored.
        """
        ...

    @overload
    def setProperty(self, name: unicode, value: ghidra.util.Saveable) -> None:
        """
        Set the named property with the given value at the address of this codeunit.
        @param name the name of the property.
        @param value value to be stored.
        """
        ...

    def setRegisterReference(self, opIndex: int, reg: ghidra.program.model.lang.Register, sourceType: ghidra.program.model.symbol.SourceType, refType: ghidra.program.model.symbol.RefType) -> None:
        """
        Sets a register reference at the <code>offset</code> on the
         specified operand index, which effectively substitutes the previous
         operation interpretation
         <br>
         <i>NOTE: If another reference was previously set on the
         operand, then it will be replaced with this register
         reference</i>
        @param opIndex the index of the operand to set this register reference
        @param reg a register
        @param sourceType the source of this reference
        @param refType type of reference, RefType.READ,WRITE,PTR...
        """
        ...

    def setStackReference(self, opIndex: int, offset: int, sourceType: ghidra.program.model.symbol.SourceType, refType: ghidra.program.model.symbol.RefType) -> None:
        """
        Sets a stack reference at the <code>offset</code> on the
         specified operand index, which effectively substitutes the previous
         operation interpretation
         <br>
         <i>NOTE: If another reference was previously set on the
         operand, then it will be replaced with this stack
         reference</i>
        @param opIndex the index of the operand to set this stack reference
        @param offset the (+/-) offset from stack base address
        @param sourceType the source of this reference
        @param refType type of reference, RefType.READ,WRITE,PTR...
        """
        ...

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

    @property
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def bigEndian(self) -> bool: ...

    @property
    def bytes(self) -> List[int]: ...

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
    def numOperands(self) -> int: ...

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
    def symbols(self) -> List[ghidra.program.model.symbol.Symbol]: ...
