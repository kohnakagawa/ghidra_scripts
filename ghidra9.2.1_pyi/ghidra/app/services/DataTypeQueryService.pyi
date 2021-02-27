from typing import List
import ghidra.program.model.data
import java.lang


class DataTypeQueryService(object):
    """
    Simplified datatype service interface to provide query capabilities
     to a set of open datatype managers
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataType(self, filterText: unicode) -> ghidra.program.model.data.DataType:
        """
        Obtain the preferred datatype which corresponds to the specified
         datatype specified by filterText.  A tool-based service provider
         may prompt the user to select a datatype if more than one possibility
         exists.
        @param filterText If not null, this text filters the visible data types to only show those
                           that start with the given text
        @return the preferred data type (e.g., chosen by the user) or null if no match found
         or selection was cancelled by user.
        """
        ...

    def getDataTypeManagers(self) -> List[ghidra.program.model.data.DataTypeManager]:
        """
        Gets the open data type managers.
        @return the open data type managers.
        """
        ...

    def getSortedDataTypeList(self) -> List[ghidra.program.model.data.DataType]:
        """
        Gets the sorted list of all datatypes known by this service via it's owned DataTypeManagers.
         This method can be called frequently, as the underlying data is indexed and only updated
         as changes are made.
        @return the sorted list of known data types.
        """
        ...

    def hashCode(self) -> int: ...

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
    def dataTypeManagers(self) -> List[ghidra.program.model.data.DataTypeManager]: ...

    @property
    def sortedDataTypeList(self) -> List[object]: ...
