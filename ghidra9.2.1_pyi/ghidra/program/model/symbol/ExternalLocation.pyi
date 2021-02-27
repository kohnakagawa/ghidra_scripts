import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.program.model.symbol
import java.lang


class ExternalLocation(object):
    """
    ExternalLocation defines a location within an external
     program (i.e., library).  The external program is uniquely identified
     by a program name, and the location within the program is identified by
     label, address or both.
    """









    def createFunction(self) -> ghidra.program.model.listing.Function:
        """
        Create an external function associated with this location or return
         the existing function if one already exists
        @return external function
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the external address if known, or null
        @return the external address if known, or null
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDataType(self) -> ghidra.program.model.data.DataType:
        """
        Returns the DataType which has been associated with this location.
        """
        ...

    def getExternalSpaceAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the address in "External" (fake) space where this location is stored.
        @return the address that represents this location in "External" space.
        """
        ...

    def getFunction(self) -> ghidra.program.model.listing.Function:
        """
        Returns the external function associated with this location or null if this is a data
         location.
        @return external function associated with this location or null
         if this is a data location.
        """
        ...

    def getLabel(self) -> unicode:
        """
        Returns the external label associated with this location.
        @return the external label associated with this location.
        """
        ...

    def getLibraryName(self) -> unicode:
        """
        Returns the name of the external program containing this location.
        @return the name of the external program containing this location.
        """
        ...

    def getOriginalImportedName(self) -> unicode:
        """
        Returns the original name for this location. Will be null if the name was never
         changed.
        @return the original name for this location. Will be null if the name was never
         changed.
        """
        ...

    def getParentName(self) -> unicode:
        """
        Returns the name of the parent namespace containing this location.
        @return the name of the parent namespace containing this location.
        """
        ...

    def getParentNameSpace(self) -> ghidra.program.model.symbol.Namespace:
        """
        Returns the parent namespace containing this location.
        @return the parent namespace containing this location.
        """
        ...

    def getSource(self) -> ghidra.program.model.symbol.SourceType:
        """
        Returns the source of this location.
        @return the source
        """
        ...

    def getSymbol(self) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the symbol associated with this external location or null.
        @return the symbol associated with this external location or null.
        """
        ...

    def hashCode(self) -> int: ...

    def isEquivalent(self, other: ghidra.program.model.symbol.ExternalLocation) -> bool:
        """
        Returns true if the given external location has the same name, namespace, original import name,
         and external address.
        @param other the other ExternalLocation to compare
        @return true if the other location is equivalent to this one.
        """
        ...

    def isFunction(self) -> bool:
        """
        @return true if location corresponds to a function
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreOriginalName(self) -> None:
        """
        If this external location has a replacement name, then the primary symbol will be deleted and
         the original symbol will become the primary symbol, effectively restoring the location to
         it's original name.
        """
        ...

    def setAddress(self, address: ghidra.program.model.address.Address) -> None:
        """
        Sets the address in the external program associated with this location.
         The address may not be null if location has a default label.
        @param address the address to set.
        @throws InvalidInputException if address is null and location currently has a default name
        """
        ...

    def setDataType(self, dt: ghidra.program.model.data.DataType) -> None:
        """
        Associate the specified data type with this location.
        @param dt data type
        """
        ...

    def setLocation(self, label: unicode, addr: ghidra.program.model.address.Address, source: ghidra.program.model.symbol.SourceType) -> None:
        """
        Set the external label which defines this location.
        @param label external label, may be null if addr is not null.  Label may also be
         namespace qualified and best effort will be used to parse namespace (see {@link SymbolPath}).
         If a namespace is not included within label, the current namespace will be preserved.
         Note that this method does not properly handle the presence of template information within the
         label.
        @param addr external address, may be null
        @param source the source of the external label name
        @throws DuplicateNameException if another location with this label has
         already been defined
        @throws InvalidInputException
        """
        ...

    def setName(self, namespace: ghidra.program.model.symbol.Namespace, name: unicode, sourceType: ghidra.program.model.symbol.SourceType) -> None:
        """
        Set a new name for this external location. The new
         name will become the primary symbol for this location. The current name
         for this location will be saved as the original symbol for this location.
        @param namespace the namespace for the original symbol.  Can be different than original symbol
        @param name the user-friendly name.
        @param sourceType the SourceType for the new name.
        @throws InvalidInputException if the name contains illegal characters (space for example)
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
    def address(self) -> ghidra.program.model.address.Address: ...

    @address.setter
    def address(self, value: ghidra.program.model.address.Address) -> None: ...

    @property
    def dataType(self) -> ghidra.program.model.data.DataType: ...

    @dataType.setter
    def dataType(self, value: ghidra.program.model.data.DataType) -> None: ...

    @property
    def externalSpaceAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def function(self) -> bool: ...

    @property
    def label(self) -> unicode: ...

    @property
    def libraryName(self) -> unicode: ...

    @property
    def originalImportedName(self) -> unicode: ...

    @property
    def parentName(self) -> unicode: ...

    @property
    def parentNameSpace(self) -> ghidra.program.model.symbol.Namespace: ...

    @property
    def source(self) -> ghidra.program.model.symbol.SourceType: ...

    @property
    def symbol(self) -> ghidra.program.model.symbol.Symbol: ...
