from typing import List
import docking.widgets.table
import ghidra.app.util.bean.SetEquateDialog
import ghidra.docking.settings
import ghidra.program.model.listing
import java.lang
import java.util
import javax.swing.event
import javax.swing.table


class SetEquateTableModel(docking.widgets.table.GDynamicColumnTableModel):




    def __init__(self, __a0: ghidra.framework.plugintool.ServiceProvider, __a1: List[object], __a2: ghidra.program.model.listing.Program): ...



    def addSortListener(self, l: docking.widgets.table.SortListener) -> None: ...

    def addTableModelListener(self, __a0: javax.swing.event.TableModelListener) -> None: ...

    def dispose(self) -> None:
        """
        Call this when the model will no longer be used
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def findColumn(self, __a0: unicode) -> int: ...

    def fireTableCellUpdated(self, __a0: int, __a1: int) -> None: ...

    def fireTableChanged(self, e: javax.swing.event.TableModelEvent) -> None: ...

    def fireTableDataChanged(self) -> None: ...

    def fireTableRowsDeleted(self, __a0: int, __a1: int) -> None: ...

    def fireTableRowsInserted(self, __a0: int, __a1: int) -> None: ...

    def fireTableRowsUpdated(self, __a0: int, __a1: int) -> None: ...

    def fireTableStructureChanged(self) -> None: ...

    @staticmethod
    def from(__a0: javax.swing.table.TableModel) -> docking.widgets.table.VariableColumnTableModel: ...

    def getClass(self) -> java.lang.Class: ...

    def getColumn(self, index: int) -> docking.widgets.table.DynamicTableColumn: ...

    def getColumnClass(self, column: int) -> java.lang.Class: ...

    def getColumnCount(self) -> int: ...

    def getColumnDescription(self, column: int) -> unicode: ...

    def getColumnDisplayName(self, columnIndex: int) -> unicode: ...

    @overload
    def getColumnIndex(self, identifier: docking.widgets.table.DynamicTableColumn) -> int: ...

    @overload
    def getColumnIndex(self, columnClass: java.lang.Class) -> int:
        """
        Returns the column index of the given column class
        @param columnClass the class for the type of DynamicTableColumn you want to find.
        @return the column index for the specified DynamicTableColumn. -1 if not found.
        """
        ...

    def getColumnName(self, column: int) -> unicode: ...

    def getColumnSettings(self, index: int) -> ghidra.docking.settings.Settings: ...

    def getColumnSettingsDefinitions(self, index: int) -> List[ghidra.docking.settings.SettingsDefinition]: ...

    def getColumnValueForRow(self, __a0: object, __a1: int) -> object: ...

    def getDataSource(self) -> ghidra.program.model.listing.Program: ...

    def getDefaultColumnCount(self) -> int: ...

    def getLastSelectedObjects(self) -> List[object]: ...

    def getListeners(self, __a0: java.lang.Class) -> List[java.util.EventListener]: ...

    def getMaxLines(self, index: int) -> int:
        """
        Gets the maximum number of text display lines needed for any given cell within the
         specified column.
        @param index column field index
        @return maximum number of lines needed for specified column
        """
        ...

    def getModelData(self) -> List[ghidra.app.util.bean.SetEquateDialog.EquateRowObject]: ...

    def getName(self) -> unicode: ...

    def getPendingSortState(self) -> docking.widgets.table.TableSortState: ...

    def getPreferredColumnWidth(self, column: int) -> int: ...

    def getPrimarySortColumnIndex(self) -> int: ...

    def getRenderer(self, index: int) -> javax.swing.table.TableCellRenderer:
        """
        Gets the special table cell renderer for the specified table field column.
         A null value indicates that this field uses a default cell renderer.
        @param index the model column index
        @return a table cell renderer for this field. Otherwise, null if a default
                 renderer should be used.
        """
        ...

    def getRowCount(self) -> int: ...

    def getRowIndex(self, rowObject: object) -> int:
        """
        Returns the index of the given row object in this model; a negative value if the model
         does not contain the given object.

         <p>Warning: if the this model has no sort applied, then performance will be O(n).  If
         sorted, then performance is O(log n).  You can call {@link #isSorted()} to know when
         this will happen.
        """
        ...

    def getRowObject(self, viewRow: int) -> object:
        """
        Returns the corresponding object for the given row.
        @param viewRow The row for which to get the row object.
        @return the row object.
        """
        ...

    def getTableModelListeners(self) -> List[javax.swing.event.TableModelListener]: ...

    def getTableSortState(self) -> docking.widgets.table.TableSortState: ...

    def getUniqueIdentifier(self, column: int) -> unicode: ...

    def getValueAt(self, rowIndex: int, columnIndex: int) -> object:
        """
        The default implementation of {@link TableModel#getValueAt(int, int)} that calls the
         abstract {@link #getColumnValueForRow(Object, int)}.
        """
        ...

    def hashCode(self) -> int: ...

    def isCellEditable(self, __a0: int, __a1: int) -> bool: ...

    def isDefaultColumn(self, modelIndex: int) -> bool:
        """
        Returns true if the column indicated by the index in the model is a default column (meaning
         that it was specified by the model and not discovered).
        @param modelIndex the index of the column in the model.
        @return true if the column is a default.
        """
        ...

    def isSortPending(self) -> bool:
        """
        Returns true if there is a pending change to the current sort state
         (this includes a sort state that signals no sort will be applied)
        @return true if there is a pending change to the current sort state
        """
        ...

    def isSortable(self, columnIndex: int) -> bool: ...

    def isSorted(self) -> bool:
        """
        Returns true if this model has been sorted and does not have a new pending sort that will
         be applied
        @return true if sorted
        @see #isSortPending()
        """
        ...

    def isVisibleByDefault(self, modelIndex: int) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def refresh(self) -> None:
        """
        Invoke this method when the underlying data has changed, but a reload is not required.
        """
        ...

    def removeTableModelListener(self, __a0: javax.swing.event.TableModelListener) -> None: ...

    def setAllColumnSettings(self, newSettings: List[ghidra.docking.settings.Settings]) -> None: ...

    def setLastSelectedObjects(self, lastSelectedObjects: List[object]) -> None: ...

    def setTableSortState(self, newSortState: docking.widgets.table.TableSortState) -> None: ...

    def setValueAt(self, __a0: object, __a1: int, __a2: int) -> None: ...

    def stateChanged(self, e: javax.swing.event.ChangeEvent) -> None:
        """
        Callback when column settings have changed
        """
        ...

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
    def dataSource(self) -> ghidra.program.model.listing.Program: ...

    @property
    def modelData(self) -> List[object]: ...

    @property
    def name(self) -> unicode: ...
