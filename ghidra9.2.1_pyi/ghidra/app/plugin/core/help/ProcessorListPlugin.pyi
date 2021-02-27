from typing import List
import docking
import docking.action
import docking.widgets.table
import ghidra.framework.main
import ghidra.framework.model
import ghidra.framework.options
import ghidra.framework.plugintool
import ghidra.framework.plugintool.util
import ghidra.program.model.lang
import ghidra.util
import java.awt.event
import java.lang
import java.util
import javax.swing
import javax.swing.event
import javax.swing.table


class ProcessorListPlugin(ghidra.framework.plugintool.Plugin, ghidra.framework.main.FrontEndable):
    ACTION_NAME: unicode = u'Installed Processors'
    PLUGIN_NAME: unicode = u'ProgramListPlugin'




    class ProcessorListTableModel(docking.widgets.table.AbstractSortedTableModel):




        def __init__(self, __a0: ghidra.app.plugin.core.help.ProcessorListPlugin, __a1: List[object]): ...



        def addSortListener(self, __a0: docking.widgets.table.SortListener) -> None: ...

        def addTableModelListener(self, __a0: javax.swing.event.TableModelListener) -> None: ...

        def dispose(self) -> None: ...

        def equals(self, __a0: object) -> bool: ...

        def findColumn(self, __a0: unicode) -> int: ...

        def fireTableCellUpdated(self, __a0: int, __a1: int) -> None: ...

        def fireTableChanged(self, __a0: javax.swing.event.TableModelEvent) -> None: ...

        def fireTableDataChanged(self) -> None: ...

        def fireTableRowsDeleted(self, __a0: int, __a1: int) -> None: ...

        def fireTableRowsInserted(self, __a0: int, __a1: int) -> None: ...

        def fireTableRowsUpdated(self, __a0: int, __a1: int) -> None: ...

        def fireTableStructureChanged(self) -> None: ...

        def getClass(self) -> java.lang.Class: ...

        def getColumnClass(self, __a0: int) -> java.lang.Class: ...

        def getColumnCount(self) -> int: ...

        def getColumnName(self, __a0: int) -> unicode: ...

        @overload
        def getColumnValueForRow(self, __a0: ghidra.program.model.lang.Processor, __a1: int) -> object: ...

        @overload
        def getColumnValueForRow(self, __a0: object, __a1: int) -> object: ...

        def getLastSelectedObjects(self) -> List[object]: ...

        def getListeners(self, __a0: java.lang.Class) -> List[java.util.EventListener]: ...

        def getModelData(self) -> List[object]: ...

        def getName(self) -> unicode: ...

        def getPendingSortState(self) -> docking.widgets.table.TableSortState: ...

        def getPreferredColumnWidth(self, __a0: int) -> int: ...

        def getPrimarySortColumnIndex(self) -> int: ...

        def getRowCount(self) -> int: ...

        def getRowIndex(self, __a0: object) -> int: ...

        def getRowObject(self, __a0: int) -> object: ...

        def getTableModelListeners(self) -> List[javax.swing.event.TableModelListener]: ...

        def getTableSortState(self) -> docking.widgets.table.TableSortState: ...

        def getValueAt(self, __a0: int, __a1: int) -> object: ...

        def hashCode(self) -> int: ...

        def isCellEditable(self, __a0: int, __a1: int) -> bool: ...

        def isSortPending(self) -> bool: ...

        def isSortable(self, __a0: int) -> bool: ...

        def isSorted(self) -> bool: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def refresh(self) -> None: ...

        def removeTableModelListener(self, __a0: javax.swing.event.TableModelListener) -> None: ...

        def setLastSelectedObjects(self, __a0: List[object]) -> None: ...

        def setTableSortState(self, __a0: docking.widgets.table.TableSortState) -> None: ...

        def setValueAt(self, __a0: object, __a1: int, __a2: int) -> None: ...

        def toString(self) -> unicode: ...

        @staticmethod
        def unwrap(__a0: javax.swing.table.TableModel) -> javax.swing.table.TableModel: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...

        @property
        def columnCount(self) -> int: ...

        @property
        def modelData(self) -> List[object]: ...

        @property
        def name(self) -> unicode: ...

        @property
        def rowCount(self) -> int: ...




    class ProcessorListTableProvider(ghidra.framework.plugintool.ComponentProviderAdapter):




        def __init__(self, __a0: ghidra.app.plugin.core.help.ProcessorListPlugin, __a1: ghidra.framework.plugintool.PluginTool, __a2: unicode): ...



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

    def __init__(self, __a0: ghidra.framework.plugintool.PluginTool): ...



    def acceptData(self, __a0: List[ghidra.framework.model.DomainFile]) -> bool: ...

    def dataStateRestoreCompleted(self) -> None: ...

    def dependsUpon(self, __a0: ghidra.framework.plugintool.Plugin) -> bool: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def eventSent(self, __a0: ghidra.framework.plugintool.PluginEvent) -> None: ...

    def firePluginEvent(self, __a0: ghidra.framework.plugintool.PluginEvent) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getData(self) -> List[ghidra.framework.model.DomainFile]: ...

    def getMissingRequiredServices(self) -> List[object]: ...

    def getName(self) -> unicode: ...

    def getPluginDescription(self) -> ghidra.framework.plugintool.util.PluginDescription: ...

    @staticmethod
    def getPluginName(__a0: java.lang.Class) -> unicode: ...

    def getSupportedDataTypes(self) -> List[java.lang.Class]: ...

    def getTool(self) -> ghidra.framework.plugintool.PluginTool: ...

    def getTransientState(self) -> object: ...

    def getUndoRedoState(self, __a0: ghidra.framework.model.DomainObject) -> object: ...

    def hasMissingRequiredService(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isDisposed(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def processEvent(self, __a0: ghidra.framework.plugintool.PluginEvent) -> None: ...

    def readConfigState(self, __a0: ghidra.framework.options.SaveState) -> None: ...

    def readDataState(self, __a0: ghidra.framework.options.SaveState) -> None: ...

    def restoreTransientState(self, __a0: object) -> None: ...

    def restoreUndoRedoState(self, __a0: ghidra.framework.model.DomainObject, __a1: object) -> None: ...

    def serviceAdded(self, __a0: java.lang.Class, __a1: object) -> None: ...

    def serviceRemoved(self, __a0: java.lang.Class, __a1: object) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeConfigState(self, __a0: ghidra.framework.options.SaveState) -> None: ...

    def writeDataState(self, __a0: ghidra.framework.options.SaveState) -> None: ...