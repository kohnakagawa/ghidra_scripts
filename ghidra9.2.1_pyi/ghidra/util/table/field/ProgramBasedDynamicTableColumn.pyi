from typing import List
import docking.widgets.table
import ghidra.docking.settings
import ghidra.framework.plugintool
import ghidra.util.table.column
import java.lang
import java.util


class ProgramBasedDynamicTableColumn(docking.widgets.table.DynamicTableColumn, object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getColumnClass(self) -> java.lang.Class: ...

    def getColumnDescription(self) -> unicode: ...

    def getColumnDisplayName(self, __a0: ghidra.docking.settings.Settings) -> unicode: ...

    def getColumnName(self) -> unicode: ...

    def getColumnPreferredWidth(self) -> int: ...

    def getColumnRenderer(self) -> ghidra.util.table.column.GColumnRenderer: ...

    def getComparator(self) -> java.util.Comparator: ...

    def getMaxLines(self, __a0: ghidra.docking.settings.Settings) -> int: ...

    def getSettingsDefinitions(self) -> List[ghidra.docking.settings.SettingsDefinition]: ...

    def getSupportedRowType(self) -> java.lang.Class: ...

    def getUniqueIdentifier(self) -> unicode: ...

    def getValue(self, __a0: object, __a1: ghidra.docking.settings.Settings, __a2: object, __a3: ghidra.framework.plugintool.ServiceProvider) -> object: ...

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
    def columnClass(self) -> java.lang.Class: ...

    @property
    def columnDescription(self) -> unicode: ...

    @property
    def columnName(self) -> unicode: ...

    @property
    def columnPreferredWidth(self) -> int: ...

    @property
    def columnRenderer(self) -> ghidra.util.table.column.GColumnRenderer: ...

    @property
    def comparator(self) -> java.util.Comparator: ...

    @property
    def settingsDefinitions(self) -> List[ghidra.docking.settings.SettingsDefinition]: ...

    @property
    def supportedRowType(self) -> java.lang.Class: ...

    @property
    def uniqueIdentifier(self) -> unicode: ...
