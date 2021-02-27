from typing import List
import docking.widgets
import ghidra.program.model.data
import java.lang
import javax.swing


class DataTypeDropDownSelectionDataModel(object, docking.widgets.DropDownTextFieldDataModel):
    """
    The data model for DropDownSelectionTextField that allows the text field to work with
     DataTypes.
    """





    @overload
    def __init__(self, dataTypeService: ghidra.app.services.DataTypeManagerService): ...

    @overload
    def __init__(self, serviceProvider: ghidra.framework.plugintool.ServiceProvider): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getDescription(self, value: ghidra.program.model.data.DataType) -> unicode: ...

    @overload
    def getDescription(self, __a0: object) -> unicode: ...

    @overload
    def getDisplayText(self, value: ghidra.program.model.data.DataType) -> unicode: ...

    @overload
    def getDisplayText(self, __a0: object) -> unicode: ...

    def getIndexOfFirstMatchingEntry(self, __a0: List[object], __a1: unicode) -> int: ...

    def getListRenderer(self) -> javax.swing.ListCellRenderer: ...

    def getMatchingData(self, searchText: unicode) -> List[ghidra.program.model.data.DataType]: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def listRenderer(self) -> javax.swing.ListCellRenderer: ...
