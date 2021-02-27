from typing import List
import ghidra.framework.model
import java.lang


class DataTypeChangeSet(ghidra.framework.model.ChangeSet, object):
    """
    Interface for a Data Type Change set.  Objects that implements this interface track
     various change information on a data type manager.
    """









    def categoryAdded(self, id: long) -> None:
        """
        adds the data type category id to the list of categories that have been added.
        """
        ...

    def categoryChanged(self, id: long) -> None:
        """
        adds the data type category id to the list of categories that have changed.
        """
        ...

    def dataTypeAdded(self, id: long) -> None:
        """
        Adds the data type ID to the list of added data types.
        @param id
        """
        ...

    def dataTypeChanged(self, id: long) -> None:
        """
        Adds the dataType ID to the list of changed data types.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getCategoryAdditions(self) -> List[long]:
        """
        returns the list of category IDs that have been added.
        """
        ...

    def getCategoryChanges(self) -> List[long]:
        """
        returns the list of category IDs that have changed.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDataTypeAdditions(self) -> List[long]:
        """
        returns a list of data type IDs that have been added.
        """
        ...

    def getDataTypeChanges(self) -> List[long]:
        """
        returns a list of data type IDs that have changed.
        """
        ...

    def getSourceArchiveAdditions(self) -> List[long]:
        """
        returns a list of data type source archive IDs that have been added.
        """
        ...

    def getSourceArchiveChanges(self) -> List[long]:
        """
        returns a list of data type source archive IDs that have changed.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def sourceArchiveAdded(self, id: long) -> None:
        """
        Adds the data type source archive ID to the list of added data type archive IDs.
        @param id the data type source archive ID
        """
        ...

    def sourceArchiveChanged(self, id: long) -> None:
        """
        Adds the data type source archive ID to the list of changed data type archive IDs.
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
    def categoryAdditions(self) -> List[long]: ...

    @property
    def categoryChanges(self) -> List[long]: ...

    @property
    def dataTypeAdditions(self) -> List[long]: ...

    @property
    def dataTypeChanges(self) -> List[long]: ...

    @property
    def sourceArchiveAdditions(self) -> List[long]: ...

    @property
    def sourceArchiveChanges(self) -> List[long]: ...
