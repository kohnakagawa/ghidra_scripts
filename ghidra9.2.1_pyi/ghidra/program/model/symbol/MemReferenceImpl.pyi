import ghidra.program.model.address
import ghidra.program.model.symbol
import java.lang


class MemReferenceImpl(object, ghidra.program.model.symbol.Reference):
    """
    Implementation for a reference, not associated with a program.
    """

    MNEMONIC: int = -1
    OTHER: int = -2



    def __init__(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, refType: ghidra.program.model.symbol.RefType, sourceType: ghidra.program.model.symbol.SourceType, opIndex: int, isPrimary: bool):
        """
        Constructs a MemReferenceImpl.
        @param fromAddr reference from address
        @param toAddr reference to address
        @param refType the type of the reference
        @param sourceType reference source type {@link SourceType}
        @param opIndex the operand index of the from location
        @param isPrimary true if this reference should substitue the operand
        """
        ...



    @overload
    def compareTo(self, ref: ghidra.program.model.symbol.Reference) -> int:
        """
        @see java.lang.Comparable#compareTo(Object)
        """
        ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool:
        """
        @see java.lang.Object#equals(Object)
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFromAddress(self) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.symbol.Reference#getFromAddress()
        """
        ...

    def getOperandIndex(self) -> int:
        """
        @see ghidra.program.model.symbol.Reference#getOperandIndex()
        """
        ...

    def getReferenceType(self) -> ghidra.program.model.symbol.RefType:
        """
        @see ghidra.program.model.symbol.Reference#getReferenceType()
        """
        ...

    def getSource(self) -> ghidra.program.model.symbol.SourceType: ...

    def getSymbolID(self) -> long:
        """
        @see ghidra.program.model.symbol.Reference#getSymbolID()
        """
        ...

    def getToAddress(self) -> ghidra.program.model.address.Address:
        """
        @see ghidra.program.model.symbol.Reference#getToAddress()
        """
        ...

    def hashCode(self) -> int: ...

    def isEntryPointReference(self) -> bool:
        """
        @see ghidra.program.model.symbol.Reference#isEntryPointReference()
        """
        ...

    def isExternalReference(self) -> bool:
        """
        @see ghidra.program.model.symbol.Reference#isExternalReference()
        """
        ...

    def isMemoryReference(self) -> bool:
        """
        @see ghidra.program.model.symbol.Reference#isMemoryReference()
        """
        ...

    def isMnemonicReference(self) -> bool:
        """
        @see ghidra.program.model.symbol.Reference#isMnemonicReference()
        """
        ...

    def isOffsetReference(self) -> bool:
        """
        @see ghidra.program.model.symbol.Reference#isOffsetReference()
        """
        ...

    def isOperandReference(self) -> bool:
        """
        @see ghidra.program.model.symbol.Reference#isOperandReference()
        """
        ...

    def isPrimary(self) -> bool:
        """
        @see ghidra.program.model.symbol.Reference#isPrimary()
        """
        ...

    def isRegisterReference(self) -> bool:
        """
        @see ghidra.program.model.symbol.Reference#isRegisterReference()
        """
        ...

    def isShiftedReference(self) -> bool:
        """
        @see ghidra.program.model.symbol.Reference#isShiftedReference()
        """
        ...

    def isStackReference(self) -> bool:
        """
        @see ghidra.program.model.symbol.Reference#isStackReference()
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setSource(self, source: ghidra.program.model.symbol.SourceType) -> None: ...

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

    @source.setter
    def source(self, value: ghidra.program.model.symbol.SourceType) -> None: ...

    @property
    def stackReference(self) -> bool: ...

    @property
    def symbolID(self) -> long: ...

    @property
    def toAddress(self) -> ghidra.program.model.address.Address: ...
