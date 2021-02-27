from typing import List
import ghidra.docking.settings
import ghidra.program.model.data
import ghidra.program.model.mem
import ghidra.util
import java.lang
import java.net


class DataType(object):
    """
    The interface that all data types must implement.
    """

    CONFLICT_SUFFIX: unicode = u'.conflict'
    DEFAULT: ghidra.program.model.data.DataType = undefined
    NO_LAST_CHANGE_TIME: long = 0x0L
    NO_SOURCE_SYNC_TIME: long = 0x0L
    VOID: ghidra.program.model.data.DataType = void







    def addParent(self, dt: ghidra.program.model.data.DataType) -> None:
        """
        Inform this data type that it has the given parent
         <br>
         TODO: This method is reserved for internal DB use and should be removed
         from the public DataType interface!!
         <br>
        @param dt parent data type
        """
        ...

    def clone(self, dtm: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType:
        """
        Returns a new instance of this DataType with its universalID and SourceArchive identity retained.
         Note: for built-in DataType's, clone and copy should have the same affect.
        @param dtm the data-type manager instance whose data-organization should apply.
        """
        ...

    def copy(self, dtm: ghidra.program.model.data.DataTypeManager) -> ghidra.program.model.data.DataType:
        """
        Returns a new instance of this DataType with a new identity.
         Note: for built-in DataType's, clone and copy should have the same affect.
        @param dtm the data-type manager instance whose data-organization should apply.
        """
        ...

    def dataTypeDeleted(self, dt: ghidra.program.model.data.DataType) -> None:
        """
        Informs this dataType that the given dataType has been deleted.
         <br>
         TODO: This method is reserved for internal DB use and should be removed
         from the public DataType interface!!
         <br>
        @param dt the dataType that has been deleted.
        """
        ...

    def dataTypeNameChanged(self, dt: ghidra.program.model.data.DataType, oldName: unicode) -> None:
        """
        Informs this data type that its name has changed from the indicated old name.
         <br>
         TODO: This method is reserved for internal DB use and should be removed
         from the public DataType interface!!
         <br>
        @param dt the data type whose name changed
        @param oldName the data type's old name
        """
        ...

    def dataTypeReplaced(self, oldDt: ghidra.program.model.data.DataType, newDt: ghidra.program.model.data.DataType) -> None:
        """
        Informs this data type that the given oldDT has been replaced with newDT
         <br>
         TODO: This method is reserved for internal DB use and should be removed
         from the public DataType interface!!
         <br>
        @param oldDt old data type
        @param newDt new data type
        """
        ...

    def dataTypeSizeChanged(self, dt: ghidra.program.model.data.DataType) -> None:
        """
        Notification that the given dataType's size has changed.  DataTypes may
         need to make internal changes in response.
         <br>
         TODO: This method is reserved for internal DB use and should be removed
         from the public DataType interface!!
         <br>
        @param dt the dataType that has changed.
        """
        ...

    def dependsOn(self, dt: ghidra.program.model.data.DataType) -> bool:
        """
        Returns true if this dataType depends on the existence of the given dataType.
         For example byte[] depends on byte.  If byte were deleted, then byte[] would
         also be deleted.
        @param dt the dataType to test that this dataType depends on.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAlignment(self) -> int:
        """
        Gets the alignment to be used when aligning this data type within another data type.
        @return this data type's alignment.
        """
        ...

    def getCategoryPath(self) -> ghidra.program.model.data.CategoryPath:
        """
        Gets the categoryPath associated with this data type
        @return the datatype's category path
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDataOrganization(self) -> ghidra.program.model.data.DataOrganization:
        """
        Returns the DataOrganization associated with this data-type
        """
        ...

    def getDataTypeManager(self) -> ghidra.program.model.data.DataTypeManager:
        """
        Returns the DataTypeManager that is associated with this dataType.
         This association should not be used to indicate whether this DataType has been
         resolved, but is intended to indicate whether the appropriate DataOrganization
         is being used.
        """
        ...

    def getDataTypePath(self) -> ghidra.program.model.data.DataTypePath:
        """
        Returns the dataTypePath for this dataType;
        @return the dataTypePath for this dataType;
        """
        ...

    def getDefaultAbbreviatedLabelPrefix(self) -> unicode:
        """
        Returns the prefix to use for this datatype when an abbreviated prefix is desired.  For
         example, some data types will built a large default label, at which is is more desirable to
         have a shortened prefix.
        @return the prefix to use for this datatype when an abbreviated prefix is desired.  May
                 return null.
        """
        ...

    @overload
    def getDefaultLabelPrefix(self) -> unicode:
        """
        Returns the appropriate string to use as the default label prefix in the absence of any data.
        @return the default label prefix or null if none specified.
        """
        ...

    @overload
    def getDefaultLabelPrefix(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, len: int, options: ghidra.program.model.data.DataTypeDisplayOptions) -> unicode:
        """
        Returns the appropriate string to use as the default label prefix.
        @param buf memory buffer containing the bytes.
        @param settings the Settings object
        @param len the length of the data.
        @param options options for how to format the default label prefix.
        @return the default label prefix or null if none specified.
        """
        ...

    def getDefaultOffcutLabelPrefix(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, len: int, options: ghidra.program.model.data.DataTypeDisplayOptions, offcutOffset: int) -> unicode:
        """
        Returns the appropriate string to use as the default label prefix, taking into account
         the fact that there exists a reference to the data that references
         <code>offcutLength</code> bytes into this type
        @param buf memory buffer containing the bytes.
        @param settings the Settings object
        @param len the length of the data.
        @param options options for how to format the default label prefix.
        @param offcutOffset
        @return the default label prefix.
        """
        ...

    def getDefaultSettings(self) -> ghidra.docking.settings.Settings:
        """
        Gets the default settings for this data type.
        @return the default settings for this dataType.
        """
        ...

    def getDescription(self) -> unicode:
        """
        Get a String briefly describing this DataType.
        @return a one-liner describing this DataType.
        """
        ...

    def getDisplayName(self) -> unicode:
        """
        Gets the name for referring to this data type.
        @return generic name for this Data Type (i.e.: Word)
        """
        ...

    def getDocs(self) -> java.net.URL:
        """
        The getDocs method should provide a URL pointing to extended
         documentation for this DataType if it exists. A typical
         use would be to return a URL pointing to the programmers
         reference for this instruction or a page describing this
         data structure.
        @return null - there is no URL documentation for this prototype.
        """
        ...

    def getLastChangeTime(self) -> long:
        """
        Get the timestamp corresponding to the last time this type was changed
         within its data type manager
        @return timestamp of last change within data type manager
        """
        ...

    def getLastChangeTimeInSourceArchive(self) -> long:
        """
        Get the timestamp corresponding to the last time this type was sync'd
         within its source archive
        @return timestamp of last sync with source archive
        """
        ...

    def getLength(self) -> int:
        """
        Get the length (number of 8-bit bytes) of this DataType.
        @return the length of this DataType
        """
        ...

    def getMnemonic(self, settings: ghidra.docking.settings.Settings) -> unicode:
        """
        Get the mnemonic for this DataType.
        @return the mnemonic for this DataType.
        """
        ...

    def getName(self) -> unicode:
        """
        Return that name of the data type
        """
        ...

    def getParents(self) -> List[ghidra.program.model.data.DataType]:
        """
        @return an array of parents of this data type
        """
        ...

    def getPathName(self) -> unicode:
        """
        Returns the full category path name that includes this dataType's name.  If
         the category is null, then this just returns the dataType's name.
        """
        ...

    def getRepresentation(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, length: int) -> unicode:
        """
        Get bytes from memory in a printable format for this type.
        @param buf the data.
        @param settings the settings to use for the representation.
        @param length the number of bytes to represent.
        @return the representation of the data in this format, never null.
        """
        ...

    def getSettingsDefinitions(self) -> List[ghidra.docking.settings.SettingsDefinition]:
        """
        Gets a list of all the settingsDefinitions used by this data type.
        @return a list of the settingsDefinitions used by this data type.
        """
        ...

    def getSourceArchive(self) -> ghidra.program.model.data.SourceArchive:
        """
        Get the source archive where this type originated
        @return source archive object
        """
        ...

    def getUniversalID(self) -> ghidra.util.UniversalID:
        """
        Get the universal ID for this data type.  This value is intended to be a
         unique identifier across all programs and archives.  The same ID indicates
         that two data types were originally the same one.  Keep in mind names, categories,
         and component makeup may differ and have changed since there origin.
        @return data type UniversalID
        """
        ...

    def getValue(self, buf: ghidra.program.model.mem.MemBuffer, settings: ghidra.docking.settings.Settings, length: int) -> object:
        """
        Get the data in the form of the appropriate Object for
         this DataType.

         For instance if the data type is an AddressDT, return an Address object.
                                          a Byte, return a Scalar* (maybe this should be a Byte)
                                          a Float, return a Float
        @param buf the data buffer.
        @param settings the settings to use.
        @param length the number of bytes to get the value from.
        @return the data Object.
        """
        ...

    def getValueClass(self, settings: ghidra.docking.settings.Settings) -> java.lang.Class:
        """
        Get the Class of the value to be returned by this data type.
        @param settings the relevant settings to use or null for default.
        @return Class of the value to be returned by this data type or null if it can vary
         or is unspecified.  Types which correspond to a string or char array will
         return the String class.
        """
        ...

    def hashCode(self) -> int: ...

    def isDeleted(self) -> bool:
        """
        Returns true if this data type has been deleted and is no longer valid
        @return true if this data type has been deleted and is no longer valid.
        """
        ...

    def isDynamicallySized(self) -> bool:
        """
        Indicates if this data-type is dynamically sized based upon DataOrganization.
        @return true if dynamically sized
        """
        ...

    def isEquivalent(self, dt: ghidra.program.model.data.DataType) -> bool:
        """
        Returns true if the given dataType is equivalent to this dataType.  The
         precise meaning of "equivalent" is dataType dependent.
         <br>
         NOTE: if invoked by a DB object or manager it should be invoked on the
         DataTypeDB object passing the other datatype as the argument.
        @param dt the dataType being tested for equivalence.
        @return true if the if the given dataType is equivalent to this dataType.
        """
        ...

    def isNotYetDefined(self) -> bool:
        """
        Indicates if type has not yet been defined.
         Such types will always return a size of 1.
         (example: empty structure)
        @return true if this type is not yet defined.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeParent(self, dt: ghidra.program.model.data.DataType) -> None:
        """
        Remove a parent data type
         <br>
         TODO: This method is reserved for internal DB use and should be removed
         from the public DataType interface!!
         <br>
        @param dt parent data type
        """
        ...

    def replaceWith(self, dataType: ghidra.program.model.data.DataType) -> None:
        """
        For dataTypes that support change, this method replaces the internals of this dataType with
         the internals of the given dataType.  The dataTypes must be of the same "type" (i.e. structure
         can only be replacedWith  another structure.
        @param dataType the dataType that contains the internals to upgrade to.
        @throws UnsupportedOperationException if the dataType does not support change.
        @throws IllegalArgumentException if the given dataType is not the same type as this dataType.
        """
        ...

    def setCategoryPath(self, path: ghidra.program.model.data.CategoryPath) -> None:
        """
        @param path set the categoryPath associated with this data type
        @throws DuplicateNameException
        """
        ...

    def setDefaultSettings(self, settings: ghidra.docking.settings.Settings) -> None:
        """
        Set the default settings for this data type.
         <br>
         TODO: This method is reserved for internal DB use and should be removed
         from the public DataType interface!!
         <br>
        @param settings the settings to be used as this dataTypes default settings.
        """
        ...

    def setDescription(self, description: unicode) -> None:
        """
        Sets a String briefly describing this DataType.
        @param description a one-liner describing this DataType.
        @throws UnsupportedOperationException if the description is not allowed to be set for this data type.
        """
        ...

    def setLastChangeTime(self, lastChangeTime: long) -> None:
        """
        Sets the lastChangeTime for this dataType.  Normally, this is updated automatically when
         a dataType is changed, but when committing or updating while synchronizing an archive, the
         lastChangeTime may need to be updated externally.
        @param lastChangeTime the time to use as the lastChangeTime for this dataType
        """
        ...

    def setLastChangeTimeInSourceArchive(self, lastChangeTimeInSourceArchive: long) -> None:
        """
        Sets the lastChangeTimeInSourceArchive for this dataType. This is used by when a dataType
         change is committed back to its source archive.
        @param lastChangeTimeInSourceArchive the time to use as the lastChangeTimeInSourceArchive for this dataType
        """
        ...

    def setName(self, name: unicode) -> None:
        """
        Sets the name of the dataType
        @param name the new name for this dataType.
        @throws InvalidNameException if the given name does not form a valid name.
        @throws DuplicateNameException if name change on stored {@link DataType}
         is a duplicate of another datatype within the same category (only applies to
         DB stored {@link DataType}).
        """
        ...

    def setNameAndCategory(self, path: ghidra.program.model.data.CategoryPath, name: unicode) -> None:
        """
        Sets the name and category of a dataType at the same time.
        @param path the new category path.
        @param name the new name
        @throws InvalidNameException if the name is invalid
        @throws DuplicateNameException if name change on stored {@link DataType}
         is a duplicate of another datatype within the same category (only applies to
         DB stored {@link DataType}).
        """
        ...

    def setSourceArchive(self, archive: ghidra.program.model.data.SourceArchive) -> None:
        """
        Set the source archive where this type originated
        @param archive source archive object
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
    def categoryPath(self) -> ghidra.program.model.data.CategoryPath: ...

    @categoryPath.setter
    def categoryPath(self, value: ghidra.program.model.data.CategoryPath) -> None: ...

    @property
    def dataOrganization(self) -> ghidra.program.model.data.DataOrganization: ...

    @property
    def dataTypeManager(self) -> ghidra.program.model.data.DataTypeManager: ...

    @property
    def dataTypePath(self) -> ghidra.program.model.data.DataTypePath: ...

    @property
    def defaultAbbreviatedLabelPrefix(self) -> unicode: ...

    @property
    def defaultLabelPrefix(self) -> unicode: ...

    @property
    def defaultSettings(self) -> ghidra.docking.settings.Settings: ...

    @defaultSettings.setter
    def defaultSettings(self, value: ghidra.docking.settings.Settings) -> None: ...

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
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def notYetDefined(self) -> bool: ...

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
