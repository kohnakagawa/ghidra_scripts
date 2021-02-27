import ghidra.program.model.data
import java.lang


class DataTypeManagerChangeListener(object):
    """
    The listener interface for notification of changes to a DataTypeManager
    """









    def categoryAdded(self, dtm: ghidra.program.model.data.DataTypeManager, path: ghidra.program.model.data.CategoryPath) -> None:
        """
        Notification when category is added.
        @param dtm the dataType manager
        @param path the categoryPath of the newly added category.
        """
        ...

    def categoryMoved(self, dtm: ghidra.program.model.data.DataTypeManager, oldPath: ghidra.program.model.data.CategoryPath, newPath: ghidra.program.model.data.CategoryPath) -> None:
        """
        Notification when a category is reparented to new category.
        @param dtm data type manager associated with the category
        @param oldPath the path of the category before it was moved.
        @param newPath the path of the category after it was moved.
        """
        ...

    def categoryRemoved(self, dtm: ghidra.program.model.data.DataTypeManager, path: ghidra.program.model.data.CategoryPath) -> None:
        """
        Notification when a category is removed.
        @param dtm data type manager associated with the category
        @param path the categoryPath of the category that was removed.
        """
        ...

    def categoryRenamed(self, dtm: ghidra.program.model.data.DataTypeManager, oldPath: ghidra.program.model.data.CategoryPath, newPath: ghidra.program.model.data.CategoryPath) -> None:
        """
        Notification when category is renamed.
        @param dtm data type manager associated with the category
        @param oldPath the path of the category before it was renamed.
        @param newPath the path of the category after it was renamed.  This path will only differ in
         the last segment of the path.
        """
        ...

    def dataTypeAdded(self, dtm: ghidra.program.model.data.DataTypeManager, path: ghidra.program.model.data.DataTypePath) -> None:
        """
        Notification when a data type is added to a category
        @param dtm data type manager for the given category paths.
        @param path the DataTypePath of the newly added datatype.
        """
        ...

    def dataTypeChanged(self, dtm: ghidra.program.model.data.DataTypeManager, path: ghidra.program.model.data.DataTypePath) -> None:
        """
        Notification when data type is changed.
        @param dtm data type manager for the given category paths.
        @param path the path of the datatype that changed.
        """
        ...

    def dataTypeMoved(self, dtm: ghidra.program.model.data.DataTypeManager, oldPath: ghidra.program.model.data.DataTypePath, newPath: ghidra.program.model.data.DataTypePath) -> None:
        """
        Notification when a data type is moved.
        @param dtm data type manager for the given category paths.
        @param oldPath the path of the datatype before it was moved.
        @param newPath the path of the datatype after it was moved.
        """
        ...

    def dataTypeRemoved(self, dtm: ghidra.program.model.data.DataTypeManager, path: ghidra.program.model.data.DataTypePath) -> None:
        """
        Notification when data type is removed.
        @param dtm data type manager for the given category paths.
        @param path the DataTypePath of the removed datatype.
        """
        ...

    def dataTypeRenamed(self, dtm: ghidra.program.model.data.DataTypeManager, oldPath: ghidra.program.model.data.DataTypePath, newPath: ghidra.program.model.data.DataTypePath) -> None:
        """
        Notification when data type is renamed.
        @param dtm data type manager for the given category paths.
        @param oldPath the path of the datatype before it was renamed.
        @param newPath the path of the datatype after it was renamed.
        """
        ...

    def dataTypeReplaced(self, dtm: ghidra.program.model.data.DataTypeManager, oldPath: ghidra.program.model.data.DataTypePath, newPath: ghidra.program.model.data.DataTypePath, newDataType: ghidra.program.model.data.DataType) -> None:
        """
        Notification when a data type has been replaced.
        @param dtm data type manager for the given category paths.
        @param oldPath the path of the datatype that was replaced.
        @param newPath the path of the datatype that replaced the existing datatype.
        @param newDataType the new dataType that replaced the old dataType
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def favoritesChanged(self, dtm: ghidra.program.model.data.DataTypeManager, path: ghidra.program.model.data.DataTypePath, isFavorite: bool) -> None:
        """
        Notification the favorite status of a datatype has changed
        @param dtm data type manager for the given category paths.
        @param path the DataTypePath of the datatype had its favorite status changed.
        @param isFavorite reflects the current favorite status of the datatype.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def sourceArchiveAdded(self, dataTypeManager: ghidra.program.model.data.DataTypeManager, sourceArchive: ghidra.program.model.data.SourceArchive) -> None:
        """
        Notification that the information for a source archive has been added. This happens when
         a data type from the indicated source archive is added to this data type manager.
        @param dataTypeManager data type manager referring to the given source information.
        @param sourceArchive the new data type source information
        """
        ...

    def sourceArchiveChanged(self, dataTypeManager: ghidra.program.model.data.DataTypeManager, sourceArchive: ghidra.program.model.data.SourceArchive) -> None:
        """
        Notification that the information for a particular source archive has changed. Typically,
         this would be because it was renamed or moved.
        @param dataTypeManager data type manager referring to the given source information.
        @param sourceArchive the changed data type source information
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
