import ghidra.program.model.address
import java.lang


class VerticalPixelAddressMap(object):








    def equals(self, __a0: object) -> bool: ...

    def findLayoutAt(self, y: int) -> int:
        """
        Finds the layout containing the given point.
        @param y the y coordinate of layout to be found.
        """
        ...

    def getAddressSet(self) -> ghidra.program.model.address.AddressSetView:
        """
        Gets the address set of this address map.
        @return the address set of this address map
        """
        ...

    def getBeginPosition(self, i: int) -> int:
        """
        Returns the y position of the top of the i'th layout.
        @param i the index of the layout.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getEndAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the index of the last layout in this map.
        """
        ...

    def getEndPosition(self, i: int) -> int:
        """
        Returns the y position of the bottom of the i'th layout.
        @param i the index of the layout.
        """
        ...

    def getLayoutAddress(self, i: int) -> ghidra.program.model.address.Address:
        """
        Returns the address of the i'th layout in this map.
        @param i the index into the local array of layouts
        @return the address of the i'th layout in this map.
        """
        ...

    def getLayoutEndAddress(self, i: int) -> ghidra.program.model.address.Address:
        """
        Returns the address of the bottom of the i'th layout.

         <P>Note: this will return null if at the end of an overlay block.
        @param i the index of the layout
        @return the address of the bottom of the i'th layout
        """
        ...

    def getMarkPosition(self, i: int) -> int:
        """
        Returns pixel location to draw marker icon.
        @param i the index of the layout to be marked with an icon.
        @return the vertical pixel location at which to draw the icon.
        """
        ...

    def getNumLayouts(self) -> int:
        """
        Returns the number of layouts in this map.
        """
        ...

    def getStartAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the Address of the first layout in this map
        """
        ...

    def hasPrimaryField(self, i: int) -> bool:
        """
        Determines if the given layout index contains the primary field
        @param i the layout index to test.
        @return true if the layout contains the primary field.
        """
        ...

    def hashCode(self) -> int: ...

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
    def addressSet(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def endAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def numLayouts(self) -> int: ...

    @property
    def startAddress(self) -> ghidra.program.model.address.Address: ...
