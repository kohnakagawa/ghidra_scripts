import ghidra.program.model.address
import ghidra.util.prop
import java.lang


class PropertyMap(object):
    """
    Interface to define a map containing properties over a set of addresses.
    """









    def applyValue(self, visitor: ghidra.util.prop.PropertyVisitor, addr: ghidra.program.model.address.Address) -> None:
        """
        Applies a property value at the indicated address without knowing its
         type (String, int, long, etc.) by using the property visitor.
        @param visitor the property visitor that lets you apply the property
         without knowing its specific type ahead of time.
        @param addr the address where the property is to be applied.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFirstPropertyAddress(self) -> ghidra.program.model.address.Address:
        """
        Get the first Address where a property value exists.
        """
        ...

    def getLastPropertyAddress(self) -> ghidra.program.model.address.Address:
        """
        Get the last Address where a property value exists.
        """
        ...

    def getName(self) -> unicode:
        """
        Get the name for this property map.
        """
        ...

    def getNextPropertyAddress(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address:
        """
        Get the next address where the property value exists.
        @param addr the address from which to begin the search (exclusive).
        """
        ...

    def getObject(self, addr: ghidra.program.model.address.Address) -> object:
        """
        Returns the property value stored at the specified
         address or null if no property found.
        @param addr property address
        @return property value
        """
        ...

    def getPreviousPropertyAddress(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address:
        """
        Get the previous Address where a property value exists.
        @param addr the address from which
         		to begin the search (exclusive).
        """
        ...

    @overload
    def getPropertyIterator(self) -> ghidra.program.model.address.AddressIterator:
        """
        Returns an iterator over the addresses that a property
         value.
        @exception TypeMismatchException thrown if the property does not
         have values of type <CODE>Object</CODE>.
        """
        ...

    @overload
    def getPropertyIterator(self, asv: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressIterator:
        """
        Returns an iterator over the addresses that have a property value and
         are in the given address set.
        @param asv the set of addresses to iterate over.
        """
        ...

    @overload
    def getPropertyIterator(self, start: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.address.AddressIterator:
        """
        Returns an iterator over the address having a property
         value.
        @param start the starting address
        @param forward if true will iterate in increasing address order, otherwise it will start at
         the end and iterate in decreasing address order
        @exception TypeMismatchException thrown if the property does not
         have values of type <CODE>Object</CODE>.
        """
        ...

    @overload
    def getPropertyIterator(self, asv: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.address.AddressIterator:
        """
        Returns an iterator over the addresses that have a property value and
         are in the given address set.
        @param forward if true will iterate in increasing address order, otherwise it will start at
         the end and iterate in decreasing address order
        """
        ...

    @overload
    def getPropertyIterator(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressIterator:
        """
        Returns an iterator over the indices having a property
         value.
        @exception TypeMismatchException thrown if the property does not
         have values of type <CODE>Object</CODE>.
        """
        ...

    @overload
    def getPropertyIterator(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.address.AddressIterator:
        """
        Returns an iterator over addresses that have a property
         value.
        @param forward if true will iterate in increasing address order, otherwise it will start at
         the end and iterate in decreasing address order
        @exception TypeMismatchException thrown if the property does not
         have values of type <CODE>Object</CODE>.
        """
        ...

    def getSize(self) -> int:
        """
        Get the number of properties in the map.
        """
        ...

    def hasProperty(self, addr: ghidra.program.model.address.Address) -> bool:
        """
        returns whether there is a property value at addr.
        @param addr the address in question
        """
        ...

    def hashCode(self) -> int: ...

    @overload
    def intersects(self, set: ghidra.program.model.address.AddressSetView) -> bool:
        """
        Indicate whether there is an address within
         the set which exists within this map.<p>
        @param set set of addresses
        @return boolean true if at least one address in the set
         has the property, false otherwise.
        """
        ...

    @overload
    def intersects(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> bool:
        """
        Given two addresses, indicate whether there is an address in
         that range (inclusive) having the property.<p>
        @param start the start of the range.
        @param end the end of the range.
        @return boolean true if at least one address in the range
         has the property, false otherwise.
        """
        ...

    def moveRange(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, newStart: ghidra.program.model.address.Address) -> None:
        """
        Moves the properties defined in the range from the start address thru the
         end address to now be located beginning at the newStart address.
         The moved properties will be located at the same relative location to
         the newStart address as they were previously to the start address.
        @param start the start of the range to move.
        @param end the end of the range to move.
        @param newStart the new start location of the range of properties
         after the move.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, addr: ghidra.program.model.address.Address) -> bool:
        """
        Remove the property value at the given address.
        @return true if the property value was removed, false
           otherwise.
        @param addr the address where the property should be removed
        """
        ...

    def removeRange(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> bool:
        """
        Removes all property values within a given range.
        @param start begin range
        @param end end range, inclusive
        @return true if any property value was removed; return
         		false otherwise.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def firstPropertyAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def lastPropertyAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def name(self) -> unicode: ...

    @property
    def propertyIterator(self) -> ghidra.program.model.address.AddressIterator: ...

    @property
    def size(self) -> int: ...
