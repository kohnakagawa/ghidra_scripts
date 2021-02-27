import ghidra.app.util.bin.format.dwarf4
import ghidra.app.util.bin.format.dwarf4.next.DWARFDataTypeImporter
import ghidra.program.model.data
import java.lang


class DWARFDataTypeImporter(object):
    """
    Creates Ghidra DataTypes using information from DWARF debug entries.  The caller
     is responsible for writing the resulting temporary DataType instances into the database.

     Create a new instance of this class for each DIEAggregate datatype that you wish
     to convert into a DataType.

    """





    def __init__(self, prog: ghidra.app.util.bin.format.dwarf4.next.DWARFProgram, dwarfDTM: ghidra.app.util.bin.format.dwarf4.next.DWARFDataTypeManager, importOptions: ghidra.app.util.bin.format.dwarf4.next.DWARFImportOptions):
        """
        Create a new data type importer.
        @param prog {@link DWARFProgram} that is being imported
        @param dwarfDTM {@link DWARFDataTypeManager} helper
        @param importOptions {@link DWARFImportOptions} control optional features during import
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDDTByInstance(self, dtInstance: ghidra.program.model.data.DataType) -> ghidra.app.util.bin.format.dwarf4.next.DWARFDataTypeImporter.DWARFDataType: ...

    def getDataType(self, diea: ghidra.app.util.bin.format.dwarf4.DIEAggregate, defaultValue: ghidra.app.util.bin.format.dwarf4.next.DWARFDataTypeImporter.DWARFDataType) -> ghidra.app.util.bin.format.dwarf4.next.DWARFDataTypeImporter.DWARFDataType:
        """
        Converts the specified DWARF debug entry into a Ghidra {@link DataType} (wrapped
         in a simple holder object to also return associated metadata).
        @param diea DWARF {@link DIEAggregate} to convert into Ghidra DataType.
        @param defaultValue value to return if the specified DIEA is null or there is a problem
         with the DWARF debug data.
        @return a {@link DWARFDataType} wrapper around the new Ghidra {@link DataType}.
        @throws IOException
        @throws DWARFExpressionException
        """
        ...

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
