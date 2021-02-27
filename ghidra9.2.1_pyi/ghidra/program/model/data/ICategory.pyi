from typing import List
import ghidra.program.model.data
import ghidra.util.task
import java.lang


class ICategory(object):
    DELIMITER_CHAR: int = '/'
    DELIMITER_STRING: unicode = u'/'
    NAME_DELIMITER: unicode = u'/'







    def addDataType(self, dt: ghidra.program.model.data.DataType, handler: ghidra.program.model.data.DataTypeConflictHandler) -> ghidra.program.model.data.DataType: ...

    def copyCategory(self, category: ghidra.program.model.data.Category, handler: ghidra.program.model.data.DataTypeConflictHandler, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.data.Category:
        """
        Make a new subcategory from the given category.
        @param category the category to copy into this category
        @return category that is added to this category
        """
        ...

    def createCategory(self, name: unicode) -> ghidra.program.model.data.Category:
        """
        Create a category with the given name.
        @param name the category name
        @throws DuplicateNameException if this category already contains a
         category or data type with the given name
        @throws InvalidNameException if name has invalid characters
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getCategories(self) -> List[ghidra.program.model.data.Category]:
        """
        Get all categories in this category.
        @return zero-length array if there are no categories
        """
        ...

    def getCategory(self, name: unicode) -> ghidra.program.model.data.Category:
        """
        Get a category with the given name.
        @param name the name of the category
        @return null if there is no category by this name
        """
        ...

    def getCategoryPath(self) -> ghidra.program.model.data.CategoryPath: ...

    def getCategoryPathName(self) -> unicode:
        """
        Get the fully qualified name for this category.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDataType(self, name: unicode) -> ghidra.program.model.data.DataType:
        """
        Get a data type with the given name.
        @param name the name of the data type
        @return null if there is no data type by this name
        """
        ...

    def getDataTypeManager(self) -> ghidra.program.model.data.DataTypeManager:
        """
        Get the data type manager associated with this category.
        """
        ...

    def getDataTypes(self) -> List[ghidra.program.model.data.DataType]:
        """
        Get all data types in this category.
        @return zero-length array if there are no data types
        """
        ...

    def getName(self) -> unicode:
        """
        Get the name of this category.
        """
        ...

    def getParent(self) -> ghidra.program.model.data.Category:
        """
        Return this category's parent; return null if this is the root category.
        """
        ...

    def getRoot(self) -> ghidra.program.model.data.Category:
        """
        Get the root category.
        """
        ...

    def hashCode(self) -> int: ...

    def isRoot(self) -> bool: ...

    def moveCategory(self, category: ghidra.program.model.data.Category, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Move the given category to this category; category is removed from
         its original parent category.
        @param category the category to move
        @throws DuplicateNameException if this category already contains a
         category or data type with the same name as the category param.
        """
        ...

    def moveDataType(self, type: ghidra.program.model.data.DataType, handler: ghidra.program.model.data.DataTypeConflictHandler) -> None:
        """
        @param type
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, type: ghidra.program.model.data.DataType, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        @param type
        """
        ...

    def removeCategory(self, name: unicode, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Remove the named category from this category.
        @param name the name of the category to remove
        @param monitor the task monitor
        @return true if the category was removed
        """
        ...

    def setName(self, name: unicode) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def categories(self) -> List[ghidra.program.model.data.Category]: ...

    @property
    def categoryPath(self) -> ghidra.program.model.data.CategoryPath: ...

    @property
    def categoryPathName(self) -> unicode: ...

    @property
    def dataTypeManager(self) -> ghidra.program.model.data.DataTypeManager: ...

    @property
    def dataTypes(self) -> List[ghidra.program.model.data.DataType]: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def parent(self) -> ghidra.program.model.data.Category: ...

    @property
    def root(self) -> bool: ...
