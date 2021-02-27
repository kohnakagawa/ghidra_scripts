from typing import List
import ghidra.app.util.bin.format.dwarf4
import ghidra.app.util.bin.format.dwarf4.next
import ghidra.program.model.data
import ghidra.util.task
import java.lang


class DWARFDataTypeManager(object):
    """
    Manages mappings between DWARF DIEs and Ghidra DataTypes.
    """





    def __init__(self, prog: ghidra.app.util.bin.format.dwarf4.next.DWARFProgram, dataTypeManager: ghidra.program.model.data.DataTypeManager, builtInDTM: ghidra.program.model.data.DataTypeManager, importSummary: ghidra.app.util.bin.format.dwarf4.next.DWARFImportSummary):
        """
        Creates a new {@link DWARFDataTypeManager} instance.
        @param prog {@link DWARFProgram} that holds the Ghidra {@link Program} being imported.
        @param dataTypeManager {@link DataTypeManager} of the Ghidra Program.
        @param builtInDTM {@link DataTypeManager} with built-in data types.
        @param importSummary {@link DWARFImportSummary} where summary information will be stored
         during the import session.
        """
        ...



    def addDataType(self, offset: long, dataType: ghidra.program.model.data.DataType, dsi: ghidra.app.util.bin.format.dwarf4.next.DWARFSourceInfo) -> None: ...

    def doGetDataType(self, diea: ghidra.app.util.bin.format.dwarf4.DIEAggregate) -> ghidra.program.model.data.DataType:
        """
        Creates a {@link DataType} from the DWARF {@link DIEAggregate DIEA}, or returns a
         pre-existing {@link DataType} created by the specified DIEA previously.
         <p>
         Creating a new DataType happens in two stages, where the DataType is created as
         an 'impl' DataType first (possibly representing a large graph of referred-to datatypes),
         and then it is submitted to the {@link DataTypeManager} to be added to the database and
         converted to a 'db' object.
         <p>
         Mapping from the DIEA's offset to the resultant 'db' DataType object is a two step
         process.
         <p>
         A {@link DataTypeGraphComparator} is used to walk the 'impl' DataType object graph
         in lock-step with the resultant 'db' DataType object graph, and the mapping between
         the 'impl' object and its creator DIEA (held in {@link DWARFDataType})
         is used to create a mapping to the resultant 'db' DataType's path.
        @param diea DWARF {@link DIEAggregate} with datatype information that needs to be converted
         to a Ghidra DataType.
        @return {@link DataType} that is ready to use.
        @throws IOException if problem
        @throws DWARFExpressionException if problem
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def forAllConflicts(self, dtp: ghidra.program.model.data.DataTypePath) -> java.lang.Iterable:
        """
        Iterate all {@link DataType}s that match the CategoryPath / name given
         in the {@link DataTypePath} parameter, including "conflict" datatypes
         that have a ".CONFLICTxx" suffix.
        @param dtp
        @return
        """
        ...

    @overload
    def getBaseType(self, name: unicode) -> ghidra.program.model.data.DataType:
        """
        Returns a DWARF base data type based on its name, or null if it does not exist.
        @param name base type name
        @return {@link DataType} or null if base type does not exist
        """
        ...

    @overload
    def getBaseType(self, name: unicode, dwarfSize: int, dwarfEncoding: int, isBigEndian: bool) -> ghidra.program.model.data.DataType:
        """
        Returns a Ghidra {@link DataType datatype} that corresponds to the DWARF named type.
         <p>
         If there is no direct matching named Ghidra type, generic types of matching
         size will be returned for integer and floating numeric dwarf encoding types, boolean,
         and character types.  Failing that, generic storage types of matching size
         (word, dword, etc) will be returned, and failing that, an array of the correct size
         will be returned.
         <p>
         If the returned data type is not a direct named match, the returned data type
         will be wrapped in a Ghdira typedef using the dwarf type's name.
         <p>
         Any newly created Ghidra data types will be cached and the same instance will be returned
         if the same DWARF named base type is requested again.
         <p>
        @param name
        @param dwarfSize
        @param dwarfEncoding
        @param isBigEndian
        @return
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getDataType(self, dieOffset: long, defaultValue: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataType:
        """
        Returns a Ghidra {@link DataType} corresponding to the specified DIE (based on its
         offset), or the specified defaultValue if the DIE does not map to a defined
         datatype (registered with {@link #addDataType(long, DataType, DWARFSourceInfo)}).
         <p>
        @param dieOffset offset of a DIE record that defines a data type
        @param defaultValue Ghidra {@link DataType} to return if the specified DIE not already defined.
        @return Ghidra {@link DataType}
        """
        ...

    @overload
    def getDataType(self, diea: ghidra.app.util.bin.format.dwarf4.DIEAggregate, defaultValue: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataType:
        """
        Returns a Ghidra {@link DataType} corresponding to the specified {@link DIEAggregate},
         or the specified defaultValue if the DIEA param is null or does not map to an already
         defined datatype (registered with {@link #addDataType(long, DataType, DWARFSourceInfo)}).
         <p>
        @param diea {@link DIEAggregate} that defines a data type
        @param defaultValue Ghidra {@link DataType} to return if the specified DIEA is null
         or not already defined.
        @return Ghidra {@link DataType}
        """
        ...

    def getFunctionSignature(self, diea: ghidra.app.util.bin.format.dwarf4.DIEAggregate) -> ghidra.program.model.data.FunctionDefinition:
        """
        Construct a temporary 'impl' {@link FunctionDefinition} DataType using the information
         found in the specified {@link DIEAggregate}.
        @param diea {@link DIEAggregate} of a subprogram, callsite, etc.
        @return {@link FunctionDefinition} impl (not saved to the DB) or null if not a valid
         DIEA.
        """
        ...

    def getImportedTypes(self) -> List[ghidra.program.model.data.DataTypePath]: ...

    def getOffsetType(self, size: int) -> ghidra.program.model.data.DataType:
        """
        Returns a Ghidra {@link DataType datatype} that corresponds to a type
         that can be used to represent an offset.
         <p>
        @param size
        @return
        """
        ...

    def getPtrTo(self, dt: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataType:
        """
        Returns a pointer to the specified data type.
        @param dt Ghidra {@link DataType}
        @return a {@link Pointer} that points to the specified datatype.
        """
        ...

    def getSourceInfo(self, dataType: ghidra.program.model.data.DataType) -> ghidra.app.util.bin.format.dwarf4.next.DWARFSourceInfo: ...

    def getSpecificDataType(self, diea: ghidra.app.util.bin.format.dwarf4.DIEAggregate, dataTypeClazz: java.lang.Class) -> object: ...

    def getUndefined1Type(self) -> ghidra.program.model.data.DataType:
        """
        Returns datatype to hold a 1 byte undefined value.
        @return undefined 1 byte {@link DataType}.
        """
        ...

    def getVoidType(self) -> ghidra.program.model.data.DataType:
        """
        Returns the void type.
        @return void {@link DataType}
        """
        ...

    def hashCode(self) -> int: ...

    def importAllDataTypes(self, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Does the actual import work.  Updates the {@link #importSummary summary} object
         with information about the types imported and errors encountered.
        @param monitor to watch for cancel
        @throws IOException if errors are encountered reading data
        @throws DWARFException if errors are encountered processing
        @throws CancelledException if the {@link TaskMonitor} is canceled by the user.
        """
        ...

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
    def importedTypes(self) -> List[object]: ...

    @property
    def undefined1Type(self) -> ghidra.program.model.data.DataType: ...

    @property
    def voidType(self) -> ghidra.program.model.data.DataType: ...
