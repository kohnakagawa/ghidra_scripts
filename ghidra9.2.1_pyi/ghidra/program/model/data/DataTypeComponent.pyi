import ghidra.docking.settings
import ghidra.program.model.data
import java.lang


class DataTypeComponent(object):
    """
    DataTypeComponents are holders for the dataTypes that make up composite (Structures
     and Unions) dataTypes.

     While most all components must have a fixed length greater than 0, structures support an
     optional trailing flexible array component whose length is zero and whose offset equals
     the length of the structure.
    """

    DEFAULT_FIELD_NAME_PREFIX: unicode = u'field'







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self) -> unicode:
        """
        Get the comment for this dataTypeComponent.
        """
        ...

    def getDataType(self) -> ghidra.program.model.data.DataType:
        """
        Returns the dataType in this component.
         <p>
         NOTE: If this component corresponds to a structure flexible array the returned data type
         reflects the base type of the array (e.g., char is returned for a flexible char array).
        @return the dataType in this component
        """
        ...

    def getDefaultFieldName(self) -> unicode:
        """
        Returns a default Field name.  Used only if a field name is not set.
        """
        ...

    def getDefaultSettings(self) -> ghidra.docking.settings.Settings:
        """
        Gets the default settings for this data type component.
        @return a Settings object that is the set of default values for this dataType component
        """
        ...

    def getEndOffset(self) -> int:
        """
        Get the byte offset of where this component ends relative to the start of the parent
         data type.
         <p>
         NOTE: The special case of a structure flexible array component returns -1 since its
         length is undefined.
        @return offset of end of component relative to the start of the parent
         data type.
        """
        ...

    def getFieldName(self) -> unicode:
        """
        Get the name of the field name as a component of a Data Type.
        @return the name as a component of another Data Type.
        """
        ...

    def getLength(self) -> int:
        """
        Get the length of this component.
         <p>
         NOTE: The special case of a structure flexible array component returns 0 since its
         length is undefined.
        @return the length of this component or 0 for a structure flexible array.
        """
        ...

    def getOffset(self) -> int:
        """
        Get the byte offset of where this component begins relative to the start of the parent
         data type.
         <p>
         NOTE: The special case of a structure flexible array component returns an offset equal
         to the length of the parent structure since the flexible array component is not included
         in a structure's length.
        @return offset of start of component relative to the start of the parent
         data type.
        """
        ...

    def getOrdinal(self) -> int:
        """
        Get the ordinal position within the parent dataType.
         <p>
         NOTE: The special case of a structure flexible array component returns an ordinal equal
         to the parent structure's {@link Structure#getNumComponents()} since it is not included
         in the list of normal components (see {@link Structure#getFlexibleArrayComponent()}.
        @return ordinal of this component within the parent data type.
        """
        ...

    def getParent(self) -> ghidra.program.model.data.DataType:
        """
        returns the dataType that contains this component.
        @return the dataType that contains this component.
        """
        ...

    def hashCode(self) -> int: ...

    def isBitFieldComponent(self) -> bool:
        """
        Determine if the specified component corresponds to a bit-field.
        @return true if bit-field else false
        """
        ...

    def isEquivalent(self, dtc: ghidra.program.model.data.DataTypeComponent) -> bool:
        """
        Returns true if the given dataTypeComponent is equivalent to this dataTypeComponent.
         A dataTypeComponent is "equivalent" if the other component has a data type
         that is equivalent to this component's data type. The dataTypeComponents must
         also have the same offset, field name, and comment.  The length is only checked
         for components which are dyanmic and whose size must be specified when creating
         a component.
        @param dtc the dataTypeComponent being tested for equivalence.
        @return true if the given dataTypeComponent is equivalent to this dataTypeComponent.
        """
        ...

    def isFlexibleArrayComponent(self) -> bool:
        """
        Determine if this component corresponds to a unsized flexible array which is
         permitted as the trailing component within a structure.
        @return true if component is a trailing flexible array component.
        """
        ...

    def isZeroBitFieldComponent(self) -> bool:
        """
        Determine if the specified component corresponds to a zero-length bit-field.
        @return true if zer-length bit-field else false
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setComment(self, comment: unicode) -> None:
        """
        Sets the comment for the component.
        @param comment this components comment.
        """
        ...

    def setDefaultSettings(self, settings: ghidra.docking.settings.Settings) -> None:
        """
        Set default settings for this dataType.
        @param settings the new default settings.
        """
        ...

    def setFieldName(self, fieldName: unicode) -> None:
        """
        Sets the field name. If the field name is empty it will be set to null,
         which is the default field name. An exception is thrown if one of the
         parent's other components already has the specified field name.
        @param fieldName the new field name for this component.
        @throws DuplicateNameException if another component of the parent has
         the specified field name.
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
    def bitFieldComponent(self) -> bool: ...

    @property
    def comment(self) -> unicode: ...

    @comment.setter
    def comment(self, value: unicode) -> None: ...

    @property
    def dataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def defaultFieldName(self) -> unicode: ...

    @property
    def defaultSettings(self) -> ghidra.docking.settings.Settings: ...

    @defaultSettings.setter
    def defaultSettings(self, value: ghidra.docking.settings.Settings) -> None: ...

    @property
    def endOffset(self) -> int: ...

    @property
    def fieldName(self) -> unicode: ...

    @fieldName.setter
    def fieldName(self, value: unicode) -> None: ...

    @property
    def flexibleArrayComponent(self) -> bool: ...

    @property
    def length(self) -> int: ...

    @property
    def offset(self) -> int: ...

    @property
    def ordinal(self) -> int: ...

    @property
    def parent(self) -> ghidra.program.model.data.DataType: ...

    @property
    def zeroBitFieldComponent(self) -> bool: ...
