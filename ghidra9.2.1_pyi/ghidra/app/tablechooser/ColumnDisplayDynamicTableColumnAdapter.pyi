from typing import List
import ghidra.app.tablechooser
import ghidra.docking.settings
import ghidra.framework.plugintool
import ghidra.program.model.listing
import ghidra.util.table.column
import ghidra.util.table.field
import java.lang
import java.util
import java.util.function


class ColumnDisplayDynamicTableColumnAdapter(ghidra.util.table.field.AbstractProgramBasedDynamicTableColumn, java.util.Comparator):




    def __init__(self, display: ghidra.app.tablechooser.ColumnDisplay): ...



    @overload
    def compare(self, o1: ghidra.app.tablechooser.AddressableRowObject, o2: ghidra.app.tablechooser.AddressableRowObject) -> int: ...

    @overload
    def compare(self, __a0: object, __a1: object) -> int: ...

    @overload
    @staticmethod
    def comparing(__a0: java.util.function.Function) -> java.util.Comparator: ...

    @overload
    @staticmethod
    def comparing(__a0: java.util.function.Function, __a1: java.util.Comparator) -> java.util.Comparator: ...

    @staticmethod
    def comparingDouble(__a0: java.util.function.ToDoubleFunction) -> java.util.Comparator: ...

    @staticmethod
    def comparingInt(__a0: java.util.function.ToIntFunction) -> java.util.Comparator: ...

    @staticmethod
    def comparingLong(__a0: java.util.function.ToLongFunction) -> java.util.Comparator: ...

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

    def getSettingsDefinitions(self) -> List[ghidra.docking.settings.SettingsDefinition]: ...

    def getSupportedRowType(self) -> java.lang.Class: ...

    def getUniqueIdentifier(self) -> unicode: ...

    @overload
    def getValue(self, rowObject: ghidra.app.tablechooser.AddressableRowObject, settings: ghidra.docking.settings.Settings, program: ghidra.program.model.listing.Program, serviceProvider: ghidra.framework.plugintool.ServiceProvider) -> COLUMN_TYPE: ...

    @overload
    def getValue(self, __a0: object, __a1: ghidra.docking.settings.Settings, __a2: object, __a3: ghidra.framework.plugintool.ServiceProvider) -> object: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def naturalOrder() -> java.util.Comparator: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def nullsFirst(__a0: java.util.Comparator) -> java.util.Comparator: ...

    @staticmethod
    def nullsLast(__a0: java.util.Comparator) -> java.util.Comparator: ...

    @staticmethod
    def reverseOrder() -> java.util.Comparator: ...

    def reversed(self) -> java.util.Comparator: ...

    @overload
    def thenComparing(self, __a0: java.util.Comparator) -> java.util.Comparator: ...

    @overload
    def thenComparing(self, __a0: java.util.function.Function) -> java.util.Comparator: ...

    @overload
    def thenComparing(self, __a0: java.util.function.Function, __a1: java.util.Comparator) -> java.util.Comparator: ...

    def thenComparingDouble(self, __a0: java.util.function.ToDoubleFunction) -> java.util.Comparator: ...

    def thenComparingInt(self, __a0: java.util.function.ToIntFunction) -> java.util.Comparator: ...

    def thenComparingLong(self, __a0: java.util.function.ToLongFunction) -> java.util.Comparator: ...

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
    def columnName(self) -> unicode: ...