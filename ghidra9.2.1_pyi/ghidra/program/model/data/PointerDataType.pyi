from typing import List
import ghidra.docking.settings
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.lang
import ghidra.program.model.mem
import ghidra.util
import java.lang
import java.net
import javax.swing.event


class PointerDataType(ghidra.program.model.data.BuiltIn, ghidra.program.model.data.Pointer):
    """
    Basic implementation for a pointer dataType
    """

    MAX_POINTER_SIZE_BYTES: int = 8
    POINTER_LABEL_PREFIX: unicode = u'PTR'
    POINTER_LOOP_LABEL_PREFIX: unicode = u'PTR_LOOP'
    POINTER_NAME: unicode = u'pointer'



    @overload
    def __init__(self):
        """
        Creates a dynamically-sized default pointer data type. A dynamic pointer size
         of 4-bytes will be in used, but will adapt to a data type manager's data
         organization when resolved.
        """
        ...

    @overload
    def __init__(self, referencedDataType: ghidra.program.model.data.DataType):
        """
        Construct a dynamically-sized pointer to a referencedDataType A dynamic
         pointer size of 4-bytes will be in used, but will adapt to a data type
         manager's data organization when resolved.
        @param referencedDataType data type this pointer points to
        """
        ...

    @overload
    def __init__(self, dtm: ghidra.program.model.data.DataTypeManager):
        """
        Creates a dynamically-sized default pointer data type. The pointer size is
         established dynamically based upon the data organization associated with the
         specified dtm but can adapt to another data type manager's data organization
         when resolved.
        @param dtm data-type manager whose data organization should be used
        """
        ...

    @overload
    def __init__(self, referencedDataType: ghidra.program.model.data.DataType, length: int):
        """
        Construct a pointer of a specified length to a referencedDataType. Note: It
         is preferred to use default sized pointers when possible (i.e., length=-1,
         see {@link #PointerDataType(DataType)}) instead of explicitly specifying the
         pointer length value.
        @param referencedDataType data type this pointer points to
        @param length pointer length (values &lt;= 0 will result in
                                   dynamically-sized pointer)
        """
        ...

    @overload
    def __init__(self, referencedDataType: ghidra.program.model.data.DataType, dtm: ghidra.program.model.data.DataTypeManager):
        """
        Construct a dynamically-sized pointer to the given data type. The pointer
         size is established dynamically based upon the data organization associated
         with the specified dtm but can adapt to another data type manager's data
         organization when resolved.
        @param referencedDataType data type this pointer points to
        @param dtm data-type manager whose data organization should be
                                   used
        """
        ...

    @overload
    def __init__(self, referencedDataType: ghidra.program.model.data.DataType, length: int, dtm: ghidra.program.model.data.DataTypeManager):
        """
        Construct a pointer of a specified length to a referencedDataType. Note: It
         is preferred to use default sized pointers when possible (i.e., length=-1,
         see {@link #PointerDataType(DataType, DataTypeManager)}) instead of
         explicitly specifying the pointer length value.
        @param referencedDataType data type this pointer points to
        @param length pointer length (-1 will result in dynamically-sized
                                   pointer)
        @param dtm associated data type manager whose data
                                   organization will be used
        """
        ...



    def addParent(self, dt: ghidra.program.model.data.DataType) -> None: ...

    def clone(self, dtm: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.Pointer: ...

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

    @staticmethod
    def getAddressValue(buf: ghidra.program.model.mem.MemBuffer, size: int, targetSpace: ghidra.program.model.address.AddressSpace) -> ghidra.program.model.address.Address:
        """
        Generate an address value based upon bytes stored at the specified buf
         location
        @param buf memory buffer and stored pointer location
        @param size pointer size in bytes
        @param targetSpace address space for returned pointer
        @return pointer value or null if unusable buf or data
        """
        ...

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

    def getDataOrganization(self) -> ghidra.program.model.data.DataOrganization: ...

    def getDataType(self) -> ghidra.program.model.data.DataType: ...

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

    @staticmethod
    def getLabelString(buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, len: int, options: ghidra.program.model.data.DataTypeDisplayOptions) -> unicode: ...

    def getLastChangeTime(self) -> long: ...

    def getLastChangeTimeInSourceArchive(self) -> long: ...

    def getLength(self) -> int: ...

    def getMnemonic(self, settings: ghidra.docking.settings.Settings) -> unicode: ...

    def getName(self) -> unicode: ...

    def getParents(self) -> List[ghidra.program.model.data.DataType]: ...

    def getPathName(self) -> unicode: ...

    @overload
    @staticmethod
    def getPointer(dt: ghidra.program.model.data.DataType, pointerSize: int) -> ghidra.program.model.data.Pointer:
        """
        Get a pointer data-type instance of the requested size. NOTE: The returned
         data-type will not be associated with any particular data-type-manager and
         may therefore not utilize dynamically-sized-pointers when a valid pointerSize
         is specified. If an invalid pointerSize is specified, a dynamically-size
         pointer will be returned whose length is based upon the
         default-data-organization.
        @param dt data-type referenced by pointer
        @param pointerSize pointer size
        @return signed integer data type
        """
        ...

    @overload
    @staticmethod
    def getPointer(dt: ghidra.program.model.data.DataType, dtm: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.Pointer:
        """
        Get a pointer data-type instance with a default size
        @param dt data-type referenced by pointer
        @param dtm program data-type manager (required) a generic data-type will be
                    returned if possible.
        @return signed integer data type
        """
        ...

    def getRepresentation(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, len: int) -> unicode: ...

    def getSettingsDefinitions(self) -> List[ghidra.docking.settings.SettingsDefinition]:
        """
        Gets a list of all the settingsDefinitions used by this datatype.
        @return a list of the settingsDefinitions used by this datatype.
        """
        ...

    def getSourceArchive(self) -> ghidra.program.model.data.SourceArchive: ...

    def getUniversalID(self) -> ghidra.util.UniversalID: ...

    def getValue(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, len: int) -> object: ...

    def getValueClass(self, settings: ghidra.docking.settings.Settings) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def isDeleted(self) -> bool: ...

    def isDynamicallySized(self) -> bool: ...

    def isEquivalent(self, dt: ghidra.program.model.data.DataType) -> bool: ...

    def isNotYetDefined(self) -> bool: ...

    def newPointer(self, dt: ghidra.program.model.data.DataType) -> ghidra.program.model.data.Pointer: ...

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
    def categoryPath(self) -> ghidra.program.model.data.CategoryPath: ...

    @categoryPath.setter
    def categoryPath(self, value: ghidra.program.model.data.CategoryPath) -> None: ...

    @property
    def dataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def defaultLabelPrefix(self) -> unicode: ...

    @property
    def deleted(self) -> bool: ...

    @property
    def description(self) -> unicode: ...

    @description.setter
    def description(self, value: unicode) -> None: ...

    @property
    def displayName(self) -> unicode: ...

    @property
    def dynamicallySized(self) -> bool: ...

    @property
    def length(self) -> int: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...
