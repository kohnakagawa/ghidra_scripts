import ghidra.docking.settings
import ghidra.program.model.data
import ghidra.program.model.symbol
import java.lang
import java.util


class DataTypeUtilities(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def equalsIgnoreConflict(name1: unicode, name2: unicode) -> bool:
        """
        Compares two data type name strings to determine if they are equivalent names, ignoring
         conflict patterns present.
        @param name1 the first name
        @param name2 the second name
        @return true if the names are equivalent when conflict suffixes are ignored.
        """
        ...

    @staticmethod
    def findDataType(dataTypeManager: ghidra.program.model.data.DataTypeManager, namespace: ghidra.program.model.symbol.Namespace, dtName: unicode, classConstraint: java.lang.Class) -> ghidra.program.model.data.DataType:
        """
        Attempt to find the data type whose dtName and specified namespace match a stored data type
         within the specified dataTypeManager. The best match will be returned. The namespace will be
         used in checking data type parent categories, however if no type corresponds to the namespace
         another type whose name matches may be returned.
        @param dataTypeManager data type manager
        @param namespace namespace associated with dtName (null indicates no namespace constraint)
        @param dtName name of data type
        @param classConstraint optional data type interface constraint (e.g., Structure), or null
        @return best matching data type
        """
        ...

    @staticmethod
    def findNamespaceQualifiedDataType(dataTypeManager: ghidra.program.model.data.DataTypeManager, dtNameWithNamespace: unicode, classConstraint: java.lang.Class) -> ghidra.program.model.data.DataType:
        """
        Attempt to find the data type whose dtNameWithNamespace match a stored data type within the
         specified dataTypeManager. The best match will be returned. The namespace will be used in
         checking data type parent categories, however if no type corresponds to the namespace another
         type whose name matches may be returned. NOTE: name parsing assumes :: delimiter and can be
         thrown off if name include template information which could contain namespaces.
        @param dataTypeManager data type manager
        @param dtNameWithNamespace name of data type qualified with namespace (e.g.,
                    ns1::ns2::dtname)
        @param classConstraint optional data type interface constraint (e.g., Structure), or null
        @return best matching data type
        """
        ...

    @staticmethod
    def getArrayBaseDataType(arrayDt: ghidra.program.model.data.Array) -> ghidra.program.model.data.DataType: ...

    @staticmethod
    def getBaseDataType(dt: ghidra.program.model.data.DataType) -> ghidra.program.model.data.DataType:
        """
        Get the base data type for the specified data type stripping away pointers and arrays only. A
         null will be returned for a default pointer.
        @param dt the data type whose base data type is to be determined.
        @return the base data type.
        """
        ...

    @staticmethod
    def getCPrimitiveDataType(dataTypeName: unicode) -> ghidra.program.model.data.DataType:
        """
        Return the appropriate datatype for a given C primitive datatype name.
        @param dataTypeName the datatype name (e.g. "unsigned int", "long long")
        @return the appropriate datatype for a given C primitive datatype name.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getContainedDataTypes(rootDataType: ghidra.program.model.data.DataType) -> java.util.Collection: ...

    @staticmethod
    def getDataTypeCategoryPath(baseCategory: ghidra.program.model.data.CategoryPath, namespace: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.data.CategoryPath:
        """
        Create a data type category path derived from the specified namespace and rooted from the
         specified baseCategory
        @param baseCategory category path from which to root the namespace-base path
        @param namespace the namespace
        @return namespace derived category path
        """
        ...

    @staticmethod
    def getDisplayName(arrayDt: ghidra.program.model.data.Array, showBaseSizeForDynamics: bool) -> unicode: ...

    @staticmethod
    def getMnemonic(arrayDt: ghidra.program.model.data.Array, showBaseSizeForDynamics: bool, settings: ghidra.docking.settings.Settings) -> unicode: ...

    @staticmethod
    def getName(arrayDt: ghidra.program.model.data.Array, showBaseSizeForDynamics: bool) -> unicode: ...

    @staticmethod
    def getNameWithoutConflict(dataType: ghidra.program.model.data.DataType, includeCategoryPath: bool) -> unicode:
        """
        Get the name of a data type with all conflict naming patterns removed.
        @param dataType data type
        @param includeCategoryPath if true the category path will be included with its
        @return name with without conflict patterns
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isSameDataType(dataType1: ghidra.program.model.data.DataType, dataType2: ghidra.program.model.data.DataType) -> bool:
        """
        Returns true if the two dataTypes have the same sourceArchive and the same UniversalID
        @param dataType1 first data type
        @param dataType2 second data type
        @return true if types correspond to the same type from a source archive
        """
        ...

    @staticmethod
    def isSameOrEquivalentDataType(dataType1: ghidra.program.model.data.DataType, dataType2: ghidra.program.model.data.DataType) -> bool:
        """
        Returns true if the two dataTypes have the same sourceArchive and the same UniversalID OR are
         equivalent
        @param dataType1 first data type (if invoked by DB object or manager, this argument must
                    correspond to the DataTypeDB).
        @param dataType2 second data type
        @return true if types correspond to the same type from a source archive or they are
                 equivelent, otherwise false
        """
        ...

    @staticmethod
    def isSecondPartOfFirst(firstDataType: ghidra.program.model.data.DataType, secondDataType: ghidra.program.model.data.DataType) -> bool:
        """
        Check to see if the second data type is the same as the first data type or is part of it.
         <br>
         Note: pointers to the second data type are references and therefore are not considered to be
         part of the first and won't cause true to be returned. If you pass a pointer to this method
         for the first or second parameter, it will return false.
        @param firstDataType the data type whose components or base type should be checked to see if
                    the second data type is part of it.
        @param secondDataType the data type to be checked for in the first data type.
        @return true if the second data type is the first data type or is part of it.
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
