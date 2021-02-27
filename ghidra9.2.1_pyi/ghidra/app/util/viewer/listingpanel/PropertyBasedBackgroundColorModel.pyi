import ghidra.app.util.viewer.listingpanel
import ghidra.framework.model
import java.awt
import java.lang


class PropertyBasedBackgroundColorModel(object, ghidra.app.util.viewer.listingpanel.ListingBackgroundColorModel, ghidra.framework.model.DomainObjectListener):
    """
    Default BackgroundColorModel for the ListingPanel where the color returned
     for an index is based on that corresponding address having a color set in the
     program's database. (You can "paint" colors over address ranges).
    """

    COLOR_PROPERTY_NAME: unicode = u'LISTING_COLOR'



    def __init__(self): ...



    def domainObjectChanged(self, ev: ghidra.framework.model.DomainObjectChangedEvent) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getBackgroundColor(self, index: long) -> java.awt.Color: ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultBackgroundColor(self) -> java.awt.Color: ...

    def hashCode(self) -> int: ...

    def modelDataChanged(self, listingPanel: ghidra.app.util.viewer.listingpanel.ListingPanel) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setDefaultBackgroundColor(self, c: java.awt.Color) -> None: ...

    def setEnabled(self, b: bool) -> None: ...

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

    @property
    def enabled(self) -> None: ...  # No getter available.

    @enabled.setter
    def enabled(self, value: bool) -> None: ...
