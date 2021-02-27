from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.pe.cli.blobs
import ghidra.docking.settings
import ghidra.program.model.data
import ghidra.program.model.mem
import ghidra.util
import java.lang
import java.net
import javax.swing.event


class CliBlobMarshalSpec(ghidra.app.util.bin.format.pe.cli.blobs.CliBlob):





    class CliNativeTypeDataType(ghidra.program.model.data.EnumDataType):
        dataType: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeTypeDataType = NativeType



        def __init__(self): ...



        def add(self, __a0: unicode, __a1: long) -> None: ...

        def addParent(self, __a0: ghidra.program.model.data.DataType) -> None: ...

        def clone(self, __a0: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType: ...

        def copy(self, __a0: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType: ...

        def dataTypeDeleted(self, __a0: ghidra.program.model.data.DataType) -> None: ...

        def dataTypeNameChanged(self, __a0: ghidra.program.model.data.DataType, __a1: unicode) -> None: ...

        def dataTypeReplaced(self, __a0: ghidra.program.model.data.DataType, __a1: ghidra.program.model.data.DataType) -> None: ...

        def dataTypeSizeChanged(self, __a0: ghidra.program.model.data.DataType) -> None: ...

        def dependsOn(self, __a0: ghidra.program.model.data.DataType) -> bool: ...

        def equals(self, __a0: object) -> bool: ...

        def getAlignment(self) -> int: ...

        def getCategoryPath(self) -> ghidra.program.model.data.CategoryPath: ...

        def getClass(self) -> java.lang.Class: ...

        def getCount(self) -> int: ...

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

        def getDescription(self) -> unicode: ...

        def getDisplayName(self) -> unicode: ...

        def getDocs(self) -> java.net.URL: ...

        def getLastChangeTime(self) -> long: ...

        def getLastChangeTimeInSourceArchive(self) -> long: ...

        def getLength(self) -> int: ...

        def getMnemonic(self, __a0: ghidra.docking.settings.Settings) -> unicode: ...

        @overload
        def getName(self) -> unicode: ...

        @overload
        def getName(self, __a0: long) -> unicode: ...

        def getNames(self) -> List[unicode]: ...

        def getParents(self) -> List[ghidra.program.model.data.DataType]: ...

        def getPathName(self) -> unicode: ...

        @overload
        def getRepresentation(self, __a0: ghidra.program.model.mem.MemBuffer, __a1: ghidra.docking.settings.Settings, __a2: int) -> unicode: ...

        @overload
        def getRepresentation(self, __a0: long, __a1: ghidra.docking.settings.Settings, __a2: int) -> unicode: ...

        def getSettingsDefinitions(self) -> List[ghidra.docking.settings.SettingsDefinition]: ...

        def getSourceArchive(self) -> ghidra.program.model.data.SourceArchive: ...

        def getUniversalID(self) -> ghidra.util.UniversalID: ...

        @overload
        def getValue(self, __a0: unicode) -> long: ...

        @overload
        def getValue(self, __a0: ghidra.program.model.mem.MemBuffer, __a1: ghidra.docking.settings.Settings, __a2: int) -> object: ...

        def getValueClass(self, __a0: ghidra.docking.settings.Settings) -> java.lang.Class: ...

        def getValues(self) -> List[long]: ...

        def hashCode(self) -> int: ...

        def isDeleted(self) -> bool: ...

        def isDynamicallySized(self) -> bool: ...

        def isEquivalent(self, __a0: ghidra.program.model.data.DataType) -> bool: ...

        def isNotYetDefined(self) -> bool: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def remove(self, __a0: unicode) -> None: ...

        def removeParent(self, __a0: ghidra.program.model.data.DataType) -> None: ...

        def replaceWith(self, __a0: ghidra.program.model.data.DataType) -> None: ...

        def setCategoryPath(self, __a0: ghidra.program.model.data.CategoryPath) -> None: ...

        def setDefaultSettings(self, __a0: ghidra.docking.settings.Settings) -> None: ...

        def setDescription(self, __a0: unicode) -> None: ...

        def setLastChangeTime(self, __a0: long) -> None: ...

        def setLastChangeTimeInSourceArchive(self, __a0: long) -> None: ...

        def setLength(self, __a0: int) -> None: ...

        def setName(self, __a0: unicode) -> None: ...

        def setNameAndCategory(self, __a0: ghidra.program.model.data.CategoryPath, __a1: unicode) -> None: ...

        def setSourceArchive(self, __a0: ghidra.program.model.data.SourceArchive) -> None: ...

        def stateChanged(self, __a0: javax.swing.event.ChangeEvent) -> None: ...

        def toString(self) -> unicode: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...






    class CliNativeType(java.lang.Enum):
        NATIVE_TYPE_ANSIBSTR: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_ANSIBSTR
        NATIVE_TYPE_ARRAY: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_ARRAY
        NATIVE_TYPE_ASANY: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_ASANY
        NATIVE_TYPE_BOOLEAN: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_BOOLEAN
        NATIVE_TYPE_BSTR: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_BSTR
        NATIVE_TYPE_BYVALSTR: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_BYVALSTR
        NATIVE_TYPE_CURRENCY: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_CURRENCY
        NATIVE_TYPE_CUSTOMMARSHALER: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_CUSTOMMARSHALER
        NATIVE_TYPE_DATE: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_DATE
        NATIVE_TYPE_DECIMAL: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_DECIMAL
        NATIVE_TYPE_END: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_END
        NATIVE_TYPE_ERROR: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_ERROR
        NATIVE_TYPE_FIXEDARRAY: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_FIXEDARRAY
        NATIVE_TYPE_FIXEDSYSSTRING: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_FIXEDSYSSTRING
        NATIVE_TYPE_FUNC: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_FUNC
        NATIVE_TYPE_HSTRING: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_HSTRING
        NATIVE_TYPE_I1: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_I1
        NATIVE_TYPE_I2: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_I2
        NATIVE_TYPE_I4: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_I4
        NATIVE_TYPE_I8: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_I8
        NATIVE_TYPE_IDISPATCH: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_IDISPATCH
        NATIVE_TYPE_IINSPECTABLE: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_IINSPECTABLE
        NATIVE_TYPE_INT: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_INT
        NATIVE_TYPE_INTF: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_INTF
        NATIVE_TYPE_IUNKNOWN: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_IUNKNOWN
        NATIVE_TYPE_LPSTR: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_LPSTR
        NATIVE_TYPE_LPSTRUCT: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_LPSTRUCT
        NATIVE_TYPE_LPTSTR: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_LPTSTR
        NATIVE_TYPE_LPWSTR: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_LPWSTR
        NATIVE_TYPE_MAX: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_MAX
        NATIVE_TYPE_NESTEDSTRUCT: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_NESTEDSTRUCT
        NATIVE_TYPE_OBJECTREF: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_OBJECTREF
        NATIVE_TYPE_PTR: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_PTR
        NATIVE_TYPE_R4: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_R4
        NATIVE_TYPE_R8: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_R8
        NATIVE_TYPE_SAFEARRAY: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_SAFEARRAY
        NATIVE_TYPE_STRUCT: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_STRUCT
        NATIVE_TYPE_SYSCHAR: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_SYSCHAR
        NATIVE_TYPE_TBSTR: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_TBSTR
        NATIVE_TYPE_U1: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_U1
        NATIVE_TYPE_U2: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_U2
        NATIVE_TYPE_U4: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_U4
        NATIVE_TYPE_U8: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_U8
        NATIVE_TYPE_UINT: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_UINT
        NATIVE_TYPE_VARIANT: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_VARIANT
        NATIVE_TYPE_VARIANTBOOL: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_VARIANTBOOL
        NATIVE_TYPE_VOID: ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType = NATIVE_TYPE_VOID







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        @staticmethod
        def fromInt(__a0: int) -> ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def id(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.app.util.bin.format.pe.cli.blobs.CliBlobMarshalSpec.CliNativeType]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self, blob: ghidra.app.util.bin.format.pe.cli.blobs.CliBlob): ...



    @overload
    @staticmethod
    def decodeCompressedSigned(codedSize: int) -> int: ...

    @overload
    @staticmethod
    def decodeCompressedSigned(codedSize: int) -> int: ...

    @overload
    @staticmethod
    def decodeCompressedSigned(codedSize: int) -> int: ...

    @staticmethod
    def decodeCompressedSignedInt(reader: ghidra.app.util.bin.BinaryReader) -> int: ...

    @overload
    @staticmethod
    def decodeCompressedUnsigned(codedSize: int) -> int: ...

    @overload
    @staticmethod
    def decodeCompressedUnsigned(codedSize: int) -> int: ...

    @overload
    @staticmethod
    def decodeCompressedUnsigned(codedSize: int) -> int: ...

    @staticmethod
    def decodeCompressedUnsignedInt(reader: ghidra.app.util.bin.BinaryReader) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getContents(self) -> List[int]:
        """
        Gets the blob's contents.
        @return the blob's contents.  Could be null if there was a problem reading the
           contents.
        """
        ...

    def getContentsComment(self) -> unicode: ...

    def getContentsDataType(self) -> ghidra.program.model.data.DataType: ...

    def getContentsName(self) -> unicode: ...

    def getContentsReader(self) -> ghidra.app.util.bin.BinaryReader:
        """
        Gets a new binary reader positioned at the start of this blob's contents.
        @return A new binary reader positioned at the start of this blob's contents.
        """
        ...

    def getContentsSize(self) -> int:
        """
        Gets the blob's contents size in bytes.
        @return The blob's contents size in bytes.
        """
        ...

    @staticmethod
    def getDataTypeForBytes(numBytes: int) -> ghidra.program.model.data.DataType: ...

    def getName(self) -> unicode:
        """
        Gets the name of this blob.
        @return The name of this blob.
        """
        ...

    def getRepresentation(self) -> unicode: ...

    def getSize(self) -> int:
        """
        Gets the blob's size in bytes (includes all fields).
        @return The blob's size in bytes.
        """
        ...

    def getSizeDataType(self) -> ghidra.program.model.data.DataType:
        """
        Gets the proper data type for the blob's size field.
        @return The proper data type for the blob's size field.
        """
        ...

    def getStreamIndex(self) -> int:
        """
        Gets the index into the blob stream of this blob.
        @return The index into the blob stream of this blob.
        """
        ...

    def hashCode(self) -> int: ...

    def isLittleEndian(self) -> bool:
        """
        Checks to see whether or not this blob is little endian.
        @return True if this blob is little endian; false if big endian.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def testSizeDecoding() -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def contentsComment(self) -> unicode: ...

    @property
    def contentsDataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def contentsName(self) -> unicode: ...

    @property
    def representation(self) -> unicode: ...
