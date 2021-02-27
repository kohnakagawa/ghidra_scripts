from typing import List
import ghidra.app.util.datatype.microsoft
import ghidra.docking.settings
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.mem
import ghidra.util
import java.lang
import java.net
import javax.swing.event


class RTTI2DataType(ghidra.app.util.datatype.microsoft.RTTIDataType):
    """
    The RTTI2 data type represents an array of either pointers or displacements to the
     BaseClassDescriptors (RTTI 1s) for a class.

     Fields for this RunTimeTypeInformation structure can be found on http://www.openrce.org

     RTTI_Base_Class_Array is the label for the RTTI2 data structure.
    """





    @overload
    def __init__(self):
        """
        Creates a dynamic Base Class Array data type.
        """
        ...

    @overload
    def __init__(self, rtti1Count: long):
        """
        Creates a dynamic Base Class Array data type.
        @param rtti1Count the number of rtti1 refs
        """
        ...

    @overload
    def __init__(self, dtm: ghidra.program.model.data.DataTypeManager):
        """
        Creates a dynamic Base Class Array data type.
        @param dtm the data type manager for this data type.
        """
        ...

    @overload
    def __init__(self, rtti1Count: long, dtm: ghidra.program.model.data.DataTypeManager):
        """
        Creates a dynamic Base Class Array data type.
        @param rtti1Count the number of rtti1 refs
        @param dtm the data type manager for this data type.
        """
        ...



    def addParent(self, dt: ghidra.program.model.data.DataType) -> None: ...

    def canSpecifyLength(self) -> bool: ...

    def clone(self, dtm: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType: ...

    def copy(self, dtm: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType:
        """
        Returns a clone of this built-in DataType
        @see ghidra.program.model.data.DataType#copy(ghidra.program.model.data.DataTypeManager)
        """
        ...

    def dataTypeDeleted(self, dt: ghidra.program.model.data.DataType) -> None: ...

    def dataTypeNameChanged(self, dt: ghidra.program.model.data.DataType, oldName: unicode) -> None: ...

    def dataTypeReplaced(self, oldDt: ghidra.program.model.data.DataType, newDt: ghidra.program.model.data.DataType) -> None: ...

    def dataTypeSizeChanged(self, dt: ghidra.program.model.data.DataType) -> None: ...

    def dependsOn(self, dt: ghidra.program.model.data.DataType) -> bool: ...

    def equals(self, obj: object) -> bool: ...

    def getAlignment(self) -> int: ...

    def getCTypeDeclaration(self, dataOrganization: ghidra.program.model.data.DataOrganization) -> unicode:
        """
        Returns null for FactoryDataType (which should never be used) and Dynamic types which should
         generally be replaced by a primitive array (e.g., char[5]) or, a primitive pointer (e.g., char *).
         For other types an appropriately sized unsigned integer typedef is returned.
        @see ghidra.program.model.data.BuiltInDataType#getCTypeDeclaration(ghidra.program.model.data.DataOrganization)
        """
        ...

    def getCategoryPath(self) -> ghidra.program.model.data.CategoryPath: ...

    def getClass(self) -> java.lang.Class: ...

    def getComponent(self, index: int, buf: ghidra.program.model.mem.MemBuffer) -> ghidra.program.model.data.DataTypeComponent:
        """
        Returns the immediate n'th component of this data type.
        @param index the components index (zero based).
        @param buf a membuffer to be used by dataTypes that change depending on
         their data context.  A null value is acceptable to indicate that a memory
         context is not available.  DataTypes that need a context will return -1
         if the context is null.
        @return the component data type or null if there is no component at the
         indicated index.
        """
        ...

    def getComponentAt(self, offset: int, buf: ghidra.program.model.mem.MemBuffer) -> ghidra.program.model.data.DataTypeComponent:
        """
        Returns the component containing the byte at the given offset
        @param offset the offset into the dataType
        @param buf the memoryBuffer containing the bytes.
        @return the component containing the byte at the given offset
        """
        ...

    def getComponents(self, buf: ghidra.program.model.mem.MemBuffer) -> List[ghidra.program.model.data.DataTypeComponent]:
        """
        Returns an array of DataTypes that make up this data type.
         Could return null if there are no subcomponents.
         If this is an Array, then only one element will be returned
         which is the Data Prototype for the elements in the array.
         Will return null if this is a subcomponent that doesn't fit in it's
         alloted space.
        @param buf a membuffer to be used by dataTypes that change depending on
         their data context.  A null value is acceptable to indicate that a memory
         context is not available.  DataTypes that need a context will return -1
         if the context is null.
        """
        ...

    def getDataOrganization(self) -> ghidra.program.model.data.DataOrganization: ...

    def getDataTypeManager(self) -> ghidra.program.model.data.DataTypeManager:
        """
        @see ghidra.program.model.data.DataType#getDataTypeManager()
        """
        ...

    def getDataTypePath(self) -> ghidra.program.model.data.DataTypePath: ...

    def getDecompilerDisplayName(self, language: ghidra.program.model.lang.DecompilerLanguage) -> unicode:
        """
        Return token used to represent this type in decompiler/source-code output
        @param language is the language being displayed
        @return the name string
        """
        ...

    def getDefaultAbbreviatedLabelPrefix(self) -> unicode: ...

    @overload
    def getDefaultLabelPrefix(self) -> unicode: ...

    @overload
    def getDefaultLabelPrefix(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, len: int, options: ghidra.program.model.data.DataTypeDisplayOptions) -> unicode: ...

    def getDefaultOffcutLabelPrefix(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, len: int, options: ghidra.program.model.data.DataTypeDisplayOptions, offcutLength: int) -> unicode: ...

    def getDefaultSettings(self) -> ghidra.docking.settings.Settings: ...

    def getDescription(self) -> unicode: ...

    def getDisplayName(self) -> unicode: ...

    def getDocs(self) -> java.net.URL: ...

    def getLastChangeTime(self) -> long: ...

    def getLastChangeTimeInSourceArchive(self) -> long: ...

    @overload
    def getLength(self) -> int: ...

    @overload
    def getLength(self, buf: ghidra.program.model.mem.MemBuffer, maxLength: int) -> int: ...

    @overload
    def getLength(self, memory: ghidra.program.model.mem.Memory, address: ghidra.program.model.address.Address, bytes: List[int]) -> int:
        """
        Gets the total length of the data created when this data type is placed at the indicated
         address in memory.
        @param memory the program memory for this data.
        @param address the start address of the data.
        @param bytes the bytes for this data.
        @return the length of the data. zero is returned if valid data can't be created at the
         indicated address using this data type.
        """
        ...

    def getMnemonic(self, settings: ghidra.docking.settings.Settings) -> unicode: ...

    def getName(self) -> unicode: ...

    def getNumComponents(self, buf: ghidra.program.model.mem.MemBuffer) -> int:
        """
        Gets the number of component data types in this data type.
        @param buf a membuffer to be used by dataTypes that change depending on
         their data context.  A null value is acceptable to indicate that a memory
         context is not available.  DataTypes that need a context will return -1
         if the context is null.
        @return the number of components that make up this data prototype
           - if this is an Array, return the number of elements in the array.
           - if this datatype is a subcomponent of another datatype and it
              won't fit in it's defined space, return -1.
        """
        ...

    def getParents(self) -> List[ghidra.program.model.data.DataType]: ...

    def getPathName(self) -> unicode: ...

    def getReplacementBaseType(self) -> ghidra.program.model.data.DataType: ...

    def getRepresentation(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, length: int) -> unicode: ...

    @overload
    def getRtti1Address(self, program: ghidra.program.model.listing.Program, rtti2Address: ghidra.program.model.address.Address, rtti1Index: int) -> ghidra.program.model.address.Address:
        """
        Gets address referred to by the RTTI 1 pointer at the specified index in the RTTI2's
         array that is at the rtti2Address.
        @param program the program containing the RTTI 2
        @param rtti2Address the address of the RTTI 2
        @param rtti1Index the index of RTTI 1 entry in the RTTI 2 array
        @return the address of the RTTI 1 referred to by the indexed array element.
        """
        ...

    @overload
    def getRtti1Address(self, memory: ghidra.program.model.mem.Memory, rtti2Address: ghidra.program.model.address.Address, rtti1Index: int) -> ghidra.program.model.address.Address:
        """
        Gets address referred to by the RTTI 1 pointer at the specified index in the RTTI2's
         array that is at the rtti2Address.
        @param memory the program memory containing the RTTI 2
        @param rtti2Address the address of the RTTI 2
        @param rtti1Index the index of RTTI 1 entry in the RTTI 2 array
        @return the address of the RTTI 1 referred to by the indexed array element.
        """
        ...

    def getSettingsDefinitions(self) -> List[ghidra.docking.settings.SettingsDefinition]:
        """
        Gets a list of all the settingsDefinitions used by this datatype.
        @return a list of the settingsDefinitions used by this datatype.
        """
        ...

    def getSourceArchive(self) -> ghidra.program.model.data.SourceArchive: ...

    def getUniversalID(self) -> ghidra.util.UniversalID: ...

    def getValue(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, length: int) -> object: ...

    def getValueClass(self, settings: ghidra.docking.settings.Settings) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def invalidateCache(self) -> None: ...

    def isDeleted(self) -> bool: ...

    def isDynamicallySized(self) -> bool:
        """
        @see ghidra.program.model.data.DataType#isDynamicallySized()
        """
        ...

    def isEquivalent(self, dt: ghidra.program.model.data.DataType) -> bool: ...

    def isNotYetDefined(self) -> bool: ...

    @overload
    def isValid(self, program: ghidra.program.model.listing.Program, startAddress: ghidra.program.model.address.Address, validationOptions: ghidra.app.util.datatype.microsoft.DataValidationOptions) -> bool: ...

    @overload
    def isValid(self, program: ghidra.program.model.listing.Program, startAddress: ghidra.program.model.address.Address, overwriteInstructions: bool, overwriteDefinedData: bool) -> bool:
        """
        Determines if the data type is valid for placing at the indicated address in the program.
        @param program the program
        @param startAddress the start address
        @param overwriteInstructions true indicates that existing instructions can be overwritten
         by this data type.
        @param overwriteDefinedData true indicates that existing defined data can be overwritten
         by this data type.
        @return true if this data type can be laid down at the specified address.
        @see #isValid(Program program, Address address, DataValidationOptions validationOptions)
        """
        ...

    @overload
    def isValidRtti1Pointer(self, program: ghidra.program.model.listing.Program, startAddress: ghidra.program.model.address.Address, pointerIndex: int, validationOptions: ghidra.app.util.datatype.microsoft.DataValidationOptions) -> bool:
        """
        Determines if the RTTI 1 pointer in the RTTI2 structure is valid.
        @param program the program
        @param startAddress the address of the RTTI 2 structure
        @param pointerIndex index of the element in the array that makes up the RTTI 2.
        @param validationOptions options indicating how to perform the validation
        @return true if the indicated RTTI1 pointer is valid.
        """
        ...

    @overload
    def isValidRtti1Pointer(self, program: ghidra.program.model.listing.Program, startAddress: ghidra.program.model.address.Address, pointerIndex: int, overwriteInstructions: bool, overwriteDefinedData: bool) -> bool:
        """
        Determines if the RTTI 1 pointer in the RTTI2 structure is valid.
        @param program the program
        @param startAddress the address of the RTTI 2 structure
        @param pointerIndex index of the element in the array that makes up the RTTI 2.
        @param overwriteInstructions true indicates that existing instructions can be overwritten
         by this data type.
        @param overwriteDefinedData true indicates that existing defined data can be overwritten
         by this data type.
        @return true if the indicated RTTI1 pointer is valid.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeParent(self, dt: ghidra.program.model.data.DataType) -> None: ...

    def replaceWith(self, dataType: ghidra.program.model.data.DataType) -> None: ...

    def setCategoryPath(self, path: ghidra.program.model.data.CategoryPath) -> None: ...

    def setDefaultSettings(self, settings: ghidra.docking.settings.Settings) -> None: ...

    def setDescription(self, description: unicode) -> None:
        """
        Sets a String briefly describing this DataType.
         <br>If a data type that extends this class wants to allow the description to be changed,
         then it must override this method.
        @param description a one-liner describing this DataType.
        @throws UnsupportedOperationException if the description is not allowed to be set for this data type.
        """
        ...

    def setLastChangeTime(self, lastChangeTime: long) -> None: ...

    def setLastChangeTimeInSourceArchive(self, lastChangeTimeInSourceArchive: long) -> None: ...

    def setName(self, name: unicode) -> None: ...

    def setNameAndCategory(self, path: ghidra.program.model.data.CategoryPath, name: unicode) -> None: ...

    def setSourceArchive(self, archive: ghidra.program.model.data.SourceArchive) -> None: ...

    def stateChanged(self, e: javax.swing.event.ChangeEvent) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def defaultLabelPrefix(self) -> unicode: ...

    @property
    def description(self) -> unicode: ...

    @description.setter
    def description(self, value: unicode) -> None: ...
