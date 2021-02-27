from typing import List
import java.lang
import java.util
import javax.swing.event
import javax.swing.table


class FVTableModel(javax.swing.table.AbstractTableModel):
    """
    The model that backs the FVTable table. This model defines 4 columns: date,
     time, log level, and the message.
    """

    DATE_COL: int = 0
    LEVEL_COL: int = 2
    MESSAGE_COL: int = 3
    TIME_COL: int = 1



    def __init__(self): ...



    @overload
    def addRow(self, row: unicode, notify: bool) -> None:
        """
        Adds a row to the model.
        @param row the data to add
        @param notify if true, a notification will be sent to subscribers
        """
        ...

    @overload
    def addRow(self, row: unicode, index: int, notify: bool) -> None:
        """
        Adds a row to the model
        @param row the data to add
        @param index the position within the model to add this to
        @param notify if true, a notification will be sent to subscribers
        """
        ...

    def addRowsToBottom(self, __a0: List[object]) -> None: ...

    def addRowsToTop(self, __a0: List[object]) -> None: ...

    def addTableModelListener(self, __a0: javax.swing.event.TableModelListener) -> None: ...

    def clear(self) -> None:
        """
        Clears all lines from the model and fires off a notification.
        """
        ...

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

    def getColumnClass(self, columnIndex: int) -> java.lang.Class: ...

    def getColumnCount(self) -> int: ...

    def getColumnName(self, column: int) -> unicode: ...

    def getListeners(self, __a0: java.lang.Class) -> List[java.util.EventListener]: ...

    def getRowCount(self) -> int: ...

    def getTableModelListeners(self) -> List[javax.swing.event.TableModelListener]: ...

    def getValueAt(self, rowIndex: int, columnIndex: int) -> object: ...

    def hashCode(self) -> int: ...

    def isCellEditable(self, __a0: int, __a1: int) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeRowsFromBottom(self, count: int) -> None:
        """
        Removes a set of rows from the bottom of the view.
        @param count the number of rows to remove
        """
        ...

    def removeRowsFromTop(self, count: int) -> None:
        """
        Removes a set of rows from the top of the view.
        @param count the number of rows to remove
        """
        ...

    def removeTableModelListener(self, __a0: javax.swing.event.TableModelListener) -> None: ...

    def setValueAt(self, __a0: object, __a1: int, __a2: int) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def columnCount(self) -> int: ...

    @property
    def rowCount(self) -> int: ...
