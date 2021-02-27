from typing import List
import ghidra.docking.settings
import ghidra.framework.main.datatable
import ghidra.framework.model
import ghidra.framework.plugintool
import ghidra.util.table.column
import java.lang
import java.util


class AddressSizeProjectDataColumn(ghidra.framework.main.datatable.ProjectDataColumn):




    def __init__(self): ...



    @overload
    def compareTo(self, other: ghidra.framework.main.datatable.ProjectDataColumn) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getColumnClass(self) -> java.lang.Class: ...

    def getColumnDescription(self) -> unicode: ...

    def getColumnDisplayName(self, settings: ghidra.docking.settings.Settings) -> unicode: ...

    def getColumnName(self) -> unicode: ...

    def getColumnPreferredWidth(self) -> int: ...

    def getColumnRenderer(self) -> ghidra.util.table.column.GColumnRenderer: ...

    def getComparator(self) -> java.util.Comparator: ...

    def getMaxLines(self, settings: ghidra.docking.settings.Settings) -> int: ...

    def getPriority(self) -> int: ...

    def getSettingsDefinitions(self) -> List[ghidra.docking.settings.SettingsDefinition]: ...

    def getSupportedRowType(self) -> java.lang.Class: ...

    def getUniqueIdentifier(self) -> unicode: ...

    @overload
    def getValue(self, info: ghidra.framework.main.datatable.DomainFileInfo, settings: ghidra.docking.settings.Settings, data: ghidra.framework.model.ProjectData, services: ghidra.framework.plugintool.ServiceProvider) -> int: ...

    @overload
    def getValue(self, __a0: object, __a1: ghidra.docking.settings.Settings, __a2: object, __a3: ghidra.framework.plugintool.ServiceProvider) -> object: ...

    def hashCode(self) -> int: ...

    def isDefaultColumn(self) -> bool: ...

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
    def columnName(self) -> unicode: ...

    @property
    def columnPreferredWidth(self) -> int: ...

    @property
    def defaultColumn(self) -> bool: ...

    @property
    def priority(self) -> int: ...
