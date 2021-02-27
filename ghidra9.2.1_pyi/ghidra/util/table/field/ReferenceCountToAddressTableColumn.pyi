from typing import List
import ghidra.docking.settings
import ghidra.framework.plugintool
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.table.column
import ghidra.util.table.field
import java.lang
import java.util


class ReferenceCountToAddressTableColumn(ghidra.util.table.field.ProgramBasedDynamicTableColumnExtensionPoint):
    """
    This table field displays the number of references to the location that was found
    """





    def __init__(self): ...



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
    def getValue(self, rowObject: ghidra.program.model.address.Address, settings: ghidra.docking.settings.Settings, pgm: ghidra.program.model.listing.Program, serviceProvider: ghidra.framework.plugintool.ServiceProvider) -> int: ...

    @overload
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
    def columnName(self) -> unicode: ...
