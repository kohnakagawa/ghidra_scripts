import docking.widgets.table
import ghidra.framework.plugintool
import java.lang


class ProgramLocationTableRowMapper(docking.widgets.table.TableRowMapper):
    """
    NOTE:  ALL TableRowMapper CLASSES MUST END IN "TableRowMapper".  If not,
     the ClassSearcher will not find them.

     An interface that allows implementors to map an object of one type to another.  This is useful
     for table models that have row types that are easily converted to other more generic types.
     For example, the Bookmarks table model's data is based upon Bookmark objects.  Furthermore,
     those objects are easily converted to ProgramLocations and Addresses.  By creating a mapper
     for the these types, the table model can now show dynamic columns that work on ProgramLocations
     and Addresses.

     This interface is an ExtensionPoint so that once created, they will be ingested automatically
     by Ghidra.  Once discovered, these mappers will be used to provide dynamic columns to to
     tables with row types that match ROW_TYPE.

     This column is an extension of TableRowMapper that has knowledge of
     ProgramLocationTableColumns, which means that it knows how to generate
     ProgramLocations.  This is the preferred mapper to use with tables that work on program
     data, as it means that the column works with navigation.
    """





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
