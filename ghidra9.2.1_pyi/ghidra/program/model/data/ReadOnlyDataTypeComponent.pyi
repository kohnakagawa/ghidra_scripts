import ghidra.docking.settings
import ghidra.program.model.data
import java.io
import java.lang


class ReadOnlyDataTypeComponent(object, ghidra.program.model.data.DataTypeComponent, java.io.Serializable):
    """
    DataTypeComponents from dataTypes that can not be modified.
    """

    DEFAULT_FIELD_NAME_PREFIX: unicode = u'field'



    @overload
    def __init__(self, dataType: ghidra.program.model.data.DataType, parent: ghidra.program.model.data.DynamicDataType, length: int, ordinal: int, offset: int):
        """
        Create a new DataTypeComponent
        @param dataType the dataType for this component
        @param parent the dataType that this component belongs to
        @param length the length of the dataType in this component.
        @param ordinal the index of this component in the parent.
        @param offset the byte offset within the parent
        """
        ...

    @overload
    def __init__(self, dataType: ghidra.program.model.data.DataType, parent: ghidra.program.model.data.DynamicDataType, length: int, ordinal: int, offset: int, fieldName: unicode, comment: unicode):
        """
        Create a new DataTypeComponent
        @param dataType the dataType for this component
        @param parent the dataType that this component belongs to
        @param length the length of the dataType in this component.
        @param offset the byte offset within the parent
        @param ordinal the index of this component in the parent.
        @param fieldName the name associated with this component
        @param comment the comment associated with ths component
        """
        ...



    def equals(self, obj: object) -> bool:
        """
        @see java.lang.Object#equals(java.lang.Object)
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self) -> unicode:
        """
        @see ghidra.program.model.data.DataTypeComponent#getComment()
        """
        ...

    def getDataType(self) -> ghidra.program.model.data.DataType:
        """
        @see ghidra.program.model.data.DataTypeComponent#getDataType()
        """
        ...

    def getDefaultFieldName(self) -> unicode:
        """
        @see ghidra.program.model.data.DataTypeComponent#getDefaultFieldName()
        """
        ...

    def getDefaultSettings(self) -> ghidra.docking.settings.Settings:
        """
        @see ghidra.program.model.data.DataTypeComponent#getDefaultSettings()
        """
        ...

    def getEndOffset(self) -> int:
        """
        @see ghidra.program.model.data.DataTypeComponent#getEndOffset()
        """
        ...

    def getFieldName(self) -> unicode:
        """
        @see ghidra.program.model.data.DataTypeComponent#getFieldName()
        """
        ...

    def getLength(self) -> int:
        """
        @see ghidra.program.model.data.DataTypeComponent#getLength()
        """
        ...

    def getOffset(self) -> int:
        """
        @see ghidra.program.model.data.DataTypeComponent#getOffset()
        """
        ...

    def getOrdinal(self) -> int:
        """
        @see ghidra.program.model.data.DataTypeComponent#getOrdinal()
        """
        ...

    def getParent(self) -> ghidra.program.model.data.DataType:
        """
        @see ghidra.program.model.data.DataTypeComponent#getParent()
        """
        ...

    def hashCode(self) -> int: ...

    def isBitFieldComponent(self) -> bool: ...

    def isEquivalent(self, dtc: ghidra.program.model.data.DataTypeComponent) -> bool: ...

    def isFlexibleArrayComponent(self) -> bool: ...

    def isZeroBitFieldComponent(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setComment(self, comment: unicode) -> None:
        """
        @see ghidra.program.model.data.DataTypeComponent#setComment(java.lang.String)
        """
        ...

    def setDefaultSettings(self, settings: ghidra.docking.settings.Settings) -> None:
        """
        @see ghidra.program.model.data.DataTypeComponent#setDefaultSettings(ghidra.docking.settings.Settings)
        """
        ...

    def setFieldName(self, fieldName: unicode) -> None:
        """
        @see ghidra.program.model.data.DataTypeComponent#setFieldName(java.lang.String)
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
