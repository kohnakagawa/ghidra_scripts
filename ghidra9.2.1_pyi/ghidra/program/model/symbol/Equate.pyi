from typing import List
import ghidra.program.model.address
import ghidra.program.model.symbol
import ghidra.util
import java.lang


class Equate(object):
    """
    An Equate associates a string with a scalar value in the program,
     and contains a list of addresses and operand positions that refer
     to this equate.
    """









    @overload
    def addReference(self, refAddr: ghidra.program.model.address.Address, opndPosition: int) -> None:
        """
        Add a reference (at the given operand position) to this equate.  If a reference already
         exists for the instruction at this address, then the old reference will be removed
         before the new reference is added.
        @param refAddr the address where the equate is used.
        @param opndPosition the operand index where the equate is used.
        """
        ...

    @overload
    def addReference(self, dynamicHash: long, refAddr: ghidra.program.model.address.Address) -> None:
        """
        Add a reference (at the given dynamic hash position) to this equate. If a reference already
         exists for the instruction at this address, then the old reference will be removed
         before the new reference is added.
        @param dynamicHash constant varnode dynamic hash value
        @param refAddr the address where the equate is used.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDisplayName(self) -> unicode:
        """
        Gets the "display name" of this equate.  Note that the display name may be different
         than the equate's actual name if the equate is based off a data type id.
        @return The "display name" of this equate.
        """
        ...

    def getDisplayValue(self) -> unicode:
        """
        Gets a more accurate representation of the equate value. Used for rendering as close to the
         listing as possible.
        @return A more accurate representation of the equate value.
        """
        ...

    def getEnumUUID(self) -> ghidra.util.UniversalID:
        """
        Gets the universal id from this equate if the equate was based off of an enum.
        @return The universal id for this equate.
        """
        ...

    def getName(self) -> unicode:
        """
        Get the actual name of this equate.  Note that this name may be different than the
         "display name," which is what the user will see.
        @return The actual name of this equate.
        """
        ...

    def getReferenceCount(self) -> int:
        """
        Get the number of references to this equate.
        """
        ...

    def getReferences(self) -> List[ghidra.program.model.symbol.EquateReference]:
        """
        Get the references for this equate.
        @return a array of EquateReferences.
        """
        ...

    def getValue(self) -> long:
        """
        Get the value of this equate.
        """
        ...

    def hashCode(self) -> int: ...

    def isEnumBased(self) -> bool:
        """
        Checks if equate is based off an enum's universal id.
        @return
        """
        ...

    def isValidUUID(self) -> bool:
        """
        Checks if equate is based off an enum's universal id and checks if the enum still exists.
         The equate is still valid if the equate is not based off an enum.
        @return true if the equate is based off an enum that still exists.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def removeReference(self, refAddr: ghidra.program.model.address.Address, opndPosition: int) -> None:
        """
        Remove the reference at the given operand position.
        @param refAddr the address that was using this equate
        @param opndPosition the operand index of the operand that was using this eqate.
        """
        ...

    @overload
    def removeReference(self, dynamicHash: long, refAddr: ghidra.program.model.address.Address) -> None:
        """
        Remove the reference at the given address
        @param dynamicHash the hash of the reference
        @param refAddr the reference's address
        """
        ...

    def renameEquate(self, newName: unicode) -> None:
        """
        Changes the name associated with the equate.
        @param newName the new name for this equate.
        @exception DuplicateNameException thrown if newName is already
           used by another equate.
        @throws InvalidInputException if newName contains blank characters,
         is zero length, or is null
        """
        ...

    def toString(self) -> unicode:
        """
        Get the name of this equate.
        @see #getName()
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def displayName(self) -> unicode: ...

    @property
    def displayValue(self) -> unicode: ...

    @property
    def enumBased(self) -> bool: ...

    @property
    def enumUUID(self) -> ghidra.util.UniversalID: ...

    @property
    def name(self) -> unicode: ...

    @property
    def referenceCount(self) -> int: ...

    @property
    def references(self) -> List[ghidra.program.model.symbol.EquateReference]: ...

    @property
    def validUUID(self) -> bool: ...

    @property
    def value(self) -> long: ...
