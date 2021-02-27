import ghidra.app.util.viewer.util
import java.lang
import javax.swing


class OverviewProvider(object):
    """
    Interface implemented by classes that provide overview components to the right side
     of the listing.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getComponent(self) -> javax.swing.JComponent:
        """
        Returns the component to diplay in the right margin of the listing.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setAddressIndexMap(self, map: ghidra.app.util.viewer.util.AddressIndexMap) -> None:
        """
        Sets the AddressIndexMap whenever it changes so that the overview provider has
         an current map.
        @param map the current AddressIndexMap of the ListingPanel
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
    def addressIndexMap(self) -> None: ...  # No getter available.

    @addressIndexMap.setter
    def addressIndexMap(self, value: ghidra.app.util.viewer.util.AddressIndexMap) -> None: ...

    @property
    def component(self) -> javax.swing.JComponent: ...
