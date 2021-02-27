import ghidra.util
import java.lang


class GenericSaveable(object, ghidra.util.Saveable):
    """
    GenericSaveable is used by the DBPropertyMapManager
     when the class can not be found and loaded for the class path name of a
     property in the database. This allows the properties for that class to be
     accessed in a generic way so that the manager can copy or remove the property
     at a particular address. This allows the Diff and MultiUser Merge to compare
     and manipulate the property as needed.
    """









    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getObjectStorageFields(self) -> java.lang.Class: ...

    def getSchemaVersion(self) -> int: ...

    def hashCode(self) -> int: ...

    def isPrivate(self) -> bool: ...

    def isUpgradeable(self, oldSchemaVersion: int) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restore(self, objStorage: ghidra.util.ObjectStorage) -> None: ...

    def save(self, objStorage: ghidra.util.ObjectStorage) -> None: ...

    def toString(self) -> unicode: ...

    def upgrade(self, oldObjStorage: ghidra.util.ObjectStorage, oldSchemaVersion: int, currentObjStorage: ghidra.util.ObjectStorage) -> bool: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def objectStorageFields(self) -> List[java.lang.Class]: ...

    @property
    def private(self) -> bool: ...

    @property
    def schemaVersion(self) -> int: ...
