from typing import List
import ghidra.docking.settings
import ghidra.program.model.data
import ghidra.program.model.mem
import ghidra.util
import java.lang
import java.net
import java.util
import java.util.function


class Structure(ghidra.program.model.data.Composite, object):
    """
    The structure interface.

     NOTE: Structures containing only a flexible array will report a length of 1 which will result in
     improper code unit sizing since we are unable to support a defined data of length 0.

     NOTE: The use of zero-length bitfields within unaligned structures is discouraged since they have
     no real affect and are easily misplaced. Their use should be reserved for aligned/packed
     structures.
    """

    CONFLICT_SUFFIX: unicode = u'.conflict'
    DEFAULT: ghidra.program.model.data.DataType = undefined
    DEFAULT_ALIGNMENT_VALUE: int = 0
    NOT_PACKING: int = 0
    NO_LAST_CHANGE_TIME: long = 0x0L
    NO_SOURCE_SYNC_TIME: long = 0x0L
    VOID: ghidra.program.model.data.DataType = void




    class OffsetComparator(object, java.util.Comparator):




        def __init__(self): ...



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

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

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






    class BitOffsetComparator(object, java.util.Comparator):




        def __init__(self, __a0: bool): ...



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

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        @staticmethod
        def getNormalizedBitfieldOffset(__a0: int, __a1: int, __a2: int, __a3: int, __a4: bool) -> int: ...

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






    class OrdinalComparator(object, java.util.Comparator):




        def __init__(self): ...



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

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

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







    @overload
    def add(self, __a0: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataTypeComponent: ...

    @overload
    def add(self, __a0: ghidra.program.model.data.DataType, __a1: int) -> ghidra.program.model.data.DataTypeComponent: ...

    @overload
    def add(self, __a0: ghidra.program.model.data.DataType, __a1: unicode, __a2: unicode) -> ghidra.program.model.data.DataTypeComponent: ...

    @overload
    def add(self, __a0: ghidra.program.model.data.DataType, __a1: int, __a2: unicode, __a3: unicode) -> ghidra.program.model.data.DataTypeComponent: ...

    def addBitField(self, __a0: ghidra.program.model.data.DataType, __a1: int, __a2: unicode, __a3: unicode) -> ghidra.program.model.data.DataTypeComponent: ...

    def addParent(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    def clearComponent(self, index: int) -> None:
        """
        Clears the defined component at the given component index. Clearing a component causes a
         defined component to be replaced with a number of undefined dataTypes to offset the removal
         of the defined dataType.
        @param index the index of the component to clear.
        @throws ArrayIndexOutOfBoundsException if component ordinal is out of bounds
        """
        ...

    def clearFlexibleArrayComponent(self) -> None:
        """
        Remove the optional trailing flexible array component associated with this structure.
        """
        ...

    def clone(self, dtm: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.Structure: ...

    def copy(self, __a0: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType: ...

    def dataTypeAlignmentChanged(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    def dataTypeDeleted(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    def dataTypeNameChanged(self, __a0: ghidra.program.model.data.DataType, __a1: unicode) -> None: ...

    def dataTypeReplaced(self, __a0: ghidra.program.model.data.DataType, __a1: ghidra.program.model.data.DataType) -> None: ...

    def dataTypeSizeChanged(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    @overload
    def delete(self, __a0: int) -> None: ...

    @overload
    def delete(self, __a0: List[int]) -> None: ...

    def deleteAll(self) -> None:
        """
        Remove all components from this structure (including flex-array), effectively setting the
         length to zero.
        """
        ...

    def deleteAtOffset(self, offset: int) -> None:
        """
        Deletes the component containing the specified offset in this structure. If the offset
         corresponds to a bit-field, all bit-fields whose base type group contains the offset will be
         removed.
        @param offset the byte offset into the structure where the datatype is to be deleted.
        """
        ...

    def dependsOn(self, __a0: ghidra.program.model.data.DataType) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getAlignment(self) -> int: ...

    def getBitFieldPacking(self) -> ghidra.program.model.data.BitFieldPacking: ...

    def getCategoryPath(self) -> ghidra.program.model.data.CategoryPath: ...

    def getClass(self) -> java.lang.Class: ...

    def getComponent(self, ordinal: int) -> ghidra.program.model.data.DataTypeComponent:
        """
        Returns the component of this structure with the indicated ordinal. If the specified ordinal
         equals {@link #getNumComponents()} the defined flexible array component will be returned,
         otherwise an out of bounds exception will be thrown. Use of
         {@link #getFlexibleArrayComponent()} is preferred for obtaining this special trailing
         component.
        @param ordinal the component's ordinal (zero based).
        @return the data type component.
        @throws ArrayIndexOutOfBoundsException if the ordinal is out of bounds
        """
        ...

    def getComponentAt(self, offset: int) -> ghidra.program.model.data.DataTypeComponent:
        """
        Gets the immediate child component that contains the byte at the given offset. If the
         specified offset corresponds to a bit-field,the first bit-field component containing the
         offset will be returned.
        @param offset the byte offset into this data type
        @return the immediate child component.
        """
        ...

    def getComponents(self) -> List[ghidra.program.model.data.DataTypeComponent]: ...

    def getDataOrganization(self) -> ghidra.program.model.data.DataOrganization: ...

    def getDataTypeAt(self, offset: int) -> ghidra.program.model.data.DataTypeComponent:
        """
        Returns the primitive Data Type that is at this offset. This is useful for prototypes that
         have components that are made up of other components If the specified offset corresponds to a
         bit-field,the BitFieldDataType of the first bit-field component containing the offset will be
         returned.
        @param offset the byte offset into this data type.
        @return the primitive data type at the offset.
        """
        ...

    def getDataTypeManager(self) -> ghidra.program.model.data.DataTypeManager: ...

    def getDataTypePath(self) -> ghidra.program.model.data.DataTypePath: ...

    def getDefaultAbbreviatedLabelPrefix(self) -> unicode: ...

    @overload
    def getDefaultLabelPrefix(self) -> unicode: ...

    @overload
    def getDefaultLabelPrefix(self, __a0: ghidra.program.model.mem.MemBuffer, __a1: ghidra.docking.settings.Settings, __a2: int, __a3: ghidra.program.model.data.DataTypeDisplayOptions) -> unicode: ...

    def getDefaultOffcutLabelPrefix(self, __a0: ghidra.program.model.mem.MemBuffer, __a1: ghidra.docking.settings.Settings, __a2: int, __a3: ghidra.program.model.data.DataTypeDisplayOptions, __a4: int) -> unicode: ...

    def getDefaultSettings(self) -> ghidra.docking.settings.Settings: ...

    def getDefinedComponents(self) -> List[ghidra.program.model.data.DataTypeComponent]: ...

    def getDescription(self) -> unicode: ...

    def getDisplayName(self) -> unicode: ...

    def getDocs(self) -> java.net.URL: ...

    def getFlexibleArrayComponent(self) -> ghidra.program.model.data.DataTypeComponent:
        """
        Get the optional trailing flexible array component associated with this structure.
        @return optional trailing flexible array component associated with this structure or null if
                 not present.
        """
        ...

    def getLastChangeTime(self) -> long: ...

    def getLastChangeTimeInSourceArchive(self) -> long: ...

    def getLength(self) -> int: ...

    def getMinimumAlignment(self) -> int: ...

    def getMnemonic(self, __a0: ghidra.docking.settings.Settings) -> unicode: ...

    def getName(self) -> unicode: ...

    def getNumComponents(self) -> int: ...

    def getNumDefinedComponents(self) -> int: ...

    def getPackingValue(self) -> int: ...

    def getParents(self) -> List[ghidra.program.model.data.DataType]: ...

    def getPathName(self) -> unicode: ...

    def getRepresentation(self, __a0: ghidra.program.model.mem.MemBuffer, __a1: ghidra.docking.settings.Settings, __a2: int) -> unicode: ...

    def getSettingsDefinitions(self) -> List[ghidra.docking.settings.SettingsDefinition]: ...

    def getSourceArchive(self) -> ghidra.program.model.data.SourceArchive: ...

    def getUniversalID(self) -> ghidra.util.UniversalID: ...

    def getValue(self, __a0: ghidra.program.model.mem.MemBuffer, __a1: ghidra.docking.settings.Settings, __a2: int) -> object: ...

    def getValueClass(self, __a0: ghidra.docking.settings.Settings) -> java.lang.Class: ...

    def growStructure(self, amount: int) -> None:
        """
        Increases the size of the structure by the given amount by adding undefined datatypes at the
         end of the structure.
        @param amount the amount by which to grow the structure.
        @throws IllegalArgumentException if amount &lt; 1
        """
        ...

    def hasFlexibleArrayComponent(self) -> bool:
        """
        Determine if a trailing flexible array component has been defined.
        @return true if trailing flexible array component has been defined.
        """
        ...

    def hashCode(self) -> int: ...

    @overload
    def insert(self, __a0: int, __a1: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataTypeComponent: ...

    @overload
    def insert(self, __a0: int, __a1: ghidra.program.model.data.DataType, __a2: int) -> ghidra.program.model.data.DataTypeComponent: ...

    @overload
    def insert(self, __a0: int, __a1: ghidra.program.model.data.DataType, __a2: int, __a3: unicode, __a4: unicode) -> ghidra.program.model.data.DataTypeComponent: ...

    @overload
    def insertAtOffset(self, offset: int, dataType: ghidra.program.model.data.DataType, length: int) -> ghidra.program.model.data.DataTypeComponent:
        """
        Inserts a new datatype at the specified offset into this structure. Inserting a component
         will causing any conflicting component to shift down to the extent necessary to avoid a
         conflict.
        @param offset the byte offset into the structure where the new datatype is to be inserted.
        @param dataType the datatype to insert.
        @param length the length to associate with the dataType. For fixed length types a length
                    &lt;= 0 will use the length of the resolved dataType.
        @return the componentDataType created.
        @throws IllegalArgumentException if the specified data type is not allowed to be inserted
                     into this composite data type or an invalid length is specified. For example,
                     suppose dt1 contains dt2. Therefore it is not valid to insert dt1 to dt2 since
                     this would cause a cyclic dependency.
        """
        ...

    @overload
    def insertAtOffset(self, offset: int, dataType: ghidra.program.model.data.DataType, length: int, name: unicode, comment: unicode) -> ghidra.program.model.data.DataTypeComponent:
        """
        Inserts a new datatype at the specified offset into this structure. Inserting a component
         will causing any conflicting component to shift down to the extent necessary to avoid a
         conflict.
        @param offset the byte offset into the structure where the new datatype is to be inserted.
        @param dataType the datatype to insert.
        @param length the length to associate with the dataType. For fixed length types a length
                    &lt;= 0 will use the length of the resolved dataType.
        @param name the field name to associate with this component.
        @param comment the comment to associate with this component.
        @return the componentDataType created.
        @throws IllegalArgumentException if the specified data type is not allowed to be inserted
                     into this composite data type or an invalid length is specified. For example,
                     suppose dt1 contains dt2. Therefore it is not valid to insert dt1 to dt2 since
                     this would cause a cyclic dependency.
        """
        ...

    def insertBitField(self, ordinal: int, byteWidth: int, bitOffset: int, baseDataType: ghidra.program.model.data.DataType, bitSize: int, componentName: unicode, comment: unicode) -> ghidra.program.model.data.DataTypeComponent:
        """
        Inserts a new bitfield at the specified ordinal position in this structure. Within aligned
         structures the specified byteWidth and bitOffset will be ignored since packing will occur at
         the specified ordinal position. The resulting component length and bitfield details will
         reflect the use of minimal storage sizing.
         <p>
         For unaligned structures, a component shift will only occur if the bitfield placement
         conflicts with another component. If no conflict occurs, the bitfield will be placed at the
         specified location consuming any DEFAULT components as needed. When a conflict does occur a
         shift will be performed at the ordinal position based upon the specified byteWidth. When
         located onto existing bitfields they will be packed together provided they do not conflict,
         otherwise the conflict rule above applies.
         <p>
         Supported aligned packing starts with bit-0 (lsb) of the first byte for little-endian, and
         with bit-7 (msb) of the first byte for big-endian. This is the default behavior for most
         compilers. Insertion behavior may not work as expected if packing rules differ from this.
        @param ordinal the ordinal where the new datatype is to be inserted.
        @param byteWidth the storage allocation unit width which contains the bitfield. Must be large
                    enough to contain the "effective bit size" and corresponding bitOffset. The actual
                    component size used will be recomputed during insertion.
        @param bitOffset corresponds to the bitfield left-shift amount with the storage unit when
                    viewed as big-endian. The final offset may be reduced based upon the minimal
                    storage size determined during insertion.
        @param baseDataType the bitfield base datatype (certain restrictions apply).
        @param bitSize the declared bitfield size in bits. The effective bit size may be adjusted
                    based upon the specified baseDataType.
        @param componentName the field name to associate with this component.
        @param comment the comment to associate with this component.
        @return the bitfield component created whose associated data type will be BitFieldDataType.
        @throws InvalidDataTypeException if the specified baseDataType is not a valid base type for
                     bitfields.
        @throws ArrayIndexOutOfBoundsException if ordinal is less than 0 or greater than the current
                     number of components.
        """
        ...

    def insertBitFieldAt(self, byteOffset: int, byteWidth: int, bitOffset: int, baseDataType: ghidra.program.model.data.DataType, bitSize: int, componentName: unicode, comment: unicode) -> ghidra.program.model.data.DataTypeComponent:
        """
        Inserts a new bitfield at the specified location in this composite. This method is intended
         to be used with unaligned structures where the bitfield will be precisely placed. Within an
         aligned structure the specified byteOffset, byteWidth and bitOffset will be used to identify
         the appropriate ordinal but may not be preserved. The component length will be computed based
         upon the specified parameters and will be reduced from byteWidth to its minimal size for the
         new component.
         <p>
         For unaligned mode, a component shift will only occur if the bitfield placement conflicts
         with another component. If no conflict occurs, the bitfield will be placed at the specified
         location consuming any DEFAULT components as needed. When a conflict does occur a shift will
         be performed at the point of conflict based upon the specified byteWidth. When located onto
         existing bitfields they will be packed together provided they do not conflict, otherwise the
         conflict rule above applies.
         <p>
         Supported packing for little-endian fills lsb first, whereas big-endian fills msb first.
         Insertion behavior may not work as expected if packing rules differ from this.
         <p>

         Zero length bitfields may be inserted although they have no real affect for unaligned
         structures. Only the resulting byte offset within the structure is of significance in
         determining its ordinal placement.
         <p>
        @param byteOffset the first byte offset within this structure which corresponds to the first
                    byte of the specified storage unit identified by its byteWidth.
        @param byteWidth the storage unit width which contains the bitfield. Must be large enough to
                    contain the specified bitSize and corresponding bitOffset. The actual component
                    size used will be recomputed during insertion.
        @param bitOffset corresponds to the bitfield left-shift amount with the storage unit when
                    viewed as big-endian. The final offset may be reduced based upon the minimal
                    storage size determined during insertion.
        @param baseDataType the bitfield base datatype (certain restrictions apply).
        @param componentName the field name to associate with this component.
        @param bitSize the bitfield size in bits. A bitSize of 0 may be specified although its name
                    will be ignored.
        @param comment the comment to associate with this component.
        @return the componentDataType created whose associated data type will be BitFieldDataType.
        @throws InvalidDataTypeException if the specified data type is not a valid base type for
                     bitfields.
        """
        ...

    def isDefaultAligned(self) -> bool: ...

    def isDeleted(self) -> bool: ...

    def isDynamicallySized(self) -> bool: ...

    def isEquivalent(self, __a0: ghidra.program.model.data.DataType) -> bool: ...

    def isInternallyAligned(self) -> bool: ...

    def isMachineAligned(self) -> bool: ...

    def isNotYetDefined(self) -> bool: ...

    def isPartOf(self, __a0: ghidra.program.model.data.DataType) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def pack(self, maxAlignment: int) -> None:
        """
        Sets the current packing value (usually a power of 2). A value of NOT_PACKING should be
         passed if this isn't a packed data type. Otherwise this value indicates a maximum alignment
         for any component within this data type. Calling this method will cause the data type to
         become an internally aligned data type. (Same as {@link Composite#setPackingValue(int)})
        @param maxAlignment the new packing value or 0 for NOT_PACKING. A negative value will be
                    treated the same as 0.
        """
        ...

    def realign(self) -> None: ...

    def removeParent(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    @overload
    def replace(self, index: int, dataType: ghidra.program.model.data.DataType, length: int) -> ghidra.program.model.data.DataTypeComponent:
        """
        Replaces the component at the given component index with a new component of the indicated
         data type.
        @param index the index where the datatype is to be replaced.
        @param dataType the datatype to insert.
        @param length the length of the dataType to insert. For fixed length types a length &lt;= 0
                    will use the length of the resolved dataType.
        @return the new componentDataType at the index.
        @throws IllegalArgumentException if the specified data type is not allowed to replace a
                     component in this composite data type or an invalid length is specified. For
                     example, suppose dt1 contains dt2. Therefore it is not valid to replace a dt2
                     component with dt1 since this would cause a cyclic dependency. In addition, any
                     attempt to replace an existing bit-field component or specify a
                     {@link BitFieldDataType} will produce this error.
        @throws ArrayIndexOutOfBoundsException if component index is out of bounds
        """
        ...

    @overload
    def replace(self, index: int, dataType: ghidra.program.model.data.DataType, length: int, name: unicode, comment: unicode) -> ghidra.program.model.data.DataTypeComponent:
        """
        Replaces the component at the given component index with a new component of the indicated
         data type.
        @param index the index where the datatype is to be replaced.
        @param dataType the datatype to insert.
        @param length the length to associate with the dataType. For fixed length types a length
                    &lt;= 0 will use the length of the resolved dataType.
        @param name the field name to associate with this component.
        @param comment the comment to associate with this component.
        @return the new componentDataType at the index.
        @throws IllegalArgumentException if the specified data type is not allowed to replace a
                     component in this composite data type or an invalid length is specified. For
                     example, suppose dt1 contains dt2. Therefore it is not valid to replace a dt2
                     component with dt1 since this would cause a cyclic dependency. In addition, any
                     attempt to replace an existing bit-field component or specify a
                     {@link BitFieldDataType} will produce this error.
        @throws ArrayIndexOutOfBoundsException if component index is out of bounds
        """
        ...

    def replaceAtOffset(self, offset: int, dataType: ghidra.program.model.data.DataType, length: int, name: unicode, comment: unicode) -> ghidra.program.model.data.DataTypeComponent:
        """
        Replaces the component at the specified byte offset with a new component of the indicated
         data type. If the offset corresponds to a bit-field, all bit-fields at that offset will be
         removed and replaced by the specified component. Keep in mind bit-field or any component
         removal must clear sufficient space for an unaligned structure to complete the replacement.
        @param offset the byte offset into the structure where the datatype is to be replaced.
        @param dataType the datatype to insert.
        @param length the length to associate with the dataType. For fixed length types a length
                    &lt;= 0 will use the length of the resolved dataType.
        @param name the field name to associate with this component.
        @param comment the comment to associate with this component.
        @return the new componentDataType at the index.
        @throws IllegalArgumentException if the specified data type is not allowed to replace a
                     component in this composite data type or an invalid length is specified. For
                     example, suppose dt1 contains dt2. Therefore it is not valid to replace a dt2
                     component with dt1 since this would cause a cyclic dependency. In addition, any
                     attempt to replace an existing bit-field component or specify a
                     {@link BitFieldDataType} will produce this error.
        """
        ...

    def replaceWith(self, __a0: ghidra.program.model.data.DataType) -> None: ...

    def setCategoryPath(self, __a0: ghidra.program.model.data.CategoryPath) -> None: ...

    def setDefaultSettings(self, __a0: ghidra.docking.settings.Settings) -> None: ...

    def setDescription(self, __a0: unicode) -> None: ...

    def setFlexibleArrayComponent(self, flexType: ghidra.program.model.data.DataType, name: unicode, comment: unicode) -> ghidra.program.model.data.DataTypeComponent:
        """
        Set the optional trailing flexible array component associated with this structure.
        @param flexType the flexible array dataType (example: for 'char[0]' the type 'char' should be
                    specified)
        @param name component field name or null for default name
        @param comment component comment
        @return updated flexible array component
        @throws IllegalArgumentException if specified flexType is not permitted (e.g., self
                     referencing or unsupported type)
        """
        ...

    def setInternallyAligned(self, __a0: bool) -> None: ...

    def setLastChangeTime(self, __a0: long) -> None: ...

    def setLastChangeTimeInSourceArchive(self, __a0: long) -> None: ...

    def setMinimumAlignment(self, __a0: int) -> None: ...

    def setName(self, __a0: unicode) -> None: ...

    def setNameAndCategory(self, __a0: ghidra.program.model.data.CategoryPath, __a1: unicode) -> None: ...

    def setPackingValue(self, __a0: int) -> None: ...

    def setSourceArchive(self, __a0: ghidra.program.model.data.SourceArchive) -> None: ...

    def setToDefaultAlignment(self) -> None: ...

    def setToMachineAlignment(self) -> None: ...

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
    def flexibleArrayComponent(self) -> ghidra.program.model.data.DataTypeComponent: ...

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
