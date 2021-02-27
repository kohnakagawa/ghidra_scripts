from typing import List
import docking.widgets.table
import docking.widgets.table.threaded
import ghidra.docking.settings
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.util
import ghidra.util.table
import ghidra.util.task
import java.lang
import java.util
import javax.swing.event
import javax.swing.table


class CustomLoadingAddressTableModel(ghidra.util.table.AddressPreviewTableModel):
    """
    An Address based table model that allows clients to load their data via
     the TableModelLoader callback provided at construction time.

     Why?  Well, this allows clients to use the existing table model framework without
     having to create a new table model.  In other words, some of the boilerplate code
     of creating a model is removed--clients need only implement one method in order to
     get full thread table functionality, which is a lot.
    """





    @overload
    def __init__(self, modelName: unicode, serviceProvider: ghidra.framework.plugintool.ServiceProvider, program: ghidra.program.model.listing.Program, loader: ghidra.util.table.TableModelLoader, monitor: ghidra.util.task.TaskMonitor): ...

    @overload
    def __init__(self, modelName: unicode, serviceProvider: ghidra.framework.plugintool.ServiceProvider, program: ghidra.program.model.listing.Program, loader: ghidra.util.table.TableModelLoader, monitor: ghidra.util.task.TaskMonitor, loadIncrementally: bool): ...



    def addInitialLoadListener(self, listener: docking.widgets.table.threaded.ThreadedTableModelListener) -> None:
        """
        Adds a listener that will be notified of the first table load of this model.  After the
         initial load, the listener is removed.
        @param listener the listener
        """
        ...

    def addObject(self, __a0: object) -> None: ...

    def addSortListener(self, l: docking.widgets.table.SortListener) -> None: ...

    def addTableModelListener(self, __a0: javax.swing.event.TableModelListener) -> None: ...

    def addThreadedTableModelListener(self, listener: docking.widgets.table.threaded.ThreadedTableModelListener) -> None:
        """
        This is a way to know about updates from the table.
        @param listener the listener to add
        @see #addInitialLoadListener(ThreadedTableModelListener)
        @see #removeThreadedTableModelListener(ThreadedTableModelListener)
        """
        ...

    def cancelAllUpdates(self) -> None:
        """
        Cancels all current and pending updates to the model. Waits until all updates have
         been cancelled.
        """
        ...

    def dispose(self) -> None:
        """
        Disposes this model.
         Once a model has been disposed, it cannot be reused.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def findColumn(self, __a0: unicode) -> int: ...

    def fireTableCellUpdated(self, __a0: int, __a1: int) -> None: ...

    def fireTableChanged(self, e: javax.swing.event.TableModelEvent) -> None:
        """
        @see javax.swing.table.AbstractTableModel#fireTableChanged(javax.swing.event.TableModelEvent)
        """
        ...

    def fireTableDataChanged(self) -> None: ...

    def fireTableRowsDeleted(self, __a0: int, __a1: int) -> None: ...

    def fireTableRowsInserted(self, __a0: int, __a1: int) -> None: ...

    def fireTableRowsUpdated(self, __a0: int, __a1: int) -> None: ...

    def fireTableStructureChanged(self) -> None: ...

    @staticmethod
    def from(__a0: javax.swing.table.TableModel) -> docking.widgets.table.VariableColumnTableModel: ...

    def getAddress(self, row: int) -> ghidra.program.model.address.Address: ...

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

    def getModelData(self) -> List[ROW_OBJECT]: ...

    def getModelIndex(self, __a0: object) -> int: ...

    def getModelRow(self, viewRow: int) -> int:
        """
        Given a row index for the view (filtered) model, return the corresponding index in the
         raw (unfiltered) model.
        @param viewRow The row index that corresponds to filtered data
        @return the index of that row in the unfiltered data
        @see #getViewRow(int)
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of this model.
        @return the name of this model
        """
        ...

    def getPendingSortState(self) -> docking.widgets.table.TableSortState: ...

    def getPreferredColumnWidth(self, column: int) -> int: ...

    def getPrimarySortColumnIndex(self) -> int: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def getProgramLocation(self, row: int, column: int) -> ghidra.program.util.ProgramLocation: ...

    def getProgramSelection(self, rows: List[int]) -> ghidra.program.util.ProgramSelection: ...

    def getRenderer(self, index: int) -> javax.swing.table.TableCellRenderer:
        """
        Gets the special table cell renderer for the specified table field column.
         A null value indicates that this field uses a default cell renderer.
        @param index the model column index
        @return a table cell renderer for this field. Otherwise, null if a default
                 renderer should be used.
        """
        ...

    def getRowCount(self) -> int:
        """
        @see javax.swing.table.TableModel#getRowCount()
        """
        ...

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

    def getRowObjects(self, rows: List[int]) -> List[ROW_OBJECT]:
        """
        Returns the corresponding row objects for the specified rows.
        @param rows the table rows
        @return the corresponding database keys
        """
        ...

    def getTableFilter(self) -> docking.widgets.table.TableFilter:
        """
        Returns the filter for this model.  The value returned from this method will not be null,
         but will instead be an instanceof {@link NullTableFilter} when no filter is applied.   The
         value returned from this method may not actually yet be applied, depending upon when the
         background thread finishes loading.
        @return the filter
        """
        ...

    def getTableModelListeners(self) -> List[javax.swing.event.TableModelListener]: ...

    def getTableSortState(self) -> docking.widgets.table.TableSortState: ...

    def getUnfilteredData(self) -> List[ROW_OBJECT]: ...

    def getUnfilteredRowCount(self) -> int: ...

    def getUniqueIdentifier(self, column: int) -> unicode: ...

    def getValueAt(self, rowIndex: int, columnIndex: int) -> object: ...

    def getViewIndex(self, __a0: object) -> int: ...

    def getViewRow(self, modelRow: int) -> int:
        """
        Given a row index for the raw (unfiltered) model, return the corresponding index in the
         view (filtered) model.
        @param modelRow The row index that corresponds to unfiltered data
        @return the index of that row in the filtered data
        @see #getModelRow(int)
        """
        ...

    def hasFilter(self) -> bool:
        """
        Returns true if there is a table filter set that is not the {@link NullTableFilter}.
        @return true if there is a table filter set.
        """
        ...

    def hashCode(self) -> int: ...

    def isBusy(self) -> bool:
        """
        Returns true if the model is busy. "Busy" means the model
         is either loading or updating.
        @return true if the model is busy
        """
        ...

    def isCellEditable(self, __a0: int, __a1: int) -> bool: ...

    def isDefaultColumn(self, modelIndex: int) -> bool:
        """
        Returns true if the column indicated by the index in the model is a default column (meaning
         that it was specified by the model and not discovered).
        @param modelIndex the index of the column in the model.
        @return true if the column is a default.
        """
        ...

    def isFiltered(self) -> bool: ...

    def isLoadIncrementally(self) -> bool: ...

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

    def reFilter(self) -> None:
        """
        Triggers this class to filter the contents of the data.
        """
        ...

    def reSort(self) -> None:
        """
        Resort the table using the current sort criteria.  This is useful if the data in the
         table has changed and is no longer sorted properly.  If the setSort method is used, nothing
         will happen because the table will think it is already sorted on that criteria.
        """
        ...

    def refresh(self) -> None:
        """
        Invoke this method when the underlying data has changed, but a reload is not required.
        """
        ...

    def reload(self) -> None:
        """
        Schedules the model to completely reload
         its underlying data.
        """
        ...

    def removeObject(self, __a0: object) -> None: ...

    def removeTableModelListener(self, __a0: javax.swing.event.TableModelListener) -> None: ...

    def removeThreadedTableModelListener(self, listener: docking.widgets.table.threaded.ThreadedTableModelListener) -> None: ...

    def setAllColumnSettings(self, newSettings: List[ghidra.docking.settings.Settings]) -> None: ...

    def setIncrementalTaskMonitor(self, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def setLastSelectedObjects(self, lastSelectedObjects: List[object]) -> None: ...

    def setProgram(self, program: ghidra.program.model.listing.Program) -> None: ...

    def setSelectionSize(self, size: int) -> None:
        """
        Sets the size of the selections generated by this model when asked to create
         program selections.  For example, some clients know that each table row represents
         a contiguous range of 4 addresses.  In this case, when the user makes a selection,
         that client wants the selection to be 4 addresses, starting at the address in
         the given table row.
        @param size the size of the selections generated by this model when asked to create
         			   program selections.
        """
        ...

    def setTableFilter(self, tableFilter: docking.widgets.table.TableFilter) -> None:
        """
        Sets the given <code>TableFilter</code> on this model.  This table filter will then be used
         by this model in the default {@link #doFilter(List, TableSortingContext, TaskMonitor)}
         method.
        @param tableFilter The filter to use for table filtering.
        """
        ...

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

    def updateObject(self, __a0: object) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
