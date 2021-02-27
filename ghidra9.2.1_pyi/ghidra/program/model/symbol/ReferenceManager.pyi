from typing import List
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.symbol
import java.lang


class ReferenceManager(object):
    """
    Interface for managing references.
    """

    MNEMONIC: int = -1







    @overload
    def addExternalReference(self, fromAddr: ghidra.program.model.address.Address, opIndex: int, location: ghidra.program.model.symbol.ExternalLocation, source: ghidra.program.model.symbol.SourceType, type: ghidra.program.model.symbol.RefType) -> ghidra.program.model.symbol.Reference:
        """
        Adds an external reference.  If a reference already
         exists for the fromAddr and opIndex, the existing reference is replaced
         with the new reference.
        @param fromAddr from address (source of the reference)
        @param opIndex operand index
        @param location external location
        @param source the source of this reference
        @param type reference type - how the location is being referenced
        @return external reference
        @throws InvalidInputException
        """
        ...

    @overload
    def addExternalReference(self, fromAddr: ghidra.program.model.address.Address, libraryName: unicode, extLabel: unicode, extAddr: ghidra.program.model.address.Address, source: ghidra.program.model.symbol.SourceType, opIndex: int, type: ghidra.program.model.symbol.RefType) -> ghidra.program.model.symbol.Reference:
        """
        Adds an external reference.  If a reference already
         exists for the fromAddr and opIndex, the existing reference is replaced
         with the new reference.
        @param fromAddr from address (source of the reference)
        @param libraryName name of external program
        @param extLabel label within the external program, may be null if extAddr is not null
        @param extAddr address within the external program, may be null
        @param source the source of this reference
        @param type reference type - how the location is being referenced
        @param opIndex operand index
        @throws InvalidInputException
        @throws DuplicateNameException
        """
        ...

    @overload
    def addExternalReference(self, fromAddr: ghidra.program.model.address.Address, extNamespace: ghidra.program.model.symbol.Namespace, extLabel: unicode, extAddr: ghidra.program.model.address.Address, source: ghidra.program.model.symbol.SourceType, opIndex: int, type: ghidra.program.model.symbol.RefType) -> ghidra.program.model.symbol.Reference:
        """
        Adds an external reference.  If a reference already
         exists for the fromAddr and opIndex, the existing reference is replaced
         with the new reference.
        @param fromAddr from address (source of the reference)
        @param extNamespace external namespace containing the named external label.
        @param extLabel label within the external program, may be null if extAddr is not null
        @param extAddr address within the external program, may be null
        @param source the source of this reference
        @param type reference type - how the location is being referenced
        @param opIndex operand index
        @throws InvalidInputException
        @throws DuplicateNameException
        """
        ...

    def addMemoryReference(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, type: ghidra.program.model.symbol.RefType, source: ghidra.program.model.symbol.SourceType, opIndex: int) -> ghidra.program.model.symbol.Reference:
        """
        Adds a memory reference.  Only first the first memory reference placed on
         an operand will be made primary by default.  All non-memory references
         will be removed from the specified operand.
        @param fromAddr address of the codeunit where the reference occurs
        @param toAddr address of the location being referenced.
         Memory, stack, and register addresses are all permitted.
        @param type reference type - how the location is being referenced.
        @param source the source of this reference
        @param opIndex the operand index
         display of the operand making this reference
        """
        ...

    def addOffsetMemReference(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, offset: long, type: ghidra.program.model.symbol.RefType, source: ghidra.program.model.symbol.SourceType, opIndex: int) -> ghidra.program.model.symbol.Reference:
        """
        Add an offset memory reference.  Only first the first memory reference placed on
         an operand will be made primary by default.  All non-memory references
         will be removed from the specified operand.
        @param fromAddr address for the "from"
        @param toAddr address of the "to"
        @param offset value added to a base address to get the toAddr
        @param type reference type - how the location is being referenced
        @param source the source of this reference
        @param opIndex the operand index
        """
        ...

    def addReference(self, reference: ghidra.program.model.symbol.Reference) -> ghidra.program.model.symbol.Reference:
        """
        Add a memory, stack, register or external reference
        @param reference
        """
        ...

    def addRegisterReference(self, fromAddr: ghidra.program.model.address.Address, opIndex: int, register: ghidra.program.model.lang.Register, type: ghidra.program.model.symbol.RefType, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.Reference:
        """
        Add a reference to a register. If a reference already
         exists for the fromAddr and opIndex, the existing reference is replaced
         with the new reference.
        @param fromAddr "from" address
        @param opIndex operand index
        @param register register to add the reference to
        @param type reference type - how the location is being referenced.
        @param source the source of this reference
        """
        ...

    def addShiftedMemReference(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, shiftValue: int, type: ghidra.program.model.symbol.RefType, source: ghidra.program.model.symbol.SourceType, opIndex: int) -> ghidra.program.model.symbol.Reference:
        """
        Add a shifted memory reference; the "to" address is computed as the value
         at the operand at opIndex shifted by some number of bits, specified in the
         shiftValue parameter.  Only first the first memory reference placed on
         an operand will be made primary by default.  All non-memory references
         will be removed from the specified operand.
        @param fromAddr address for the "from"
        @param toAddr computed as the value of the operand at opIndex shifted
         by the number of bits specified by shiftValue
        @param shiftValue
        @param type reference type - how the location is being referenced
        @param source the source of this reference
        @param opIndex the operand index
        """
        ...

    def addStackReference(self, fromAddr: ghidra.program.model.address.Address, opIndex: int, stackOffset: int, type: ghidra.program.model.symbol.RefType, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.Reference:
        """
        Add a reference to a stack location. If a reference already
         exists for the fromAddr and opIndex, the existing reference is replaced
         with the new reference.
        @param fromAddr "from" address within a function
        @param opIndex operand index
        @param stackOffset stack offset of the reference
        @param type reference type - how the location is being referenced.
        @param source the source of this reference
        """
        ...

    def delete(self, ref: ghidra.program.model.symbol.Reference) -> None:
        """
        Deletes the given reference object
        @param ref the reference to be deleted.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getExternalReferences(self) -> ghidra.program.model.symbol.ReferenceIterator:
        """
        Returns an iterator over all external references
        """
        ...

    def getFlowReferencesFrom(self, addr: ghidra.program.model.address.Address) -> List[ghidra.program.model.symbol.Reference]:
        """
        Get the flow references from the given address.
        @param addr the address of the codeunit to get all flows from.
        """
        ...

    def getPrimaryReferenceFrom(self, addr: ghidra.program.model.address.Address, opIndex: int) -> ghidra.program.model.symbol.Reference:
        """
        Get the primary reference from the given address.
        @param addr from address
        @param opIndex operand index
        """
        ...

    def getReference(self, fromAddr: ghidra.program.model.address.Address, toAddr: ghidra.program.model.address.Address, opIndex: int) -> ghidra.program.model.symbol.Reference:
        """
        Get the reference that has the given from and to address, and
         operand index.
        @param fromAddr the address of the codeunit making the reference.
        @param toAddr the address being referred to.
        @param opIndex the operand index.
        """
        ...

    def getReferenceCountFrom(self, fromAddr: ghidra.program.model.address.Address) -> int:
        """
        Returns the number of memory References from the specified
         <code>fromAddr</code>
        @param fromAddr the address of the codeunit making the reference.
        """
        ...

    def getReferenceCountTo(self, toAddr: ghidra.program.model.address.Address) -> int:
        """
        Returns the number of memory References to the specified
         <code>toAddr</code>
        @param toAddr the address being referenced
        """
        ...

    def getReferenceDestinationCount(self) -> int:
        """
        Return the number of references for "to" addresses.
        """
        ...

    @overload
    def getReferenceDestinationIterator(self, startAddr: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.address.AddressIterator:
        """
        Returns an iterator over all addresses that are the "To" address in a
         reference.
        @param startAddr start of iterator
        @param forward true means to iterate in the forward direction
        """
        ...

    @overload
    def getReferenceDestinationIterator(self, addrSet: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.address.AddressIterator:
        """
        Returns an iterator over all addresses that are the "To" address in a
         memory reference, restricted by the given address set.
        @param addrSet the set of address to restrict the iterator.
        @param forward true means to iterate in the forward direction
        """
        ...

    def getReferenceIterator(self, startAddr: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.ReferenceIterator:
        """
        Get an iterator over references starting with the specified
         fromAddr.  A forward iterator is returned with references sorted on
         the from address.
        @param startAddr the first from address to consider.
        @return a forward memory reference iterator.
        """
        ...

    def getReferenceLevel(self, toAddr: ghidra.program.model.address.Address) -> int:
        """
        Returns the reference level for the references to the given address
        @param toAddr the address at which to find the highest reference level
        """
        ...

    def getReferenceSourceCount(self) -> int:
        """
        Return the number of references for "from" addresses.
        """
        ...

    @overload
    def getReferenceSourceIterator(self, startAddr: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.address.AddressIterator:
        """
        Returns an iterator over addresses that are the "From" address in a
         reference
        @param startAddr address to position iterator.
        @param forward true means to iterate in the forward direction
        """
        ...

    @overload
    def getReferenceSourceIterator(self, addrSet: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.address.AddressIterator:
        """
        Returns an iterator over all addresses that are the "From" address in a
         reference, restricted by the given address set.
        @param addrSet the set of address to restrict the iterator.
        @param forward true means to iterate in the forward direction
        """
        ...

    def getReferencedVariable(self, reference: ghidra.program.model.symbol.Reference) -> ghidra.program.model.listing.Variable:
        """
        Returns the referenced function variable.
        @param reference
        @return function variable or null if variable not found
        """
        ...

    @overload
    def getReferencesFrom(self, addr: ghidra.program.model.address.Address) -> List[ghidra.program.model.symbol.Reference]:
        """
        Get all references "from" the specified addr.
        @param addr address of code-unit making the references.
        @return array of all references "from" the specified addr.
        """
        ...

    @overload
    def getReferencesFrom(self, fromAddr: ghidra.program.model.address.Address, opIndex: int) -> List[ghidra.program.model.symbol.Reference]:
        """
        Returns all references "from" the given fromAddr and operand (specified by opIndex).
        @param fromAddr the from which to get references
        @param opIndex the operand from which to get references
        @return all references "from" the given fromAddr and operand.
        """
        ...

    @overload
    def getReferencesTo(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.ReferenceIterator:
        """
        Get an iterator over all references that have the given address as
         their "To" address.
        @param addr the address that all references in the iterator refer to.
        """
        ...

    @overload
    def getReferencesTo(self, var: ghidra.program.model.listing.Variable) -> List[ghidra.program.model.symbol.Reference]:
        """
        Returns all references to the given variable.  Only data references to storage
         are considered.
        @param var variable to retrieve references to
        @return array of variable references, or zero length array if no
         references exist
        """
        ...

    def hasFlowReferencesFrom(self, addr: ghidra.program.model.address.Address) -> bool:
        """
        Return whether the given address has flow references from this address.
        @param addr the address to test for flow references.
        """
        ...

    @overload
    def hasReferencesFrom(self, fromAddr: ghidra.program.model.address.Address) -> bool:
        """
        Returns true if there are any memory references at the given
         address.
        @param fromAddr the address of the codeunit being tested
        """
        ...

    @overload
    def hasReferencesFrom(self, fromAddr: ghidra.program.model.address.Address, opIndex: int) -> bool:
        """
        Returns true if there are any memory references at the given
         address/opIndex.  Keep in mind this is a rather inefficient
         method as it must examine all references from the specified
         fromAddr.
        @param fromAddr the address of the codeunit being tested
        @param opIndex the index of the operand being tested.
        """
        ...

    def hasReferencesTo(self, toAddr: ghidra.program.model.address.Address) -> bool:
        """
        Return true if a memory reference exists with the given "to" address.
        @param toAddr address being referred to.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def removeAllReferencesFrom(self, fromAddr: ghidra.program.model.address.Address) -> None:
        """
        Remove all stack, external, and memory references for the given
         from address.
        @param fromAddr the address of the codeunit from which to remove all references.
        """
        ...

    @overload
    def removeAllReferencesFrom(self, beginAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address) -> None:
        """
        Removes all references where "From address" is in the given range.
        @param beginAddr the first address in the range.
        @param endAddr the last address in the range.
        """
        ...

    def removeAssociation(self, ref: ghidra.program.model.symbol.Reference) -> None:
        """
        Removes any symbol associations with the given reference.
        @param ref the reference for which any symbol association is to be removed.
        @throws IllegalArgumentException if the given references does not exist.
        """
        ...

    def setAssociation(self, s: ghidra.program.model.symbol.Symbol, ref: ghidra.program.model.symbol.Reference) -> None:
        """
        Associates the given reference with the given symbol.
        @param s the symbol to associate with the given reference.
        @param ref the reference to associate with the given symbol
        @throws IllegalArgumentException If the given reference does not already
         exist or its "To" address
         is not the same as the symbol's address.
        """
        ...

    def setPrimary(self, ref: ghidra.program.model.symbol.Reference, isPrimary: bool) -> None:
        """
        Set the given reference's primary attribute
        @param ref the reference to make primary.
        @param isPrimary true to make the reference primary, false to make it non-primary
        """
        ...

    def toString(self) -> unicode: ...

    def updateRefType(self, ref: ghidra.program.model.symbol.Reference, refType: ghidra.program.model.symbol.RefType) -> ghidra.program.model.symbol.Reference:
        """
        Uodate the reference type on a memory reference.
        @param ref reference to be updated
        @param refType new reference type
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def externalReferences(self) -> ghidra.program.model.symbol.ReferenceIterator: ...

    @property
    def referenceDestinationCount(self) -> int: ...

    @property
    def referenceSourceCount(self) -> int: ...
