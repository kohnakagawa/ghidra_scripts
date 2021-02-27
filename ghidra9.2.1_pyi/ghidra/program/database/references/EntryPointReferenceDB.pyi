import ghidra.program.database.references
import ghidra.program.model.address
import ghidra.program.model.symbol
import java.lang


class EntryPointReferenceDB(ghidra.program.database.references.ReferenceDB):








    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool: ...

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

    def hashCode(self) -> int:
        """
        @see java.lang.Object#hashCode
        """
        ...

    def isEntryPointReference(self) -> bool: ...

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
        Return true if this reference is on the mnemonic (versus an operand)
        """
        ...

    def isOffsetReference(self) -> bool:
        """
        @see ghidra.program.model.symbol.Reference#isOffsetReference()
        """
        ...

    def isOperandReference(self) -> bool:
        """
        Return true if this reference is on an operand.
        """
        ...

    def isPrimary(self) -> bool: ...

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

    def toString(self) -> unicode:
        """
        Return a string that represents this references, for debugging purposes.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
