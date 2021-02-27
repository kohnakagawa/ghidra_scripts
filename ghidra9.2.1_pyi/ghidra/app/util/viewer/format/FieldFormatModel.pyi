from typing import List
import ghidra.app.util.viewer.field
import ghidra.app.util.viewer.format
import ghidra.app.util.viewer.proxy
import ghidra.framework.options
import java.lang
import org.jdom


class FieldFormatModel(object):
    """
    Maintains the size and ordering for a layout of fields.
    """

    ARRAY: int = 6
    DIVIDER: int = 0
    FUNCTION: int = 2
    FUNCTION_VARS: int = 3
    INSTRUCTION_OR_DATA: int = 4
    OPEN_DATA: int = 5
    PLATE: int = 1







    def addAllFactories(self) -> None:
        """
        Adds all unused fields to this model.
        """
        ...

    def addFactory(self, factory: ghidra.app.util.viewer.field.FieldFactory, rowIndex: int, colIndex: int) -> None:
        """
        Adds a new field to this format.
        @param factory the FieldFactory to add
        @param rowIndex the row to add the field to
        @param colIndex the position in the row for the new field.
        """
        ...

    def addLayouts(self, __a0: List[object], __a1: int, __a2: ghidra.app.util.viewer.proxy.ProxyObj) -> None: ...

    def addRow(self, index: int) -> None:
        """
        Adds new empty row at the given position.  The position must be in the
         interval [0,numRows].
        @exception IllegalArgumentException thrown if the position is outside the
         interval [0,numRows].
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAllFactories(self) -> List[ghidra.app.util.viewer.field.FieldFactory]: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getFactorys(self) -> List[ghidra.app.util.viewer.field.FieldFactory]:
        """
        Returns the list factories valid for this format.
        """
        ...

    @overload
    def getFactorys(self, row: int) -> List[ghidra.app.util.viewer.field.FieldFactory]:
        """
        Returns the FieldFactorys on a given row.
        """
        ...

    def getFormatManager(self) -> ghidra.app.util.viewer.format.FormatManager:
        """
        Returns the formatMgr that is managing this model.
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of this format model.
        """
        ...

    def getNumFactorys(self, row: int) -> int:
        """
        Returns the number of FieldFactorys on any given row.
        """
        ...

    def getNumRows(self) -> int:
        """
        Returns the number of rows in the model.
        """
        ...

    def getUnusedFactories(self) -> List[ghidra.app.util.viewer.field.FieldFactory]:
        """
        Returns a list of unused valid fields for this model
        @return a list of unused valid fields for this model
        """
        ...

    def getWidth(self) -> int:
        """
        Returns the width of this model
        """
        ...

    def hashCode(self) -> int: ...

    def modelChanged(self) -> None:
        """
        Notifies the formatMgr that this format model has changed.
        """
        ...

    def moveFactory(self, oldRowIndex: int, oldColIndex: int, newRowIndex: int, newColIndex: int) -> None:
        """
        Moves the Field at (oldrow,oldCol) to (row,col)
        @param oldRowIndex the row containing the field to be moved.
        @param oldColIndex the column index of the field to be moved.
        @param newRowIndex the row to move to.
        @param newColIndex the column to move to.
        @exception IllegalArgumentException thrown if any of the parameters don't
         map to a valid grid position.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def optionsChanged(self, options: ghidra.framework.options.Options, optionName: unicode, oldValue: object, newValue: object) -> None:
        """
        Notifies that the options have changed.
        @param options the Options object that changed.
        @param optionName the name of the property that changed.
        @param oldValue the old value of the property.
        @param newValue the new value of the property.
        """
        ...

    def removeAllFactories(self) -> None:
        """
        Removes all fields from this model.
        """
        ...

    def removeFactory(self, rowIndex: int, colIndex: int) -> None:
        """
        Removes a field from the format.
        @param rowIndex the row index of the field to remove.
        @param colIndex the column index of the field to remove.
        """
        ...

    def removeRow(self, index: int) -> None:
        """
        Removes the row currently at the given position.
        @param index the index of the row to remove.
        """
        ...

    def restoreFromXml(self, root: org.jdom.Element) -> None:
        """
        Restores the format for this model from XML.
        @param root the root XML element from which to get the format information.
        """
        ...

    def saveToXml(self) -> org.jdom.Element:
        """
        Saves this format to XML.
        """
        ...

    def servicesChanged(self) -> None:
        """
        Notifies each row that the services have changed.
        """
        ...

    def setBaseRowID(self, id: int) -> None:
        """
        Sets the base id for this model. Each row in a model gets an id which must
         be unique across all models.
        @param id the base id for this format.
        """
        ...

    def toString(self) -> unicode: ...

    def update(self) -> None:
        """
        Updates users of the formatMgr to indicate the format has changed.
        """
        ...

    def updateRow(self, index: int) -> None:
        """
        Updates the fields on the given row.
        @param index the row to update.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def allFactories(self) -> List[ghidra.app.util.viewer.field.FieldFactory]: ...

    @property
    def baseRowID(self) -> None: ...  # No getter available.

    @baseRowID.setter
    def baseRowID(self, value: int) -> None: ...

    @property
    def factorys(self) -> List[ghidra.app.util.viewer.field.FieldFactory]: ...

    @property
    def formatManager(self) -> ghidra.app.util.viewer.format.FormatManager: ...

    @property
    def name(self) -> unicode: ...

    @property
    def numRows(self) -> int: ...

    @property
    def unusedFactories(self) -> List[ghidra.app.util.viewer.field.FieldFactory]: ...

    @property
    def width(self) -> int: ...
