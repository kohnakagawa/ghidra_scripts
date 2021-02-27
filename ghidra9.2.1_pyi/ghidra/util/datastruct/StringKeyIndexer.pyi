from typing import Iterator
from typing import List
import java.io
import java.lang


class StringKeyIndexer(object, java.io.Serializable):
    """
    This class converts arbitrary Strings into compacted int indexes suitable
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
        Constructs a StringKeyIndexer with a default capacity.
        """
        ...

    @overload
    def __init__(self, capacity: int):
        """
        Constructs a StringKeyIndexer with a given initial capacity.
        @param capacity the initial capacity.
        """
        ...



    def clear(self) -> None:
        """
        Remove all keys.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def get(self, key: unicode) -> int:
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

    def getKeyIterator(self) -> Iterator[unicode]:
        """
        Returns an iterator over all the keys.
        @return an iterator over all the keys.
        """
        ...

    def getKeys(self) -> List[unicode]:
        """
        Returns an array containing all the keys stored in this object.
        """
        ...

    def getSize(self) -> int:
        """
        Returns the number of keys stored in the table.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def put(self, key: unicode) -> int:
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

    def remove(self, key: unicode) -> int:
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
    def keyIterator(self) -> java.util.Iterator: ...

    @property
    def keys(self) -> List[unicode]: ...

    @property
    def size(self) -> int: ...
