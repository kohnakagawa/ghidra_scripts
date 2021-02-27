import ghidra.app.util.viewer.listingpanel
import java.awt
import java.lang


class MarkerServiceBackgroundColorModel(object, ghidra.app.util.viewer.listingpanel.ListingBackgroundColorModel):




    @overload
    def __init__(self, __a0: ghidra.app.services.MarkerService, __a1: ghidra.app.util.viewer.util.AddressIndexMap): ...

    @overload
    def __init__(self, __a0: ghidra.app.services.MarkerService, __a1: ghidra.program.model.listing.Program, __a2: ghidra.app.util.viewer.util.AddressIndexMap): ...



    def equals(self, __a0: object) -> bool: ...

    def getBackgroundColor(self, __a0: long) -> java.awt.Color: ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultBackgroundColor(self) -> java.awt.Color: ...

    def hashCode(self) -> int: ...

    def modelDataChanged(self, __a0: ghidra.app.util.viewer.listingpanel.ListingPanel) -> None: ...

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
