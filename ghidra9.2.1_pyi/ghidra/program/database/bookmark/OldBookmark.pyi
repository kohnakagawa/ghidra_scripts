import ghidra.program.model.address
import ghidra.util
import java.lang


class OldBookmark(object, ghidra.util.Saveable):




    @overload
    def __init__(self):
        """
        Constructs a Note Bookmark (required for Saveable property objects).
         Contains no address.
        """
        ...

    @overload
    def __init__(self, type: unicode, category: unicode, comment: unicode, addr: ghidra.program.model.address.Address):
        """
        Constructs a Bookmark.
        @param type
        @param category
        @param comment
        @param addr
        """
        ...



    def equals(self, obj: object) -> bool:
        """
        Return true if this object is the same as obj.
        """
        ...

    def getAddress(self) -> ghidra.program.model.address.Address:
        """
        Get the address of this bookmark info.
        @return Address
        """
        ...

    def getCategory(self) -> unicode: ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self) -> unicode: ...

    def getObjectStorageFields(self) -> java.lang.Class: ...

    def getSchemaVersion(self) -> int: ...

    def getType(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def isPrivate(self) -> bool: ...

    def isUpgradeable(self, oldSchemaVersion: int) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restore(self, objStorage: ghidra.util.ObjectStorage) -> None:
        """
        @see Saveable#restore(ObjectStorage)
        """
        ...

    def save(self, objStorage: ghidra.util.ObjectStorage) -> None:
        """
        @see Saveable#save(ObjectStorage)
        """
        ...

    def setCategory(self, category: unicode) -> None: ...

    def setComment(self, comment: unicode) -> None: ...

    def toString(self) -> unicode: ...

    def upgrade(self, oldObjStorage: ghidra.util.ObjectStorage, oldSchemaVersion: int, currentObjStorage: ghidra.util.ObjectStorage) -> bool: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def category(self) -> unicode: ...

    @category.setter
    def category(self, value: unicode) -> None: ...

    @property
    def comment(self) -> unicode: ...

    @comment.setter
    def comment(self, value: unicode) -> None: ...

    @property
    def objectStorageFields(self) -> List[java.lang.Class]: ...

    @property
    def private(self) -> bool: ...

    @property
    def schemaVersion(self) -> int: ...

    @property
    def type(self) -> unicode: ...
