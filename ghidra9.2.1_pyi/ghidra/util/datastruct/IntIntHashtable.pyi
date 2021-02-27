from typing import List
import java.lang


class IntIntHashtable(object):
    """
    Class that implements a hashtable with int keys and int values.
         Because this class uses array of primitives
         to store the information, it serializes very fast.  This implementation uses
         separate chaining to resolve collisions.
    """





    @overload
    def __init__(self):
        """
        Default constructor creates a table with an initial default capacity.
        """
        ...

    @overload
    def __init__(self, capacity: int):
        """
        Constructor creates a table with an initial given capacity.  The capacity
         will be adjusted to the next highest prime in the PRIMES table.
        @param capacity the initial capacity.
        """
        ...



    def contains(self, key: int) -> bool:
        """
        Return true if the given key is in the hashtable.
        @param key the key to be tested for existence in the hashtable.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def get(self, key: int) -> int:
        """
        Returns the value for the given key.
        @param key the key for which to retrieve a value.
        @exception NoValueException thrown if there is no value for the given key.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getKeys(self) -> List[int]:
        """
        Returns an array containing all the int keys.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def put(self, key: int, value: int) -> None:
        """
        Adds a key/value pair to the hashtable. If the key is already in the table,
         the old value is replaced with the new value.  If the hashtable is already
         full, the hashtable will attempt to approximately double in size
         (it will use a prime number), and all the current entries will
         be rehashed.
        @param key the key for the new entry.
        @param value the value for the new entry.
        @exception ArrayIndexOutOfBoundsException thrown if the maximum capacity is
         reached.
        """
        ...

    def remove(self, key: int) -> int:
        """
        Removes a key/value from the hashtable
        @param key the key to remove from the hashtable.
        @return true if key is found and removed, false otherwise.
        @throws NoValueException
        @exception NoValueException thrown if there is no value for the given key.
        """
        ...

    def removeAll(self) -> None:
        """
        Remove all entries from the hashtable.
        """
        ...

    def size(self) -> int:
        """
        Return the number of key/value pairs stored in the hashtable.
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
    def keys(self) -> List[int]: ...
