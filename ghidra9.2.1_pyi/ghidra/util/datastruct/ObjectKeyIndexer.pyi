from typing import List
import java.lang


class ObjectKeyIndexer(object):
    """
    This class converts arbitrary Objects into compacted int indexes suitable
     for use as indexes into an array or table.  Whenever a new key is added,
     the smallest unused index is allocated and associated with that key.
     Basically hashes the keys into linked lists using the IntListIndexer class,
     where all values in a list have
     the same hashcode.  Does most of the work in implementing a separate chaining
     version of a hashtable - the only thing missing is the values which are stored
     in the individual implementations of the various hashtables.
    """





    @overload
    def __init__(self):
        """
        Constructs an ObjectKeyIndexer with a default capacity.
        """
        ...

    @overload
    def __init__(self, capacity: int):
        """
        Constructs an ObjectKeyIndexer with a given initial capacity.
        @param capacity the initial capacity.
        """
        ...



    def clear(self) -> None:
        """
        Remove all keys.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def get(self, key: object) -> int:
        """
        Returns the index for the given key, or
         -1 if key is not in the table.
        @param key the key for which to find an index.
        """
        ...

    def getCapacity(self) -> int:
        """
        Returns the current size of the key table.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getKeys(self, keyArray: List[object]) -> List[object]: ...

    def getSize(self) -> int:
        """
        Returns the number of keys stored in the table.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def put(self, key: object) -> int:
        """
        Returns an index that will always be associated to the given key as long as
         the key remains in the table. If the key already exists, then the index where
         that key is stored is returned.  If the key is new, then a new index is allocated,
         the key is stored at that index, and the new index is returned.
        @param key the key to be stored.
        @return index for key, or -1 if there was no room to put the key.
        @exception IndexOutOfBoundsException thrown if this object is at maximum capacity.
        """
        ...

    def remove(self, key: object) -> int:
        """
        Removes the key from the table.
        @param key the key to remove.
        @return index of the key if the key was found, -1 if
         key did not exist in the table
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
    def capacity(self) -> int: ...

    @property
    def size(self) -> int: ...
