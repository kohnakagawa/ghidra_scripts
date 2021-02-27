import docking.widgets.table
import ghidra.app.tablechooser
import ghidra.framework.plugintool
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.table
import java.lang


class AddressableRowObjectToAddressTableRowMapper(ghidra.util.table.ProgramLocationTableRowMapper):




    def __init__(self): ...



    def createMappedTableColumn(self, destinationColumn: docking.widgets.table.DynamicTableColumn) -> docking.widgets.table.DynamicTableColumn:
        """
        Creates a table column that will create a table column that knows how to map the
         given <b>ROW_TYPE</b> to the type of the column passed in, the <b>EXPECTED_ROW_TYPE</b>.
        @param <COLUMN_TYPE> The column type of the given and created columns
        @param destinationColumn The existing column, which is based upon EXPECTED_ROW_TYPE,
                that we want to be able to use with the type we have, the ROW_TYPE.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDestinationType(self) -> java.lang.Class: ...

    def getSourceType(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @overload
    def map(self, rowObject: ghidra.app.tablechooser.AddressableRowObject, program: ghidra.program.model.listing.Program, serviceProvider: ghidra.framework.plugintool.ServiceProvider) -> ghidra.program.model.address.Address: ...

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
