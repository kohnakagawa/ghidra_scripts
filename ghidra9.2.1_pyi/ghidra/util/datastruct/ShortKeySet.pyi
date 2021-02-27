import java.lang


class ShortKeySet(object):
    """
    The ShortKeySet provides an interface for managing a set of ordered short keys
     between the values of 0 and N.  It can add keys, remove keys, find the next key
     greater than some value , and find the previous key less than some value.
    """









    def containsKey(self, key: int) -> bool:
        """
        Determines if a given key is in the set.
        @param key the key whose presence is to be tested.
        @return true if the key is in the set.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFirst(self) -> int:
        """
        Returns the first (lowest) key in the set.
        """
        ...

    def getLast(self) -> int:
        """
        Returns the last (highest) key in the set.
        """
        ...

    def getNext(self, key: int) -> int:
        """
        finds the next key that is in the set that is greater than the given key.
        @param key the key for which to find the next key after.
        """
        ...

    def getPrevious(self, key: int) -> int:
        """
        finds the previous key that is in the set that is less than the given key.
        @param key the key for which to find the previous key.
        """
        ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool:
        """
        Checks if the set is empty.
        @return true if the set is empty.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def put(self, key: int) -> None:
        """
        Adds a key to the set.
        @param key the key to add to the set.
        """
        ...

    def remove(self, key: int) -> bool:
        """
        Removes the key from the set.
        @param key the key to remove from the set.
        """
        ...

    def removeAll(self) -> None:
        """
        Removes all keys from the set.
        """
        ...

    def size(self) -> int:
        """
        Returns the number of keys currently in the set.
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
    def empty(self) -> bool: ...

    @property
    def first(self) -> int: ...

    @property
    def last(self) -> int: ...
