import docking.widgets.fieldpanel.support
import ghidra.app.util.viewer.listingpanel
import java.awt
import java.lang


class ListingBackgroundColorModel(docking.widgets.fieldpanel.support.BackgroundColorModel, object):
    """
    This interface extends the  BackgroundColorModel  exclusively for BackgroundColorModels used by
     the ListingPanel.  The BackgroundColorModel is a general contract for dealing with
     background colors in a FieldPanel.  ListingBackgroundColorModels require additional
     information such as the AddressIndexMap and the program so that it translate the indexes
     to specific addresses and look up information in the program.
    """









    def equals(self, __a0: object) -> bool: ...

    def getBackgroundColor(self, __a0: long) -> java.awt.Color: ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultBackgroundColor(self) -> java.awt.Color: ...

    def hashCode(self) -> int: ...

    def modelDataChanged(self, listingPanel: ghidra.app.util.viewer.listingpanel.ListingPanel) -> None:
        """
        Called when the {@link AddressIndexMap} or the {@link Program} changes.
        @param listingPanel the {@link ListingPanel} that changed and where the new {@link AddressIndexMap}
         and {@link Program} can be retrieved.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setDefaultBackgroundColor(self, __a0: java.awt.Color) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def defaultBackgroundColor(self) -> java.awt.Color: ...

    @defaultBackgroundColor.setter
    def defaultBackgroundColor(self, value: java.awt.Color) -> None: ...
