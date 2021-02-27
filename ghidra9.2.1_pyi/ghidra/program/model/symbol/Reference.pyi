import ghidra.program.model.address
import ghidra.program.model.symbol
import java.lang


class Reference(java.lang.Comparable, object):
    """
    Base class to hold information about a referring address. Derived classes add
     what the address is referring to. A basic reference consists of a "from"
     address, the reference type, the operand index for where the reference is,
     and whether the reference is user defined.
    """

    MNEMONIC: int = -1
    OTHER: int = -2







    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFromAddress(self) -> ghidra.program.model.address.Address:
        """
        Get the address of the codeunit that is making the reference.
        """
        ...

    def getOperandIndex(self) -> int:
        """
        Get the operand index of where this reference was placed.
        @return op index or ReferenceManager.MNEMONIC
        """
        ...

    def getReferenceType(self) -> ghidra.program.model.symbol.RefType:
        """
        Get the type of reference being made.
        """
        ...

    def getSource(self) -> ghidra.program.model.symbol.SourceType:
        """
        Gets the source of this reference. {@link SourceType}s
        @return the source of this reference
        """
        ...

    def getSymbolID(self) -> long:
        """
        Get the symbol ID associated with this reference.
        @return symbol ID or -1 if no symbol is associated with this reference
        """
        ...

    def getToAddress(self) -> ghidra.program.model.address.Address:
        """
        Get the "to" address for this reference.
        """
        ...

    def hashCode(self) -> int: ...

    def isEntryPointReference(self) -> bool:
        """
        Returns true if this reference is an instance of EntryReference.
        """
        ...

    def isExternalReference(self) -> bool:
        """
        Returns true if this reference is an instance of ExternalReference.
        """
        ...

    def isMemoryReference(self) -> bool:
        """
        Returns true if this reference to an address in the programs memory
         space. This includes offset and shifted references.
        """
        ...

    def isMnemonicReference(self) -> bool:
        """
        Return true if this reference is on the Mnemonic and not on an operand
        """
        ...

    def isOffsetReference(self) -> bool:
        """
        Returns true if this reference is an instance of OffsetReference.
        """
        ...

    def isOperandReference(self) -> bool:
        """
        Return true if this reference is on an operand and not on the Mnemonic.
        """
        ...

    def isPrimary(self) -> bool:
        """
        Return whether this reference is marked as primary.
        """
        ...

    def isRegisterReference(self) -> bool:
        """
        Returns true if this reference to an address in the programs register
         space.
        """
        ...

    def isShiftedReference(self) -> bool:
        """
        Returns true if this reference is an instance of ShiftedReference.
        """
        ...

    def isStackReference(self) -> bool:
        """
        Returns true if this reference is an instance of StackReference and
         refers to a stack location.
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
    def entryPointReference(self) -> bool: ...

    @property
    def externalReference(self) -> bool: ...

    @property
    def fromAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def memoryReference(self) -> bool: ...

    @property
    def mnemonicReference(self) -> bool: ...

    @property
    def offsetReference(self) -> bool: ...

    @property
    def operandIndex(self) -> int: ...

    @property
    def operandReference(self) -> bool: ...

    @property
    def primary(self) -> bool: ...

    @property
    def referenceType(self) -> ghidra.program.model.symbol.RefType: ...

    @property
    def registerReference(self) -> bool: ...

    @property
    def shiftedReference(self) -> bool: ...

    @property
    def source(self) -> ghidra.program.model.symbol.SourceType: ...

    @property
    def stackReference(self) -> bool: ...

    @property
    def symbolID(self) -> long: ...

    @property
    def toAddress(self) -> ghidra.program.model.address.Address: ...
