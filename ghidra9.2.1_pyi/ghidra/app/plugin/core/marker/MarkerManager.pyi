import ghidra.app.nav
import ghidra.app.services
import ghidra.app.util.viewer.listingpanel
import ghidra.program.model.address
import ghidra.program.model.listing
import java.awt
import java.lang
import javax.swing
import javax.swing.event


class MarkerManager(object, ghidra.app.services.MarkerService):
    BOOKMARK_PRIORITY: int = 0
    BREAKPOINT_PRIORITY: int = 50
    CHANGE_PRIORITY: int = -50
    CURSOR_PRIORITY: int = 200
    DIFF_PRIORITY: int = 80
    FUNCTION_COMPARE_CURSOR_PRIORITY: int = 49
    GROUP_PRIORITY: int = -25
    HIGHLIGHT_GROUP: unicode = u'HIGHLIGHT_GROUP'
    HIGHLIGHT_PRIORITY: int = 50
    PROPERTY_PRIORITY: int = 75
    REFERENCE_PRIORITY: int = -10
    SEARCH_PRIORITY: int = 75
    SELECTION_PRIORITY: int = 100



    @overload
    def __init__(self, __a0: ghidra.framework.plugintool.Plugin): ...

    @overload
    def __init__(self, __a0: unicode, __a1: ghidra.framework.plugintool.PluginTool): ...



    def addChangeListener(self, __a0: javax.swing.event.ChangeListener) -> None: ...

    @overload
    def createAreaMarker(self, __a0: unicode, __a1: unicode, __a2: ghidra.program.model.listing.Program, __a3: int, __a4: bool, __a5: bool, __a6: bool, __a7: java.awt.Color) -> ghidra.app.services.MarkerSet: ...

    @overload
    def createAreaMarker(self, __a0: unicode, __a1: unicode, __a2: ghidra.program.model.listing.Program, __a3: int, __a4: bool, __a5: bool, __a6: bool, __a7: java.awt.Color, __a8: bool) -> ghidra.app.services.MarkerSet: ...

    @overload
    def createPointMarker(self, __a0: unicode, __a1: unicode, __a2: ghidra.program.model.listing.Program, __a3: int, __a4: bool, __a5: bool, __a6: bool, __a7: java.awt.Color, __a8: javax.swing.ImageIcon) -> ghidra.app.services.MarkerSet: ...

    @overload
    def createPointMarker(self, __a0: unicode, __a1: unicode, __a2: ghidra.program.model.listing.Program, __a3: int, __a4: bool, __a5: bool, __a6: bool, __a7: java.awt.Color, __a8: javax.swing.ImageIcon, __a9: bool) -> ghidra.app.services.MarkerSet: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    def getBackgroundColor(self, __a0: ghidra.program.model.address.Address) -> java.awt.Color: ...

    @overload
    def getBackgroundColor(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address) -> java.awt.Color: ...

    def getClass(self) -> java.lang.Class: ...

    def getGoToService(self) -> ghidra.app.services.GoToService: ...

    def getMarginProvider(self) -> ghidra.app.util.viewer.listingpanel.MarginProvider: ...

    def getMarkerSet(self, __a0: unicode, __a1: ghidra.program.model.listing.Program) -> ghidra.app.services.MarkerSet: ...

    def getOverviewProvider(self) -> ghidra.app.util.viewer.listingpanel.OverviewProvider: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeChangeListener(self, __a0: javax.swing.event.ChangeListener) -> None: ...

    def removeMarker(self, __a0: ghidra.app.services.MarkerSet, __a1: ghidra.program.model.listing.Program) -> None: ...

    def removeMarkerForGroup(self, __a0: unicode, __a1: ghidra.app.services.MarkerSet, __a2: ghidra.program.model.listing.Program) -> None: ...

    def setGoToService(self, __a0: ghidra.app.services.GoToService) -> None: ...

    def setMarkerForGroup(self, __a0: unicode, __a1: ghidra.app.services.MarkerSet, __a2: ghidra.program.model.listing.Program) -> None: ...

    def setNavigatable(self, __a0: ghidra.app.nav.Navigatable) -> None: ...

    def setProgram(self, __a0: ghidra.program.model.listing.Program) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def goToService(self) -> ghidra.app.services.GoToService: ...

    @goToService.setter
    def goToService(self, value: ghidra.app.services.GoToService) -> None: ...

    @property
    def marginProvider(self) -> ghidra.app.util.viewer.listingpanel.MarginProvider: ...

    @property
    def navigatable(self) -> None: ...  # No getter available.

    @navigatable.setter
    def navigatable(self, value: ghidra.app.nav.Navigatable) -> None: ...

    @property
    def overviewProvider(self) -> ghidra.app.util.viewer.listingpanel.OverviewProvider: ...

    @property
    def program(self) -> None: ...  # No getter available.

    @program.setter
    def program(self, value: ghidra.program.model.listing.Program) -> None: ...
