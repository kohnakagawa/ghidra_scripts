import ghidra.program.model.address
import ghidra.program.model.symbol
import java.lang


class ThunkReference(object, ghidra.program.model.symbol.DynamicReference):
    """
    Implementation for a Thunk Function reference.
     These references are dynamic in nature and may not be explicitly added,
     removed or altered.  There presence is inferred by the existence
     of a thunk function.
    """

    MNEMONIC: int = -1
    OTHER: int = -2



    def __init__(self, thunkAddr: ghidra.program.model.address.Address, thunkedAddr: ghidra.program.model.address.Address):
        """
        Thunk reference constructor
        @param thunkAddr thunk function address
        @param thunkedAddr "thunked" function address
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
