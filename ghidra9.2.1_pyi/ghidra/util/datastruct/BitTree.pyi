import ghidra.util.datastruct
import java.io
import java.lang


class BitTree(object, ghidra.util.datastruct.ShortKeySet, java.io.Serializable):
    """
    The BitTree class maintains a set of ordered keys between the values of
     0 and N.  It can quickly (O(log(n))) add keys, remove keys, find the next key
     greater than some value , and find the prev key less than some value.  It can
     determine if a key is in the set in O(1) time. This implementation has been
     limited to short keys so that it can implement the ShortKeySet interface.
    """





    @overload
    def __init__(self, maxKey: int):
        """
        The BitTree constructor takes the maximum key value. The legal
         keys for this set range from 0 to maxKey.
        @param maxKey the maximum key that will ever be put into this BitTree.
        """
        ...

    @overload
    def __init__(self, maxKey: int, isFull: bool):
        """
        The BitTree constructor takes the maximum key value. The legal
         keys for this set range from 0 to maxKey.
        @param maxKey the maximum key value.
        @param isFull if true, then the set is initilized to contain all legal keys.
        """
        ...



    def containsKey(self, key: int) -> bool:
        """
        Determines if a given key is in the set.
        @param key the key to check if it is in this set.
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
        @param key from which to search forward.
        @return the next key greater than the given key or -1 if there is no key
         greater than the given key.
        @exception IndexOutOfBoundsException if the given key is not
         in the range [0, size-1].
        """
        ...

    def getPrevious(self, key: int) -> int:
        """
        Finds the next key that is in the set that is less than the given key.
        @param key the key to search before.
        @return the next key less than the given key or -1 if there is no key
         less than the given key.
        @exception IndexOutOfBoundsException if the given key is not
         in the range [0, size-1].
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
        @param key to be added.
        @exception IndexOutOfBoundsException if the given key is not
         in the range [0, size-1].
        """
        ...

    def remove(self, key: int) -> bool:
        """
        Removes the key from the set.
        @param key The key to remove.
        @exception IndexOutOfBoundsException if the given key is not
         in the range [0, size-1].
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
