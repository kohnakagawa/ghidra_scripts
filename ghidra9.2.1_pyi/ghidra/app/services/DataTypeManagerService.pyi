from typing import List
import ghidra.app.plugin.core.datamgr.archive
import ghidra.app.services
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util
import java.io
import java.lang
import java.util
import javax.swing.tree


class DataTypeManagerService(ghidra.app.services.DataTypeQueryService, object):
    """
    Service to provide list of cycle groups and data types identified as
     "favorites." Favorites will show up on the popup menu for creating
     data and defining function return types and parameters.
    """









    def addDataTypeManagerChangeListener(self, listener: ghidra.program.model.data.DataTypeManagerChangeListener) -> None:
        """
        Adds a listener to be notified when changes occur to any open datatype manager.
        @param listener the listener to be added.
        """
        ...

    def closeArchive(self, dtm: ghidra.program.model.data.DataTypeManager) -> None:
        """
        Closes the archive for the given {@link DataTypeManager}.  This will ignore request to
         close the open Program's manager and the built-in manager.
        @param dtm the data type manager of the archive to close
        """
        ...

    def edit(self, dt: ghidra.program.model.data.DataType) -> None:
        """
        Pop up an editor dialog for the given data type.
        @param dt data type that either a Structure or a Union; built in types cannot be edited
        @throws IllegalArgumentException if the given has not been resolved by a DataTypeManager;
                 in other words, if {@link DataType#getDataTypeManager()} returns null.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getBuiltInDataTypesManager(self) -> ghidra.program.model.data.DataTypeManager:
        """
        Get the data type manager that has all of the built in types.
        @return data type manager for built in data types
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getDataType(self, __a0: unicode) -> ghidra.program.model.data.DataType: ...

    @overload
    def getDataType(self, selectedPath: javax.swing.tree.TreePath) -> ghidra.program.model.data.DataType:
        """
        Shows the user a dialog that allows them to choose a data type from a tree of all available
         data types.
        @param selectedPath An optional tree path to select in the tree
        @return A data type chosen by the user
        """
        ...

    def getDataTypeManagers(self) -> List[ghidra.program.model.data.DataTypeManager]: ...

    def getEditorHelpLocation(self, dataType: ghidra.program.model.data.DataType) -> ghidra.util.HelpLocation:
        """
        Gets the location of the help for editing the specified data type.
        @param dataType the data type to be edited.
        @return the help location for editing the data type.
        """
        ...

    def getFavorites(self) -> List[ghidra.program.model.data.DataType]:
        """
        Get the data types marked as favorites that will show up on
         a popup menu.
        @return list of favorite datatypess
        """
        ...

    def getPossibleEquateNames(self, value: long) -> java.util.Set:
        """
        Examines all enum dataTypes for items that match the given value. Returns a list of Strings
         that might make sense for the given value.
        @param value the value to search for.
        @return the list of enum item names that match the given value
        """
        ...

    def getRecentlyUsed(self) -> ghidra.program.model.data.DataType:
        """
        Get the data type that was most recently used to apply data to a
         Program.
        @return data type that was most recently used
        """
        ...

    def getSortedDataTypeList(self) -> List[object]: ...

    def hashCode(self) -> int: ...

    def isEditable(self, dt: ghidra.program.model.data.DataType) -> bool:
        """
        Determine if the indicated data type can be edited
         (i.e. it has an editor that this service knows how to invoke).
        @param dt data type to be edited
        @return true if this service can invoke an editor for changing the data type.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def openArchive(self, dataTypeArchive: ghidra.program.model.listing.DataTypeArchive) -> ghidra.app.plugin.core.datamgr.archive.Archive:
        """
        A method to open an Archive for the given, pre-existing DataTypeArchive (like one that
         was opened during the import process.
        @param dataTypeArchive the archive from which to create an Archive
        @return an Archive based upon the given DataTypeArchive
        """
        ...

    @overload
    def openArchive(self, file: java.io.File, acquireWriteLock: bool) -> ghidra.app.plugin.core.datamgr.archive.Archive:
        """
        A method to open an Archive for the given, pre-existing archive file (*.gdt)
        @param file data type archive file
        @param acquireWriteLock true if write lock should be acquired (i.e., open for update)
        @return an Archive based upon the given archive files
        @throws IOException if an i/o error occurs opening the data type archive
        @throws DuplicateIdException if another archive with the same ID is already open
        """
        ...

    def openDataTypeArchive(self, archiveName: unicode) -> ghidra.program.model.data.DataTypeManager:
        """
        Opens the specified data type archive contained within the Ghidra installation.
         NOTE: This is predicated upon all archive files having a unique name within the installation.
         Any path prefix specified may prevent the file from opening (or reopening) correctly.
        @param archiveName archive file name (i.e., "generic_C_lib")
        @return the data type archive or null if an archive with the specified name
         can not be found.
        @throws IOException if an i/o error occurs opening the data type archive
        @throws DuplicateIdException if another archive with the same ID is already open
        """
        ...

    def removeDataTypeManagerChangeListener(self, listener: ghidra.program.model.data.DataTypeManagerChangeListener) -> None:
        """
        Removes the given listener from receiving dataTypeManger change notifications.
        @param listener the listener to be removed.
        """
        ...

    def setDataTypeSelected(self, dataType: ghidra.program.model.data.DataType) -> None:
        """
        Selects the given data type in the display of data types.  A null <code>dataType</code>
         value will clear the current selection.
        @param dataType The data type to select.
        """
        ...

    def setRecentlyUsed(self, dt: ghidra.program.model.data.DataType) -> None:
        """
        Set the given data type as the most recently used to apply a
         data type to a Program.
        @param dt data type that was most recently used
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
    def builtInDataTypesManager(self) -> ghidra.program.model.data.DataTypeManager: ...

    @property
    def dataTypeManagers(self) -> List[ghidra.program.model.data.DataTypeManager]: ...

    @property
    def dataTypeSelected(self) -> None: ...  # No getter available.

    @dataTypeSelected.setter
    def dataTypeSelected(self, value: ghidra.program.model.data.DataType) -> None: ...

    @property
    def favorites(self) -> List[object]: ...

    @property
    def recentlyUsed(self) -> ghidra.program.model.data.DataType: ...

    @recentlyUsed.setter
    def recentlyUsed(self, value: ghidra.program.model.data.DataType) -> None: ...

    @property
    def sortedDataTypeList(self) -> List[object]: ...
