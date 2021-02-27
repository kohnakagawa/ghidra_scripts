import docking.widgets.table
import ghidra.app.plugin.core.datawindow
import ghidra.framework.plugintool
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.table
import java.lang


class DataRowObjectToAddressTableRowMapper(ghidra.util.table.ProgramLocationTableRowMapper):




    def __init__(self): ...



    def createMappedTableColumn(self, __a0: docking.widgets.table.DynamicTableColumn) -> docking.widgets.table.DynamicTableColumn: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDestinationType(self) -> java.lang.Class: ...

    def getSourceType(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @overload
    def map(self, __a0: ghidra.app.plugin.core.datawindow.DataRowObject, __a1: ghidra.program.model.listing.Program, __a2: ghidra.framework.plugintool.ServiceProvider) -> ghidra.program.model.address.Address: ...

    @overload
    def map(self, __a0: object, __a1: object, __a2: ghidra.framework.plugintool.ServiceProvider) -> object: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
