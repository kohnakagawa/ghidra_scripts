import ghidra.util
import java.awt
import java.lang


class SaveableColor(ghidra.util.PrivateSaveable):




    @overload
    def __init__(self): ...

    @overload
    def __init__(self, color: java.awt.Color): ...



    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getColor(self) -> java.awt.Color: ...

    def getObjectStorageFields(self) -> java.lang.Class: ...

    def getSchemaVersion(self) -> int:
        """
        @see ghidra.util.Saveable#getSchemaVersion()
        """
        ...

    def hashCode(self) -> int: ...

    def isPrivate(self) -> bool: ...

    def isUpgradeable(self, oldSchemaVersion: int) -> bool:
        """
        @see ghidra.util.Saveable#isUpgradeable(int)
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restore(self, objStorage: ghidra.util.ObjectStorage) -> None:
        """
        @see Saveable#save(ObjectStorage)
        """
        ...

    def save(self, objStorage: ghidra.util.ObjectStorage) -> None:
        """
        @see Saveable#restore(ObjectStorage)
        """
        ...

    def toString(self) -> unicode: ...

    def upgrade(self, oldObjStorage: ghidra.util.ObjectStorage, oldSchemaVersion: int, currentObjStorage: ghidra.util.ObjectStorage) -> bool:
        """
        @see ghidra.util.Saveable#upgrade(ghidra.util.ObjectStorage, int, ghidra.util.ObjectStorage)
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def color(self) -> java.awt.Color: ...

    @property
    def objectStorageFields(self) -> List[java.lang.Class]: ...

    @property
    def schemaVersion(self) -> int: ...
