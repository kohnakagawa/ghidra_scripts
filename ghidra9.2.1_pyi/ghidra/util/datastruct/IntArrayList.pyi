from typing import List
import ghidra.util
import java.io
import java.lang


class IntArrayList(object, java.io.Serializable, ghidra.util.Saveable):
    """
    An ArrayList type object for ints.
    """

    MIN_SIZE: int = 4



    @overload
    def __init__(self):
        """
        Creates new intArrayList
        """
        ...

    @overload
    def __init__(self, arr: List[int]):
        """
        Creates a new intArrayList using the values in the given array
        @param arr array of ints to initialize to.
        """
        ...



    @overload
    def add(self, value: int) -> None:
        """
        Adds a new int value at the end of the list.
        @param value the int value to add.
        """
        ...

    @overload
    def add(self, index: int, value: int) -> None:
        """
        Puts the given int value in the int array at
         the given index
        @param index Index into the array.
        @param value value to store
        @throws IndexOutOfBoundsException if the index is negative OR index &gt; size
        """
        ...

    def clear(self) -> None:
        """
        Clears the entire array of data.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def get(self, index: int) -> int:
        """
        Returns the int at the given index
        @param index index into the array
        @return The int value at the given index. A 0 will
         be returned for any index not initialized to
         another value.
        @throws IndexOutOfBoundsException if the index is negative or greater than the list size.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

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

    def removeValue(self, value: int) -> None:
        """
        Removes the first occurrence of the given
         value.
        @param value the value to be removed.
        """
        ...

    def removeValueAt(self, index: int) -> None:
        """
        Removes the value at the given index decreasing the array list size by 1.
        @param index the index to remove.
        @throws IndexOutOfBoundsException if the index is negative
        """
        ...

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

    def set(self, index: int, value: int) -> None:
        """
        Sets the array value at index to value.
        @param index the index to set.
        @param value the value to store.
        """
        ...

    def size(self) -> int:
        """
        Returns the size of this virtual array.
        @return int the size of this virtual array.
        """
        ...

    def toArray(self) -> List[int]:
        """
        Converts to a primitive array.
        @return int[] int array for results.
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
    def objectStorageFields(self) -> List[java.lang.Class]: ...

    @property
    def private(self) -> bool: ...

    @property
    def schemaVersion(self) -> int: ...
