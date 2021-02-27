import ghidra.app.services
import ghidra.program.model.address
import java.awt
import java.lang


class MarkerSet(java.lang.Comparable, object):
    """
    Defines methods for working with a set of addresses that correspond to markers.
    """









    @overload
    def add(self, addr: ghidra.program.model.address.Address) -> None:
        """
        Add a marker at the address
        @param addr the address
        """
        ...

    @overload
    def add(self, range: ghidra.program.model.address.AddressRange) -> None:
        """
        Add a marker across the address range
        @param range the addresses
        """
        ...

    @overload
    def add(self, addrSet: ghidra.program.model.address.AddressSetView) -> None:
        """
        Add a marker at each address in the given address set
        @param addrSet the addresses
        """
        ...

    @overload
    def add(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> None:
        """
        Add the range given the start and end of the range
        @param start the start address
        @param end the end address
        """
        ...

    @overload
    def clear(self, addr: ghidra.program.model.address.Address) -> None:
        """
        Clear any marker at the address
        @param addr the address
        """
        ...

    @overload
    def clear(self, range: ghidra.program.model.address.AddressRange) -> None:
        """
        Clear any marker across the address range
        @param range the addresses
        """
        ...

    @overload
    def clear(self, addrSet: ghidra.program.model.address.AddressSetView) -> None:
        """
        Clear any marker at each address in the address set
        @param addrSet the addresses
        """
        ...

    @overload
    def clear(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> None:
        """
        Remove the given range from the marker set
        @param start the start of the range to remove
        @param end the end of the range to remove
        """
        ...

    def clearAll(self) -> None:
        """
        Clear all defined markers
        """
        ...

    def compareTo(self, __a0: object) -> int: ...

    def contains(self, addr: ghidra.program.model.address.Address) -> bool:
        """
        Determine if this marker set contains the specified address
        @param addr address
        @return true if marker set contains addr
        """
        ...

    def displayInMarkerBar(self) -> bool:
        """
        True if this marker manager displays in the left hand marker bar
        @return true if this marker manager displays in the left hand marker bar
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAddressSet(self) -> ghidra.program.model.address.AddressSet:
        """
        Return the address set for this marker set
        @return the addresses
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getMarkerColor(self) -> java.awt.Color:
        """
        Get the color for the marker
        @return the color
        """
        ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the maximum Address in this MarkerSet;
        @return the maximum Address in this MarkerSet;
        """
        ...

    def getMinAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the minimum Address in this MarkerSet;
        @return the minimum Address in this MarkerSet;
        """
        ...

    def getName(self) -> unicode:
        """
        Return the name of this MarkerSet
        @return the name
        """
        ...

    def getPriority(self) -> int:
        """
        Get display priority
        @return the priority
        """
        ...

    def hashCode(self) -> int: ...

    def intersects(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> bool:
        """
        Returns true if any address in this MarkerSet is contained in the range defined by
         start and end.
        @param start the start address of the range to check for intersection.
        @param end the end address of the range to check for intersection.
        @return true if the set of addresses contained in this MarkerSet intersects the given range.
        """
        ...

    def isActive(self) -> bool:
        """
        Returns true if this MarkerSet is active.  Being "active" means that it is displayed
         in the listing
        @return true if active
        """
        ...

    def isColoringBackground(self) -> bool:
        """
        Returns true if this MarkerSet is coloring the background in the listing for locations
         contained in this MarkerSet
        @return true if coloring background
        """
        ...

    def isDisplayedInNavigationBar(self) -> bool:
        """
        True if this marker manager displays in the right hand navigation bar
        @return true if this marker manager displays in the right hand navigation bar
        """
        ...

    def isPreferred(self) -> bool:
        """
        Gets whether this marker is in the preferred group when determining display priority.
         Typically point markers are in the preferred group and area markers are not.
        @return true if preferred
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setActive(self, state: bool) -> None:
        """
        Return true if this marker set is active
        @param state the state
        """
        ...

    def setAddressSet(self, set: ghidra.program.model.address.AddressSetView) -> None:
        """
        Clears the current set off addresses in this markerSet and adds in the addresses
         from the given AddressSet
        @param set the set of addresses to use in this marker set
        """
        ...

    def setAddressSetCollection(self, set: ghidra.program.model.address.AddressSetCollection) -> None:
        """
        Sets the AddressSetCollection to be used for this this marker set.

         <p><strong>Warning!</strong>
         Using this method will cause this MarkerSet to directly use the given AddressSetCollection.
         If the given AddressSetCollection is not an instance of ModifiableAddressSetCollection,
         then the markerSet methods that add and remove addresses will thrown an
         IllegalArgumentException.
        @param set the addressSetCollection to use as this markerSet's addressSetCollection.
        """
        ...

    def setColoringBackground(self, b: bool) -> None:
        """
        Sets whether or not the MarkerSet is coloring the background of areas in the listing
         contained in this MarkerSet.
        @param b true to color the background.
        """
        ...

    def setMarkerColor(self, color: java.awt.Color) -> None:
        """
        Set the color for the marker
        @param color marker color
        """
        ...

    def setMarkerDescriptor(self, markerDescriptor: ghidra.app.services.MarkerDescriptor) -> None:
        """
        Set the marker manager listener to use for user interaction
         with markers owned by this manager.
        @param markerDescriptor the descriptor
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
    def active(self) -> bool: ...

    @active.setter
    def active(self, value: bool) -> None: ...

    @property
    def addressSet(self) -> ghidra.program.model.address.AddressSet: ...

    @property
    def addressSetCollection(self) -> None: ...  # No getter available.

    @addressSetCollection.setter
    def addressSetCollection(self, value: ghidra.program.model.address.AddressSetCollection) -> None: ...

    @property
    def coloringBackground(self) -> bool: ...

    @coloringBackground.setter
    def coloringBackground(self, value: bool) -> None: ...

    @property
    def displayedInNavigationBar(self) -> bool: ...

    @property
    def markerColor(self) -> java.awt.Color: ...

    @markerColor.setter
    def markerColor(self, value: java.awt.Color) -> None: ...

    @property
    def markerDescriptor(self) -> None: ...  # No getter available.

    @markerDescriptor.setter
    def markerDescriptor(self, value: ghidra.app.services.MarkerDescriptor) -> None: ...

    @property
    def maxAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def minAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def name(self) -> unicode: ...

    @property
    def preferred(self) -> bool: ...

    @property
    def priority(self) -> int: ...
