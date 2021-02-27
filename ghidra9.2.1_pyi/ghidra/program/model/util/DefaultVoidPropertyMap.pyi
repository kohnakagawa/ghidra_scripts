import ghidra.program.model.address
import ghidra.program.model.util
import ghidra.util.prop
import java.io
import java.lang


class DefaultVoidPropertyMap(ghidra.program.model.util.DefaultPropertyMap, ghidra.program.model.util.VoidPropertyMap):
    """
    Property manager that deals with properties that are of
     "void" type, which is a marker for whether a property exists.
    """





    def __init__(self, name: unicode):
        """
        Construct a new VoidPropertyMap
        @param name of property
        """
        ...



    def add(self, addr: ghidra.program.model.address.Address) -> None:
        """
        Mark the specified address as having a property
        @param addr address for the property
        """
        ...

    def applyValue(self, visitor: ghidra.util.prop.PropertyVisitor, addr: ghidra.program.model.address.Address) -> None:
        """
        @see ghidra.program.model.util.PropertyMap#applyValue(ghidra.util.prop.PropertyVisitor, ghidra.program.model.address.Address)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode:
        """
        Return the property description.
        @return the property description
        """
        ...

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
        Get the name for this property manager.
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
        @see ghidra.program.model.util.PropertyMap#getObject(ghidra.program.model.address.Address)
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
        Returns an iterator over addresses that have a property value within the
         property map.
        @exception TypeMismatchException thrown if the property does not
         have values of type <CODE>Object</CODE>.
        """
        ...

    @overload
    def getPropertyIterator(self, asv: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressIterator:
        """
        Returns an iterator over the addresses that have a property value and
         are in the given address set.
        """
        ...

    @overload
    def getPropertyIterator(self, start: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.address.AddressIterator:
        """
        @see ghidra.program.model.util.PropertyMap#getPropertyIterator(ghidra.program.model.address.Address, boolean)
        """
        ...

    @overload
    def getPropertyIterator(self, asv: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.address.AddressIterator:
        """
        @see ghidra.program.model.util.PropertyMap#getPropertyIterator(ghidra.program.model.address.AddressSetView, boolean)
        """
        ...

    @overload
    def getPropertyIterator(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> ghidra.program.model.address.AddressIterator:
        """
        Returns an iterator over addresses that have a property value within the
         given address range.
        @param start the first address in the range.
        @param end the last address in the range.
        @exception TypeMismatchException thrown if the property does not
         have values of type <CODE>Object</CODE>.
        """
        ...

    @overload
    def getPropertyIterator(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.address.AddressIterator:
        """
        @see ghidra.program.model.util.PropertyMap#getPropertyIterator(ghidra.program.model.address.Address, ghidra.program.model.address.Address, boolean)
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
    def intersects(self, set: ghidra.program.model.address.AddressSetView) -> bool: ...

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
        @see ghidra.program.model.util.PropertyMap#moveRange(ghidra.program.model.address.Address, ghidra.program.model.address.Address, ghidra.program.model.address.Address)
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

    def restoreProperties(self, ois: java.io.ObjectInputStream) -> None:
        """
        Restore properties from the given input stream.
        @param ois input stream
        @throws IOException if there is a problem reading from the stream
        @throws ClassNotFoundException if the class for the object being
         read is not in the class path
        """
        ...

    def saveProperties(self, oos: java.io.ObjectOutputStream, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> None:
        """
        Save the properties in the given range to output stream.
        @param oos output stream to write to
        @param start start address in the range
        @param end end address in the range
        @throws IOException if there a problem doing the write
        """
        ...

    def setDescription(self, description: unicode) -> None:
        """
        Set the description for this property.
        @param description property description
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
