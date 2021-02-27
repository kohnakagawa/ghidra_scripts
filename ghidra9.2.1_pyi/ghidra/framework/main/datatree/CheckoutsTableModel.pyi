from typing import List
import docking.widgets.table
import ghidra.framework.store
import java.lang
import java.util
import javax.swing.event
import javax.swing.table


class CheckoutsTableModel(docking.widgets.table.AbstractSortedTableModel):
    """
    Table model for showing checkout information for a domain file.
    """





    @overload
    def __init__(self): ...

    @overload
    def __init__(self, defaultSortColumn: int): ...



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

    def getClass(self) -> java.lang.Class: ...

    def getColumnClass(self, columnIndex: int) -> java.lang.Class: ...

    def getColumnCount(self) -> int: ...

    def getColumnName(self, column: int) -> unicode: ...

    def getColumnValueForRow(self, __a0: object, __a1: int) -> object: ...

    def getLastSelectedObjects(self) -> List[object]: ...

    def getListeners(self, __a0: java.lang.Class) -> List[java.util.EventListener]: ...

    def getModelData(self) -> List[ghidra.framework.store.ItemCheckoutStatus]: ...

    def getName(self) -> unicode: ...

    def getPendingSortState(self) -> docking.widgets.table.TableSortState: ...

    def getPreferredColumnWidth(self, columnIndex: int) -> int: ...

    def getPrimarySortColumnIndex(self) -> int: ...

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

    def getValueAt(self, rowIndex: int, columnIndex: int) -> object:
        """
        The default implementation of {@link TableModel#getValueAt(int, int)} that calls the
         abstract {@link #getColumnValueForRow(Object, int)}.
        """
        ...

    def hashCode(self) -> int: ...

    def isCellEditable(self, rowIndex: int, columnIndex: int) -> bool: ...

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

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def refresh(self) -> None:
        """
        Invoke this method when the underlying data has changed, but a reload is not required.
        """
        ...

    def removeTableModelListener(self, __a0: javax.swing.event.TableModelListener) -> None: ...

    def setLastSelectedObjects(self, lastSelectedObjects: List[object]) -> None: ...

    def setTableSortState(self, newSortState: docking.widgets.table.TableSortState) -> None: ...

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
