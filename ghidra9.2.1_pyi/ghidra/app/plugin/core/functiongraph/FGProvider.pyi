import docking
import docking.action
import ghidra.app.nav
import ghidra.app.services
import ghidra.app.util
import ghidra.framework.model
import ghidra.framework.options
import ghidra.graph
import ghidra.graph.viewer
import ghidra.program.model.listing
import ghidra.program.util
import ghidra.util
import java.awt.event
import java.lang
import java.util
import javax.swing


class FGProvider(ghidra.graph.VisualGraphComponentProvider, ghidra.app.nav.Navigatable, ghidra.framework.model.DomainObjectListener):




    def __init__(self, __a0: ghidra.app.plugin.core.functiongraph.FunctionGraphPlugin, __a1: bool): ...



    def addLocalAction(self, __a0: docking.action.DockingActionIf) -> None: ...

    def addNavigatableListener(self, __a0: ghidra.app.nav.NavigatableRemovalListener) -> None: ...

    def addToTool(self) -> None: ...

    def clearViewSettings(self) -> None: ...

    def closeComponent(self) -> None: ...

    def componentActivated(self) -> None: ...

    def componentDeactived(self) -> None: ...

    def componentHidden(self) -> None: ...

    def componentShown(self) -> None: ...

    def configChanged(self) -> None: ...

    def contextChanged(self) -> None: ...

    def dispose(self) -> None: ...

    def domainObjectChanged(self, __a0: ghidra.framework.model.DomainObjectChangedEvent) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def formatChanged(self) -> None: ...

    def functionGraphDataChanged(self) -> None: ...

    def getActionContext(self, __a0: java.awt.event.MouseEvent) -> docking.ActionContext: ...

    def getClass(self) -> java.lang.Class: ...

    def getComponent(self) -> javax.swing.JComponent: ...

    def getContextType(self) -> java.lang.Class: ...

    def getDefaultWindowPosition(self) -> docking.WindowPosition: ...

    def getHelpInfo(self) -> unicode: ...

    def getHelpLocation(self) -> ghidra.util.HelpLocation: ...

    def getHelpObject(self) -> object: ...

    def getHighlight(self) -> ghidra.program.util.ProgramSelection: ...

    def getIcon(self) -> javax.swing.Icon: ...

    def getInstanceID(self) -> long: ...

    def getIntraGroupPosition(self) -> docking.WindowPosition: ...

    def getLocation(self) -> ghidra.program.util.ProgramLocation: ...

    @staticmethod
    def getMappedName(__a0: unicode, __a1: unicode) -> unicode: ...

    @staticmethod
    def getMappedOwner(__a0: unicode, __a1: unicode) -> unicode: ...

    def getMemento(self) -> ghidra.app.nav.LocationMemento: ...

    def getName(self) -> unicode: ...

    def getNavigatableIcon(self) -> javax.swing.Icon: ...

    def getOwner(self) -> unicode: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def getSelectedVertices(self) -> java.util.Set: ...

    def getSelection(self) -> ghidra.program.util.ProgramSelection: ...

    def getSubTitle(self) -> unicode: ...

    def getTabText(self) -> unicode: ...

    def getTitle(self) -> unicode: ...

    def getTool(self) -> docking.Tool: ...

    def getView(self) -> ghidra.graph.viewer.VisualGraphView: ...

    def getWindowGroup(self) -> unicode: ...

    def getWindowSubMenuName(self) -> unicode: ...

    def goTo(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.util.ProgramLocation) -> bool: ...

    def graphLocationChanged(self, __a0: ghidra.program.util.ProgramLocation) -> None: ...

    def graphSelectionChanged(self, __a0: ghidra.program.util.ProgramSelection) -> None: ...

    def hashCode(self) -> int: ...

    def internalGoTo(self, __a0: ghidra.program.util.ProgramLocation, __a1: ghidra.program.model.listing.Program) -> None: ...

    def isActive(self) -> bool: ...

    def isConnected(self) -> bool: ...

    def isDisposed(self) -> bool: ...

    def isFocusedProvider(self) -> bool: ...

    def isInTool(self) -> bool: ...

    def isSatelliteDocked(self) -> bool: ...

    def isSatelliteShowing(self) -> bool: ...

    def isSnapshot(self) -> bool: ...

    def isTransient(self) -> bool: ...

    def isVisible(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def readConfigState(self, __a0: ghidra.framework.options.SaveState) -> None: ...

    def readDataState(self, __a0: ghidra.framework.options.SaveState) -> None: ...

    def refreshAndKeepPerspective(self) -> None: ...

    def refreshAndResetPerspective(self) -> None: ...

    def refreshDisplayWithoutRebuilding(self) -> None: ...

    @staticmethod
    def registerProviderNameOwnerChange(__a0: unicode, __a1: unicode, __a2: unicode, __a3: unicode) -> None: ...

    def removeFromTool(self) -> None: ...

    def removeHighlightProvider(self, __a0: ghidra.app.util.HighlightProvider, __a1: ghidra.program.model.listing.Program) -> None: ...

    def removeNavigatableListener(self, __a0: ghidra.app.nav.NavigatableRemovalListener) -> None: ...

    def requestFocus(self) -> None: ...

    def saveLocationToHistory(self) -> None: ...

    def setClipboardService(self, __a0: ghidra.app.services.ClipboardService) -> None: ...

    def setClipboardStringContent(self, __a0: unicode) -> None: ...

    def setHelpLocation(self, __a0: ghidra.util.HelpLocation) -> None: ...

    def setHighlight(self, __a0: ghidra.program.util.ProgramSelection) -> None: ...

    def setHighlightProvider(self, __a0: ghidra.app.util.HighlightProvider, __a1: ghidra.program.model.listing.Program) -> None: ...

    def setIntraGroupPosition(self, __a0: docking.WindowPosition) -> None: ...

    def setMemento(self, __a0: ghidra.app.nav.LocationMemento) -> None: ...

    def setPopupsVisible(self, __a0: bool) -> None: ...

    def setSelection(self, __a0: ghidra.program.util.ProgramSelection) -> None: ...

    def setSubTitle(self, __a0: unicode) -> None: ...

    def setTabText(self, __a0: unicode) -> None: ...

    def setTitle(self, __a0: unicode) -> None: ...

    def setVisible(self, __a0: bool) -> None: ...

    def supportsHighlight(self) -> bool: ...

    def supportsMarkers(self) -> bool: ...

    def toFront(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeConfigState(self, __a0: ghidra.framework.options.SaveState) -> None: ...

    def writeDataState(self, __a0: ghidra.framework.options.SaveState) -> None: ...

    @property
    def clipboardService(self) -> None: ...  # No getter available.

    @clipboardService.setter
    def clipboardService(self, value: ghidra.app.services.ClipboardService) -> None: ...

    @property
    def clipboardStringContent(self) -> None: ...  # No getter available.

    @clipboardStringContent.setter
    def clipboardStringContent(self, value: unicode) -> None: ...

    @property
    def component(self) -> javax.swing.JComponent: ...

    @property
    def connected(self) -> bool: ...

    @property
    def disposed(self) -> bool: ...

    @property
    def focusedProvider(self) -> bool: ...

    @property
    def highlight(self) -> ghidra.program.util.ProgramSelection: ...

    @highlight.setter
    def highlight(self, value: ghidra.program.util.ProgramSelection) -> None: ...

    @property
    def icon(self) -> javax.swing.Icon: ...

    @property
    def location(self) -> ghidra.program.util.ProgramLocation: ...

    @property
    def memento(self) -> ghidra.app.nav.LocationMemento: ...

    @memento.setter
    def memento(self, value: ghidra.app.nav.LocationMemento) -> None: ...

    @property
    def navigatableIcon(self) -> javax.swing.Icon: ...

    @property
    def popupsVisible(self) -> None: ...  # No getter available.

    @popupsVisible.setter
    def popupsVisible(self, value: bool) -> None: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...

    @property
    def selection(self) -> ghidra.program.util.ProgramSelection: ...

    @selection.setter
    def selection(self, value: ghidra.program.util.ProgramSelection) -> None: ...

    @property
    def snapshot(self) -> bool: ...

    @property
    def tool(self) -> ghidra.framework.plugintool.PluginTool: ...

    @property
    def view(self) -> ghidra.graph.viewer.VisualGraphView: ...

    @property
    def windowGroup(self) -> unicode: ...
