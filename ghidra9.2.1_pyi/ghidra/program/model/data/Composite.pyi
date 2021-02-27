from typing import List
import ghidra.docking.settings
import ghidra.program.model.data
import ghidra.program.model.mem
import ghidra.util
import java.lang
import java.net


class Composite(ghidra.program.model.data.DataType, object):
    """
    Interface for common methods in Structure and Union
    """

    CONFLICT_SUFFIX: unicode = u'.conflict'
    DEFAULT: ghidra.program.model.data.DataType = undefined
    DEFAULT_ALIGNMENT_VALUE: int = 0
    NOT_PACKING: int = 0
    NO_LAST_CHANGE_TIME: long = 0x0L
    NO_SOURCE_SYNC_TIME: long = 0x0L
    VOID: ghidra.program.model.data.DataType = void




    class NamedAlignment(object):








        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getName(self) -> unicode: ...

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
        def name(self) -> unicode: ...




    class AlignmentType(java.lang.Enum, ghidra.program.model.data.Composite.NamedAlignment):
        ALIGNED_BY_VALUE: ghidra.program.model.data.Composite.AlignmentType = Align By Value
        DEFAULT_ALIGNED: ghidra.program.model.data.Composite.AlignmentType = Default Aligned
        MACHINE_ALIGNED: ghidra.program.model.data.Composite.AlignmentType = Machine Aligned







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def getName(self) -> unicode: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.program.model.data.Composite.AlignmentType: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.program.model.data.Composite.AlignmentType]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...







    @overload
    def add(self, dataType: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataTypeComponent:
        """
        Adds a new datatype to the end of this composite.  This is the preferred method
         to use for adding components to an aligned structure for fixed-length dataTypes.
        @param dataType the datatype to add.
        @return the DataTypeComponent created.
        @throws IllegalArgumentException if the specified data type is not
         allowed to be added to this composite data type.
         For example, suppose dt1 contains dt2. Therefore it is not valid
         to add dt1 to dt2 since this would cause a cyclic dependency.
        """
        ...

    @overload
    def add(self, dataType: ghidra.program.model.data.DataType, length: int) -> ghidra.program.model.data.DataTypeComponent:
        """
        Adds a new datatype to the end of this composite. This is the preferred method
         to use for adding components to an aligned structure for dynamic dataTypes such as
         strings whose length must be specified.
        @param dataType the datatype to add.
        @param length the length to associate with the datatype.
         For fixed length types a length &lt;= 0 will use the length of the resolved dataType.
        @return the componentDataType created.
        @throws IllegalArgumentException if the specified data type is not
         allowed to be added to this composite data type or an invalid length
         is specified.
         For example, suppose dt1 contains dt2. Therefore it is not valid
         to add dt1 to dt2 since this would cause a cyclic dependency.
        """
        ...

    @overload
    def add(self, dataType: ghidra.program.model.data.DataType, name: unicode, comment: unicode) -> ghidra.program.model.data.DataTypeComponent:
        """
        Adds a new datatype to the end of this composite.  This is the preferred method
         to use for adding components to an aligned structure for fixed-length dataTypes.
        @param dataType the datatype to add.
        @param name the field name to associate with this component.
        @param comment the comment to associate with this component.
        @return the componentDataType created.
        @throws IllegalArgumentException if the specified data type is not
         allowed to be added to this composite data type.
         For example, suppose dt1 contains dt2. Therefore it is not valid
         to add dt1 to dt2 since this would cause a cyclic dependency.
        """
        ...

    @overload
    def add(self, dataType: ghidra.program.model.data.DataType, length: int, name: unicode, comment: unicode) -> ghidra.program.model.data.DataTypeComponent:
        """
        Adds a new datatype to the end of this composite.  This is the preferred method
         to use for adding components to an aligned structure for dynamic dataTypes such as
         strings whose length must be specified.
        @param dataType the datatype to add.
        @param length the length to associate with the datatype.
         For fixed length types a length &lt;= 0 will use the length of the resolved dataType.
        @param name the field name to associate with this component.
        @param comment the comment to associate with this component.
        @return the componentDataType created.
        @throws IllegalArgumentException if the specified data type is not
         allowed to be added to this composite data type or an invalid length is specified.
         For example, suppose dt1 contains dt2. Therefore it is not valid
         to add dt1 to dt2 since this would cause a cyclic dependency.
        """
        ...

    def addBitField(self, baseDataType: ghidra.program.model.data.DataType, bitSize: int, componentName: unicode, comment: unicode) -> ghidra.program.model.data.DataTypeComponent:
        """
        Adds a new bitfield to the end of this composite.  This method is intended
         to be used with aligned structures/unions only where the bitfield will be
         appropriately packed.  The minimum storage storage byte size will be applied.
         It will not provide useful results within unaligned composites.
        @param baseDataType the bitfield base datatype (certain restrictions apply).
        @param bitSize the bitfield size in bits
        @param componentName the field name to associate with this component.
        @param comment the comment to associate with this component.
        @return the componentDataType created whose associated data type will
         be BitFieldDataType.
        @throws InvalidDataTypeException if the specified data type is
         not a valid base type for bitfields.
        """
        ...

    def addParent(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    def clone(self, __a0: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType: ...

    def copy(self, __a0: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType: ...

    def dataTypeAlignmentChanged(self, dt: ghidra.program.model.data.DataType) -> None:
        """
        The overall (external) alignment changed for the specified data type.
         In other words, the data type has a different alignment when placed inside other structures.
        @param dt the data type whose alignment changed.
        """
        ...

    def dataTypeDeleted(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    def dataTypeNameChanged(self, __a0: ghidra.program.model.data.DataType, __a1: unicode) -> None: ...

    def dataTypeReplaced(self, __a0: ghidra.program.model.data.DataType, __a1: ghidra.program.model.data.DataType) -> None: ...

    def dataTypeSizeChanged(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    @overload
    def delete(self, ordinal: int) -> None:
        """
        Deletes the component at the given ordinal position.
         <BR>Note: Removal of bitfields from an unaligned structure will
         not shift other components with vacated bytes reverting to undefined.
        @param ordinal the ordinal of the component to be deleted.
        @throws ArrayIndexOutOfBoundsException if component ordinal is out of bounds
        """
        ...

    @overload
    def delete(self, ordinals: List[int]) -> None:
        """
        Deletes the components at the given ordinal positions.
         <BR>Note: Removal of bitfields from an unaligned structure will
         not shift other components with vacated bytes reverting to undefined.
        @param ordinals the ordinals of the component to be deleted.
        @throws ArrayIndexOutOfBoundsException if any specified component ordinal is out of bounds
        """
        ...

    def dependsOn(self, __a0: ghidra.program.model.data.DataType) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getAlignment(self) -> int: ...

    def getBitFieldPacking(self) -> ghidra.program.model.data.BitFieldPacking:
        """
        Get the bitfield packing information associated with the underlying
         data organization.
        @return bitfield packing information
        """
        ...

    def getCategoryPath(self) -> ghidra.program.model.data.CategoryPath: ...

    def getClass(self) -> java.lang.Class: ...

    def getComponent(self, ordinal: int) -> ghidra.program.model.data.DataTypeComponent:
        """
        Returns the component of this data type with the indicated ordinal.
        @param ordinal the component's ordinal (zero based).
        @return the data type component.
        @throws ArrayIndexOutOfBoundsException if the ordinal is out of bounds
        """
        ...

    def getComponents(self) -> List[ghidra.program.model.data.DataTypeComponent]:
        """
        Returns an array of Data Type Components that make up this composite including
         undefined filler components which may be present within an unaligned structure.
         The number of components corresponds to {@link #getNumComponents()}.
        @return list all components
        """
        ...

    def getDataOrganization(self) -> ghidra.program.model.data.DataOrganization: ...

    def getDataTypeManager(self) -> ghidra.program.model.data.DataTypeManager: ...

    def getDataTypePath(self) -> ghidra.program.model.data.DataTypePath: ...

    def getDefaultAbbreviatedLabelPrefix(self) -> unicode: ...

    @overload
    def getDefaultLabelPrefix(self) -> unicode: ...

    @overload
    def getDefaultLabelPrefix(self, __a0: ghidra.program.model.mem.MemBuffer, __a1: ghidra.docking.settings.Settings, __a2: int, __a3: ghidra.program.model.data.DataTypeDisplayOptions) -> unicode: ...

    def getDefaultOffcutLabelPrefix(self, __a0: ghidra.program.model.mem.MemBuffer, __a1: ghidra.docking.settings.Settings, __a2: int, __a3: ghidra.program.model.data.DataTypeDisplayOptions, __a4: int) -> unicode: ...

    def getDefaultSettings(self) -> ghidra.docking.settings.Settings: ...

    def getDefinedComponents(self) -> List[ghidra.program.model.data.DataTypeComponent]:
        """
        Returns an array of Data Type Components that make up this composite excluding
         undefined filler components which may be present within an unaligned structure.
         The number of components corresponds to {@link #getNumComponents()}.  For Unions and
         aligned Structures this is equivalent to {@link #getComponents()}
         since they do not contain undefined components.  Structures do not include the
         optional trailing flexible array component in this list
         (see {@link Structure#getFlexibleArrayComponent()}).
        @return list all explicitly defined components
        """
        ...

    def getDescription(self) -> unicode: ...

    def getDisplayName(self) -> unicode: ...

    def getDocs(self) -> java.net.URL: ...

    def getLastChangeTime(self) -> long: ...

    def getLastChangeTimeInSourceArchive(self) -> long: ...

    def getLength(self) -> int: ...

    def getMinimumAlignment(self) -> int:
        """
        Get the external alignment (a minimum alignment) for this DataType.
         This controls where this data type will get aligned within other data types.
         It also causes the end of this data type to get padded so its length is a multiple
         of the alignment.
        @return the external alignment for this DataType or DEFAULT_ALIGNMENT_VALUE.
        """
        ...

    def getMnemonic(self, __a0: ghidra.docking.settings.Settings) -> unicode: ...

    def getName(self) -> unicode: ...

    def getNumComponents(self) -> int:
        """
        Gets the number of component data types in this composite.
         The count will include all undefined filler components which may be present
         within an unaligned structure.  Structures do not include the
         optional trailing flexible array component in this count
         (see {@link Structure#hasFlexibleArrayComponent()}).
        @return the number of components that make up this composite
        """
        ...

    def getNumDefinedComponents(self) -> int:
        """
        Returns the number of explicitly defined components in this composite.
         For Unions and aligned Structures this is equivalent to {@link #getNumComponents()}
         since they do not contain undefined components.  The count will exclude all undefined
         filler components which may be present within an unaligned structure.
        @return the number of explicitly defined components in this composite
        """
        ...

    def getPackingValue(self) -> int:
        """
        Gets the current packing value (typically a power of 2). If this isn't a packed data
         type then NOT_PACKING is returned. The packing value only pertains to internally aligned composite
         data types. Aligned structures allow packing.
        @return the current packing value or NOT_PACKING.
        """
        ...

    def getParents(self) -> List[ghidra.program.model.data.DataType]: ...

    def getPathName(self) -> unicode: ...

    def getRepresentation(self, __a0: ghidra.program.model.mem.MemBuffer, __a1: ghidra.docking.settings.Settings, __a2: int) -> unicode: ...

    def getSettingsDefinitions(self) -> List[ghidra.docking.settings.SettingsDefinition]: ...

    def getSourceArchive(self) -> ghidra.program.model.data.SourceArchive: ...

    def getUniversalID(self) -> ghidra.util.UniversalID: ...

    def getValue(self, __a0: ghidra.program.model.mem.MemBuffer, __a1: ghidra.docking.settings.Settings, __a2: int) -> object: ...

    def getValueClass(self, __a0: ghidra.docking.settings.Settings) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @overload
    def insert(self, ordinal: int, dataType: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataTypeComponent:
        """
        Inserts a new datatype at the specified ordinal position in this composite.
         <BR>Note: For an aligned structure the ordinal position will get adjusted
         automatically to provide the proper alignment.
        @param ordinal the ordinal where the new datatype is to be inserted.
        @param dataType the datatype to insert.
        @return the componentDataType created.
        @throws IllegalArgumentException if the specified data type is not
         allowed to be inserted into this composite data type.
         For example, suppose dt1 contains dt2. Therefore it is not valid
         to insert dt1 to dt2 since this would cause a cyclic dependency.
        @throws ArrayIndexOutOfBoundsException if component ordinal is out of bounds
        """
        ...

    @overload
    def insert(self, ordinal: int, dataType: ghidra.program.model.data.DataType, length: int) -> ghidra.program.model.data.DataTypeComponent:
        """
        Inserts a new datatype at the specified ordinal position in this composite.
         <BR>Note: For an aligned structure the ordinal position will get adjusted
         automatically to provide the proper alignment.
        @param ordinal the ordinal where the new datatype is to be inserted.
        @param dataType the datatype to insert.
        @param length the length to associate with the datatype.
         For fixed length types a length &lt;= 0 will use the length of the resolved dataType.
        @return the componentDataType created.
        @throws IllegalArgumentException if the specified data type is not
         allowed to be inserted into this composite data type or an invalid
         length is specified.
         For example, suppose dt1 contains dt2. Therefore it is not valid
         to insert dt1 to dt2 since this would cause a cyclic dependency.
        @throws ArrayIndexOutOfBoundsException if component ordinal is out of bounds
        """
        ...

    @overload
    def insert(self, ordinal: int, dataType: ghidra.program.model.data.DataType, length: int, name: unicode, comment: unicode) -> ghidra.program.model.data.DataTypeComponent:
        """
        Inserts a new datatype at the specified ordinal position in this composite.
         <BR>Note: For an aligned structure the ordinal position will get adjusted
         automatically to provide the proper alignment.
        @param ordinal the ordinal where the new datatype is to be inserted.
        @param dataType the datatype to insert.
        @param length the length to associate with the datatype.
         For fixed length types a length &lt;= 0 will use the length of the resolved dataType.
        @param name the field name to associate with this component.
        @param comment the comment to associate with this component.
        @return the componentDataType created.
        @throws IllegalArgumentException if the specified data type is not
         allowed to be inserted into this composite data type or an invalid length
         is specified.
         For example, suppose dt1 contains dt2. Therefore it is not valid
         to insert dt1 to dt2 since this would cause a cyclic dependency.
        @throws ArrayIndexOutOfBoundsException if component ordinal is out of bounds
        """
        ...

    def isDefaultAligned(self) -> bool:
        """
        Whether or not this data type is using the default external (minimum) alignment.
        @return true if this data type has the default external alignment.
        """
        ...

    def isDeleted(self) -> bool: ...

    def isDynamicallySized(self) -> bool: ...

    def isEquivalent(self, __a0: ghidra.program.model.data.DataType) -> bool: ...

    def isInternallyAligned(self) -> bool:
        """
        Determine if this data type has its internal components currently aligned.
        @return true if this data type's components are aligned relative to each other using the
         current data organization. When internally aligned the end of this data type will be padded
         to a multiple of its actual alignment.
        """
        ...

    def isMachineAligned(self) -> bool:
        """
        Whether or not this data type is using the machine alignment value from the
         DataOrganization for its external (minimum) alignment.
        @return true if this data type is using the machine alignment as the minimum alignment.
        """
        ...

    def isNotYetDefined(self) -> bool: ...

    def isPartOf(self, dataType: ghidra.program.model.data.DataType) -> bool:
        """
        Check if a data type is part of this data type.  A data type could
         be part of another by:
         <br>Being the same data type.
         <br>containing the data type directly
         <br>containing another data type that has the data type as a part of it.
        @param dataType the data type to look for.
        @return true if the indicated data type is part of a sub-component of
         this data type.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def realign(self) -> None:
        """
        Updates the composite to any changes in the data organization. If the composite is not
         internally aligned, this method does nothing.
        """
        ...

    def removeParent(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    def replaceWith(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    def setCategoryPath(self, __a0: ghidra.program.model.data.CategoryPath) -> None: ...

    def setDefaultSettings(self, __a0: ghidra.docking.settings.Settings) -> None: ...

    def setDescription(self, desc: unicode) -> None:
        """
        Sets the string describing this data type.
        @param desc the new description.
        """
        ...

    def setInternallyAligned(self, aligned: bool) -> None:
        """
        Sets whether this data type's internal components are currently aligned or unaligned.
        @param aligned true means align the internal components of this data type.
         false means don't align it. True also causes the end of this data type to be padded
         to a multiple of its actual alignment.
        """
        ...

    def setLastChangeTime(self, __a0: long) -> None: ...

    def setLastChangeTimeInSourceArchive(self, __a0: long) -> None: ...

    def setMinimumAlignment(self, minimumAlignment: int) -> None:
        """
        Sets the external alignment (a minimum alignment) for this DataType.
         This controls where this data type will get aligned within other data types.
         It also causes the end of this data type to get padded so its length is a multiple
         of the alignment. Calling this method will cause the data type to
         become an internally aligned data type.
        @param minimumAlignment the external (minimum) alignment for this DataType.
         Any value less than 1 will revert to default alignment.
        """
        ...

    def setName(self, __a0: unicode) -> None: ...

    def setNameAndCategory(self, __a0: ghidra.program.model.data.CategoryPath, __a1: unicode) -> None: ...

    def setPackingValue(self, packingValue: int) -> None:
        """
        Sets the current packing value (usually a power of 2). A value of NOT_PACKING should be passed
         if this isn't a packed data type. Otherwise this value indicates a maximum alignment
         for any component within this data type. Calling this method will cause the data type to
         become an internally aligned data type.
         <br>Note: If a component's data type has a specific external alignment, it will
         override this value if necessary.
        @param packingValue the new packing value or 0 for NOT_PACKING.
         A negative value will be treated the same as 0.
        """
        ...

    def setSourceArchive(self, __a0: ghidra.program.model.data.SourceArchive) -> None: ...

    def setToDefaultAlignment(self) -> None:
        """
        Sets this data type's external (minimum) alignment to the default alignment. This data type's
         external alignment will be based upon the components it contains. This should be used
         when a data type doesn't have an alignment attribute specified. Calling this method will
         cause the data type to become an internally aligned data type.
        """
        ...

    def setToMachineAlignment(self) -> None:
        """
        Sets this data type's external (minimum) alignment to a multiple of the machine alignment that is
         specified in the DataOrganization. The machine alignment is defined as the maximum useful
         alignment for the target machine. This should be used when a data type has an alignment
         attribute specified without a size (indicating to use the machine alignment).
         Calling this method will cause the data type to become an internally aligned data type.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def alignment(self) -> int: ...

    @property
    def bitFieldPacking(self) -> ghidra.program.model.data.BitFieldPacking: ...

    @property
    def categoryPath(self) -> ghidra.program.model.data.CategoryPath: ...

    @categoryPath.setter
    def categoryPath(self, value: ghidra.program.model.data.CategoryPath) -> None: ...

    @property
    def components(self) -> List[ghidra.program.model.data.DataTypeComponent]: ...

    @property
    def dataOrganization(self) -> ghidra.program.model.data.DataOrganization: ...

    @property
    def dataTypeManager(self) -> ghidra.program.model.data.DataTypeManager: ...

    @property
    def dataTypePath(self) -> ghidra.program.model.data.DataTypePath: ...

    @property
    def defaultAbbreviatedLabelPrefix(self) -> unicode: ...

    @property
    def defaultAligned(self) -> bool: ...

    @property
    def defaultLabelPrefix(self) -> unicode: ...

    @property
    def defaultSettings(self) -> ghidra.docking.settings.Settings: ...

    @defaultSettings.setter
    def defaultSettings(self, value: ghidra.docking.settings.Settings) -> None: ...

    @property
    def definedComponents(self) -> List[ghidra.program.model.data.DataTypeComponent]: ...

    @property
    def deleted(self) -> bool: ...

    @property
    def description(self) -> unicode: ...

    @description.setter
    def description(self, value: unicode) -> None: ...

    @property
    def displayName(self) -> unicode: ...

    @property
    def docs(self) -> java.net.URL: ...

    @property
    def dynamicallySized(self) -> bool: ...

    @property
    def internallyAligned(self) -> bool: ...

    @internallyAligned.setter
    def internallyAligned(self, value: bool) -> None: ...

    @property
    def lastChangeTime(self) -> long: ...

    @lastChangeTime.setter
    def lastChangeTime(self, value: long) -> None: ...

    @property
    def lastChangeTimeInSourceArchive(self) -> long: ...

    @lastChangeTimeInSourceArchive.setter
    def lastChangeTimeInSourceArchive(self, value: long) -> None: ...

    @property
    def length(self) -> int: ...

    @property
    def machineAligned(self) -> bool: ...

    @property
    def minimumAlignment(self) -> int: ...

    @minimumAlignment.setter
    def minimumAlignment(self, value: int) -> None: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def notYetDefined(self) -> bool: ...

    @property
    def numComponents(self) -> int: ...

    @property
    def numDefinedComponents(self) -> int: ...

    @property
    def packingValue(self) -> int: ...

    @packingValue.setter
    def packingValue(self, value: int) -> None: ...

    @property
    def parents(self) -> List[ghidra.program.model.data.DataType]: ...

    @property
    def pathName(self) -> unicode: ...

    @property
    def settingsDefinitions(self) -> List[ghidra.docking.settings.SettingsDefinition]: ...

    @property
    def sourceArchive(self) -> ghidra.program.model.data.SourceArchive: ...

    @sourceArchive.setter
    def sourceArchive(self, value: ghidra.program.model.data.SourceArchive) -> None: ...

    @property
    def universalID(self) -> ghidra.util.UniversalID: ...
