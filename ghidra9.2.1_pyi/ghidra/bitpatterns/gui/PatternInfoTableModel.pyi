from typing import List
import docking.widgets.table
import docking.widgets.table.threaded
import ghidra.docking.settings
import ghidra.util.task
import java.lang
import java.util
import javax.swing.event
import javax.swing.table


class PatternInfoTableModel(docking.widgets.table.threaded.ThreadedTableModelStub):




    def __init__(self, __a0: ghidra.bitpatterns.gui.FunctionBitPatternsExplorerPlugin): ...



    def addInitialLoadListener(self, __a0: docking.widgets.table.threaded.ThreadedTableModelListener) -> None: ...

    def addObject(self, __a0: object) -> None: ...

    def addSortListener(self, __a0: docking.widgets.table.SortListener) -> None: ...

    def addTableModelListener(self, __a0: javax.swing.event.TableModelListener) -> None: ...

    def addThreadedTableModelListener(self, __a0: docking.widgets.table.threaded.ThreadedTableModelListener) -> None: ...

    def cancelAllUpdates(self) -> None: ...

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

    @staticmethod
    def from(__a0: javax.swing.table.TableModel) -> docking.widgets.table.VariableColumnTableModel: ...

    def getClass(self) -> java.lang.Class: ...

    def getColumn(self, __a0: int) -> docking.widgets.table.DynamicTableColumn: ...

    def getColumnClass(self, __a0: int) -> java.lang.Class: ...

    def getColumnCount(self) -> int: ...

    def getColumnDescription(self, __a0: int) -> unicode: ...

    def getColumnDisplayName(self, __a0: int) -> unicode: ...

    @overload
    def getColumnIndex(self, __a0: docking.widgets.table.DynamicTableColumn) -> int: ...

    @overload
    def getColumnIndex(self, __a0: java.lang.Class) -> int: ...

    def getColumnName(self, __a0: int) -> unicode: ...

    def getColumnSettings(self, __a0: int) -> ghidra.docking.settings.Settings: ...

    def getColumnSettingsDefinitions(self, __a0: int) -> List[ghidra.docking.settings.SettingsDefinition]: ...

    def getColumnValueForRow(self, __a0: object, __a1: int) -> object: ...

    def getDataSource(self) -> object: ...

    def getDefaultColumnCount(self) -> int: ...

    def getLastSelectedObjects(self) -> List[object]: ...

    def getListeners(self, __a0: java.lang.Class) -> List[java.util.EventListener]: ...

    def getMaxLines(self, __a0: int) -> int: ...

    def getModelData(self) -> List[object]: ...

    def getModelIndex(self, __a0: object) -> int: ...

    def getModelRow(self, __a0: int) -> int: ...

    def getName(self) -> unicode: ...

    def getPendingSortState(self) -> docking.widgets.table.TableSortState: ...

    def getPreferredColumnWidth(self, __a0: int) -> int: ...

    def getPrimarySortColumnIndex(self) -> int: ...

    def getRenderer(self, __a0: int) -> javax.swing.table.TableCellRenderer: ...

    def getRowCount(self) -> int: ...

    def getRowIndex(self, __a0: object) -> int: ...

    def getRowObject(self, __a0: int) -> object: ...

    def getRowObjects(self, __a0: List[int]) -> List[object]: ...

    def getTableFilter(self) -> docking.widgets.table.TableFilter: ...

    def getTableModelListeners(self) -> List[javax.swing.event.TableModelListener]: ...

    def getTableSortState(self) -> docking.widgets.table.TableSortState: ...

    def getUnfilteredData(self) -> List[object]: ...

    def getUnfilteredRowCount(self) -> int: ...

    def getUniqueIdentifier(self, __a0: int) -> unicode: ...

    def getValueAt(self, __a0: int, __a1: int) -> object: ...

    def getViewIndex(self, __a0: object) -> int: ...

    def getViewRow(self, __a0: int) -> int: ...

    def hasFilter(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isBusy(self) -> bool: ...

    def isCellEditable(self, __a0: int, __a1: int) -> bool: ...

    def isDefaultColumn(self, __a0: int) -> bool: ...

    def isFiltered(self) -> bool: ...

    def isLoadIncrementally(self) -> bool: ...

    def isSortPending(self) -> bool: ...

    def isSortable(self, __a0: int) -> bool: ...

    def isSorted(self) -> bool: ...

    def isVisibleByDefault(self, __a0: int) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def reFilter(self) -> None: ...

    def reSort(self) -> None: ...

    def refresh(self) -> None: ...

    def reload(self) -> None: ...

    def removeObject(self, __a0: object) -> None: ...

    def removeTableModelListener(self, __a0: javax.swing.event.TableModelListener) -> None: ...

    def removeThreadedTableModelListener(self, __a0: docking.widgets.table.threaded.ThreadedTableModelListener) -> None: ...

    def setAllColumnSettings(self, __a0: List[ghidra.docking.settings.Settings]) -> None: ...

    def setIncrementalTaskMonitor(self, __a0: ghidra.util.task.TaskMonitor) -> None: ...

    def setLastSelectedObjects(self, __a0: List[object]) -> None: ...

    def setTableFilter(self, __a0: docking.widgets.table.TableFilter) -> None: ...

    def setTableSortState(self, __a0: docking.widgets.table.TableSortState) -> None: ...

    def setValueAt(self, __a0: object, __a1: int, __a2: int) -> None: ...

    def stateChanged(self, __a0: javax.swing.event.ChangeEvent) -> None: ...

    def toString(self) -> unicode: ...

    @staticmethod
    def unwrap(__a0: javax.swing.table.TableModel) -> javax.swing.table.TableModel: ...

    def updateObject(self, __a0: object) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
