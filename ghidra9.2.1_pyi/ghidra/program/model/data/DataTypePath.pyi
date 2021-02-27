import ghidra.program.model.data
import java.lang


class DataTypePath(object):
    """
    Object to hold a category path and a datatype name.  They are held separately so that
     the datatype name can contain a categoryPath delimiter ("/") character.
    """





    @overload
    def __init__(self, categoryPath: unicode, dataTypeName: unicode):
        """
        Create DatatypePath
        @param categoryPath the category path for the datatype
        @param dataTypeName the name of the datatype.
        @throws IllegalArgumentException if an invalid category path or dataTypeName is given.
        """
        ...

    @overload
    def __init__(self, categoryPath: ghidra.program.model.data.CategoryPath, dataTypeName: unicode):
        """
        Create DatatypePath
        @param categoryPath the category path for the datatype
        @param dataTypeName the name of the datatype.
        @throws IllegalArgumentException if a null category path or dataTypeName is given.
        """
        ...



    def equals(self, obj: object) -> bool: ...

    def getCategoryPath(self) -> ghidra.program.model.data.CategoryPath:
        """
        Returns the categoryPath for the datatype represented by this datatype path.
         (ie. the CategoryPath that contains the DataType that this DataTypePath points to).
        @return the parent {@link CategoryPath} of the {@link DataType} that this DataTypePath
         points to.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDataTypeName(self) -> unicode:
        """
        Returns the name of the datatype.
        @return the name
        """
        ...

    def getPath(self) -> unicode:
        """
        Returns the full path of this datatype.  NOTE: if the datatype name contains any
         "/" characters, then the resulting path string may be ambiguous as to where the
         category path ends and the datatype name begins.
        @return the full path
        """
        ...

    def hashCode(self) -> int: ...

    def isAncestor(self, otherCategoryPath: ghidra.program.model.data.CategoryPath) -> bool:
        """
        Determine if the specified otherCategoryPath is an ancestor of this data type
         path (i.e., does this data types category or any of its parent hierarchy correspond
         to the specified categoryPath).
        @param otherCategoryPath category path
        @return true if otherCategoryPath is an ancestor of this data type path, else false
        """
        ...

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
    def categoryPath(self) -> ghidra.program.model.data.CategoryPath: ...

    @property
    def dataTypeName(self) -> unicode: ...

    @property
    def path(self) -> unicode: ...
