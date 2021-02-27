from typing import List
import docking
import docking.action
import ghidra.app.plugin.core.format
import ghidra.app.services
import ghidra.framework.options
import ghidra.framework.plugintool
import ghidra.util
import java.awt.event
import java.lang
import java.util
import javax.swing


class ByteViewerComponentProvider(ghidra.framework.plugintool.ComponentProviderAdapter, ghidra.framework.options.OptionsChangeListener):








    def addLocalAction(self, __a0: docking.action.DockingActionIf) -> None: ...

    def addToTool(self) -> None: ...

    def closeComponent(self) -> None: ...

    def componentActivated(self) -> None: ...

    def componentDeactived(self) -> None: ...

    def componentHidden(self) -> None: ...

    def componentShown(self) -> None: ...

    def contextChanged(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getActionContext(self, __a0: java.awt.event.MouseEvent) -> docking.ActionContext: ...

    def getClass(self) -> java.lang.Class: ...

    def getComponent(self) -> javax.swing.JComponent: ...

    def getContextType(self) -> java.lang.Class: ...

    def getCurrentViews(self) -> java.util.Set: ...

    def getDataFormatModel(self, __a0: unicode) -> ghidra.app.plugin.core.format.DataFormatModel: ...

    def getDataFormatNames(self) -> List[object]: ...

    def getDefaultWindowPosition(self) -> docking.WindowPosition: ...

    def getHelpInfo(self) -> unicode: ...

    def getHelpLocation(self) -> ghidra.util.HelpLocation: ...

    def getHelpObject(self) -> object: ...

    def getIcon(self) -> javax.swing.Icon: ...

    def getInstanceID(self) -> long: ...

    def getIntraGroupPosition(self) -> docking.WindowPosition: ...

    @staticmethod
    def getMappedName(__a0: unicode, __a1: unicode) -> unicode: ...

    @staticmethod
    def getMappedOwner(__a0: unicode, __a1: unicode) -> unicode: ...

    def getMarkerService(self) -> ghidra.app.services.MarkerService: ...

    def getName(self) -> unicode: ...

    def getOwner(self) -> unicode: ...

    def getSubTitle(self) -> unicode: ...

    def getTabText(self) -> unicode: ...

    def getTitle(self) -> unicode: ...

    def getTool(self) -> docking.Tool: ...

    def getWindowGroup(self) -> unicode: ...

    def getWindowSubMenuName(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def isActive(self) -> bool: ...

    def isFocusedProvider(self) -> bool: ...

    def isInTool(self) -> bool: ...

    def isSnapshot(self) -> bool: ...

    def isTransient(self) -> bool: ...

    def isVisible(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def optionsChanged(self, __a0: ghidra.framework.options.ToolOptions, __a1: unicode, __a2: object, __a3: object) -> None: ...

    @staticmethod
    def registerProviderNameOwnerChange(__a0: unicode, __a1: unicode, __a2: unicode, __a3: unicode) -> None: ...

    def removeFromTool(self) -> None: ...

    def requestFocus(self) -> None: ...

    def setHelpLocation(self, __a0: ghidra.util.HelpLocation) -> None: ...

    def setIntraGroupPosition(self, __a0: docking.WindowPosition) -> None: ...

    def setSubTitle(self, __a0: unicode) -> None: ...

    def setTabText(self, __a0: unicode) -> None: ...

    def setTitle(self, __a0: unicode) -> None: ...

    def setVisible(self, __a0: bool) -> None: ...

    def toFront(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def component(self) -> javax.swing.JComponent: ...

    @property
    def currentViews(self) -> java.util.Set: ...

    @property
    def dataFormatNames(self) -> List[object]: ...

    @property
    def helpLocation(self) -> ghidra.util.HelpLocation: ...

    @helpLocation.setter
    def helpLocation(self, value: ghidra.util.HelpLocation) -> None: ...

    @property
    def markerService(self) -> ghidra.app.services.MarkerService: ...
