import java.io
import java.lang


class RedBlackLongKeySet(object, java.io.Serializable):
    """
    A RedBlack Tree implementation of a long key set.
    """

    NODESIZE: int = 15



    def __init__(self):
        """
        Creates a new RedBlackLongKeySet that can store keys between 0 and n.
        """
        ...



    def containsKey(self, key: long) -> bool:
        """
        Returns true if the key is in the set.
        @param key the key whose presence is to be tested.
        @exception IndexOutOfBoundsException thrown if the given key is not
         in the range [0, maxKey].
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFirst(self) -> long:
        """
        Returns the first key in this set.
        """
        ...

    def getLast(self) -> long:
        """
        Returns the last key in this set.
        """
        ...

    def getNext(self, key: long) -> long:
        """
        Returns the smallest key in the set that is greater than the given key.  Returns
         -1 if there are no keys greater than the given key.
        @param key the key for which to find the next key after.
        @exception IndexOutOfBoundsException thrown if the given key is not
         in the range [0, maxKey].
        """
        ...

    def getPrevious(self, key: long) -> long:
        """
        Returns the largest key in the set that is less than the given key. Returns -1 if
         there are not keys less than the given key.
        @param key the key for which to find the previous key.
        @exception IndexOutOfBoundsException thrown if the given key is not
         in the range [0, maxKey].
        """
        ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool:
        """
        Test if the set is empty.
        @return true if the set is empty.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def put(self, key: long) -> None:
        """
        Adds the given key to the set.
        @param key the key to add to the set.
        @exception IndexOutOfBoundsException thrown if the given key is not
         in the range [0, maxKey].
        """
        ...

    def remove(self, key: long) -> bool:
        """
        Removes the given key from the set.
        @param key the key to remove from the set.
        @exception IndexOutOfBoundsException thrown if the given key is not
         in the range [0, maxKey].
        """
        ...

    def removeAll(self) -> None:
        """
        Removes all keys from the set.
        """
        ...

    def size(self) -> int:
        """
        Returns the number keys in this set.
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
    def first(self) -> long: ...

    @property
    def last(self) -> long: ...
